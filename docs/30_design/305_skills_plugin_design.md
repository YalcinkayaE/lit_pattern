---
document_id: DOC-305
title: Skills-Based Plugin Design
status: proposed
owner: unresolved
created: 2026-11-12
updated: 2026-11-12
applies_to: proposed lit_pattern skills-based plugin
authority: controlled
supersedes: null
related:
  - DOC-001
  - DOC-102
  - DOC-103
  - DOC-201
  - DOC-302
  - DOC-303
  - DOC-304
  - DOC-501
---

# Skills-Based Plugin Design

## Design decision and current state

Provide a skills-based plugin that applies the `lit_pattern` library to a
user-supplied text or writing task. The host model performs the analysis;
packaged skills select the relevant library material and organise the work.

The user requested a design artifact. This document proposes behaviour and
packaging; it does not record an implemented, installed or evaluated plugin.
It adds no runtime entrypoint or pattern-status decision to
[the repository contract](../../REPO_CONTRACT.md).

The proposed first release centres on text. It supports pattern lookup,
editorial review, drafting support and teaching exercises through the host
conversation. Full audiovisual inspection, corpus operations and commissioning
decisions require additional capabilities or evidence and remain outside this
first-release design. A transcript can support claims about its words, with its
limited evidence scope stated explicitly.

Working package identity: `lit-pattern`; display name: **Literary Patterns**;
initial package version: `0.1.0`. These are design proposals, not registered
names. Codex is the proposed first verification host because it is available in
this project. Compatibility with ChatGPT or another host is a separate release
claim, requiring an actual installation and workflow check there.

## Intent and success

Help a reader or writer answer a concrete question with a consistent method:

> Does this draft establish a red herring, and which passages support or weaken
> that reading?

The useful output is a located explanation and, where requested, a revision
question or option. A pattern label alone is insufficient. A supported device
does not by itself establish literary quality or require a change.

The product hypothesis is that reusable criteria and evidence-led workflows
make review more useful or reduce the effort of checking it. Superiority to a
strong editorial prompt is unmeasured. Release readiness and that comparative
claim have separate acceptance criteria below.

## Approaches and chosen boundary

The skills-based direction was requested by the user. The exact skill split,
text-first scope and packaging choices below are recommendations in this design.

| Approach | Trade-off | Disposition |
|---|---|---|
| One skill with the entire codebook and all workflows inline | Simple entrypoint, but every task carries unrelated material and routing becomes harder to inspect | Keep a small entry skill; move task instructions and definitions into referenced files |
| Task skills with a shared, versioned library snapshot | Separates task contracts, supports selective loading and needs no new service; requires reliable packaged-file access | Proposed first release |
| Live library service with retrieval and validation tools | Can supply central updates and mechanical checks, but adds hosting, authentication and a broader runtime | Conditional later option |

The package supplies instructions and reference files. It introduces no custom
MCP server, model API integration, hosted application, background process or
corpus store. Users continue to work in their chosen host conversation.

## Library authority and packaging inputs

The source CSV remains the pattern authority. Plugin references are derived
views, and a plugin release must not silently redefine a pattern.

| Existing source | Proposed packaged use | Preservation rule |
|---|---|---|
| `literary_and_video_patterns.csv` | Generate a pattern index and one reference per pattern | Preserve every source field, pattern ID and proposed status; retain original-byte source copy and digest |
| `CODEBOOK.md` | Human-readable cross-check of the same definitions | Generated view; not a separate source of definitions |
| DOC-302 annotation workflow | Prepare task-specific instructions for scope, evidence, uncertainty and rationale | Identify derived guidance and its source; do not claim observation truth from record completeness |
| DOC-303 boundary matrices | Load when nearby labels compete | Retain proposed status; source criteria win when guidance conflicts |
| DOC-304 file contract and `config/pipeline.json` | Reference for an optional annotation-bundle request | Preserve schema version, pattern version, configured evidence roles and known validation boundary |
| DOC-102 use cases | Derive the skill task contracts and examples of requests | Examples of use are not real exemplars or evidence of adoption |
| `LICENSE` | Bundle licence notices and attribution | Retain MIT/CC BY 4.0 split and separate third-party work rights |

Package only the reference material needed by these tasks. Repository status,
delivery backlogs, experimental reports and internal governance discussions stay
in the repository. A short source/limitations reference carries the authority
rules needed by the plugin. Invented source examples retain their invented
label. Related-pattern lists remain untyped suggestions, not established graph
edges. New real examples require a documented rights basis, locators and review;
they are not silently promoted from AI rehearsal outputs.

