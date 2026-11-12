# Changelog

This file records repository changes that affect pattern meaning, the annotation
contract, status claims, or the verification surface. Git history holds routine
editorial changes.

## Unreleased

### Added

- Proposed skills-based plugin design covering library packaging, task skills,
  evidence handling, host capability boundaries and comparative evaluation.
- Initial repository contract and documentation set.
- Confirmed public-release status and the MIT and CC BY 4.0 licence split.
- Product overview, use cases, and scope limits.
- Codebook generator and generated codebook for the 59-row source CSV.
- Proposed normalised data model and annotation workflow.
- Boundary matrices for the sequential and irony clusters.
- Pilot and schema-validation plans.
- Provenance and external-reference notes.
- Contributing and licensing documents.
- Repository atlas, agent onboarding guide, and concrete use cases.
- Public repository at [YalcinkayaE/lit_pattern](https://github.com/YalcinkayaE/lit_pattern).

### Implemented file tooling

- Deterministic source extraction with an exact retained source copy, manifests,
  candidate tables, and explicit semantic review items.
- Proposed annotation JSON Schema 0.1.0 and validator for structure, references,
  absence inspection, ordered evidence, and knowledge-state records.
- Invented conformance fixtures and failure-path tests.
- Independent-review fixes for linked evidence, finite timestamps, timezone
  ranges, and offline dynamic schema references.

### Verified

- The source CSV parses as CSV, contains the expected 18 columns, and has 59
  unique pattern IDs.
- The source CSV SHA-256 is recorded in the repository contract.
- The generated codebook can be checked against the source CSV.
- Repository-atlas freshness and local documentation links pass their checks.
- GitHub reports public visibility and default branch `main`; the published
  README includes use-case and atlas links. The hosted licence file matches
  the local MIT and CC BY 4.0 text.

### Not done

- Discrete indicators, typed relations, and mapping rationale still require review.
- No SQL schema or persistent status-history enforcement has been added.
- No annotation tool has been selected or integrated.
- No real exemplar, hard negative, or borderline case has been adjudicated.
- No pilot has been run.
- No pattern has been validated.
- Repository owner contact metadata remains unresolved.

