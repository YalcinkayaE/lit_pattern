---
document_id: DOC-302
title: Annotation Workflow
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed annotation contract
authority: controlled
supersedes: null
related:
  - DOC-201
  - DOC-202
  - DOC-301
  - DOC-501
---

# Annotation Workflow

## 1. Register the work

Record a work ID, title, modality, edition or release version, and the storage
location or permitted access basis.

## 2. Segment the unit

Define the unit before coding. Record its type, start and end locator, and any
ambiguity in segmentation. Do not change unit boundaries after seeing a
convenient pattern.

## 3. Apply pattern criteria

Use the inclusion criteria first. Apply the exclusion criteria and near-miss
guidance before assigning presence. Multiple labels are allowed only when each is
independently supported.

## 4. Record evidence

Provide a short quotation, description, or timestamp span with a stable locator.
For video, describe the relevant channel: image, speech, sound, music, or
editing. For knowledge asymmetry, record who knows what and when.

## 5. Record sequence relationships

For sequential patterns, link event IDs in presentation order. Add story order
only where it is recoverable. Assign roles only where evidenced:

- setup;
- expectation;
- disruption;
- reveal;
- consequence.

## 6. Recuse or mark uncertainty

Use `uncertain` when evidence is incomplete or interpretations remain genuinely
competitive. Use `not_applicable` when the pattern cannot meaningfully apply to
the unit. Use `absent` only after adequate inspection.

## 7. Record rationale

The rationale must explain which criteria are satisfied and which near-miss was
excluded. "I know it when I see it" is not a usable coding rationale.

## 8. Adjudicate disagreements

Preserve both original annotations. An adjudicator records the final decision,
the rule or evidence used, and whether the result changes the codebook.

## 9. Version

Store schema and pattern versions on every annotation. If a definition changes,
do not overwrite the annotations made under the earlier definition.

## 10. Report by scope

Report counts by inspected unit, pattern, reviewer, modality, and version. A
missing row is not an absence annotation. An uninspected corpus is not a negative
sample.

