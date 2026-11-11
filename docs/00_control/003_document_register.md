---
document_id: DOC-003
title: Document Register
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-002
---

# Document Register

| ID | Document | Purpose | Authority | Lifecycle |
|---|---|---|---|---|
| DOC-001 | `REPO_CONTRACT.md` | Repository identity, scope, sources, and update rules | Authoritative | Living |
| DOC-002 | `docs/00_control/002_repo_status.md` | Observed current state and unsupported claims | Controlled | Living |
| DOC-003 | `docs/00_control/003_document_register.md` | Document ownership map | Controlled | Living |
| DOC-101 | `docs/10_product/101_product_overview.md` | Product intent and intended benefits | Controlled | Living |
| DOC-102 | `docs/10_product/102_use_cases.md` | Intended uses and preconditions | Controlled | Living |
| DOC-103 | `docs/10_product/103_scope_and_limitations.md` | Current boundaries and risks | Controlled | Living |
| DOC-201 | `CODEBOOK.md` | Human-readable coding manual generated from the source CSV | Controlled, generated | Living |
| DOC-202 | `docs/20_requirements/201_data_requirements.md` | Required data fields, states, and constraints | Controlled | Living |
| DOC-301 | `docs/30_design/301_normalised_data_model.md` | Proposed relational structure | Controlled | Proposed |
| DOC-302 | `docs/30_design/302_annotation_workflow.md` | Proposed annotation and review workflow | Controlled | Proposed |
| DOC-303 | `docs/30_design/303_boundary_matrices.md` | Pairwise disambiguation and decision rules | Controlled | Proposed |
| DOC-304 | `docs/30_design/304_annotation_file_contract.md` | Executable proposed file contract, commands, and boundaries | Controlled | Living |
| DOC-401 | `docs/40_delivery/401_implementation_plan.md` | Controlled implementation sequence | Controlled | Proposed |
| DOC-402 | `docs/40_delivery/402_data_pipeline_implementation.md` | Data pipeline implementation decisions and execution plan | Controlled | Living |
| DOC-403 | `docs/40_delivery/403_remaining_work.md` | Actionable remaining-work checklist with completion evidence | Controlled | Living |
| DOC-501 | `PILOT.md` | Proposed first validation study | Controlled | Proposed |
| DOC-502 | `docs/50_verification/501_schema_validation_plan.md` | Planned schema and workflow checks | Controlled | Proposed |
| DOC-503 | `docs/50_verification/502_data_pipeline_verification.md` | File pipeline conformance evidence and remaining gaps | Evidence | Dated |
| DOC-801 | `docs/80_reference/801_glossary.md` | Shared working vocabulary | Informative | Living |
| DOC-802 | `docs/80_reference/802_design_proposal_provenance.md` | Source and limitations of the AI-generated proposal | Informative | Reference |
| DOC-804 | `docs/80_reference/804_tooling_and_corpus_requirements.md` | Candidate tools, standards, and corpus needs | Informative | Reference |
| DOC-805 | `docs/80_reference/repo_context/README.md` | Repository atlas and agent onboarding navigation | Informative, generated | Living |
| DOC-CONTRIB | `CONTRIBUTING.md` | Contribution, versioning, and review rules | Controlled | Living |
| DOC-CHANGELOG | `CHANGELOG.md` | Material repository changes | Informative | Living |
| DOC-LICENCE | `LICENSE` | Software and content licence terms | Authoritative | Living |

`REPO_CONTRACT.md` remains at the repository root because repository tooling and
assistants expect it there. `README.md`, `AGENTS.md`, `CONTRIBUTING.md`,
`CHANGELOG.md`, and `LICENSE` also remain at the root for discoverability and
tool compatibility.


The DOC-805 context pack is a generated navigation aid subordinate to this
register and `REPO_CONTRACT.md`. Maintain its reviewed claims in
`docs/80_reference/repo_context/evidence.json`, then regenerate its Markdown and
snapshot with the copied `repo_context.py`. The pack has no separate authority
over pattern definitions, implementation status, or validation decisions. Owner
metadata remains unresolved as recorded in the repository contract.
