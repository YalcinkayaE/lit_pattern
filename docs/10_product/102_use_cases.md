---
document_id: DOC-102
title: Use Cases
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: repository
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-101
  - DOC-103
  - DOC-201
  - DOC-202
  - DOC-301
  - DOC-302
  - DOC-303
  - DOC-501
  - DOC-502
  - DOC-804
---

# Use Cases

These are proposed uses of the vocabulary and coding materials. They describe
work a person could undertake and the prerequisites for more structured use.
They are not records of completed studies or observed user adoption.

The current materials are the
[source CSV](../../literary_and_video_patterns.csv), the generated
[codebook](../../CODEBOOK.md), and the registered plans. There is no annotation
application, implemented annotation schema, tool integration, or pilot result.
The [repository contract](../../REPO_CONTRACT.md) governs status and scope.

## Choosing a use case

| Task | Use case | What the current repository provides | Further prerequisites |
|---|---|---|---|
| Code passages or scenes for a research question | Corpus annotation and computational humanities | Proposed definitions, evidence rules, and annotation design | Fixed units, located cases, a tested schema, independent coding, and analysis tooling |
| Examine a pattern across prose and screen | Comparative media analysis | Separate literature and video indicators | Selected versions, comparable units, and reviewed examples in both modalities |
| Prepare a close-reading or film-analysis exercise | Teaching | Definitions, criteria, invented examples, and creative prompts | Teacher review and located real cases before assessment or calibration |
| Plan a narrative device while drafting | Creative tooling | The source `creative_use` guidance | A writer's draft and manual tracking; software support would require implementation |
| Propose labels for human review | LLM-assisted pre-annotation | Criteria that could inform a future prompt | A stable schema, calibrated cases, model configuration, and human comparison data |
| Review whether a draft supports a claimed device | Editorial and commissioning review | Proposed criteria and evidence rules | A defined review brief, adequate inspection, and access to the relevant draft |
| Examine ambiguities and revise the vocabulary | Taxonomy research | Source-workbook mappings and proposed boundary matrices | Retained coding disagreements and versioned evidence before empirical revision |

Manual exploration can start with the current materials. Research findings,
automated processing, and pattern status changes require the additional work
specified in the [implementation plan](../40_delivery/401_implementation_plan.md)
and [pilot protocol](../../PILOT.md).

## Shared evidence and recording rules

For observations about an existing work, identify its edition or release
version, the inspected unit, the pattern ID, the reviewer, and the evidence
locator. Record the source CSV checksum or repository revision used; record
schema and pattern versions once those versions are defined.

Use `present`, `absent`, `uncertain`, or `not_applicable` according to the
contract. An absence claim needs an adequate-inspection record. Sequential
patterns need linked locators and event order. Keep pattern presence separate
from narrative function, proposed effect, authorial intention, and measured
audience response.