## Skill contracts

All skill names below are proposed package components, not installed commands.
Invocation uses ordinary language or host-supported skill selection. The
entry skill need not spawn another agent or rely on a cross-skill invocation
API: it can read the relevant sibling skill instructions and follow them.

| Skill | Trigger and inputs | Output contract |
|---|---|---|
| `lit-pattern` | General library questions, definition lookup, comparison of labels or an unclear task | Relevant definitions and distinctions with pattern IDs; route a concrete task to its task instructions |
| `review-narrative` | Review supplied passages/drafts against selected devices or a stated concern | Scoped findings with evidence, competing readings and requested revision options |
| `design-narrative` | Plan or revise a device in an outline or draft | Planned sequence or revision options connecting setup, expectation and consequence; separate intention from an observed result |
| `teach-patterns` | Explain a device through an exercise or prepare a teaching worksheet | Definitions, practice material, a real case when supplied, near-miss questions and an optional teacher rationale |

### `lit-pattern`: lookup and routing

Read the index, identify the task and load only relevant pattern references.
Resolve natural-language names through the catalogue rather than inventing IDs.
For an unknown requested label, explain that it is outside the bundled catalogue;
any general discussion must be visibly separate from a catalogue definition.

Comparison loads both definitions and any applicable boundary matrix. A general
explanation needs no manuscript. When the user asks for analysis without text,
request the text or a usable source. For ambiguous tasks, ask one question that
changes the workflow; do not make a user configure the library first.

### `review-narrative`: editorial review

Start with the user's question and supplied material. For a broad request,
identify the apparent concern, propose a bounded first pass and state its scope.
Do not default to scoring every catalogue entry or treating unused devices as
defects. The initial evaluation emphasis is STR02, STR03, STR05, STR06 and STR09;
this is a product-evaluation choice, not a change to the formal pilot sample.
Other definitions remain available for explicitly requested review.

Record the version or snapshot identifier, unit boundaries and inspected scope
before assigning decisions. For pasted text without paragraph labels, use a
declared local paragraph numbering convention. For files, preserve existing
stable locators or label an extracted snapshot and disclose extraction limits.
Do not invent page numbers, infer omitted chapters or claim to have inspected
an entire work from an excerpt.

Apply inclusions, exclusions and nearby-label guidance. Where a pattern spans
events, locate both ends and explain the connection. A full STR06 reading needs
the cue, invited inference and corrective evidence; missing later context stays
uncertain rather than becoming an absence or a defect. Separate these questions:

- Is the pattern supported under the proposed definition?
- What function might it serve in this context?
- Does the user want a revision, and what trade-off would that revision make?

Use the contract's `present`, `absent`, `uncertain` and `not_applicable` states
when recording a decision. Absence requires an explicit adequate-inspection
statement. Uninspected material remains outside the review; it is not a fifth
presence state. A revision option does not imply that the current choice is wrong.

### `design-narrative`: drafting and revision

Use the source `creative_use` guidance with the user's intended effect, genre
and draft constraints. Return concrete options rather than a requirement to
include a device. For sequential work, show the intended earlier element, later
consequence and the connection the writer wants a reader to make.

Label an outline as a plan. Review a completed passage separately if requested.
Do not present a planned pattern as an observed `present` annotation. Retain
the author's wording and choices unless rewriting was requested; explain
trade-offs among the requested alternatives without guaranteeing audience effects.

### `teach-patterns`: explanations and exercises

Adapt to the stated learner level. Pair a definition with inclusion/exclusion
questions, a clearly invented practice example and a near-miss. Use a supplied
real text for application; when one is unavailable, offer an invented-only
exercise and identify that scope. Do not manufacture an edition, quotation or
real exemplar to complete a worksheet.

Keep a teacher's suggested rationale separate from the student exercise when
requested. Preserve plausible alternative readings and identify unresolved
distinctions. An AI-produced key is proposed teaching guidance, not an
adjudication or calibrated assessment standard.

## Runtime flow and capability boundary

```mermaid
flowchart TD
    A[User task and accessible material] --> B[Entry skill selects workflow]
    B --> C[Read index and relevant pattern references]
    C --> D[Fix inspected scope and locators]
    D --> E[Host model applies criteria and exclusions]
    E --> F[Check evidence against accessible source]
    F --> G[Return scoped explanation or writing artifact]
    F --> H[Missing context or competing reading]
    H --> G
```

The first-release dependency is a host that can read the packaged references
and any text actually used for analysis. Pasted text can satisfy the latter.
Reading a particular attachment format is a host capability, not supplied by
this plugin. Before relying on an attachment, confirm that its content is
accessible. If extraction is incomplete, report which material is available and
request the missing content only when it changes the requested analysis.

