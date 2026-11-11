---
document_id: DOC-304
title: Annotation File Contract
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: file pipeline 0.1.0
authority: controlled
supersedes: null
related: [DOC-001, DOC-202, DOC-301, DOC-302, DOC-402, DOC-502, DOC-503]
---

# Annotation File Contract

The executable contract is proposed version `0.1.0`. Its implementation verifies
record conformance; pilot review and interpretation of real works remain open.

## Setup and commands

Run from the repository root with Python 3.11 or later:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised --check
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/literary.json
.venv/bin/python -m unittest discover -s tests -v
```

The validation example uses an invented conformance fixture. For actual work,
pass the path to a privately stored bundle with `--input`. The validator reads
that file and writes a report to stdout; it does not import, modify, or publish
the annotation file.

Configuration paths are resolved relative to the configuration file. CLI input,
catalogue, and output paths are resolved from the working directory. Missing
files, malformed JSON, duplicate JSON keys, invalid configuration, source
checksum mismatches, and missing dependencies fail explicitly. The missing
jsonschema error names the requirements installation command.

## Extraction and provenance

`config/pipeline.json` records the expected source digest, source field set,
label and unit vocabularies, source-status mapping, definition-version token,
relation vocabulary/decisions, and pattern-specific evidence-role rules. It is
validated against `schemas/pipeline.schema.json` before processing.

The authoritative CSV is read without alteration. `.gitattributes` disables
Git text conversion for both original-byte copies, retaining their CRLF line
endings and checksum across checkouts. The extractor checks the
expected checksum, duplicate headers, field set, row widths, non-empty values,
pattern namespaces/IDs, unit membership, and referenced pattern IDs.

| Output under `data/normalised/` | Meaning |
|---|---|
| `source.csv` | Exact original bytes, retained with their SHA-256 |
| `patterns.csv` | Definitions and criteria, canonical proposed status, version token, and evidence-rule reference |
| `label_types.csv`, `analysis_units.csv` | Lookup values for this extraction |
| `pattern_units.csv` | Explicit pattern-to-unit membership |
| `examples.csv` | Source examples marked `invented`; no real corpus evidence |
| `evidence_rules.csv` | Deduplicated source evidence, annotation, and sequence defaults |
| `indicator_candidates.csv` | Complete modality-specific source cells pending discrete-cue segmentation |
| `relation_candidates.csv` | IDs listed by each source row, with no inferred relation type or symmetry |
| `relations.csv` | Only explicitly configured typed decisions; currently empty |
| `workbook_mappings.csv` | Preserved mapping cells pending decomposition and rationale review |
| `review_items.json` | Unresolved segmentation, typing, mapping rationale, false-positive guidance, and evidential thresholds |
| `manifest.json` | Generator/version identity, source/configuration digests, output counts and hashes |

Regeneration is deterministic for the same source and configuration. `--check`
compares every expected output byte and rejects extra files. Generation rejects
unowned output directories, symlink entries, and a destination containing the
source. Existing generated files may be replaced; unrelated files are retained
and cause a clear error rather than being deleted.

For a typed relation, add a decision with `source`, `target`, `relation_type`,
and a non-empty `rationale`. Both IDs must form a listed source pair. The relation
vocabulary supplies symmetry; reverse duplicates of symmetric decisions fail.
These are explicit maintainer decisions, not evidence that the proposed relation
has been observed. Review them under CONTRIBUTING.md before changing shared data.

The pipeline has not resolved the review queue. Discrete indicator extraction,
decomposed mappings with justified actions, and complete per-pattern guidance
remain work needed before an operational source replaces the original CSV.

## Bundle structure

The schema is [annotation.schema.json](../../schemas/annotation.schema.json).
Each object rejects unknown fields. Bundle arrays may be empty; missing
annotations do not become absence records.

| Bundle field | Required content |
|---|---|
| `schema_version` | Supported annotation schema version |
| `source_sha256` | The configured, checked source digest |
| `works` | Unique `work_id`, title, edition/release `version`, and `modality` |
| `units` | Unique `unit_id`, a known `work_id`, supported `unit_type`, and locator |
| `reviewers` | Unique non-empty `reviewer_id` values |
| `annotations` | Coding decisions and inline evidence, described below |
| `events` | Linked evidence events with ordering and role |
| `adjudications` | Decisions referencing retained original annotations |

An annotation requires `annotation_id`, `work_id`, `unit_id`, `pattern_id`,
`pattern_version`, `schema_version`, `presence`, `rationale`, `reviewer`,
`modality`, `created_at`, and `evidence`. `connection`, `function`, and
`proposed_effect` are separate optional statements. The initial pattern-version
token is `source-` followed by the full source SHA-256: it identifies the frozen
source definitions, not a pilot-tested revision.

Every evidence object requires `evidence_id`, `kind`, `description`, and
`locator`. Optional `role` values connect evidence to configured pattern rules.
Allowed kinds are quotation, paraphrase, timestamp span, visual description,
audio description, knowledge state, and inspection, encoded with underscores.

Literature locators are `{"type":"text","reference":"<stable locator>"}`.
Video locators are `{"type":"timestamp","start":0,"end":1}` with numeric
seconds, a non-negative start, and end strictly after start. Booleans and non-finite numbers are rejected. `created_at` uses an RFC 3339 date-time with seconds and a timezone.

`present` and `uncertain` need located evidence. `absent` needs evidence of kind
`inspection`, with non-empty `inspection_scope` and `adequacy`. `not_applicable`
may have no evidence, but still requires a rationale. A structurally complete
inspection record remains the reviewer's claim, which must be checked in the
study.

Events require `event_id`, `annotation_id`, an `evidence_id` inside that
annotation, `presentation_order`, and `role`. Order values are non-negative
integers and presentation order is unique within an annotation. Optional
`story_order` stays separate. Event roles follow the workflow: setup,
expectation, disruption, reveal, or consequence.

Adjudications require `adjudication_id`, `annotation_ids`, `reviewer`, `decision`,
and `rationale`. Original annotations must remain in the bundle, and the
referenced decisions must concern the same work, unit, and pattern. The validator
checks one supplied bundle; it does not enforce append-only storage over time.

## Positive evidence rules

The following rules apply to `present` annotations. Uncertainty and inspected
absence are not required to manufacture a positive pattern's complete chain.
Rules are data in `config/pipeline.json`.

| Pattern | Required evidence roles | Additional checks |
|---|---|---|
| STR05 | `cue`, `later_event` | Distinct required-role locators and linked events, cue before later event |
| STR09 | `setup`, `payoff` | Distinct required-role locators, linked events in order, and `connection` |
| STR06 | `misleading_cue`, `invited_inference`, `corrective_evidence` | Distinct required-role locators and linked cue/correction events in order |
| STR07 | `claim`, `disconfirming_evidence` | Distinct required-role locators with events linked to both roles |
| STR10 | `knowledge_state` | Evidence kind `knowledge_state` with a knowledge map |

A knowledge map lists `holder`, `information`, and Boolean `knows` records.
At least two holders must differ on knowledge of the same information. Duplicate
holder/information pairs fail. The map records the supplied knowledge claim;
it does not infer anyone's mental state.

Other patterns receive general structural and reference checks. The tool does
not yet enforce every possible pattern-specific or sequential constraint.

## Reports and limitations

Successful conformance returns exit 0 and `valid: true`. Failed conformance
returns exit 1 with `valid: false` and errors containing `path`, `code`, and
`message`. Paths such as `$.annotations[0].evidence` identify the affected record.
Malformed inputs or unavailable dependencies return exit 1 with an `error:`
message on stderr rather than a conformance report.

Reports identify schema and validator versions, source checksum, supplied
annotation counts by presence state, errors, and a scope warning. A stale or
modified catalogue is rejected before annotations are validated. JSON Schema
uses local references, including dynamic references; a registry with retrieval
disabled prevents network resolution. Broken references fail explicitly.

The tests exercise reference integrity, versions, locators, ordering, inspection,
knowledge states, and the named negative cases in DOC-502. They establish file
behaviour, not that a quotation exists, inspection was adequate, an interpretation
is correct, annotators agree, or a pattern is validated. SQL persistence, platform
adapters, agreement statistics, and pilot evidence remain outside this release.

The implementation uses the documented
[jsonschema validator API](https://python-jsonschema.readthedocs.io/en/stable/validate/)
for schema checking and error collection, plus repository-specific Python rules.
