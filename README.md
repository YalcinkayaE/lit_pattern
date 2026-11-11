# Literary and Video Pattern Database

This repository holds a proposed pattern vocabulary and coding manual for
literary and audiovisual analysis, with file-based extraction and annotation
validation tools. The current definitions have not been validated on a labelled
corpus.

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