Store corpus material and private annotation records according to the
[copyright and privacy rules](../../CONTRIBUTING.md#copyright-and-privacy).
For structured annotation, follow the
[data requirements](../20_requirements/201_data_requirements.md) and
[annotation workflow](../30_design/302_annotation_workflow.md). This document
adds no annotation fields or schema constraints.

The scenarios below are illustrative tasks, not located exemplars or completed
annotations.

## Corpus annotation and computational humanities

**User and question:** a researcher or annotation team asks where selected
patterns occur in a defined corpus and whether reviewers can apply the criteria
consistently.

**Inputs:** lawfully accessible works with fixed versions, a frozen codebook
reference, selected pattern IDs, stable units, and located positive, negative,
and borderline cases.

The source `annotation_rule` names `work_id`, `unit_id`, `pattern_id`,
`evidence`, and `reviewer`. These provide a starting record structure for a
relational database or schema-validated JSONL records. In the proposed model,
work and unit references identify what was inspected; pattern and reviewer
references identify whose decision is being compared; evidence supports review.
Presence state and version information are also needed for interpretable
agreement analysis.

INCEpTION, CATMA, and ELAN are candidate annotation tools in the
[tooling reference](../80_reference/804_tooling_and_corpus_requirements.md).
Using one would require a field mapping, configuration, and a tested import and
export route. The current CSV contains pattern definitions, rather than the
work, unit, and reviewer observations needed to compute agreement.

**Workflow:**

1. Define the research question and inspected units before coding.
2. Prepare and test the annotation schema against the
   [validation plan](../50_verification/501_schema_validation_plan.md).
3. Have annotators apply the criteria independently and retain their original
   decisions, evidence, rationales, and uncertainty.
4. Align decisions by work, unit, and pattern across reviewers. Calculate
   per-pattern agreement using the design selected in the pilot protocol, then
   adjudicate disagreements and retain the decision history. Missing annotations
   remain missing rather than being counted as `absent`.
5. Summarise results by inspected scope, pattern, reviewer, modality, and version.

**Output:** versioned annotation records, an agreement report, and an adjudication
log that lets another reviewer recover how a label was assigned.

**Illustrative task:** for STR05, foreshadowing, link an earlier cue to a later
event or disclosure. Retain ominous atmosphere without a supported later link as
a possible negative or uncertain case, applying the source criteria.

**Prerequisites and boundary:** the schema, cases, independent annotations, and
analysis tooling still need to be prepared. Counts from an untested coding
procedure do not establish pattern reliability. Follow the pilot before making
status decisions.

## Comparative media analysis

**User and question:** a literary or media researcher asks how a proposed
pattern is realised in prose and audiovisual material, including an adaptation.

**Inputs:** exact editions or release versions, a justified pairing of passages
and sequences, relevant pattern criteria, and modality-specific evidence.

**Workflow:**

1. State why the units are comparable and record differences in their scope.
2. Apply the pattern criteria separately in each modality.
3. Locate the textual cues and the relevant image, speech, sound, music, or
   editing evidence.
4. Compare the supported decisions, including cases where the pattern is
   uncertain, absent after inspection, or not applicable.
5. Record any proposed cross-media analogue as a hypothesis for review.

**Output:** a comparison with recoverable locators, coding rationales, and
explicit differences in how each medium supplies evidence.

**Illustrative task:** ask how STR10, dramatic irony / knowledge asymmetry, is
established in a literary passage and a screen adaptation. Record who knows what
and when in each version. Examine whether selective description or focalisation
in prose corresponds to VID07, framing / visual information control, on screen.
If cross-cutting supplies the information, consider VID03, parallel editing /
cross-cutting, separately. Code each pattern only where its own criteria hold.

Use `literature_indicators`, `video_indicators`, and `related_patterns` to find
candidate comparisons. For example, VID07 lists STR10 in its related-pattern
cell. These lists can seed a proposed graph for investigation, but currently
have no relation type or explicit symmetry. They do not establish a migration,
equivalence, or causal link. Record the observed connection and rationale before
proposing a typed relation under the
[normalised model](../30_design/301_normalised_data_model.md).

**Prerequisites and boundary:** comparable units and reviewed cases are needed
before a study can support broader claims. Matching labels alone do not
establish equivalent mechanisms or audience responses across media.

## Teaching

**User and question:** a teacher or student asks how to distinguish a pattern
from a similar label and support a close reading with evidence.

**Inputs:** a reviewed selection from the codebook, an invented practice
example, a lawfully accessible real case with a locator, and a near-miss.

**Workflow:**

1. Build a lesson around definition → inclusion/exclusion criteria →
   `invented_example` → a "now build one" exercise using `creative_use`.
2. Use the invented example for practice, clearly identified as invented.
3. Ask students to apply the criteria to the real case and near-miss before
   seeing the teacher's rationale.
4. Have students write a passage or plan a shot sequence, then explain how their
   choices address the criteria and where the proposed reading remains uncertain.
5. Apply `interpretation_boundary` when discussing the work: distinguish located
   support from claims about intention or actual audience response. Retain
   alternative readings.

**Output:** a creative-writing or film-analysis worksheet with the pattern ID,
definition, criteria, example, construction exercise, and evidence-based
reflection. Selected rows can supply the material for a teacher-reviewed workbook.
The shared `interpretation_boundary` text provides a recurring check against
over-reading; it is currently identical across source rows.

**Illustrative task:** compare DEV02, verbal irony, with DEV03, sarcasm. Ask
students what supports a non-literal evaluative reading and, separately, what
identifies a target and contextual evidence of mockery.

**Prerequisites and boundary:** teacher review is needed before classroom use.
Pair invented examples with located real cases before assessment or annotator
calibration. The proposed vocabulary supplies discussion material; it has no
recorded educational evaluation.

## Creative tooling

**User and question:** a writer or story-development team asks how to plan and
revise a device in a new draft.

**Inputs:** the writer's draft or outline, selected pattern definitions, and
the corresponding `creative_use` guidance.

**Workflow:**

1. Choose the narrative task and relevant pattern rather than adding labels
   without a purpose.
2. Translate the creative prompt into draft-specific choices and locators.
3. Track any linked setup, cue, consequence, or disclosure across the draft.
4. Re-read the draft against the inclusion and exclusion criteria, then revise
   or retain uncertainty about whether the device is supported.
5. In a writers' room, use the same criteria as a discussion checklist. For
   model-assisted story generation, include them in the prompt and review the
   generated draft against them; this is separate from annotating an existing
   corpus.

**Output:** an annotated outline or revision plan linking intended devices to
specific passages or scenes. A planned occurrence remains distinct from a
supported reading of the completed draft.

**Illustrative task:** use STR09, setup and payoff, to track an introduced element
and its later consequence. Explain the causal or interpretive connection;
repetition by itself does not supply the payoff.

Combination prompts can use `related_patterns` as a starting point. GEN03,
thriller, lists STR04, suspense, and EFF02, fear / dread / anticipation. An
illustrative generation request is:

> Within an outline organised around sustained threat (GEN03), draft a scene
> that makes a consequential outcome and its stakes clear, then delays resolution
> (STR04). Identify the threat or uncertainty intended to invite anticipation
> (EFF02), and mark which passages support each choice.

Review the genre, narrative structure, and proposed effect separately. A brief
tense beat alone does not establish GEN03, and the combination does not guarantee
that an audience will experience fear. STR05's `creative_use` instruction,
"Plant a cue that remains plausible before its later significance is known",
can likewise become a drafting constraint paired with a later-event check.

**Prerequisites and boundary:** this is currently a manual use of the source
material. An interactive planner or writing application would need separate
implementation. A drafting choice does not guarantee an audience effect.

## LLM-assisted pre-annotation

**User and question:** an annotation team asks whether a model can propose useful
candidate labels and evidence for human review.

**Inputs:** a stable annotation schema, fixed units, reviewed criteria and
calibrated cases, hard negatives, a permitted model-access arrangement, and
recorded prompt and model versions.

Inclusion/exclusion pairs can supply branches in a proposed decision tree or
instructions in a few-shot prompt. Include examples that meet the criteria and
hard negatives that resemble the pattern but are ruled out by the exclusions. For STR05,
ask whether an earlier cue and a supported later event can both be located;
ominous atmosphere alone is an exclusion, not sufficient support.

The hypothesis is that explicit exclusions help reject false positives. To test
it, compare prompts with and without those exclusions on the same held-out,
human-coded cases, keeping the model and other prompt content fixed. Report
false positives and missed positives; no reduction has been measured here.

**Workflow:**

1. Establish independent human coding for a comparison set under the pilot
   protocol and preserve it before model-assisted review.
2. Supply the model with the relevant criteria and sufficient permitted context
   to assess the requested unit and linked events.
3. Request candidate decisions with recoverable evidence locators and uncertainty.
4. Validate record structure and have a human verify each evidence reference and
   coding rationale, retaining rejected and revised suggestions.
5. Compare suggestions with independent coding and report errors by pattern and
   inspected scope before deciding whether to extend use.

**Output:** model proposals kept distinct from human-reviewed annotations,
together with recorded corrections, failure cases, and comparison results.

**Illustrative task:** ask for candidate STR05 cue-event pairs, then check that
both locators exist and that the later event supports the proposed connection.
A model suggestion without the later context cannot establish foreshadowing.

**Prerequisites and boundary:** no model integration, prompt evaluation, or
annotation validator exists here. This is a future evaluated workflow. A model
miss or unavailable segment cannot establish pattern absence, authorial
intention, or audience response.

## Editorial and commissioning review

**User and question:** an editor or commissioning reviewer asks whether a draft
supports a claimed device and what revision would make the intended structure
clearer.

**Inputs:** an agreed review brief, the exact draft version, sufficient context
for the selected patterns, and access to the relevant criteria.

**Workflow:**

1. Agree which claims and units are being reviewed and whether absence claims
   are within scope.
2. Inspect the relevant units and any linked earlier or later material.
3. Record the supported label, evidence, uncertainty, or adequately inspected
   absence, keeping intended effects separate from observed structure.
4. Give a revision action tied to the evidence and retain alternative readings
   where the criteria do not resolve the question.

**Output:** a commissioning or script-editing checklist and review memo. For each
claimed pattern, show the inspected unit, supporting or contrary evidence,
presence decision, uncertainty, and any proposed revision. Keep an uninspected
claim visibly distinct from an `absent` decision. An absence entry records which
material was inspected and why that scope was adequate for the pattern.

**Illustrative task:** review a proposed red herring under STR06. Locate the
misleading cue, the inference it invites, and corrective evidence. If a required
link is unsupported, identify it as a revision question rather than assuming the
device has succeeded.

**Prerequisites and boundary:** adequate inspection and an agreed brief are
needed. Pattern coverage alone does not establish literary quality, commercial
potential, or a commissioning decision. The repository provides no automated
review service.

## Taxonomy research

**User and question:** a maintainer or researcher asks which definitions,
relations, or workbook mappings cause ambiguity and what evidence supports a
revision.

**Inputs:** the preserved source CSV and checksum, source-workbook mappings,
version history, and, for empirical revision, located cases and retained
independent coding disagreements.

**Workflow:**

1. Trace a definition to its source-workbook mapping and record the issue being
   examined.
2. Compare the source criteria with real positive, negative, and borderline
   cases; distinguish a documentation concern from an observed coding failure.
3. Examine disagreements using the proposed
   [boundary matrices](../30_design/303_boundary_matrices.md), retaining cases
   that the matrices do not resolve.
4. Propose a change with its evidence, mapping rationale, and version
   consequences under [CONTRIBUTING.md](../../CONTRIBUTING.md).
5. Preserve earlier definitions and annotations and record any status decision
   through the contract's evidence requirements.

**Output:** a traceable change proposal or revision record that explains the
problem, supporting cases, and consequences for existing annotations. A methods
or provenance report with a supplementary mapping table is a potential research
output once its reasoning and evidence have been assembled.

The current `original_workbook_mapping` cells already identify transformations:

| Pattern | Source mapping text | Question for the provenance record |
|---|---|---|
| DEV06, metaphor | `D2 Metaphors; D3:D17 corrected` | What was corrected, and which source material and coding evidence justify it? |
| DEV11, shared experience / generalisation | `F2 Shared Truths; F3:F17 reframed` | Why was the original concept reframed, and what distinction does that preserve? |
| VID05, startle cue / jump scare | `C11 Jump scares relocated` | Why was the item relocated to audiovisual expression, and what cases support that choice? |

These cells record mapping actions, not their full justification. A research
record would pair each original label and locator with the revised definition,
action, rationale, evidence, and version consequence. Inspect the original
workbook where available and record any source gap. Retained disagreements can
then show where the original grouping fails under coding pressure; the action
labels alone do not establish such a failure or publication readiness.

**Illustrative task:** investigate disagreements between STR05, foreshadowing,
and STR09, setup and payoff. Test whether the proposed boundary guidance helps
on retained cases rather than treating the matrix as an accepted result.

**Prerequisites and boundary:** a source and mapping audit can begin now.
Claims about reliability or improved coding need pilot observations. This use
case does not itself authorise changed definitions, typed relations, or pattern
status upgrades.
