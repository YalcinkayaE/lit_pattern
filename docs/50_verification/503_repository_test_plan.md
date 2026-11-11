---
document_id: DOC-504
title: Repository Test Plan
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: file pipeline verification and pilot preparation
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-202
  - DOC-304
  - DOC-403
  - DOC-501
  - DOC-502
  - DOC-503
---

# Repository Test Plan

## Purpose and authority

Define how to test the implemented file pipeline, close its verification gaps,
and assess whether it can support a real-case rehearsal and formal pilot.
This is a proposed execution plan, not a new test-result report.

- [REPO_CONTRACT.md](../../REPO_CONTRACT.md) governs scope and status claims.
- [DOC-502](501_schema_validation_plan.md) defines schema/workflow expectations.
- [DOC-304](../30_design/304_annotation_file_contract.md) defines the current file
  format, commands, supported pattern rules, and limitations.
- [DOC-503](502_data_pipeline_verification.md) records earlier observed results.
- [PILOT.md](../../PILOT.md) owns the empirical study design and status gates.
- [DOC-403](../40_delivery/403_remaining_work.md) tracks delivery actions.

The TC identifiers below name test groups defined by this plan. They are not
new data requirements or pattern lifecycle states.

## Inspected baseline

On 2026-11-11, branch `codex/data-pipeline` at `19c64b8` was inspected and the
current suite rerun. All 19 unittest methods passed on Python 3.14.5 with
jsonschema 4.26.0 and referencing 0.37.0. `pip check` found no broken requirements.
Methods include subtests; the count is not a coverage percentage or an empirical
sample size.

The inspected source is
`a6bc51c4d6cdf61f6fc488164e8bc4d43e64b2cb350e3b149ed21653fb8c2f7d`.
Schema, normalisation, validator, and fixture-set versions are `0.1.0`.
The definition-version token is `source-` plus the complete source digest.

Existing tests live in [test_normalise.py](../../tests/test_normalise.py) and
[test_annotations.py](../../tests/test_annotations.py). Invented fixture bundles
and their version manifest live in [tests/fixtures](../../tests/fixtures).
The matrix distinguishes assertions already present from proposed additions.

## Scope

In scope for the current implementation:

- source preservation, deterministic extraction, and generated-file freshness;
- explicit configuration, input parsing, and dependency failures;
- schema conformance and work/unit/pattern/reviewer/evidence references;
- versions, modality, locators, event ordering, inspection and knowledge records;
- positive evidence rules currently configured for STR05, STR06, STR07, STR09,
  and STR10;
- CLI reports, exit codes, output-directory protection, and offline schemas;
- codebook and repository-atlas consistency;
- clean-checkout execution on Python 3.11 and 3.14.

Semantic review decisions, persistent status history, database storage, platform
adapters, and agreement calculations need additional implementation. Their
planned tests are identified separately below. There is no agreed performance
budget, deployment target, or service availability requirement to test here.

File conformance does not prove evidence truth, adequate inspection, a sound
interpretation, annotator agreement, authorial intention, or audience response.
Those questions require the rehearsal and empirical protocol.

## Environments and test data

Run automated verification in separate clean checkouts on Python 3.11 and 3.14.
Use the repository's requirements.txt and an ignored `.venv` in each checkout.
Record actual interpreter and dependency versions; do not substitute an available
newer interpreter for the declared minimum without recording the gap.

Use the original CSV as the source-preservation oracle. Use temporary copies
for malformed-source/configuration cases and temporary output directories for
write-failure tests. Never corrupt the authoritative CSV or retained source copy
in the working repository to perform a negative test.

Use the checked-in invented literature, video, and knowledge fixtures for
conformance. Derive negative inputs by changing one condition at a time. Store
real works and private annotation records outside version control; retain
permitted locators and access metadata for human review.

Expected values must be derived independently of the implementation: compare
source bytes and canonical IDs, assert named error codes/paths, and use manually
checked numerical examples for future agreement calculations. An expectation
computed by the same production helper is not an independent oracle.

