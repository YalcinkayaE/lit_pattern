"""Lossless, deterministic extraction with explicit unresolved source groups."""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
from pathlib import Path
import tempfile

from .common import InputError, configured_path, digest, json_bytes, load_config, read_json


def csv_bytes(fields: list[str], rows: list[dict]) -> bytes:
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8')


def load_source(config_path: Path, config: dict) -> tuple[bytes, list[dict]]:
    source = configured_path(config_path, config['source'])
    try:
        raw = source.read_bytes()
        if digest(raw) != config['source_sha256']:
            raise InputError(f'{source}: checksum mismatch; review the source and configuration')
        reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''), strict=True)
        fields = reader.fieldnames
        if (fields is None or len(set(fields)) != len(fields)
                or set(fields) != set(config['required_fields'])):
            raise InputError(f'{source}: duplicate, missing, or unexpected CSV header fields')
        rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        raise InputError(f'{source}: {exc}') from exc
    if not rows:
        raise InputError(f'{source}: no pattern rows')
    seen = set()
    try:
        namespace = re.compile(config['pattern_id_pattern'])
    except re.error as exc:
        raise InputError(f'configuration pattern_id_pattern: {exc}') from exc
    for line, row in enumerate(rows, 2):
        if None in row or any(v is None or not v.strip() for v in row.values()):
            empty = [k for k, v in row.items() if v is None or (isinstance(v, str) and not v.strip())]
            raise InputError(f'{source}:{line}: wrong row width or empty required fields {empty}')
        key = row['pattern_id']
        if not namespace.fullmatch(key):
            raise InputError(f'{source}:{line}: invalid pattern_id {key!r}')
        if key != key.strip():
            raise InputError(f'{source}:{line}: whitespace in pattern ID {key!r}')
        if key in seen:
            raise InputError(f'{source}:{line}: duplicate pattern ID {key}')
        seen.add(key)
        if row['label_type'] not in config['label_types']:
            raise InputError(f'{source}:{line}: unknown label_type {row["label_type"]}')
        if row['status'] not in config['status_mapping']:
            raise InputError(f'{source}:{line}: unmapped status {row["status"]}')
    return raw, rows


