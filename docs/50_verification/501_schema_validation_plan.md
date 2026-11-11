---
document_id: DOC-502
title: Schema Validation Plan
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed annotation contract
authority: controlled
supersedes: null
related:
  - DOC-202
  - DOC-301
  - DOC-302
  - DOC-401
---

# Schema Validation Plan

## Purpose

The plan defines the intended verification scope. JSON Schema and a Python
validator now enforce the initial file contract with conformance tests. See
[the verification record](502_data_pipeline_verification.md) for commands and
coverage. Database schema checks and persistent status-history enforcement
remain future work.

## Structural checks

- CSV parses without duplicate headers.
- Pattern IDs are unique and use the accepted namespace.
- Controlled values match lookup tables.
- Required pattern fields are non-empty.
- Relation endpoints exist.
- `superseded_by` chains have no cycles.
- Work, unit, reviewer, and annotation identifiers are non-empty.
- Timestamps and dates parse.
- Evidence includes a kind and description.
- Sequential evidence includes presentation order.

## Behavioural checks

These checks must detect the named failure, not merely accept well-formed input.

1. An `absent` annotation with no inspection evidence must fail.
2. A foreshadowing annotation with one locator must fail.
3. A setup-and-payoff annotation with no connection statement must fail.
4. A red-herring annotation without corrective evidence must fail.
5. A dramatic-irony annotation without a knowledge-state record must fail.
6. A sequence event that references a missing annotation must fail where the
   contract requires a reference.
7. An annotation claiming an unsupported schema or pattern version must fail or
   be explicitly marked legacy.
8. A detached missing row must not be counted as an absence annotation.

## Conformance fixtures

Add positive fixtures that exercise complete literary, video, sequential, and
knowledge-asymmetry records. Add negative fixtures for each failure above.

Each negative fixture should identify the expected error path. A test that only
checks "schema rejected" cannot show that the intended rule is working.

## Cross-record checks

Use code alongside JSON Schema where dependencies span records:

- referenced pattern IDs exist;
- referenced annotation or event IDs exist;
- version combinations are permitted;
- relation symmetry is consistent;
- status history is append-only;
- adjudication references retained original annotations;
- sequence presentation orders are unique where the protocol requires it.

## Reporting

Verification output must include:

- source revision or checksum;
- schema version;
- validator version;
- fixture set version;
- commands run;
- pass and fail counts;
- expected versus actual error paths;
- unresolved warnings.

Schema verification is separate from taxonomy validation. It establishes record
shape and enforceable rules, not agreement, validity, or usefulness.