## Current implementation test matrix

“Baseline” means an explicit assertion was found in the inspected tests; it does
not mean every input in that test group is covered. Proposed additions below
are not implemented or passing merely because they appear in this plan.

| ID | Objective and expected result | Baseline coverage | Additions needed |
|---|---|---|---|
| TC-01 | Preserve exact source bytes/checksum and reconcile extracted pattern IDs; repeated extraction and `--check` agree | `test_lossless_deterministic_extraction_and_review_queue` | Fresh-clone checks on both interpreters, with default checkout and `core.autocrlf=true`; verify all output hashes and full ID/field reconciliation |
| TC-02 | Reject malformed source/configuration before output changes | `test_invalid_source_and_configuration_fail_explicitly`, `test_source_digest_mismatch_and_missing_config_fail`, namespace case in `test_explicit_typed_relations_and_invalid_source_namespace` | Empty/header-only input, wrong row widths, malformed quoting, unknown vocabularies/statuses, invalid configuration types and contradictory rule references; assert unchanged source/output on failure |
| TC-03 | Protect source and unrelated output data; reject unsafe destinations | `test_rejects_unowned_or_source_directory`, `test_unowned_manifest_and_extra_files_are_not_overwritten` | Output-directory/file symlinks, non-directory targets, and permission failures where the test account can enforce them; verify no unrelated target changes |
| TC-04 | Detect stale, missing, tampered, or extra catalogue files | `test_stale_or_extra_output_is_detected_by_check`, `test_checked_in_fixtures_and_tampered_catalogue`, extra-file cases | Delete or alter each generated file in isolated copies, not just patterns.csv; check manifest/configuration drift and verify `--check` never repairs files |
| TC-05 | Keep untyped candidates separate; admit only valid configured typed decisions | Candidate assertions and explicit symmetric relation test in test_normalise.py | Unknown types/endpoints, duplicate decisions, reverse duplicates for symmetric types, directed decisions, and invalid rule pattern IDs |
| TC-06 | Reject malformed/duplicate-key/non-finite JSON, unknown fields, and missing required fields | `test_structure_malformed_json_stale_catalogue_and_dependency`, overflow regression | Expand required-field/type/empty-value cases across bundle collections; verify malformed schemas and configuration fail explicitly |
| TC-07 | Enforce unique IDs and resolve all work/unit/pattern/reviewer/evidence references | `test_reference_integrity_ids_order_spans_and_knowledge` covers duplicate work and missing unit/reviewer/event evidence; other cases check missing annotation references | Duplicate unit/reviewer/annotation/event/evidence/adjudication IDs; unknown work/pattern; unit-work, pattern-unit, work-modality and locator-modality mismatches |
| TC-08 | Enforce source, envelope/schema, annotation/schema, and definition versions | Unsupported pattern version and stale catalogue cases | Wrong bundle source digest, unsupported envelope and annotation schema versions, missing version fields, and valid version combinations |
| TC-09 | Validate numeric spans and RFC 3339 timestamps | Reversed span, Boolean start, missing seconds, invalid date, invalid offset, overflow and lowercase date-time cases | Equal endpoints, negative endpoints, invalid calendar dates/timezones, and valid offset/fractional-second boundaries |
| TC-10 | Keep `present`, `absent`, `uncertain`, `not_applicable`, and missing annotations distinct | Named absence case, nonpositive-state test, and empty-annotation count assertion | Independently remove scope or adequacy from an inspection; reject empty evidence for present/uncertain; assert all reported state counts on mixed bundles |
| TC-11 | Enforce positive evidence roles, linked distinct locators, connections, and event order | Positive five-pattern cases, DOC-502 negative cases, duplicate order/missing references, and linked/unlinked-evidence regressions | Event-count boundary cases, negative/Boolean order fields, independently valid event chains for multiple annotations, and unknown/duplicate evidence-role edge cases |
| TC-12 | Enforce knowledge asymmetry and retained adjudication inputs | Positive STR10, missing knowledge map, identical knowledge states, and missing original annotation cases | Duplicate holder/information pairs; unknown adjudicator; cross-work/unit/pattern adjudication; complete valid retained-adjudication bundle |
| TC-13 | Keep schema resolution offline and report invalid schemas explicitly | `test_external_dynamic_reference_is_rejected_before_validation`; earlier independent-review replay recorded in DOC-503 | Automated zero-network assertions for external `$ref` and `$dynamicRef`; unresolved local references and invalid schema tests at the public CLI boundary |
| TC-14 | Preserve CLI/report contract, dependency failures, and generated documentation | Existing subprocess tests assert selected success reports, errors and exits; missing dependency startup is exercised | Missing/unreadable input files, complete success/failure report fields, non-mutation of input bundles, codebook/atlas checks in hosted CI, and readable configuration/schema errors without tracebacks |

