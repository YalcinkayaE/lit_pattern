# Literary and Video Pattern Database

This repository holds a proposed pattern vocabulary and coding manual for
literary and audiovisual analysis. It is documentation-first. The current
definitions have not been validated on a labelled corpus.

The public repository is [YalcinkayaE/lit_pattern](https://github.com/YalcinkayaE/lit_pattern).
Its software is MIT licensed and its original taxonomy and documentation content
are CC BY 4.0 licensed.

The current source vocabulary is
[`literary_and_video_patterns.csv`](literary_and_video_patterns.csv). It contains
59 proposed patterns across genre, narrative structure, rhetorical devices,
audiovisual expression, interpreted effects, and related label types.

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

