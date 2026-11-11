---
document_id: DOC-804
title: Tooling and Corpus Requirements
status: reference
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: pilot and implementation planning
authority: informative
supersedes: null
related:
  - DOC-401
  - DOC-501
  - DOC-502
---

# Tooling and Corpus Requirements

This is a decision reference. The file pipeline now uses jsonschema 4.26.0,
pinned with referencing 0.37.0 in `requirements.txt`, with standard-library unittest for its tests.
Other packages and annotation platforms below remain candidates; no annotation
platform integration has been implemented.

## Minimum local tooling

- Python 3.11 or later for generators, validation, and agreement analysis.
- Python standard library for the current codebook generator.
- jsonschema 4.26.0 for pipeline configuration and annotation JSON Schema checks.
- SQLite, normally bundled with Python, for the first relational store.
- Git for source and schema history.

Add dependencies only when their tests and import path exist:

- `pytest` for conformance tests;
- `pandas` or DuckDB for exploratory tabular analysis;
- `scikit-learn`, `statsmodels`, `krippendorff`, or another reviewed implementation
  for agreement statistics;
- `ruff` for Python linting.

Avoid DVC, a database server, or a commercial annotation service until the pilot
requirements justify them.

## Annotation platform candidates

The choice depends on the selected corpus.

| Candidate | Likely use | Trade-off |
|---|---|---|
| INCEpTION | Text annotation with custom layers and human review | Requires configuration and an export path to the repository schema |
| CATMA | Humanities close reading and text annotation | Needs an explicit mapping to the proposed pattern records |
| ELAN | Timestamped audiovisual annotation | Best suited to video sequences, but text and relational export require adaptation |
| Advene | Structured video annotation | Requires checking fit with the pattern and evidence model |
| VIA | Lightweight visual or video marking | Limited fit for complex cross-record constraints |
| Locked spreadsheet | Small pilot fallback | Manual validation is needed and concurrency is poor |

Do not select one until the pilot works and unit types are fixed.

## Reference standards

- RFC 4180 for CSV quoting, or an explicit choice of another interchange format.
- JSON Schema 2020-12 for a future annotation contract.
- ISO 8601 for dates and timestamps.
- ISO 639 language codes for work metadata where needed.
- Dublin Core for basic work metadata if later interoperability requires it.
- Krippendorff's alpha, Cohen's kappa, and Fleiss' kappa references for the
  agreement analysis design actually used.

## Corpus requirements

### Literature

- Two or three works for the pilot, ideally spanning different periods or
  styles.
- Reliable edition metadata.
- Stable page, chapter, or paragraph locators.
- Lawful access and storage.
- A plain-text or structured copy for searching where permitted.

### Video

- Two or three films or episodes with fixed release versions.
- Stable timestamps tied to the exact version.
- Lawful access and storage.
- Logged differences between theatrical, festival, broadcast, and streaming cuts.

### Cases

- One located exemplar per pilot pattern.
- One hard negative per pilot pattern.
- One or two borderline cases per pilot pattern.
- Rationales and adjudicated labels for borderline cases.
- Separation between invented teaching examples and observed corpus evidence.

Do not commit full copyrighted works or private corpora to a public repository.
Use permitted short quotations, locators, hashes, and a private storage reference
where necessary.

