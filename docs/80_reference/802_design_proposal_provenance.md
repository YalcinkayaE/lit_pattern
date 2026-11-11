---
document_id: DOC-802
title: Design Proposal Provenance
status: reference
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: initial documentation set
authority: informative
supersedes: null
related:
  - DOC-001
  - DOC-101
  - DOC-201
---

# Design Proposal Provenance

## Source

The initial repository documentation is based on an owner-supplied conversation
with DeepSeek on 2026-11-11. The conversation reviewed the benefits and limits of
the pattern database and proposed:

- normalising the flat CSV into linked pattern, indicator, relation, mapping,
  evidence-rule, example, and annotation entities;
- typed relation vocabularies and explicit direction or symmetry;
- formal analysis-unit definitions;
- a pattern lifecycle that records evidence rather than a uniform disclaimer;
- pattern-specific evidence rules;
- real exemplars, hard negatives, and borderline cases;
- boundary matrices for the sequential and irony clusters;
- a small mixed-media pilot;
- JSON Schema and conformance-test follow-up work.

The pasted conversation also included generated SQL, CSV rows, matrices, JSON
Schema text, and examples. Those are design drafts, not independent evidence.

## How the proposal is treated

The conversation is informative. Its recommendations have been rephrased into
controlled documents and kept subordinate to `REPO_CONTRACT.md` and the original
CSV. Proposed artefacts that were not actually placed, parsed, or tested in this
repository are not described as implemented.

## Corrections made during repository initialisation

- The final conversation text refers to 48 patterns. The provided CSV contains
  59. Repository documents use 59 because that is the observed source count.
- The conversation's SQL and JSON documents were not copied as authoritative
  implementation files. The repository records them as proposed designs.
- Boilerplate was not described as per-pattern evidence guidance. The source CSV
  repeats identical default text in all 59 rows.
- The pilot threshold was retained as a proposal and marked for review rather
  than treated as an accepted criterion.

## Verification limit

This provenance note confirms where the design ideas came from. It cannot verify
the factual accuracy of every claim generated in that conversation. Those claims
must be checked against source data or empirical results before use.

