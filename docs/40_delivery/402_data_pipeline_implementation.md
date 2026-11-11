---
document_id: DOC-402
title: Data Pipeline Implementation Plan
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: normalisation and annotation validation
authority: controlled
supersedes: null
related: [DOC-001, DOC-202, DOC-301, DOC-302, DOC-502]
---

# Data Pipeline Implementation Plan

> For agentic workers: use the executing-plans workflow, implementing each task
> with failing tests first and an independent review of the whole change.

**Goal:** deterministic, lossless source extraction and an executable annotation
contract before pilot data is collected.

**Architecture:** keep the original CSV authoritative. Generate related tables
under `data/normalised/` and preserve an exact source copy and checksum. Separate
untyped relations, unsplit indicator text, and unexplained workbook mappings
from reviewed operational records. Validate annotation bundles with JSON Schema
2020-12 plus Python cross-record and pattern-specific checks.

**Stack:** Python 3.11+, jsonschema 4.26.0, referencing 0.37.0 for offline schema resolution, and standard-library unittest. No service,
database server, annotation platform, model call, or corpus download is needed.

**Specification:** DOC-202, DOC-301, DOC-302, DOC-502 and REPO_CONTRACT.md.

## Decisions and boundaries

- New code lives in `lit_pattern/`; the existing codebook script is unchanged.
- Explicit JSON configuration owns paths, versions, vocabularies, source digest,
  relation decisions, and pattern-specific evidence requirements.
- The initial annotation schema version is `0.1.0`. Pattern versions reference
  the frozen source digest, rather than implying revised definitions.
- Bundles contain works, units, reviewers, annotations, events, and adjudications.
  Each annotation has inline located evidence; external references must resolve
  inside the supplied bundle. Uncertain annotations need evidence, but do not
  have to satisfy the positive pattern's complete evidence roles.
- Presence, function, and proposed effect remain separate fields. Absence needs
  inspected scope and adequate-inspection evidence.
- A validator confirms recorded structure and relationships. It cannot establish
  that a quotation, locator, inspection claim, or interpretation is true.
- Typed relations require explicit configuration decisions. Indicator groups and
  mapping cells remain review items until their decomposition is specified.
- SQL DDL, platform adapters, agreement statistics, real exemplars, and pilot work
  remain separate follow-up work.

## Review focus

- Duplicate JSON keys, CSV headers, IDs, empty data, and unsupported fields must
  fail explicitly instead of being silently overwritten or discarded.
- Tampered source/catalogue, stale generated files, and unsafe output directories
  must fail without modifying the authoritative source.
- Boolean timestamps, reversed spans, missing references, duplicate sequence
  order, and mismatched work/unit/modality must be rejected at their exact path.
- Positive sequential/knowledge patterns need their particular evidence roles;
  absence and uncertainty must not be forced into a positive label.
- Fixture data is invented solely to test conformance and must stay separate from
  real annotation records. Missing records never become absence annotations.

## Tasks

### Task 1: Lossless extraction

Files: `lit_pattern/common.py`, `lit_pattern/normalise.py`, `config/pipeline.json`,
`schemas/pipeline.schema.json`, `requirements.txt`, `tests/test_normalise.py`.

Interface: `normalise.build(config_path: Path) -> dict[str, bytes]` creates the
expected outputs in memory; CLI `--output` writes or `--check` compares them.

- [x] Write subprocess tests for deterministic extraction, preserved source,
  malformed source/configuration, untyped links, and stale/tampered outputs.
- [x] Observe the tests fail before implementing the modules.
- [x] Implement explicit loading, extraction, manifest, review queue, and CLI.
- [x] Run the task tests and generate the real-source outputs.

### Task 2: Annotation contract and validator

Files: `schemas/annotation.schema.json`, `lit_pattern/validate.py`,
`tests/test_annotations.py`, `tests/fixtures/annotation_cases.json`.

Interface: `validate.validate_bundle(bundle, config, patterns) -> list[dict]`
returns errors with `path`, `code`, and `message`; CLI validates a JSON bundle
against the checked source catalogue and emits a JSON report with exit status.

- [x] Write positive and named negative conformance cases from DOC-502; test the
  real CLI, malformed inputs, and missing dependency startup.
- [x] Observe failures before implementing the validator.
- [x] Add structural schema and cross-record/evidence-role validation.
- [x] Run the complete unittest suite and CLI conformance checks.

### Task 3: Documentation, atlas, and release verification

Files: contract, status, README, relevant design/verification/delivery documents,
register, use cases, changelog, and existing atlas evidence/generated outputs.

- [x] Replace stale implementation claims with observed behaviour and commands.
- [x] Document JSON format, extraction review items, versions and error codes.
- [x] Refresh the atlas after reviewing changed cited sources.
- [ ] Run full checks, independent review, fix material findings, commit and push
  the implementation branch for review.

## Execution record

Implementation is authorised by the owner's selection of normalisation and
annotation validation. Execute inline on `codex/data-pipeline`; independent
review follows verification. This plan does not authorise promotion of patterns
to `pilot_tested` or `validated`.

Task 1 and Task 2: red/green checks completed. A fresh virtual environment
installed the declared dependencies and passed the conformance suite. Ruling:
extract candidates losslessly and retain semantic review work, as required by
the source-preservation contract; no pattern statuses were upgraded.

The independent review identified five validator defects in linked-role
coverage, linked-locator separation, finite-number parsing, timezone offsets,
and dynamic schema references. Regression cases failed before the fixes; the
full 19-test-method suite then passed. The reviewer independently replayed and
confirmed all five fixes. No reviewed finding is being deferred.
