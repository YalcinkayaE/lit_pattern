---
document_id: DOC-501
title: Pilot Protocol
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed pattern vocabulary
authority: controlled
supersedes: null
related:
  - DOC-201
  - DOC-302
  - DOC-303
  - DOC-502
---

# Pilot Protocol

This is a planned pilot. No annotator has been recruited, no corpus has been
selected, and no agreement result exists.

## Question

Can independent annotators apply selected pattern definitions consistently to
small literary and audiovisual units when given criteria, examples, and evidence
rules?

## Pattern sample

Start with these ten patterns across label types and difficulty:

- GEN05, science fiction;
- MODE02, magical realism;
- DEV02, verbal irony;
- DEV03, sarcasm;
- STR02, surprise;
- STR03, revelation;
- STR05, foreshadowing;
- STR06, red herring;
- STR09, setup and payoff;
- EFF02, fear, dread, or anticipation.

This is a proposed sample. Do not change it after seeing agreement results unless
the change and its reason are recorded.

## Case set

For each pattern, prepare:

- one invented teaching example;
- one real exemplar with edition or release version and locator;
- one hard negative that meets the apparent surface cue but not all criteria;
- one borderline case;
- one adjudicated label for the borderline case;
- the expected false positive named in operational terms.

Use at least two works: one literary and one video. Prefer two or three works in
each modality if practical, but do not commit full copyrighted files to the
public repository.

## Unit design

Code 20 to 30 units per pattern across the works selected. Units should include
clear positives, hard negatives, and context that lets a sequential pattern
extend beyond a single passage or scene.

Record exact unit definitions before coding. Segment video with stable
timestamps. Segment literature by stable edition and chapter, page, paragraph,
or another recoverable locator.

## Annotator sequence

1. Recruit two or three annotators with relevant close-reading or media-analysis
   experience.
2. Give them the pattern definitions, global evidence rules, unit rules, and
   case examples.
3. Withhold the boundary matrices during the first independent round so natural
   disagreement can be observed.
4. Ask each annotator to code independently.
5. Preserve every original annotation before adjudication.
6. Calculate agreement by pattern and report uncertainty where sample size is
   small.
7. Discuss disagreements against `docs/30_design/303_boundary_matrices.md`.
8. Record every recurring disagreement class and revise the matrix or definition
   as needed.
9. Run a second round with the revised materials if the first round exposes
   material instability.

## Agreement measures

Use an agreement approach suited to the final design:

- Cohen's kappa for two annotators on categorical presence;
- Fleiss' kappa for more than two annotators on categorical labels;
- Krippendorff's alpha when missing values or ordinal interpretation need a
  general coefficient.

Report raw agreement, the coefficient, the number of units, the number of
annotators, and the exact coding categories. Do not report a coefficient without
its baseline and interpretation context.

The proposal mentions a threshold of at least 0.6 kappa on at least 6 of 10
patterns. Treat that as a provisional target, not an accepted scientific
criterion. Review it before the pilot.

## Outputs

- Dated pilot protocol version.
- Work and version register.
- Located case set.
- Independent annotation exports.
- Agreement report.
- Adjudication log.
- Revised boundary matrix.
- Versioned codebook.
- Pattern status decisions.

## Status progression

- `proposed` at the current stage.
- `drafted` after the pattern materials and cases are complete but before
  independent coding.
- `pilot_tested` after the pilot produces recorded observations.
- `validated` only after the fixed protocol and revision round are complete and
  reviewed.

## Stop conditions

Pause the pilot if:

- the same unit can refer to different text or release versions;
- annotators cannot determine which unit to inspect;
- the evidence package contains copyrighted or private material that cannot be
  stored lawfully;
- many pattern definitions lack a real exemplar;
- the case set contains only invented examples;
- the current pattern version is changed during independent coding without
  restarting or versioning that round.

