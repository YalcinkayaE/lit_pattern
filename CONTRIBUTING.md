# Contributing

## Read the control documents first

Read `REPO_CONTRACT.md`, `CODEBOOK.md`, and the relevant design or verification
document before proposing a change.

The source vocabulary currently lives in `literary_and_video_patterns.csv`.
`CODEBOOK.md` is generated from that file and must not be edited by hand.

## What counts as a change

Treat these as different change classes:

1. Editorial: spelling, wording that does not alter a coding decision, or link
   repair.
2. Schema: a field, controlled value, required constraint, or validation rule.
3. Pattern definition: inclusion criteria, exclusion criteria, analysis unit,
   evidence threshold, or interpretation boundary.
4. Evidence: a new exemplar, hard negative, borderline case, annotation, or
   adjudication record.
5. Tooling: generator, validator, import/export, or analysis code.
6. Governance: repository identity, scope, authority order, licence, or privacy
   boundary.

State the change class in the proposal. Governance changes require an explicit
update to `REPO_CONTRACT.md`.

## Pattern change rules

- Preserve the pattern ID unless the concept is genuinely retired.
- Keep the label, definition, inclusion criteria, exclusion criteria, analysis
  unit, and evidence threshold coherent.
- Name a realistic near-miss separately from the exclusion criteria.
- Do not use an invented example as a substitute for a located real exemplar.
- Record cross-media claims as hypotheses until tested.
- Keep presence of a pattern separate from its function or proposed effect.
- Do not claim audience response from textual or audiovisual evidence alone.
- Do not claim authorial intention from presence alone.
- Record relation direction explicitly. Use a controlled relation type rather
  than a semicolon-separated list once the normalised data model exists.

When annotations already exist, increment `pattern_version`. When a required
annotation field or validation rule changes, increment `schema_version`.

## Status changes

Use only the vocabulary in `REPO_CONTRACT.md`.

A move from `proposed` to `drafted` requires complete coding materials.

A move to `pilot_tested` requires:

- a recorded pilot protocol;
- identified works and versions;
- real exemplars and hard negatives;
- independent annotations;
- observed agreement results;
- documented adjudication;
- retained disagreement cases.

A move to `validated` requires completion against a protocol that was fixed
before the validation run and reviewed independently.

Do not use "validated" for a schema that merely parses or a CSV that merely
loads.

## Evidence standards

For literature, record the edition or version, chapter and page, paragraph, or
other stable locator, and a short supporting quotation where copyright allows.

For video, record the work version and start and end timestamps, then describe
the relevant visual, speech, sound, music, or editing evidence.

For absence, record the inspected unit and why the inspection was adequate.
Never infer absence from an uninspected segment or an analysis-tool miss.

For knowledge asymmetry, record who knows what and when. A character's general
ignorance is not enough to establish dramatic irony.

For sequential patterns, link event IDs and distinguish presentation order from
recoverable story order.

## Copyright and privacy

Do not commit full copyrighted works, private corpora, participant data, secrets,
or local annotation files without a documented right and privacy basis.

Prefer stable locators, short permitted quotations, hashes, and private storage
for the underlying corpus.

## Data and tooling changes

- External configuration must be explicit and validated.
- Missing inputs must fail with a clear error.
- Do not add silent fallback data.
- Keep source and generated artefacts distinguishable.
- Add tests when a change affects parsing, validation, exports, agreement
  statistics, or status transitions.
- Do not introduce a database dependency before the file-based pilot questions
  are clear.

## Review

Before merge:

1. Run `python3 scripts/generate_codebook.py --check`.
2. Run any relevant tests.
3. Inspect the Git diff.
4. Confirm that status and validation claims match observed evidence.
5. Ensure a pattern definition change has version and provenance consequences
   documented.

Risky changes to the annotation contract, pattern definitions, or validation
logic should receive an independent review before merge.

## AI-assisted work

AI assistance may propose definitions, examples, summaries, or code. Treat the
output as a draft. A person must review it against the source vocabulary and
evidence rules. AI-generated examples do not establish that a pattern is
observable or that annotators will agree on it.

