---
document_id: DOC-103
title: Scope and Limitations
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository
authority: controlled
supersedes: null
related:
  - DOC-101
  - DOC-201
  - DOC-502
---

# Scope and Limitations

## In scope

- Literary and audiovisual pattern definitions.
- Coding criteria, evidence rules, and analysis units.
- A versioned annotation record structure.
- A pilot that tests agreement and boundary cases.
- Provenance and open documentation.

## Out of scope for the current phase

- Claims about authorial intention or measured audience response.
- Universal meanings for symbols, colours, shots, or sounds.
- Merging a large external trope catalogue into this vocabulary without review.
- Treating generated examples as real-world exemplars.
- A production database or multi-user service.
- Public distribution of copyrighted works.

## Known limitations in the source CSV

- Status is identical across all rows.
- `evidence_required`, `annotation_rule`, `sequence_recording`, and
  `interpretation_boundary` repeat without pattern-specific differences.
- Indicators and related patterns use text lists rather than controlled records.
- Relation direction and relation kind are not encoded.
- Several definitions depend on judgement that requires worked boundary cases.
- The examples are primarily invented and cannot calibrate real-world coding.
- The analysis units are named but not operationally tested.
- Cross-media analogies are not distinguished from tested equivalence.

## Validation boundary

A parseable CSV, a passing JSON Schema, or a complete database does not show that
annotators agree. A completed pilot does not validate every pattern in the source
list. A high agreement statistic does not by itself establish construct validity,
theoretical usefulness, or audience effect.

## Security and privacy boundary

No security-sensitive runtime exists yet. Future annotation data may still
contain private or copyrighted material. Corpus paths, participant identities,
and annotation exports must not be committed without a documented basis.

