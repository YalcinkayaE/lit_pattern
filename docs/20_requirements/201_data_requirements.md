---
document_id: DOC-202
title: Data Requirements
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed data model
authority: controlled
supersedes: null
related:
  - DOC-201
  - DOC-301
  - DOC-302
---

# Data Requirements

## DR-001: Preserve provenance

The original source CSV and its checksum must remain recoverable after
normalisation. Every pattern must retain its source-workbook mapping and mapping
action.

## DR-002: Separate pattern kinds from labels

Each pattern must have one controlled label type. Adding a label type requires a
documented rationale and version consequence.

## DR-003: Store indicators as records

Each literature or video indicator must be a separate record associated with a
pattern and modality. A comma-separated cell is acceptable only in the retained
legacy source.

## DR-004: Type every pattern relation

Relations must record source pattern, target pattern, controlled relation type,
and whether the relation is symmetric. Free-text semicolon lists are legacy
source notation.

## DR-005: Keep criteria visible

Every pattern must retain a definition, inclusion criteria, exclusion criteria,
analysis unit, evidence threshold, interpretation boundary, and lifecycle status.

## DR-006: Make near-misses explicit

The operational model must support `common_false_positive` and worked negative
cases separately from generic exclusion prose.

## DR-007: Version definitions and contracts

Pattern definitions and annotation contracts must have independent versions.
Every annotation must record the versions under which it was produced.

## DR-008: Require located evidence

Every present, absent, or uncertain annotation must reference evidence or an
adequate-inspection record. A rationale alone is not a locator.

## DR-009: Distinguish evidence kinds

Evidence kinds must distinguish at least quotation, paraphrase, timestamp span,
visual description, audio description, and knowledge state.

## DR-010: Support linked events

Sequential annotations must support linked event IDs, presentation order,
optional story order, and a controlled role.

## DR-011: Retain negative cases

The model must retain invented examples, real exemplars, hard negatives,
borderline cases, adjudicated labels, rationales, and source locators.

## DR-012: Avoid false absence

The model and workflow must represent the inspected scope. Absence must not be
inferred from an uninspected or unavailable segment.

## DR-013: Separate presence, function, and effect

An annotation record must be able to identify what pattern is present without
forcing one narrative function or interpreted effect into the same label.

## DR-014: Record controlled status

Status values must come from the repository contract. Status changes must record
the evidence and date that justify them.

## DR-015: Keep private corpora external

Source works, timestamps, quotations, and participant data must be stored only
where the project has a right to retain them. Public repository records should
use stable locators, short quotations, hashes, or references to a private store.

