---
document_id: DOC-001
title: Repository Contract
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository
authority: authoritative
supersedes: null
related:
  - DOC-002
  - DOC-003
---

# Repository Contract

## Identity

Repository name: `lit_pattern`

Purpose: maintain a proposed, evidence-oriented pattern database and coding
manual for literary and audiovisual analysis, together with the governance,
normalisation, annotation, and validation work required before empirical use.

Current status: documentation-first repository initialised on 2026-11-11. The
source pattern CSV is present. The normalised schema, validation tooling, pilot
corpus, annotations, inter-annotator results, and validated pattern statuses do
not yet exist in this repository.

Distribution status: public release confirmed by the repository owner on
2026-11-11. The software, taxonomy, documentation, corpus, and privacy boundaries
described in this contract still apply.

Licence status: confirmed on 2026-11-11. Software uses the MIT licence. Original
taxonomy and documentation content use CC BY 4.0, as stated in `LICENSE`.

## Current scope

- Preserve and describe the owner-supplied `literary_and_video_patterns.csv`.
- Define coding units, evidence rules, annotation states, and version rules.
- Specify a proposed normalised data model and a controlled annotation contract.
- Plan a small pilot that can test the definitions and move selected patterns
  beyond the current proposed status.
- Record the provenance and limitations of AI-generated design proposals.

## Current non-scope

- No claim that any pattern definition has been validated.
- No claim that an annotation tool, database, validator, or pilot has been
  implemented.
- No distribution of copyrighted literary or audiovisual corpora.
- No automated assumption that an LLM can infer authorial intention, audience
  response, or pattern absence.
- No commitment to a particular annotation platform before pilot requirements
  are assessed.

## Authoritative sources

Use this order:

1. `REPO_CONTRACT.md` for repository identity, scope, authority, status, and
   update rules.
2. `literary_and_video_patterns.csv` for the current proposed pattern labels,
   criteria, indicators, examples, and source-workbook mappings. Its definitions
   are proposed coding rules, not empirical findings.
3. Controlled documents listed in `docs/00_control/003_document_register.md`
   for interpretation, data requirements, workflow, and verification plans.
4. The owner-supplied DeepSeek conversation recorded in provenance material as
   an informative design proposal. It does not override the repository contract
   or the source CSV.

The source CSV's SHA-256 at initialisation is:

```text
a6bc51c4d6cdf61f6fc488164e8bc4d43e64b2cb350e3b149ed21653fb8c2f7d
```

A future normalised dataset may replace the CSV as the operational pattern
source only after an explicit contract update, preservation of the original,
and validation of the normalised extract.

## Preferred runtime and entry points

There is no runtime application yet.

The intended analysis toolchain is Python 3.11 or later with SQLite for the
initial single-user implementation. Dependency versions are not selected.
Planned entry points are:

- `literary_and_video_patterns.csv`: current source vocabulary.
- `CODEBOOK.md`: generated human-readable view of the source vocabulary.
- `PILOT.md`: controlled pilot plan.
- Future normalised CSV or SQL artefacts under `data/`.
- Future annotation validation scripts and conformance tests under `tests/`.

## Verification surface

Current checks are limited to:

- confirming that the source CSV parses with the Python `csv` module;
- confirming unique `pattern_id` values and the expected column set;
- confirming that `CODEBOOK.md` matches the source CSV through its generator.

The following do not count as verification of the taxonomy:

- a valid CSV;
- a successful schema check;
- agreement among generated documents;
- an example invented by the schema author.

Pattern validation requires located real exemplars, hard negatives, borderline
cases, independent coding, documented adjudication, and versioned annotation
records.

## Open items

- Record the repository owner's public contact identity. The licence and public
  distribution decision are confirmed, but the owner metadata value remains
  unresolved in controlled-document headers.
- Decide whether the operational source of truth will be normalised CSV, SQLite,
  or both.
- Extract indicators, typed relations, workbook mappings, examples, and
  per-pattern evidence overrides from the flat source CSV.
- Define and validate the annotation JSON Schema.
- Add the proposed SQL DDL and conformance tests.
- Select a text and video annotation tool for the pilot.
- Populate located exemplars, hard negatives, and borderline cases for the pilot
  patterns.
- Run the pilot and record observed agreement and adjudication evidence.
- Update pattern statuses only from recorded evidence.

## Vocabulary rules

- `proposed`: a candidate definition or rule; not tested.
- `drafted`: definitions and coding materials exist, but no pilot has been run.
- `pilot_tested`: a pilot has produced recorded observations.
- `validated`: a defined validation protocol has been completed and reviewed.
- `retired`: the pattern or definition is superseded and retained for provenance.
- `present`, `absent`, `uncertain`, and `not_applicable`: annotation outcomes,
  not descriptions of authorial intention or audience response.
- "Evidence" means a located quotation, description, timestamp span, or
  knowledge-state record that supports the annotation.
- "Absent" requires documented inspection of an adequate unit. Missing data is
  never evidence of absence.

## Required update discipline

- Keep pattern definitions separate from their observed functions and effects.
- Change a pattern definition with a `pattern_version` increment or an explicit
  supersession record once annotations exist.
- Increment `schema_version` for changes to required annotation fields or
  validation constraints.
- Record why a source-workbook mapping was kept, corrected, reframed, relocated,
  redefined, or added as an extension.
- Preserve failed and negative cases; do not rewrite them into positive evidence.
- Do not infer pattern absence from an uninspected segment.
- Do not use AI-generated prose as a substitute for located exemplars or
  independent coding evidence.
- Keep public-release changes consistent with the confirmed MIT and CC BY 4.0
  licence split.

