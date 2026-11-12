---
document_id: DOC-001
title: Repository Contract
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-12
applies_to: repository
authority: authoritative
supersedes: null
related:
  - DOC-002
  - DOC-003
---

# Repository Contract

## Identity

Repository name: `literary-audiovisual-patterns`

The Python package remains `lit_pattern`.

Purpose: maintain a proposed, evidence-oriented pattern database and coding
manual for literary and audiovisual analysis, together with the governance,
normalisation, annotation, and validation work required before empirical use.

Current status: file-based command-line tooling and proposed coding materials.
The original source CSV, deterministic extraction, annotation JSON Schema,
validator, and conformance tests are present. Extracted indicator groups, untyped
relations, and workbook mappings retain explicit review items. No real pilot
corpus, annotations, agreement results, or validated pattern statuses exist.

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
- No claim that an annotation platform, database, or pilot has been implemented.
- No claim that extraction review items have been resolved or that conformance
  checks establish the truth of an annotation.
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

The runtime consists of command-line file tools; there is no service or
annotation application. Python 3.11 or later is required. The extraction and
annotation tools use jsonschema 4.26.0, declared in `requirements.txt`; the
codebook generator uses the standard library. SQLite remains a future storage
option. Current entry points are:

- `literary_and_video_patterns.csv`: current source vocabulary.
- `CODEBOOK.md`: generated human-readable view of the source vocabulary.
- `PILOT.md`: controlled pilot plan.
- `python3 -m lit_pattern.normalise --config config/pipeline.json --output data/normalised`: deterministic extraction; add `--check` for freshness.
- `python3 -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input <bundle.json>`: JSON bundle validation.
- `schemas/annotation.schema.json`: proposed annotation contract version 0.1.0.
- `config/pipeline.json`: explicit versions, vocabularies, source checksum, typed
  relation decisions, and evidence-role rules.
- `python3 -m unittest discover -s tests -v`: conformance and boundary tests.

`data/normalised/` is a derived extraction, not a replacement authority. Its
manifest records counts and hashes and it retains an exact `source.csv` copy.
`indicator_candidates.csv` preserves whole indicator cells.
`relation_candidates.csv` preserves listed ID pairs without assigning types;
`relations.csv` contains only explicit configured decisions. Workbook mapping
cells remain intact pending decomposition and rationale review.

## Verification surface

Current file and conformance checks cover:

- confirming that the source CSV parses with the Python `csv` module;
- confirming unique `pattern_id` values and the expected column set;
- confirming that `CODEBOOK.md` matches the source CSV through its generator;
- deterministic extraction, source/configuration checksums, source preservation,
  and freshness checks for generated outputs;
- JSON structure, IDs, work/unit/reviewer/evidence references, versions, locator
  spans, sequence order, and retained adjudication inputs;
- adequate-inspection records for absence and positive evidence-role rules for
  STR05, STR06, STR07, STR09, and STR10;
- invented positive and negative conformance fixtures. These are test data, not
  pilot observations.

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
- Resolve indicator segmentation, relation typing, workbook mapping rationale,
  and missing per-pattern false-positive/evidence-threshold guidance recorded
  in `data/normalised/review_items.json`.
- Pilot and review the implemented proposed annotation contract; extend
  pattern-specific evidence rules where justified.
- Add SQL DDL only if a relational store is selected.
- Define persistent status-history enforcement before permitting status updates.
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