For TC-02/05, a test exposing an accepted contradictory configuration is a
finding to resolve before claiming that configuration is validated. Adding a
negative test must not silently redefine valid pattern semantics.

For permission/symlink cases, record the operating system and privileges. A case
that cannot exercise the failure must be reported as not run or inapplicable,
with a reason, rather than passed.

## Pattern-specific acceptance cases

Retain the existing positive fixtures and pair every new rejection case with a
nearby valid case. Check the intended error path/code, not only nonzero exit.

| Pattern/state | Valid control | Negative change and expected diagnostic |
|---|---|---|
| STR05 present | Cue and later event have distinct locators and linked events in order | Remove a required role: `evidence_roles`; remove its linked event: `sequence_roles`; reverse the chain: `event_order`; duplicate the linked location: `distinct_locators` at annotation evidence |
| STR09 present | Ordered setup/payoff chain plus supported connection | Remove connection: `connection_required` at `.connection`; reverse the linked chain: `event_order` at annotation evidence |
| STR06 present | Misleading cue, invited inference and corrective evidence; linked cue/correction chain | Remove corrective evidence: `evidence_roles` at annotation evidence |
| STR07 present | Claim and disconfirmation each have linked evidence events | Point both events to the claim: `sequence_roles` at annotation evidence |
| STR10 present | Different holders differ on knowledge of the same information | Remove map: `knowledge_required`; remove asymmetry: `knowledge_asymmetry` at the affected `.knowledge` path |
| Absent | Located inspection evidence with scope and adequacy | Remove inspection support: `inspection_required` at annotation evidence |
| Uncertain/not applicable/missing | Incomplete positive chain with uncertainty evidence; justified non-applicability; no row for a missing decision | Do not demand a manufactured positive chain; do not count a missing row as absent |

Paths in the actual assertion must include the affected bundle index, for
example `$.annotations[0].evidence`, rather than a prose placeholder.

## Execution sequence

### 1. Establish a clean runtime and capture identity

In each selected interpreter environment, record the tested commit, branch,
working-tree state, source checksum, configuration/schema hashes, fixture-set
version, OS, and privileges. A dirty checkout requires an exact patch reference.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip check
```

The `python3` in this procedure must resolve to the interpreter named in the run
record. Check installation exit status before proceeding.

### 2. Run the implemented baseline

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised --check
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/literary.json
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/video.json
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/knowledge.json
.venv/bin/python scripts/generate_codebook.py --check
.venv/bin/python docs/80_reference/repo_context/repo_context.py check --root . --context docs/80_reference/repo_context
```

Every command must return its expected exit status. Preserve the command's own
status when logging; a successful `tail` or `grep` is not evidence that the
underlying command passed. For each fixture, also inspect `valid`, counts,
versions, source digest, and the errors array.

### 3. Add the missing regression cases

Implement the matrix additions in isolated fixtures and observe a failing case
before fixing a real defect. Preserve passing controls. For existing correct
behaviour, a new test may already pass; record it as added coverage, not a fix.
Rerun the affected group after a change and the full suite before publication.

### 4. Rehearse with real cases

