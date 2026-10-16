# Argument Development

Use this protocol before drafting or deeply revising an introduction, discussion, or conclusion when the evidence exists but the interpretation remains fragmented, parallel, or defensive.

## Contents

- Core Distinction
- Reconstruct The Problem
- Build Relational Synthesis
- Construct The Argument Sequence
- Decide Evidence Actions
- Preserve Or Reconsider The Contribution
- Compare Architectures And Obtain Author Approval
- Output Contract
- Failure Diagnostics

## Core Distinction

Keep three layers separate:

1. internal controls: route, identification status, evidence strength, and workflow decisions;
2. argument architecture: relations among patterns, processes, mechanisms, scales, and debates;
3. manuscript prose: the clearest evidence-bounded expression of that architecture.

Internal controls govern claim strength. They do not become the paper's substantive argument unless the method itself is under discussion.

## Reconstruct The Problem

Identify:

- the main empirical or historical tension;
- the results that appear contradictory, disconnected, or merely parallel;
- the question that the existing discussion has not yet answered;
- the debate whose interpretation could change;
- the strongest positive answer supported by the evidence.

Do not assume that every paper needs a contradiction. Select only relations that arise from the materials.

## Build Relational Synthesis

For the most relevant results or processes, ask:

- What economic, social, political, cultural, and biophysical processes are related?
- Is the relation one of tension, co-constitution, mediation, displacement, accumulation, feedback, comparison, sequence, or scalar transformation?
- Which actors, institutions, infrastructures, technologies, knowledge systems, and practices mediate it?
- How does the relation vary across periods, territories, populations, or scales?
- Which material or ecological process is transformed, and through what social organization?
- What rival relation could produce the same observed pattern?
- What does the combined interpretation change in the literature?

Use relational categories as prompts, not as a fixed template. Rank candidate connections by explanatory yield and evidentiary support. Prefer a few consequential relations over an exhaustive network.

When integration is part of the claimed contribution, require a named mediation connecting the domains. A sequence of adjacent summaries does not establish a relation.

## Construct The Argument Sequence

Choose an order suited to the case. A useful but non-mandatory sequence is:

`patterns in tension -> mediations -> differentiated outcomes -> conceptual consequence`

Other valid forms include historical accumulation, process comparison, feedback, conjunctural explanation, and scale reversal. Preserve chronology when sequence is itself explanatory.

For each major section, specify:

- analytical job;
- opening claim;
- evidence mobilized;
- relation developed;
- mechanism or mediation;
- rival or boundary;
- payoff for the debate;
- transition to the next section.

## Decide Evidence Actions

Classify every central bridge as:

- `supported`: draft positively and cite;
- `supported with boundary`: draft positively, then state one material limit;
- `retrievable`: invoke `wiki-consult` in `argument_support` mode;
- `author decision`: ask for the interpretation or emphasis that cannot be inferred from artifacts;
- `blocking gap`: do not finalize the affected section;
- `nonblocking gap`: use a precise placeholder;
- `park`: omit from the current argument.

Do not solve a missing bridge by adding repeated hedging. Do not ask the user for information that can be retrieved safely from the project or KnowledgeWiki.

## Preserve Or Reconsider The Contribution

Before `narrow`, `park`, or `delete`, apply the contribution-preservation test in [project-argument-profile.md](project-argument-profile.md).

Distinguish:

- an overclaim that should be removed because the proposed relation exceeds the design or contradicts evidence;
- a plausible explanatory bridge whose current support is insufficient but retrievable;
- an intellectual choice among defensible contributions that belongs to the author.

Do not reward the least ambitious formulation merely because it is easiest to defend. If removing a bridge turns the discussion into an audit of indicator limits, a list of findings, or a contribution weaker than the introduction promises, retrieve evidence and request a precise author decision. Mark the affected architecture provisional or blocked.

## Compare Architectures And Obtain Author Approval

When more than one materially different contribution remains defensible, follow [project-argument-profile.md](project-argument-profile.md) and compare two to four architectures. Do not draft polished discussion prose until the author selects or revises the architecture, unless the user explicitly requests a provisional draft.

Treat approval as an intellectual checkpoint. A workflow log, gate result, target journal, or existing manuscript does not substitute for author approval.

## Output Contract

Produce `analysis/discussion_argument_map.qmd` or the user-requested equivalent with:

```markdown
## Central Tension Or Problem

## Strongest Warranted Interpretation

## Relational Synthesis

| Result or process A | Result or process B | Relation | Mediations | Timing and scale | Evidence | Rival or boundary | Status |
|---|---|---|---|---|---|---|---|

## Section Architecture

| Section job | Main claim | Evidence | Relational move | Debate payoff | Transition |
|---|---|---|---|---|---|

## Evidence Actions

## Author Decisions

## Workflow Language To Keep Out Of Prose

## Contribution-Preservation Assessment

## Author Approval Status
```

When contribution or architecture remains open, also produce `project/project_argument_profile.qmd` using [project-argument-profile.md](project-argument-profile.md).

## Failure Diagnostics

- `PARALLEL DISCUSSION`: themes accumulate without changing one another.
- `RESULT RESTATEMENT`: prose repeats findings without interpretive work.
- `MISSING SYNTHESIS`: a consequential relation is asserted but not developed.
- `CAVEAT DOMINANCE`: limitations organize the paragraph or section.
- `WORKFLOW LEAKAGE`: route or audit language substitutes for substantive argument.
- `UNSUPPORTED BRIDGE`: a transition carries a claim without traceable support.
- `FORCED DIALECTIC`: the prose invents opposition because the protocol mentioned tension.
- `CONTRIBUTION COLLAPSE`: narrowing or parking leaves a safe but substantively weak paper.
- `ADJACENT DOMAINS`: economic, social, institutional, or biophysical material appears side by side without a named mediation.
- `DEBATE NON-TRANSFORMATION`: the discussion states limits but does not change how the relevant literature should interpret the evidence.
- `EDITORIAL LABEL LEAKAGE`: a journal-family or calibration identifier appears as manuscript argument.

Do not proceed to polished prose when a central relation remains a blocking gap or an unresolved author decision.
