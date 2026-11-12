---
document_id: DOC-002
title: Repository Status
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-12
applies_to: repository
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-003
---

# Repository Status

This document records observed repository state. Plans and design proposals are
not evidence that the proposed functionality exists.

## Observed on 2026-11-11

- `/Users/erkanyalcinkaya/projects/lit_pattern` is an independent Git working
  tree initialised on 2026-11-11.
- `literary_and_video_patterns.csv` is present.
- The CSV parses with Python's `csv.DictReader`.
- The CSV has 59 data rows and 18 columns.
- All 59 `pattern_id` values are non-empty and unique.
- Every row has status `Proposed; not yet validated on a labelled corpus`.
- Public distribution and the MIT and CC BY 4.0 licence split were confirmed by
  the repository owner on 2026-11-11.
- Published on 2026-11-11 at
  [YalcinkayaE/lit_pattern](https://github.com/YalcinkayaE/lit_pattern).
- GitHub reports public visibility and `main` as the default branch. The local
  `origin` points to that repository and `main` tracks `origin/main`.
- The hosted README includes the use-case and repository-atlas links. The hosted
  `LICENSE` matches the local MIT and CC BY 4.0 text; GitHub reports
  `NOASSERTION` for automatic classification of the combined licence file.
- The source SHA-256 is
  `a6bc51c4d6cdf61f6fc488164e8bc4d43e64b2cb350e3b149ed21653fb8c2f7d`.
- Four source fields are identical across all 59 rows: `evidence_required`,
  `annotation_rule`, `sequence_recording`, and `interpretation_boundary`.

## Observed on 2026-11-12

- GitHub repository renamed from `YalcinkayaE/lit_pattern` to
  [YalcinkayaE/literary-audiovisual-patterns](https://github.com/YalcinkayaE/literary-audiovisual-patterns).
  The previous URL redirects. The Python package name remains `lit_pattern`.

## Implemented

- Repository control and documentation structure.
- A codebook generator.
- Deterministic extraction CLI and checked derived tables under `data/normalised/`.
- An exact copy of the source CSV and hash manifest in the extraction.
- Proposed annotation JSON Schema 0.1.0 and executable structural/cross-record
  validator, including absence and five pattern-specific evidence rules.
- Conformance tests using invented fixtures, separate from any pilot evidence.
- A generated `CODEBOOK.md`.
- Proposed data, annotation, boundary, pilot, and validation plans.
- Evidence-backed repository atlas with a refresh and freshness-check helper.
- Concrete use cases with current capabilities and future prerequisites separated.

## Not implemented

- Fully reviewed operational indicators, typed relations, and decomposed mappings.
- SQL DDL and database persistence.
- Platform-specific import/export adapters.
- Persistent append-only status-history enforcement.
- Annotation-tool integration.
- Real pilot cases and adjudications.
- Agreement analysis.

## Claims not yet supported

- That the pattern definitions are reliable.
- That the label types are mutually exclusive.
- That literary and audiovisual indicators are equivalent.
- That the proposed success threshold for a pilot is appropriate.
- That any pattern is `pilot_tested` or `validated`.
- That a valid file format or successful schema load establishes taxonomy
  quality.

## Required next action

Review the extraction queue without changing pattern meaning, select lawful
pilot cases, and review the proposed annotation contract against those cases.
Then perform the independent coding and adjudication described in `PILOT.md`.

Repository-owner public contact metadata remains unresolved. It does not block
publication of the current documentation set, but it should be recorded in the
controlled-document headers when supplied.

