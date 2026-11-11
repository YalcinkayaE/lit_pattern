---
document_id: DOC-503
title: Data Pipeline Verification
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: file pipeline 0.1.0
authority: evidence
supersedes: null
related: [DOC-001, DOC-304, DOC-402, DOC-502]
---

# Data Pipeline Verification

## Scope and source

File conformance checks on 2026-11-11, using Python 3.14.5 and jsonschema 4.26.0.
Python 3.11 is the declared minimum; it has not been separately exercised here.
The source SHA-256 is
`a6bc51c4d6cdf61f6fc488164e8bc4d43e64b2cb350e3b149ed21653fb8c2f7d`.
Schema, normalisation, validator, and fixture-set versions are `0.1.0`.
The invented fixtures in `tests/fixtures/` are not pilot records.

## Commands and observed checks

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised --check
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/literary.json
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/video.json
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/knowledge.json
.venv/bin/python scripts/generate_codebook.py --check
.venv/bin/python docs/80_reference/repo_context/repo_context.py check --root . --context docs/80_reference/repo_context
```

The executable tests assert specific error codes and paths, including:

| Negative case | Expected code | Expected path |
|---|---|---|
| Absence without inspection | `inspection_required` | `$.annotations[0].evidence` |
| Foreshadowing with one distinct locator | `distinct_locators` | `$.annotations[0].evidence` |
| Setup/payoff without connection | `connection_required` | `$.annotations[0].connection` |
| Red herring without correction | `evidence_roles` | `$.annotations[0].evidence` |
| Dramatic irony without knowledge map | `knowledge_required` | `$.annotations[0].evidence[0].knowledge` |
| Event referencing missing annotation | `unknown_annotation` | `$.events[0].annotation_id` |
| Unsupported definition version | `pattern_version` | `$.annotations[0].pattern_version` |

The missing-row case supplies no annotation or event: the observed absence count
must remain zero. Other tests cover malformed/duplicate-key JSON, missing
dependencies, source/configuration failures, preserved source bytes, deterministic
outputs, unowned directories, stale catalogues, endpoint checks, and explicit
relation decisions. Unrelated evidence cannot satisfy the distinct-locator rule.

## Open verification boundaries

- Indicator groups, relation typing, mapping rationale, and missing per-pattern
  guidance remain unresolved extraction review items.
- No SQL schema, persistent status history, platform adapter, agreement analysis,
  or real pilot data has been tested.
- Evidence truth, annotation adequacy, and taxonomy reliability require human
  review and the separate pilot protocol.

## Observed results

- Fresh `.venv` installed the declared requirements; the suite passed 19 test
  methods, with parameterised/subtest coverage for additional cases.
- The three checked-in positive fixture bundles returned exit 0, `valid: true`,
  and no errors. Each report counted one supplied annotation and no absences.
- Extraction freshness, exact source preservation, manifest hashes, codebook
  consistency, and local documentation links passed their checks.
- Independent review found five validator defects. Regression tests reproduced
  the defects, then passed after fixes to linked-role/event coverage,
  linked-locator separation, finite-number parsing, RFC 3339 offset ranges, and
  offline dynamic-reference resolution. The reviewer replayed all five original
  reproductions and confirmed rejection, including zero network calls for an
  external dynamic reference. Unresolvable local references also failed with
  explicit input errors.

The implementation branch started from `0f59ebb`; the reviewed implementation
commit is `b81eaa0`. Tests and fixtures travel with that commit.
[Draft pull request 1](https://github.com/YalcinkayaE/lit_pattern/pull/1) records
the publication and keeps integration into `main` pending. The
checks above are local conformance evidence, not hosted CI or pilot results.