Use existing pilot patterns such as STR05 and STR09 in literary and video cases,
as tracked in DOC-403. Record exact work versions, locators, inspected scope,
annotation/schema/definition versions, and permitted access references. Run the
validator and have another reader examine the supplied evidence and decision.

Pass for this rehearsal means that the evidence can be recovered, the record can
represent the observation without invented support, and disagreements or format
gaps are documented. Agreement is not required to make the rehearsal useful.
It does not replace the formal pilot, alter the pilot sample, or authorise a
pattern-status upgrade.

### 5. Publish a run record and disposition findings

Record expected and actual outcomes for each executed TC group, failed assertion
paths/codes, command exits, pass/fail/not-run counts, logs, and warnings. Link
fixes and rerun evidence for defects. Register a new dated verification record
under the existing document conventions; do not overwrite DOC-503 as though
unperformed checks had been part of its original run. Keep raw local/private
logs in the ignored local-report area when needed.

## Proposed gates

These gates are proposals for review. They do not mark any pending checklist
item complete.

| Gate | Required evidence | What it permits |
|---|---|---|
| Before merging the file pipeline | Clean-checkout Python 3.11/3.14 baseline and merge-critical TC-01 through TC-14 additions pass; required hosted checks are green; defects affecting source integrity, record acceptance, offline resolution or explicit error handling are resolved; review approval is recorded | Integrating the implemented file tooling, without a taxonomy-validity claim |
| Before broad semantic review | Real-case rehearsal records and human inspection expose and disposition representation problems; source/definition references remain recoverable | Prioritising review and contract changes using observed cases |
| Before the formal pilot | Protocol, lawful corpus access, units, examples, reviewer materials, versions and chosen measures are fixed under PILOT.md; the contract supports the chosen cases and relevant conformance checks pass | Starting the independent pilot round |
| Before pattern-status changes | Recorded independent coding, adjudication and other evidence satisfy the exact contract/protocol transition; required history enforcement exists | A scoped, evidenced status decision for evaluated patterns only |

A waived, blocked, skipped, or not-run mandatory case is an unresolved gate item,
not a pass. Record the reviewer and rationale for any proposed change to these
gates. Do not use a raw test-method count as the acceptance criterion.

## Tests for work not implemented yet

These groups become executable when their corresponding backlog work exists.
They are not current pipeline capabilities or immediate merge requirements.

| ID | Trigger | Required checks |
|---|---|---|
| TC-15 | Structured semantic review decisions and revised extraction | Accepted/rejected/unresolved decisions retain source, rationale, reviewer and version; regeneration does not recreate closed flags; changed cited definitions reopen affected decisions; unreviewed indicator boundaries/types are not silently inferred |
| TC-16 | Persistent annotation/status history | Prior annotations survive revisions; unsupported transitions fail; history cannot be silently overwritten; versions and supersession references remain recoverable and cycles fail |
| TC-17 | Agreement calculations and selected pilot workflow | Manually checked coefficient examples, missingness/category handling and per-pattern scope; if an adapter is used, preserve IDs, locators, ordering, versions and reviewer decisions through export/import |
| TC-18 | SQLite, platform adapter or model-assisted extension | Add a separate scoped test extension before delivery: relational integrity/round trips, platform conformance, or fixed-model/prompt comparison against independent human coding as applicable |

The formal pilot's interpretation, measures, provisional threshold review,
independent coding, adjudication and revision remain governed by PILOT.md.
Software tests must not be used to close those empirical tasks.

## Maintenance and responsibilities

Owner/test executor and accepting reviewer remain unresolved until assigned.
The executor records results; the reviewer checks the oracle, scope and failure
paths. Independent interpretation of real cases requires the human review
specified by the pilot, rather than agreement between generated documents.

Update this plan when interfaces, rules, schemas, dependencies, supported
interpreters, or intended test scope change. Update the coverage matrix from
actual assertions and link new evidence. Keep the README, checklist, document
register and atlas references current while preserving the contract's authority.