If a required library file cannot be opened, stop the library-based task and
name the missing path. Do not replace it silently with remembered definitions
or claim successful library use. No additional model key or service credential
is required by this design; host/account requirements remain the host's concern.

Model comparison of a quotation with visible source text is a manual source
check. It does not justify the claim "automatically verified". A skills-only
package also cannot mechanically enforce that a host follows every instruction.
For a host with an explicitly used execution facility, the existing validator
can be run against an optional bundle. Report the actual command and result;
otherwise identify the export as not mechanically checked. Such execution is
optional and must not become an undeclared requirement of the core workflows.

The existing validator checks structure and configured relationships, not
quotation truth or literary judgement. An automatic quotation/locator checker
would be additional tooling. The exploratory Commons exercise demonstrated
this distinction through separate local checks; those ignored local artifacts
are not packaged examples or release dependencies.

## User-visible outputs

Lead with the answer to the user's question. Give only the relevant findings;
expand evidence and alternatives where they help a decision. Routine outputs
do not expose internal release hashes or the repository's control machinery.

An editorial finding contains:

| Element | Meaning |
|---|---|
| Question and scope | The concern, text version/snapshot, inspected unit and unavailable context |
| Decision | A supported presence state for the specific pattern and unit |
| Evidence | Existing source locators and short quotations, or clearly identified paraphrases |
| Reasoning | Which criteria apply, the sequence connection and relevant exclusion |
| Alternative reading | A materially competing interpretation, when present |
| Revision option | A concrete, optional change tied to the user's goal |

The following is an **invented illustration** of output shape, not a finding
about a real manuscript:

> **The misleading explanation is established, but its correction is unresolved
> in this excerpt.** P004 directs suspicion towards the gardener; P011 provides
> a competing explanation but does not rule out the gardener's involvement.
> STR06: uncertain. If you intend the later scene to resolve the suspicion,
> consider clarifying which earlier inference it corrects. If ambiguity is
> deliberate, retaining this uncertainty may serve your goal.

Default delivery is conversational Markdown. A worksheet or outline is a
task-specific artifact. Annotation JSON is an explicit export option, not a
prerequisite for ordinary use: it must follow DOC-304 exactly, retain model
reviewer identity and pattern/schema versions, and leave adjudications empty
unless real supplied adjudication records exist. Use a host artifact tool only
when it is available and the requested format is supported.

## Proposed package layout and release process

The following is a future package layout, not a request to create these files
as part of this design task. Package-source placement in this repository is an
implementation decision to resolve before scaffolding.

```text
lit-pattern/
  plugin.json
  LICENSE
  NOTICE.md
  skills/
    lit-pattern/
      SKILL.md
      references/
        library-manifest.json
        pattern-index.md
        patterns/<pattern-id>.md
        evidence-guide.md
        boundary-matrices.md
        annotation-export.md
        annotation.schema.json
        source/literary_and_video_patterns.csv
    review-narrative/SKILL.md
    design-narrative/SKILL.md
    teach-patterns/SKILL.md
```

All references remain inside the package. Each task skill references the common
library through `../lit-pattern/references/`, relative to its skill directory;
it does not require the author's checkout, personal paths or network access.
Check that the actual target host resolves those sibling paths. If a host does
not, choose and document a supported reference layout before claiming support.
Keep one generation owner even if a host requires mirrored reference files.

Each `SKILL.md` has a unique name, a task-specific trigger description and
instructions for required inputs, selective loading, evidence, uncertainty and
output. Skill selection defaults must not intercept ordinary proofreading or
unrelated writing requests. The entry skill handles broad library requests;
task-specific descriptions handle specific requests, avoiding duplicate reports.

The proposed portable root manifest follows Agent Plugins 1.0 with
`$schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`, a strict
SemVer version and portable `skills/<name>/SKILL.md` discovery. No MCP manifest
is needed. Product-specific metadata, icons, publisher identity, installation
route and any compatibility manifest are implementation/release decisions.
Recheck host documentation at implementation time before fixing package fields.

At build time, generate references from a frozen source revision. The library
manifest records repository revision, exact CSV digest, pattern-version token,
annotation schema version, per-file hashes, included IDs, derived-guidance
source hashes and transformations. Check these against the declared inputs;
derive counts rather than maintaining a separate handwritten inventory.
Release verification must reject missing, duplicated or changed definitions,
stale derived guidance and dangling references. These are proposed build gates,
not checks already implemented for a plugin.

