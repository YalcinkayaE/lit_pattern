---
document_id: DOC-303
title: Boundary Matrices
status: proposed
owner: unresolved
created: 2026-11-11
updated: 2026-11-11
applies_to: proposed coding rules
authority: controlled
supersedes: null
related:
  - DOC-201
  - DOC-302
  - DOC-501
---

# Boundary Matrices

These matrices are proposed decision aids. They need pilot testing. They do not
override the source pattern definitions.

## Sequential cluster

Patterns: STR02, STR03, STR05, STR06, STR09, with DEV01 as a local mismatch
comparison.

| Pair | What differs | Decision rule |
|---|---|---|
| STR02 Surprise vs STR03 Revelation | Surprise revises a future expectation through an event; revelation revises interpretation of earlier evidence | Does new information change what will happen or what earlier material meant? If the latter, STR03 |
| STR03 Revelation vs STR06 Red herring | Revelation adds a new reading; red herring displaces an invited prior reading | Was a specific alternative interpretation actively encouraged earlier? If yes and later weakened, code STR06 and STR03 |
| STR05 Foreshadowing vs STR09 Setup and payoff | Foreshadowing is a cue-event link; setup and payoff is an introduced-element-consequence link | Is the earlier item a non-salient hint or a salient introduced element? Hint suggests STR05; element suggests STR09; both can apply |
| STR05 Foreshadowing vs STR03 Revelation | Foreshadowing anticipates an event; revelation recontextualises prior material | Does the later event fulfil the cue or reinterpret it? Both can occur |
| STR02 Surprise vs STR06 Red herring | Surprise revises expectation in a beat; red herring sustains a mistaken interpretation over time | Is the revision immediate or sustained and later corrected? |
| STR09 Setup and payoff vs STR05 Foreshadowing | Salience at first introduction and the nature of the later consequence distinguish the pair | Code both only when both Criterion sets are independently supported |
| The sequential cluster vs DEV01 Incongruity | DEV01 can operate within one passage; sequential patterns depend on a later unit | If the effect depends only on a local internal mismatch, code DEV01 |

Proposed adjudication ladder:

1. Is there a later consequential event? If no, stop.
2. Does the later event revise the interpretation of earlier material? Then
   consider STR03.
3. Was a specific alternative interpretation actively invited and later
   weakened? Then consider STR06.
4. Is the earlier item non-salient and later fulfilled? Then consider STR05.
5. Is the earlier item salient and later used? Then consider STR09.
6. Does one event revise an expectation at presentation? Then consider STR02.

## Irony cluster

Patterns: DEV02, DEV03, DEV08, STR10, with MODE01 as a work-level contrast.

| Pair | What differs | Decision rule |
|---|---|---|
| DEV02 Verbal irony vs DEV03 Sarcasm | Verbal irony invites a non-literal reading; sarcasm adds a target and cutting stance | If there is a specific target and mockery, code DEV03 and DEV02 |
| DEV02 Verbal irony vs STR10 Dramatic irony | Verbal irony is utterance-internal; dramatic irony depends on a knowledge asymmetry | Does the effect come from what is said or from who knows what? |
| DEV03 Sarcasm vs DEV08 Rhetorical question | Sarcasm is a mocking act; rhetorical question is a pragmatic interrogative act | Ask whether the primary act is an assertion or a challenge and appeal; a mocking question may be both |
| DEV02 Verbal irony vs DEV08 Rhetorical question | Irony invites an evaluative inversion; a rhetorical question invites a pragmatic response | Does the utterance invert an evaluation or solicit a response it does not literally expect? |
| DEV03 Sarcasm vs STR10 Dramatic irony | Sarcasm can use dramatic irony but does not require it | Is the cut dependent on audience knowledge that the addressee lacks? |
| Irony cluster vs MODE01 Satire | Satire is a sustained critical stance; the other patterns can realise it locally | Treat work or mode level separately from utterance or scene level |

Proposed decision tree:

```text
START: An utterance is under consideration.
|
+-- Is there a context-supported non-literal evaluative reading?
|   +-- No: not in this cluster; consider DEV01 or literal speech.
|   +-- Yes: continue.
|
+-- Is there a specific target and a cutting or mocking stance?
|   +-- Yes: DEV03 is present; also code DEV02 when its criteria hold.
|   +-- No: continue.
|
+-- Is the primary pragmatic act an interrogative challenge or appeal
|   with limited expectation of an answer?
|   +-- Yes: DEV08 is present; also code DEV03 when the question mocks a target.
|   +-- No: continue.
|
+-- Does the effect depend on audience knowledge unavailable to a character?
|   +-- Yes: STR10 is present; co-code the form-based patterns as applicable.
|   +-- No: continue.
|
+-- Does the utterance invert an evaluation without requiring a target
|   or interrogative form?
|   +-- Yes: DEV02 is present.
|   +-- No: re-examine the first question.
```

## Adjudication caveat

These matrices are hypotheses. The pilot must preserve cases where the ladder
does not settle the disagreement. Those unresolved cases are evidence that the
definition or matrix needs revision.