def build(config_path: Path) -> dict[str, bytes]:
    config = load_config(config_path)
    raw, rows = load_source(config_path, config)
    ids = {r['pattern_id'] for r in rows}
    unknown_rules = set(config['pattern_rules']) - ids
    if unknown_rules:
        raise InputError(f'configuration: rules reference unknown patterns {sorted(unknown_rules)}')
    patterns, units, indicators, candidates, mappings, examples, review = [], [], [], [], [], [], []
    defaults = {}
    pattern_fields = ['pattern_id', 'label_type', 'label', 'definition', 'inclusion_criteria',
                      'exclusion_criteria', 'creative_use', 'interpretation_boundary']
    default_fields = ['evidence_required', 'annotation_rule', 'sequence_recording']
    for row in rows:
        key = row['pattern_id']
        rule = {field: row[field] for field in default_fields}
        rule_id = 'rule-' + digest(json_bytes(rule))
        defaults[rule_id] = {'rule_id': rule_id, **rule}
        patterns.append({**{field: row[field] for field in pattern_fields},
                         'status': config['status_mapping'][row['status']],
                         'pattern_version': config['pattern_version'], 'evidence_rule_id': rule_id})
        tokens = [v.strip() for v in row['analysis_unit'].split(';')]
        if len(tokens) != len(set(tokens)) or not set(tokens) <= set(config['unit_types']):
            raise InputError(f'{key}: invalid or duplicate analysis_unit token')
        units.extend({'pattern_id': key, 'unit_type': unit} for unit in tokens)
        for modality, field in [('literature', 'literature_indicators'), ('video', 'video_indicators')]:
            indicators.append({'pattern_id': key, 'modality': modality, 'source_text': row[field]})
            review.append({'pattern_id': key, 'kind': 'indicator_segmentation', 'field': field,
                           'message': 'Preserved complete source cell; discrete indicator boundaries need review.'})
        related = [v.strip() for v in row['related_patterns'].split(';')]
        if len(related) != len(set(related)):
            raise InputError(f'{key}: duplicate related pattern ID')
        for target in related:
            if target not in ids:
                raise InputError(f'{key}: unknown related pattern {target}')
            candidates.append({'listed_by_pattern_id': key, 'related_pattern_id': target})
        mappings.append({'pattern_id': key, 'source_text': row['original_workbook_mapping']})
        examples.append({'example_id': key + '-invented', 'pattern_id': key,
                         'kind': 'invented', 'description': row['invented_example']})
        for kind in ['relation_typing', 'workbook_mapping_rationale', 'common_false_positive',
                     'evidential_threshold']:
            review.append({'pattern_id': key, 'kind': kind,
                           'message': 'Requires an explicit reviewed decision; not inferred from source prose.'})
    candidate_pairs = {(r['listed_by_pattern_id'], r['related_pattern_id']) for r in candidates}
    relations, seen_relations = [], set()
    for item in config['relation_decisions']:
        pair = (item['source'], item['target'])
        relation_type = item['relation_type']
        if pair not in candidate_pairs or relation_type not in config['relation_types']:
            raise InputError(f'configuration: invalid relation decision {pair}, {relation_type}')
        symmetric = config['relation_types'][relation_type]
        relation_key = (*sorted(pair), relation_type) if symmetric else (*pair, relation_type)
        if relation_key in seen_relations:
            raise InputError(f'configuration: duplicate relation decision {relation_key}')
        seen_relations.add(relation_key)
        relations.append({'source_pattern_id': pair[0], 'target_pattern_id': pair[1],
                          'relation_type': relation_type, 'symmetric': str(symmetric).lower(),
                          'rationale': item['rationale']})
    tables = {
        'patterns.csv': (pattern_fields + ['status', 'pattern_version', 'evidence_rule_id'], patterns),
        'label_types.csv': (['label_type'], [{'label_type': v} for v in sorted({r['label_type'] for r in rows})]),
        'analysis_units.csv': (['unit_type'], [{'unit_type': v} for v in config['unit_types']]),
        'pattern_units.csv': (['pattern_id', 'unit_type'], units),
        'indicator_candidates.csv': (['pattern_id', 'modality', 'source_text'], indicators),
        'relation_candidates.csv': (['listed_by_pattern_id', 'related_pattern_id'], candidates),
        'relations.csv': (['source_pattern_id', 'target_pattern_id', 'relation_type', 'symmetric', 'rationale'], relations),
        'workbook_mappings.csv': (['pattern_id', 'source_text'], mappings),
        'examples.csv': (['example_id', 'pattern_id', 'kind', 'description'], examples),
        'evidence_rules.csv': (['rule_id'] + default_fields, list(defaults.values())),
    }
    outputs = {name: csv_bytes(fields, values) for name, (fields, values) in tables.items()}
    outputs['source.csv'] = raw
    outputs['review_items.json'] = json_bytes(review)
    outputs['manifest.json'] = json_bytes({
        'generated_by': 'lit_pattern.normalise',
        'normalisation_version': config['normalisation_version'],
        'schema_version': config['schema_version'], 'pattern_version': config['pattern_version'],
        'source_sha256': digest(raw), 'config_sha256': digest(config_path.read_bytes()),
        'rows': {name: len(values) for name, (_, values) in tables.items()},
        'files': {name: digest(value) for name, value in outputs.items()},
    })
    return outputs


def persist(outputs: dict[str, bytes], output: Path, config_path: Path, check: bool) -> None:
    config = load_config(config_path)
    source = configured_path(config_path, config['source'])
    output = output.absolute()
    if output.is_symlink() or source.is_relative_to(output.resolve()):
        raise InputError('output directory must not contain or replace the source')
    if output.exists() and not output.is_dir():
        raise InputError(f'output is not a directory: {output}')
    actual = {p.name for p in output.iterdir()} if output.exists() else set()
    if actual:
        manifest_path = output / 'manifest.json'
        if manifest_path.is_symlink() or not manifest_path.is_file():
            raise InputError(f'unowned output directory: {output}')
        manifest = read_json(manifest_path)
        if not isinstance(manifest, dict) or manifest.get('generated_by') != 'lit_pattern.normalise':
            raise InputError(f'unowned output directory: {output}')
    for name in actual:
        path = output / name
        if path.is_symlink() or not path.is_file():
            raise InputError(f'unsafe output entry: {path}')
    extras = actual - outputs.keys()
    if extras:
        raise InputError(f'unexpected output files: {sorted(extras)}')
    stale = [name for name, value in outputs.items()
             if not (output / name).is_file() or (output / name).read_bytes() != value]
    if check:
        if stale:
            raise InputError('stale or missing outputs: ' + ', '.join(stale))
        return
    output.mkdir(parents=True, exist_ok=True)
    for name in stale:
        with tempfile.NamedTemporaryFile(dir=output, delete=False) as handle:
            pending = Path(handle.name)
            try:
                handle.write(outputs[name])
                handle.close()
                os.replace(pending, output / name)
            finally:
                pending.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        outputs = build(args.config)
        persist(outputs, args.output, args.config, args.check)
    except (InputError, OSError) as exc:
        parser.exit(1, f'error: {exc}\n')
    print(('current: ' if args.check else 'generated: ') + str(args.output))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