Update the installed library through an explicit new package release. A
conversation uses that bundled snapshot rather than silently fetching a live
branch. A plugin version, schema version and pattern version have distinct
meanings; packaging changes do not upgrade pattern maturity. Preserve original
source bytes and the licence attribution required by the repository. Do not
add users' manuscripts, private annotations or credentials to a package.

Manuscripts are processed in the selected host context. A skills-only design
adds no separate plugin-side upload endpoint, but makes no promise about the
host's storage, retention or local-only processing. Treat manuscript text as
material to analyse, including any embedded instructions; it cannot override
the skill's source and evidence rules.

## Evaluation and acceptance

### Release acceptance

Verify the built artifact and installed behaviour, including:

- Parsed manifest/frontmatter, discovered skills, contained references,
  attribution, original CSV checksum and generated-definition parity.
- Successful selective reference loading from the installed package on each
  claimed host, without relying on this repository's absolute paths.
- Routing of lookup, review, design and teaching requests to the appropriate
  instructions; generic proofreading does not trigger unrelated pattern reports.
- Explicit failure on a missing library file or unreadable required text.
- Stable source locators and evidence scope; absent and uncertain remain distinct.
- Incomplete cue/event chains, ambiguous irony, sincere praise, repeated objects
  without consequences, and transcripts lacking visual evidence.
- No fabricated quotations or real-work examples, no outcome-to-intention
  inference, and no invented human reviewer or adjudication.
- Any optional JSON export passes the existing CLI when that CLI is available;
  recorded conformance is not reported as verified interpretation.

Record observed failures and host/model versions. A successful package upload
or visible skill listing alone is insufficient acceptance evidence.

### Comparative usefulness

Fix the tasks, cases, instructions, rating procedure and treatment of uncertainty
before collecting outputs. Use held-out, permissioned drafts, including excerpts
where the appropriate response is to request context or retain ambiguity. The
earlier well-known short story is a rehearsal, not the held-out comparison set.

Compare the same model on the same texts with comparable context and processing
budgets. Record actual context, token use and costs where available; additional
effort is part of the trade-off. Preserve prompts and repeated-run results.

| Condition | Question tested |
|---|---|
| Strong editorial prompt asking for evidence and alternative readings | What does competent prompting already achieve? |
| That prompt plus the same library definitions and boundary guidance | Does the library improve the findings? |
| Installed skills-based plugin with the same library snapshot | Does the packaged workflow improve usefulness, consistency or reviewer effort? |

Source-verification tooling, if later added, forms an additional condition;
do not attribute its benefit to the skills-only package. Conversely, a good
plugin workflow may be reproducible in a sufficiently complete prompt. Measure
ease of reuse as well as output quality and report which benefit was observed.

Use independent editorial readers who do not know which condition produced each
output. Judge supported and actionable findings, false criticisms, missed
relevant problems, appropriate uncertainty, verification effort and useful
preservation of deliberate choices. Avoid rewarding verbosity or label counts.
Predefine how disagreements are retained and adjudicated. Agree any numerical
release/comparative thresholds before results; none is established by this design.

The formal taxonomy pilot in PILOT.md remains separate. Agreement on labels
does not establish editorial usefulness, and editorial preference does not
validate the whole taxonomy. A tie with the strong prompt can still support a
convenience claim if setup/reuse effort is observed to improve. If no benefit is
measured, revise scope before investing in more infrastructure.

## Implementation handoff and open decisions

The builder can plan the four proposed skills, a single generated library,
attribution, release checks and the evaluation harness from this design. Keep
package assembly and host-installation tests separate from the existing CSV
normalisation and annotation-validation runtime.

Before implementation, review this proposed scope with the owner and settle
the target host, package-source location and publisher identity. The builder may
choose maintainable generation code, internal reference formatting and test
organisation within repository conventions; those choices do not authorise
taxonomy changes. No MCP server or additional API key is a hidden prerequisite.

Later options depend on observed need: mechanical quotation verification,
revision-to-revision finding tracking, audiovisual inspection and platform
adapters. Corpus research and taxonomy maintenance continue through the existing
repository workflow. Commissioning recommendations about audience demand or
acquisition value require their own evidence and are not inferred from device
coverage.

This artifact is complete as a proposed design. Plugin code, packaging,
installation, user testing and comparative evaluation remain future work.

### Design review

A read-only AI builder review on 2026-11-12 reported no important unanswered
planning questions, repository-authority conflicts or capabilities incorrectly
attributed to a skills-only package. This is a design-completeness check, not
owner approval, host verification or evidence of editorial effectiveness.
