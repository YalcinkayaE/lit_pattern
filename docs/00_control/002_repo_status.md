---
document_id: DOC-002
title: Repository Status
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
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
- The source SHA-256 is
  `a6bc51c4d6cdf61f6fc488164e8bc4d43e64b2cb350e3b149ed21653fb8c2f7d`.
- Four source fields are identical across all 59 rows: `evidence_required`,
  `annotation_rule`, `sequence_recording`, and `interpretation_boundary`.

## Implemented

- Repository control and documentation structure.
- A codebook generator.
- A generated `CODEBOOK.md`.
- Proposed data, annotation, boundary, pilot, and validation plans.

## Not implemented

- Normalised source tables.
- SQL DDL.
- Annotation JSON Schema.
- Schema conformance tests.
- Import and export tools.
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

Configure the public Git remote and publish the initial repository. Then
normalise the source vocabulary without changing pattern meaning. After that,
add conformance checks and prepare the pilot cases.

Repository-owner public contact metadata remains unresolved. It does not block
publication of the current documentation set, but it should be recorded in the
controlled-document headers when supplied.

