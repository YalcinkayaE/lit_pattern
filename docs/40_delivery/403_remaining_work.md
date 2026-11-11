---
document_id: DOC-403
title: Remaining Work
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository delivery backlog
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-002
  - DOC-202
  - DOC-301
  - DOC-304
  - DOC-401
  - DOC-402
  - DOC-501
  - DOC-502
  - DOC-503
---

# Remaining Work

This is the actionable checklist for work remaining after the initial file
pipeline implementation. It follows the
[repository contract](../../REPO_CONTRACT.md) and
[delivery sequence](401_implementation_plan.md); it does not replace their
scope or acceptance rules. The order below is proposed, with conditional work
identified separately.

At creation on 2026-11-11, [PR 1](https://github.com/YalcinkayaE/lit_pattern/pull/1)
is open and draft. The extraction and annotation validator are implemented on
`codex/data-pipeline`, with local conformance evidence in
[DOC-503](../50_verification/502_data_pipeline_verification.md). Integration into
`main`, semantic review, and empirical pilot work remain open.

Mark an item complete only when its output and verification can be linked from
this checklist. Keep unresolved cases and decisions visible.

## Integrate and verify the implementation

- [ ] Review PR 1 against the contract, file format, and recorded verification;
  record the disposition of any further findings.
- [ ] Exercise the declared minimum Python 3.11 in a fresh environment. Record
  interpreter/dependency versions and run the suite, extraction freshness,
  fixture validation, codebook consistency, and atlas checks. Existing recorded
  execution used Python 3.14.5.
- [ ] Verify a fresh clone preserves the original CSV and retained source copy
  byte-for-byte, including their checksum and Git line-ending attributes.
- [ ] Add GitHub Actions checks for Python 3.11 and 3.14 before merging. Run the
  conformance suite, source preservation, generated-data freshness, all positive
  fixture validations, codebook consistency, and atlas freshness. Record hosted
  results separately from existing local verification.
- [ ] Move PR 1 out of draft and merge after review approval. Verify the checks
  on the resulting `main` revision and update branch-specific status references.

## Complete repository control decisions

- [ ] Clarify the scope of DOC-002: distinguish published `main`, the current
  implementation branch, and pending PR integration. Date observed Git metadata
  and refresh it from Git when reporting status rather than treating a recorded
  commit hash as permanently current.
- [ ] Keep status authority in the existing contract, DOC-002, and this checklist.
  Adjust orientation guidance to use them instead of creating a competing dated
  status-baseline document solely to satisfy a skill's filename convention.
- [ ] Correct runtime summaries to name both declared dependencies:
  `jsonschema==4.26.0` and `referencing==0.37.0`, consistent with requirements.txt.
- [ ] Obtain the owner's intended public contact identity and update unresolved
  owner metadata in controlled documents.
- [ ] Decide whether reviewed operational data will use normalised CSV, SQLite,
  or both, using actual pilot requirements. Keep the original CSV authoritative
  until an explicit contract change is approved and the replacement is checked.

## Rehearse with real cases before broad semantic review

- [ ] Choose real literary and video cases for existing pilot patterns such as
  STR05 and STR09. Record editions/releases, locators, and lawful access without
  changing the formal pilot sample or committing private corpus material.
- [ ] Record the cases in annotation bundles, run the validator, and have another
  reader inspect the evidence and decisions. Capture representation problems,
  ambiguous criteria, and differences in interpretation.
- [ ] Use the rehearsal findings to prioritise contract changes and semantic
  review. Keep this rehearsal distinct from the formal pilot and its independent
  coding rounds; it does not by itself justify a pattern-status change.

## Resolve the semantic extraction queue

Use [review_items.json](../../data/normalised/review_items.json),
[the manifest](../../data/normalised/manifest.json), and the original source
rather than editing generated tables by hand. The following is the queue at
checklist creation, not evidence that the flagged content is wrong.

| Review kind | Current scope | Required resolution |
|---|---|---|
| Indicator segmentation | 118 literature/video source cells | Identify discrete cues without losing qualifications or source text |
| Relation typing | 59 source-row flags covering 137 listed ID pairs | Review meaning, direction, symmetry, and rationale; no typed decisions are configured yet |
| Workbook mapping rationale | 59 mapping cells | Recover locators, actions, and reasons, retaining any source gaps |
| Common false positives | 59 pattern flags | Supply realistic near-misses separately from general exclusion prose |
| Evidential thresholds | 59 pattern flags | State the located support needed for a coding decision |

- [ ] Add structured review-decision records with a source reference, decision,
  rationale, reviewer, definition version, and disposition. Preserve accepted,
  rejected, and unresolved outcomes without changing pattern lifecycle status.
- [ ] Derive outstanding review items from those records. The current extractor
  emits flags unconditionally, including relation-typing flags when configured
  decisions exist. Test that regeneration keeps completed decisions closed,
  retains unresolved cases, and reopens affected items when their cited source
  or definition version changes.
- [ ] Segment indicator cells into reviewed cue records with modality and source
  traceability. Preserve composite or ambiguous cases for explicit resolution.
- [ ] Review each listed relation. Record accepted typed decisions and rationale
  in configuration; retain rejected or unresolved candidates without treating
  the source list as an established graph.
- [ ] Decompose workbook mappings and document whether each item was kept,
  corrected, reframed, relocated, redefined, or added as an extension. Inspect
  the original workbook where available; record missing source evidence.
- [ ] Add worked false-positive guidance and per-pattern evidence thresholds,
  prioritising the pilot sample. Keep invented teaching cases separate from
  located empirical cases.
- [ ] Extend the extraction inputs and outputs to carry reviewed indicator and
  mapping decisions. Add tests for source traceability, row/ID reconciliation,
  and ambiguous transformations before closing those queue items.
- [ ] Regenerate and check the tables, review queue, and manifest. Record each
  resolved decision and verify that the original source and checksum remain
  unchanged. A successful extraction alone does not close semantic review.

## Review the annotation contract for pilot use

- [ ] Review [the proposed file contract](../30_design/304_annotation_file_contract.md)
  against the real-case rehearsal findings. Record gaps in unit design,
  locators, evidence roles, or uncertainty handling and their disposition.
- [ ] Assess pattern-specific rule coverage for the pilot sample. The current
  positive rules cover STR05, STR06, STR07, STR09, and STR10; add further rules
  only with an explicit rationale and positive/negative conformance cases.
- [ ] Define how annotation history and status decisions will be retained
  persistently. Implement append-only status-history enforcement before a
  workflow permits status updates; current checks validate one supplied bundle.
- [ ] Record schema and definition-version consequences for any changes and
  retain earlier annotations under the versions that produced them.

## Prepare the pilot

Follow [PILOT.md](../../PILOT.md); this checklist does not change its proposed
sample, unit counts, measures, or stop conditions.

- [ ] Confirm the pilot pattern sample before coding and record any change with
  its reason.
- [ ] Select lawfully accessible literary and audiovisual works. Record exact
  editions/releases, stable locators, access rights, and private storage routes.
- [ ] Prepare the real exemplar, hard negative, borderline case, and invented
  teaching example required for each pilot pattern. Record rationale and
  adjudication material separately from first-round independent coding.
- [ ] Fix unit boundaries, inspected scope, work/unit identifiers, and annotation
  instructions before coding begins.
- [ ] Choose the text/video annotation tool or file workflow after the corpus and
  unit types are fixed. Demonstrate a complete export/validation route using the
  selected workflow; keep copyrighted works and private records out of Git.
- [ ] Recruit the annotators specified by the pilot protocol and prepare their
  materials. Withhold boundary matrices during the first independent round as
  the protocol requires.
- [ ] Review the provisional agreement threshold and choose measures suited to
  the final coding design before observing results. Freeze a dated protocol,
  codebook, schema, and pattern-version reference for the round.
- [ ] Implement and independently test the selected agreement calculations,
  including missing annotations and the actual coding categories. Missing rows
  must remain missing rather than becoming absence labels.

## Run, adjudicate, and revise

- [ ] Collect independent annotations, validate their records, and retain every
  original export and disagreement.
- [ ] Report per-pattern agreement with raw agreement, the selected coefficient,
  unit/annotator counts, coding categories, inspected scope, and uncertainty.
- [ ] Adjudicate against located evidence and the boundary guidance, keeping the
  original decisions and unresolved cases.
- [ ] Revise definitions or boundary matrices only where observations support
  the change. Apply the required schema/definition versions and mapping rationale.
- [ ] Run a second round if the first exposes material instability, recording
  the revised materials and resulting observations.
- [ ] Record pattern status decisions against the contract and fixed protocol.
  Distinguish `pilot_tested` from `validated`; do not extend a result to patterns
  or modalities that were not evaluated.
- [ ] Publish a dated verification report using permitted locators, short
  quotations, hashes, or private references. Update the contract, status, source
  views, and repository atlas consistently with the recorded outcome.

## Conditional later work

These items are not prerequisites for starting the pilot unless the selected
workflow makes them necessary.

- [ ] If SQLite is selected, add SQL DDL, migration and integrity tests, and a
  demonstrated round trip from the reviewed files.
- [ ] If an annotation platform is selected, implement the needed adapter and
  test preservation of IDs, evidence, order, versions, and reviewer decisions.
- [ ] If LLM pre-annotation is pursued, fix model/prompt versions, use a held-out
  human-coded comparison set, and measure errors with and without exclusion
  guidance. Retain human review and rejected suggestions.
- [ ] If teaching or creative workbooks are produced, pair invented practice
  material with located cases and teacher/editor review before assessment use.

Multi-user services, broad ontology alignment, and large-scale model annotation
remain deferred under the delivery plan. Public corpus distribution remains
outside the repository's current scope.
