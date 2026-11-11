---
document_id: DOC-301
title: Normalised Data Model
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed data model
authority: controlled
supersedes: null
related:
  - DOC-202
  - DOC-302
  - DOC-303
---

# Normalised Data Model

This is a design proposal. No SQLite or PostgreSQL schema is implemented in this
repository yet.

## Core entities

| Entity | Purpose | Main key |
|---|---|---|
| `label_type` | Controlled pattern-kind vocabulary | `label_type` |
| `analysis_unit` | Working definitions and segmentation instructions | `unit_type` |
| `status` | Pattern lifecycle values | `status` |
| `relation_type` | Typed and directed or symmetric pattern relations | `relation_type` |
| `mapping_action` | Provenance action against the original workbook | `action` |
| `modality` | Literature or video context | `modality` |
| `pattern` | Pattern definition and coding criteria | `pattern_id` |
| `indicator` | One literature or video cue per record | `indicator_id` |
| `pattern_relation` | Typed link between two patterns | Composite |
| `workbook_mapping` | Pattern-to-workbook-cell provenance | Composite |
| `evidence_rule` | Global default or pattern-specific evidence rule | `rule_id` |
| `pattern_example` | Invented, exemplar, hard-negative, or borderline case | `example_id` |
| `annotation` | A reviewer's coding decision for one unit and pattern | `annotation_id` |
| `annotation_evidence` | Located evidence linked to an annotation | `evidence_id` |
| `sequence_link` | Event ordering and role for sequential patterns | Sequence and event |

## Pattern fields

The minimum operational pattern record contains:

- `pattern_id`
- one controlled `label_type`
- `label`
- `definition`
- `inclusion_criteria`
- `exclusion_criteria`
- `common_false_positive`
- `evidential_threshold`
- `analysis_unit`
- `creative_use`
- `interpretation_boundary`
- one controlled lifecycle status
- status date and evidence reference
- schema version
- pattern version
- optional `superseded_by`

## Relation vocabulary

| Relation | Symmetric | Working meaning |
|---|---|---|
| `contrasts_with` | Yes | Opposed in function or effect |
| `co_occurs_with` | Yes | Frequently present in the same unit |
| `commonly_confused_with` | Yes | A near-miss that boundary guidance should disambiguate |
| `prerequisite_for` | No | A must be established for B to operate |
| `subtype_of` | No | A is a narrower case of B |
| `analogue_in_other_media` | No | Proposed cross-media realisation, tested or untested |
| `extends` | No | One pattern generalises or supersedes another |

The previous short list stored in `related_patterns` does not identify which
relation applies. It must not be imported as a typed relation without review.

## Annotation constraints

An annotation must include:

- annotation ID;
- work identity and version;
- unit ID, unit type, and locator;
- pattern ID;
- presence state;
- rationale;
- evidence records;
- modality;
- reviewer;
- schema version and pattern version;
- creation time;
- optional adjudication record.

Pattern-specific constraints should be represented as data or validated rules,
not only prose. Examples:

- foreshadowing requires a cue locator and a later payoff locator;
- setup and payoff requires setup, payoff, and a supported connection;
- red herring requires a misleading cue, invited inference, and corrective
  evidence;
- unreliable narration requires a claim and work-level disconfirming evidence;
- dramatic irony requires a knowledge-state map.

## Storage choice

Use normalised CSV or JSONL first for a small pilot. SQLite is the likely next
step for relational constraints and queries. PostgreSQL is not justified until
multi-user access or concurrent annotation requirements exist.

## Migration rules

1. Preserve the original CSV unchanged.
2. Extract one entity at a time with a deterministic script.
3. Compare generated row counts and stable identifiers with the source.
4. Record unresolved text that cannot be assigned to a controlled value.
5. Do not silently split semicolon or comma text into relations or indicators
   when the boundaries are ambiguous.
6. Add schema versioning before annotation data is collected.

