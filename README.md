# Literary and audiovisual patterns

A proposed coding manual and pattern vocabulary for literary and audiovisual
analysis. It keeps a pattern label separate from the evidence, the unit, and
the reviewer decision needed to apply that label.

The public repository is
[YalcinkayaE/literary-audiovisual-patterns](https://github.com/YalcinkayaE/literary-audiovisual-patterns).
It was published on 2026-11-11 as `lit_pattern`. GitHub redirects that URL.
Software in this repository is MIT licensed. Original taxonomy and documentation
content are CC BY 4.0 licensed.

## What it is

The project is a controlled coding instrument with three connected parts, as
set out in the
[product overview](docs/10_product/101_product_overview.md):

1. A coding manual with inclusion and exclusion criteria.
2. A versioned annotation record structure.
3. A pilot protocol that can test whether independent annotators apply the
   definitions consistently.

The current source vocabulary is
[`literary_and_video_patterns.csv`](literary_and_video_patterns.csv). It
contains 59 proposed patterns across genre, narrative structure, rhetorical
devices, audiovisual expression, interpreted effects, and related label types.
[`CODEBOOK.md`](CODEBOOK.md) is the human-readable manual generated from that
file. [`PILOT.md`](PILOT.md) is the planned validation study.

The vocabulary separates broad pattern kinds from pattern labels, gives
literature and video their own indicators, pairs inclusions with exclusions,
requires located evidence, and states an interpretation boundary. Those design
choices need empirical testing before the taxonomy can support comparative or
computational claims.

Intended users are literary and media-studies researchers,
computational-humanities and annotation teams, students learning close reading,
film analysis, or narrative construction, and writers, editors, and
story-development teams. No user research or adoption evidence is recorded yet.

## What it does today

A reader can use the proposed definitions, criteria, invented examples, and
creative prompts, and can check that the generated codebook matches the source
CSV. Normalisation, an annotation schema, a validator, an annotation
application, and a pilot result are still planned. The
[repository contract](REPO_CONTRACT.md) is the status authority.

```bash
python3 scripts/generate_codebook.py --check
```

That check establishes file consistency. It does not validate the taxonomy.

## Use cases

These are proposed uses from
[`docs/10_product/102_use_cases.md`](docs/10_product/102_use_cases.md). They
describe work a person could undertake and the prerequisites for more
structured use. They are not records of completed studies or observed adoption.
That document holds the scenarios, shared evidence rules, and boundaries.

| Task | Use case | What the repository provides now | Further prerequisites |
|---|---|---|---|
| Code passages or scenes for a research question | Corpus annotation and computational humanities | Proposed definitions, evidence rules, and annotation design | Fixed units, located cases, a tested schema, independent coding, and analysis tooling |
| Examine a pattern across prose and screen | Comparative media analysis | Separate literature and video indicators | Selected versions, comparable units, and reviewed examples in both modalities |
| Prepare a close-reading or film-analysis exercise | Teaching | Definitions, criteria, invented examples, and creative prompts | Teacher review and located real cases before assessment or calibration |
| Plan a narrative device while drafting | Creative tooling | The source `creative_use` guidance | A writer's draft and manual tracking; software support would require implementation |
| Propose labels for human review | LLM-assisted pre-annotation | Criteria that could inform a future prompt | A stable schema, calibrated cases, model configuration, and human comparison data |
| Review whether a draft supports a claimed device | Editorial and commissioning review | Proposed criteria and evidence rules | A defined review brief, adequate inspection, and access to the relevant draft |
| Examine ambiguities and revise the vocabulary | Taxonomy research | Source-workbook mappings and proposed boundary matrices | Retained coding disagreements and versioned evidence before empirical revision |

Manual exploration can start from the codebook. Research findings, automated
processing, and pattern status changes require the work in the
[implementation plan](docs/40_delivery/401_implementation_plan.md) and the
[pilot protocol](PILOT.md).

## Boundaries

Annotation outcomes are `present`, `absent`, `uncertain`, and `not_applicable`.
They record a reviewer's decision about located material. Authorial intention
and measured audience response are outside those outcomes. Pattern status stays
`proposed` until a pilot records located exemplars, hard negatives, borderline
cases, independent coding, and adjudication. Copyrighted works stay out of
version control. A production database or multi-user annotation service is
outside the current phase. Detail is in
[`docs/10_product/103_scope_and_limitations.md`](docs/10_product/103_scope_and_limitations.md).

## Current state

- Repository initialised as an independent Git working tree.
- Source CSV preserved with 59 pattern rows and 18 columns.
- Human-readable coding manual generated from the CSV.
- Proposed normalization, annotation, pilot, and verification plans documented.
- No SQL schema, annotation validator, annotation platform integration, or pilot
  result is implemented in this repository yet.

## Read first

1. [`REPO_CONTRACT.md`](REPO_CONTRACT.md): repository authority and status.
2. [`CODEBOOK.md`](CODEBOOK.md): proposed coding rules generated from the source
   CSV.
3. [`PILOT.md`](PILOT.md): the planned validation study.
4. [`CONTRIBUTING.md`](CONTRIBUTING.md): definition, versioning, and review
   rules.
5. [`docs/00_control/002_repo_status.md`](docs/00_control/002_repo_status.md):
   verified current status and unfinished work.

## Documentation map

| Area | Document |
|---|---|
| Repository control | [`REPO_CONTRACT.md`](REPO_CONTRACT.md) |
| Current status | [`docs/00_control/002_repo_status.md`](docs/00_control/002_repo_status.md) |
| Document register | [`docs/00_control/003_document_register.md`](docs/00_control/003_document_register.md) |
| Product intent | [`docs/10_product/101_product_overview.md`](docs/10_product/101_product_overview.md) |
| Use cases | [`docs/10_product/102_use_cases.md`](docs/10_product/102_use_cases.md) |
| Scope and limits | [`docs/10_product/103_scope_and_limitations.md`](docs/10_product/103_scope_and_limitations.md) |
| Coding manual | [`CODEBOOK.md`](CODEBOOK.md) |
| Data requirements | [`docs/20_requirements/201_data_requirements.md`](docs/20_requirements/201_data_requirements.md) |
| Proposed data model | [`docs/30_design/301_normalised_data_model.md`](docs/30_design/301_normalised_data_model.md) |
| Annotation workflow | [`docs/30_design/302_annotation_workflow.md`](docs/30_design/302_annotation_workflow.md) |
| Boundary matrices | [`docs/30_design/303_boundary_matrices.md`](docs/30_design/303_boundary_matrices.md) |
| Delivery plan | [`docs/40_delivery/401_implementation_plan.md`](docs/40_delivery/401_implementation_plan.md) |
| Pilot | [`PILOT.md`](PILOT.md) |
| Verification plan | [`docs/50_verification/501_schema_validation_plan.md`](docs/50_verification/501_schema_validation_plan.md) |
| Provenance | [`docs/80_reference/802_design_proposal_provenance.md`](docs/80_reference/802_design_proposal_provenance.md) |
| Tool and corpus requirements | [`docs/80_reference/804_tooling_and_corpus_requirements.md`](docs/80_reference/804_tooling_and_corpus_requirements.md) |
| Repository atlas and agent onboarding | [`docs/80_reference/repo_context/README.md`](docs/80_reference/repo_context/README.md) |

## Verify the source CSV and generated codebook

The codebook generator performs basic structural checks:

```bash
python3 scripts/generate_codebook.py --check
```

Regenerate the codebook after an intentional source CSV change:

```bash
python3 scripts/generate_codebook.py
```

These checks establish file consistency. They do not validate the taxonomy.

## Immediate next work

1. Normalise the source CSV into separate patterns, indicators, examples,
   relations, mappings, and evidence-rule tables.
2. Add a schema, validator, and conformance tests.
3. Prepare a small mixed-media pilot with located cases.
4. Run independent annotation and record the observed disagreements before
   changing any pattern definition.

## Licence

See [`LICENSE`](LICENSE). Software uses the MIT licence. Original taxonomy and
documentation content use CC BY 4.0 unless a file states otherwise. Third-party
source works and corpus material are not licensed by this repository.
