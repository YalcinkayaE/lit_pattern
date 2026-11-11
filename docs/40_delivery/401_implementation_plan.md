---
document_id: DOC-401
title: Implementation Plan
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository
authority: controlled
supersedes: null
related:
  - DOC-301
  - DOC-302
  - DOC-501
  - DOC-502
---

# Implementation Plan

The sequence is designed to establish the coding instrument before investing in
software or annotation at scale.

## Phase 0: Control

Status: public distribution and licence choices confirmed; owner metadata
incomplete.

- Public repository intent confirmed on 2026-11-11.
- MIT software and CC BY 4.0 content licence split confirmed on 2026-11-11.
- Repository owner public contact identity remains unresolved.
- Confirm that the original source CSV remains the current pattern authority.
- Select the pilot work and video version without committing corpus files.

Exit evidence: public status and licence records are complete. Owner metadata
still needs a supplied value before the control phase is fully complete.

## Phase 0a: Public publication

Status: ready for remote configuration; not published.

- Configure a public Git remote under the confirmed owner account.
- Push the initial commit.
- Verify public visibility and licence rendering after publication.

Exit evidence: a verified public repository URL and observed render of the
README and licence files.

## Phase 1: Normalisation

Status: proposed.

- Create deterministic extraction scripts.
- Generate lookup tables and a normalised `pattern.csv`.
- Extract indicators, relations, mappings, and invented examples.
- Keep unresolved source text in an exceptions report.
- Compare row counts and stable IDs with the source.

Exit evidence: repeatable normalisation, source checksum, entity counts, and a
review of every transformation.

## Phase 2: Annotation contract

Status: proposed.

- Define SQL DDL or JSON Schema.
- Define required evidence and sequence objects.
- Add pattern-specific constraints as data.
- Add positive and negative conformance fixtures.
- Implement a validator with clear errors.

Exit evidence: fixtures that pass or fail for the intended reasons and tests that
exercise cross-record constraints.

## Phase 3: Pilot materials

Status: proposed.

- Select ten patterns.
- Locate one real exemplar, one hard negative, and one borderline case per
  pattern.
- Separate exemplars from invented teaching examples.
- Freeze the initial codebook version used by annotators.
- Prepare a minimal annotation export and import route.

Exit evidence: located cases and an annotation package that a second person can
use without undocumented knowledge.

## Phase 4: Pilot

Status: not started.

- Run independent annotation.
- Retain disagreements.
- Calculate the planned agreement measures.
- Adjudicate cases.
- Identify recurring boundary failures.

Exit evidence: a dated verification report with observed results, not a proposed
target.

## Phase 5: Revision and second round

Status: not started.

- Revise definitions or boundary rules only where supported by pilot evidence.
- Increment versions.
- Run a second round when the first round exposes instability.
- Update pattern status based on the completed protocol.

Exit evidence: versioned codebook, revised annotation records, and a recorded
status decision.

## Deferred

- Multi-user database service.
- Large-scale LLM pre-annotation.
- Full ontology alignment.
- Public corpus distribution.
- A claim of validated cross-media equivalence.

