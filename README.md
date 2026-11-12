# Literary and audiovisual patterns

A proposed coding manual and pattern vocabulary for literary and audiovisual
analysis, with file-based extraction and annotation validation tools. It keeps
a pattern label separate from the evidence, the unit, and the reviewer decision
needed to apply that label.

The public repository is
[YalcinkayaE/literary-audiovisual-patterns](https://github.com/YalcinkayaE/literary-audiovisual-patterns).
It was published on 2026-11-11 as `lit_pattern`. GitHub redirects that URL.
The Python package name remains `lit_pattern`. Software in this repository is
MIT licensed. Original taxonomy and documentation content are CC BY 4.0
licensed.

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

The file tools extract the source vocabulary into checked tables and validate a
proposed annotation bundle. There is no annotation application and no pilot
result. A passing check establishes file conformance. It does not establish
that a pattern definition is reliable. Commands are below. The
[file contract](docs/30_design/304_annotation_file_contract.md) documents the
fields, error reports, supported rules, and extraction review items.

## Use cases

These are proposed uses from
[`docs/10_product/102_use_cases.md`](docs/10_product/102_use_cases.md). They
describe work a person could undertake and the prerequisites for more
structured use. They are not records of completed studies or observed adoption.
That document holds the scenarios, shared evidence rules, and boundaries.

| Task | Use case | What the repository provides now | Further prerequisites |
|---|---|---|---|
| Code passages or scenes for a research question | Corpus annotation and computational humanities | Proposed definitions, extracted tables, evidence rules, and an initial annotation validator | Fixed units, located cases, pilot review of the implemented schema, independent coding, and agreement tooling |
| Examine a pattern across prose and screen | Comparative media analysis | Separate literature and video indicators | Selected versions, comparable units, and reviewed examples in both modalities |
| Prepare a close-reading or film-analysis exercise | Teaching | Definitions, criteria, invented examples, and creative prompts | Teacher review and located real cases before assessment or calibration |
| Plan a narrative device while drafting | Creative tooling | The source `creative_use` guidance | A writer's draft and manual tracking; software support would require implementation |
| Propose labels for human review | LLM-assisted pre-annotation | Criteria that could inform a future prompt | A stable schema, calibrated cases, model configuration, and human comparison data |
| Review whether a draft supports a claimed device | Editorial and commissioning review | Proposed criteria and evidence rules | A defined review brief, adequate inspection, and access to the relevant draft |
| Examine ambiguities and revise the vocabulary | Taxonomy research | Source-workbook mappings and proposed boundary matrices | Retained coding disagreements and versioned evidence before empirical revision |

Manual exploration can start from the codebook and the file tools. Research
findings, automated processing, and pattern status changes require the work in
the [implementation plan](docs/40_delivery/401_implementation_plan.md) and the
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
- Deterministic extraction preserves the source and records unresolved indicator,
  relation, and mapping review items.
- JSON Schema and a Python validator check the proposed annotation file contract.
- No SQL schema, annotation platform integration, or real pilot result exists.

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
| Annotation file contract and commands | [`docs/30_design/304_annotation_file_contract.md`](docs/30_design/304_annotation_file_contract.md) |
| Boundary matrices | [`docs/30_design/303_boundary_matrices.md`](docs/30_design/303_boundary_matrices.md) |
| Remaining-work checklist | [`docs/40_delivery/403_remaining_work.md`](docs/40_delivery/403_remaining_work.md) |
| Delivery plan | [`docs/40_delivery/401_implementation_plan.md`](docs/40_delivery/401_implementation_plan.md) |
| Pilot | [`PILOT.md`](PILOT.md) |
| Verification plan | [`docs/50_verification/501_schema_validation_plan.md`](docs/50_verification/501_schema_validation_plan.md) |
| Repository test plan | [`docs/50_verification/503_repository_test_plan.md`](docs/50_verification/503_repository_test_plan.md) |
| Data pipeline verification | [`docs/50_verification/502_data_pipeline_verification.md`](docs/50_verification/502_data_pipeline_verification.md) |
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

## Extract and validate annotation files

Use Python 3.11+ from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised
.venv/bin/python -m lit_pattern.normalise --config config/pipeline.json --output data/normalised --check
.venv/bin/python -m lit_pattern.validate --config config/pipeline.json --catalogue data/normalised --input tests/fixtures/literary.json
.venv/bin/python -m unittest discover -s tests -v
```

The validation example is invented test data. Pass a privately stored bundle to
`--input` for actual annotations. See the
[file contract](docs/30_design/304_annotation_file_contract.md) for fields, error
reports, supported rules, and extraction review items. The original CSV remains
authoritative; the derived tables do not resolve ambiguous source semantics.

## Immediate next work

See the [remaining-work checklist](docs/40_delivery/403_remaining_work.md) for
sequenced tasks, completion evidence, and conditional follow-up work.

1. Review indicator segmentation, relation typing, mapping rationale, and missing
   per-pattern guidance in `data/normalised/review_items.json`.
2. Prepare a small mixed-media pilot with located cases and review the proposed
   annotation contract against it.
3. Run independent annotation and record the observed disagreements before
   changing any pattern definition.

## Licence

See [`LICENSE`](LICENSE). Software uses the MIT licence. Original taxonomy and
documentation content use CC BY 4.0 unless a file states otherwise. Third-party
source works and corpus material are not licensed by this repository.
