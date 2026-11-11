"""Validate annotation bundles against the proposed file-based contract."""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime
from itertools import product
import io
import json
from pathlib import Path
import sys

from .common import (Draft202012Validator, FormatChecker, InputError, SchemaError, configured_path,
                     json_path, load_config, read_json)
from .normalise import build, persist
from referencing import Registry
from referencing.exceptions import NoSuchResource, Unresolvable


def annotation_schema(config: dict) -> dict:
    schema = read_json(Path(config['_annotation_schema']))
    def local_references(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in {'$ref', '$dynamicRef'} and (not isinstance(item, str) or not item.startswith('#')):
                    raise InputError('annotation schema must use local references; remote retrieval is disabled')
                local_references(item)
        elif isinstance(value, list):
            for item in value:
                local_references(item)
    local_references(schema)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise InputError(f'invalid annotation schema: {exc.message}') from exc
    return schema


def validate_bundle(bundle: dict, config: dict, patterns: dict) -> list[dict]:
    errors = []
    def error(path, code, message):
        errors.append({'path': path, 'code': code, 'message': message})

    formats = FormatChecker()
    @formats.checks('date-time', raises=(ValueError, TypeError))
    def date_time(value):
        if not isinstance(value, str):
            return True  # The schema type check handles non-strings.
        parsed = datetime.fromisoformat(value.upper().replace('Z', '+00:00'))
        return ('T' in value or 't' in value) and parsed.tzinfo is not None

    def deny_retrieval(uri):
        raise NoSuchResource(ref=uri)

    structural = Draft202012Validator(annotation_schema(config), format_checker=formats,
                                     registry=Registry(retrieve=deny_retrieval))
    try:
        issues = sorted(structural.iter_errors(bundle), key=lambda e: str(list(e.path)))
    except Unresolvable as exc:
        raise InputError(f'annotation schema reference cannot be resolved locally: {exc}') from exc
    for issue in issues:
        error(json_path(issue.path), 'schema', issue.message)
    if errors:
        return errors
    if bundle['schema_version'] != config['schema_version']:
        error('$.schema_version', 'schema_version', 'unsupported annotation schema version')
    if bundle['source_sha256'] != config['source_sha256']:
        error('$.source_sha256', 'source_version', 'bundle references a different source checksum')

    def index(items, key, base):
        values = {}
        for i, item in enumerate(items):
            identifier = item[key]
            if identifier in values:
                error(f'{base}[{i}].{key}', 'duplicate_id', f'duplicate {key}: {identifier}')
            else:
                values[identifier] = item
        return values

    works = index(bundle['works'], 'work_id', '$.works')
    units = index(bundle['units'], 'unit_id', '$.units')
    reviewers = index(bundle['reviewers'], 'reviewer_id', '$.reviewers')
    annotations = index(bundle['annotations'], 'annotation_id', '$.annotations')
    index(bundle['events'], 'event_id', '$.events')
    index(bundle['adjudications'], 'adjudication_id', '$.adjudications')

    def locator(value, modality, path):
        if value['type'] == 'timestamp' and value['end'] <= value['start']:
            error(path, 'locator_span', 'timestamp end must be greater than start')
        if modality and value['type'] != ('timestamp' if modality == 'video' else 'text'):
            error(path, 'locator_modality', 'locator type does not match the work modality')

    for i, unit in enumerate(bundle['units']):
        path = f'$.units[{i}]'
        work = works.get(unit['work_id'])
        if work is None:
            error(path + '.work_id', 'unknown_work', 'unit references an unknown work')
        if unit['unit_type'] not in config['unit_types']:
            error(path + '.unit_type', 'unit_type', 'unsupported analysis unit')
        locator(unit['locator'], work['modality'] if work else None, path + '.locator')

    evidence_by_annotation = {}
    for i, annotation in enumerate(bundle['annotations']):
        path = f'$.annotations[{i}]'
        unit = units.get(annotation['unit_id'])
        work = works.get(annotation['work_id'])
        pattern = patterns.get(annotation['pattern_id'])
        if work is None:
            error(path + '.work_id', 'unknown_work', 'annotation references an unknown work')
        elif annotation['modality'] != work['modality']:
            error(path + '.modality', 'modality', 'annotation and work modality differ')
        if unit is None:
            error(path + '.unit_id', 'unknown_unit', 'annotation references an unknown unit')
        elif unit['work_id'] != annotation['work_id']:
            error(path + '.unit_id', 'unit_work', 'unit belongs to another work')
        if annotation['reviewer'] not in reviewers:
            error(path + '.reviewer', 'unknown_reviewer', 'unknown reviewer')
        if pattern is None:
            error(path + '.pattern_id', 'unknown_pattern', 'pattern is not in the source catalogue')
        else:
            if annotation['pattern_version'] != pattern['pattern_version']:
                error(path + '.pattern_version', 'pattern_version', 'unsupported pattern definition version')
            if unit and unit['unit_type'] not in pattern['_unit_types']:
                error(path + '.unit_id', 'pattern_unit', 'unit type is not listed for this pattern')
        if annotation['schema_version'] != config['schema_version']:
            error(path + '.schema_version', 'schema_version', 'unsupported annotation schema version')
        evidence = annotation['evidence']
        evidence_by_annotation[annotation['annotation_id']] = index(evidence, 'evidence_id', path + '.evidence')
        if annotation['presence'] in {'present', 'uncertain'} and not evidence:
            error(path + '.evidence', 'evidence_required', 'located evidence is required for this decision')
        if annotation['presence'] == 'absent' and not any(
            e['kind'] == 'inspection' and e.get('inspection_scope') and e.get('adequacy') for e in evidence
        ):
            error(path + '.evidence', 'inspection_required', 'absence requires inspected scope and adequacy evidence')
        for j, item in enumerate(evidence):
            ep = f'{path}.evidence[{j}]'
            locator(item['locator'], annotation['modality'], ep + '.locator')
            if item['kind'] == 'knowledge_state':
                knowledge = item.get('knowledge')
                if not knowledge:
                    error(ep + '.knowledge', 'knowledge_required', 'knowledge-state evidence needs a knowledge map')
                else:
                    states = defaultdict(dict)
                    for k, state in enumerate(knowledge):
                        holders = states[state['information']]
                        if state['holder'] in holders:
                            error(f'{ep}.knowledge[{k}].holder', 'duplicate_knowledge', 'holder repeated for the same information')
                        holders[state['holder']] = state['knows']
                    if not any(set(holders.values()) == {True, False} for holders in states.values()):
                        error(ep + '.knowledge', 'knowledge_asymmetry', 'map must distinguish information known and unknown by different holders')
        if annotation['presence'] == 'present':
            rule = config['pattern_rules'].get(annotation['pattern_id'])
            if rule:
                roles = {e.get('role') for e in evidence}
                if not set(rule['roles']) <= roles:
                    error(path + '.evidence', 'evidence_roles', 'missing roles: ' + ', '.join(sorted(set(rule['roles']) - roles)))
                if len({json.dumps(e['locator'], sort_keys=True) for e in evidence
                        if e.get('role') in rule['roles']}) < rule['min_locators']:
                    error(path + '.evidence', 'distinct_locators', f'at least {rule["min_locators"]} distinct locators required')
                if rule['connection'] and not annotation.get('connection'):
                    error(path + '.connection', 'connection_required', 'a supported connection statement is required')
                if rule['knowledge'] and not any(e['kind'] == 'knowledge_state' for e in evidence):
                    error(path + '.evidence', 'knowledge_required', 'knowledge-state evidence is required')

    orders = defaultdict(set)
    events_by_annotation = defaultdict(list)
    for i, event in enumerate(bundle['events']):
        path = f'$.events[{i}]'
        key = event['annotation_id']
        if key not in annotations:
            error(path + '.annotation_id', 'unknown_annotation', 'event references an unknown annotation')
            continue
        if event['evidence_id'] not in evidence_by_annotation[key]:
            error(path + '.evidence_id', 'unknown_evidence', 'event must reference evidence in its annotation')
        if event['presentation_order'] in orders[key]:
            error(path + '.presentation_order', 'duplicate_order', 'presentation order must be unique within an annotation')
        orders[key].add(event['presentation_order'])
        events_by_annotation[key].append(event)
    for i, annotation in enumerate(bundle['annotations']):
        rule = config['pattern_rules'].get(annotation['pattern_id'])
        if not rule or annotation['presence'] != 'present':
            continue
        path = f'$.annotations[{i}]'
        events = events_by_annotation[annotation['annotation_id']]
        if len(events) < rule['min_events']:
            error(path + '.evidence', 'sequence_events', f'at least {rule["min_events"]} linked sequence events required')
        roles = defaultdict(list)
        for event in events:
            item = evidence_by_annotation[annotation['annotation_id']].get(event['evidence_id'])
            if item:
                roles[item.get('role')].append((event['presentation_order'],
                                               json.dumps(item['locator'], sort_keys=True)))
        if not set(rule['event_roles']) <= roles.keys():
            error(path + '.evidence', 'sequence_roles', 'required sequence roles must have linked events')
        if rule['min_events']:
            linked_locators = {loc for role in rule['event_roles'] for _, loc in roles[role]}
            if len(linked_locators) < rule['min_locators']:
                error(path + '.evidence', 'distinct_locators', 'required linked events need distinct evidence locators')
        ordered = rule['ordered_roles']
        if ordered:
            chains = product(*(roles[role] for role in ordered))
            coherent = any(all(left[0] < right[0] for left, right in zip(chain, chain[1:]))
                           and len({item[1] for item in chain}) >= min(rule['min_locators'], len(ordered))
                           for chain in chains)
            if not coherent:
                error(path + '.evidence', 'event_order', 'required roles need a distinct linked chain in presentation order')
    for i, adjudication in enumerate(bundle['adjudications']):
        path = f'$.adjudications[{i}]'
        if adjudication['reviewer'] not in reviewers:
            error(path + '.reviewer', 'unknown_reviewer', 'unknown adjudicator')
        retained = []
        for j, key in enumerate(adjudication['annotation_ids']):
            if key not in annotations:
                error(f'{path}.annotation_ids[{j}]', 'unknown_annotation', 'original annotation is not retained')
            else:
                item = annotations[key]
                retained.append((item['work_id'], item['unit_id'], item['pattern_id']))
        if len(set(retained)) > 1:
            error(path + '.annotation_ids', 'adjudication_scope', 'adjudication must concern one work, unit, and pattern')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--catalogue', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    args = parser.parse_args()
    try:
        config = load_config(args.config)
        config['_annotation_schema'] = str(configured_path(args.config, config['annotation_schema']))
        expected = build(args.config)
        persist(expected, args.catalogue, args.config, check=True)
        patterns = {r['pattern_id']: r for r in csv.DictReader(io.StringIO(expected['patterns.csv'].decode()))}
        for pattern in patterns.values():
            pattern['_unit_types'] = []
        for item in csv.DictReader(io.StringIO(expected['pattern_units.csv'].decode())):
            patterns[item['pattern_id']]['_unit_types'].append(item['unit_type'])
        bundle = read_json(args.input)
        errors = validate_bundle(bundle, config, patterns)
    except (InputError, OSError) as exc:
        parser.exit(1, f'error: {exc}\n')
    annotations = bundle.get('annotations', []) if isinstance(bundle, dict) else []
    if not isinstance(annotations, list):
        annotations = []
    counts = Counter(a.get('presence') for a in annotations if isinstance(a, dict))
    report = {
        'schema_version': config['schema_version'], 'validator_version': config['validator_version'],
        'source_sha256': config['source_sha256'],
        'counts': {'annotations': len(annotations), **{s: counts[s] for s in ['present','absent','uncertain','not_applicable']}},
        'errors': errors, 'valid': not errors,
        'warnings': ['Structural conformance does not verify evidence truth or pattern validity.'],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
