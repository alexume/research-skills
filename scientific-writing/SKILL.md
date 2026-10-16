---
name: scientific-writing
description: Scientific writing and authorial revision rules for academic prose in social and environmental science. Use when Codex needs to edit, tighten, or review article prose; preserve an author's existing voice; or revise an AI-assisted draft so that its claims, rhythm, and wording reflect documented intellectual choices rather than generic academic templates.
---

# Scientific Writing

Use this skill as a line-editing and argument-tightening layer for academic prose.

Read `project/project_profile.yaml` when operating inside a research project. Revise in the declared manuscript language unless the user explicitly requests a translation or a journal requirement overrides it. Do not treat the language of an existing draft as authoritative when it conflicts with the profile.

Use it alone when the main problem is weak prose, inflated rhetoric, or imprecise claims.
Use it together with `alex-urrego-style` when the text also needs stronger historical, socioecological, and Latin American framing.
When the problem is missing synthesis rather than sentence quality, diagnose it and return the text to `writing-paper-draft` in `develop_argument` mode before line editing.

## Select the Intervention Mode

### `line_edit`

Use for local problems of clarity, precision, repetition, syntax, or register.

### `revise_author_text`

Use when editing prose written by the author.
Preserve analytical sequence, distinctive vocabulary, historical texture, and justified rhythm.
Make the smallest intervention that solves the problem.

### `authorial_revision`

Use for AI-assisted or heavily reconstructed prose.
Read and apply [references/authorial-revision.md](references/authorial-revision.md).
The purpose is to restore intellectual ownership and manuscript-specific reasoning, not to evade AI detection.

## Workflow

1. Identify the section type and intervention mode.
2. Reconstruct the paragraph's analytical job before changing its prose.
3. Revise so that the claim, evidence, and interpretation appear in the order best suited to that argument.
4. Remove filler, vague emphasis, stacked hedging, and performative contribution language.
5. Replace abstract nouns with named mechanisms, quantities, places, periods, or citations.
6. Check that each major claim is evaluable.
7. Check for structural writing failures that line editing cannot repair.
8. Check whether defensive editing has removed the manuscript's debate payoff or left claimed domains merely adjacent.
9. For publication prose, apply the authorial revision check before treating the text as final.

Record intellectual interventions in `paper/authorial_revision_log.md`. Record the invocation and technical outputs of this skill in `project/skill_execution_log.csv`; the two logs are not substitutes for each other.

## Section Calibration

- Apply most strictly to abstracts, introductions, discussions, and conclusions.
- Apply with moderation to results and methods.
- Allow passive voice in methods when it matches disciplinary convention.
- Keep impersonal academic register in submission prose.
- Do not apply these rules rigidly to code, README files, or internal notes.

## Editing Rules

- State the finding directly. Do not announce that a finding is coming.
- Prefer one controlling analytical move per paragraph, while allowing a cumulative historical sequence when the explanation requires it.
- Allow longer or layered paragraphs when successive sentences develop the same historical mechanism, empirical sequence, or interpretive problem.
- Prefer specifics over abstractions.
- Keep signposting minimal and functional.
- Use binary contrasts only when the contrast carries analytical content.
- Keep adverbs only when they add epistemic or quantitative meaning.
- Replace generic importance claims with the actual implication.
- Replace generic contribution claims with the actual finding.

## Structural Diagnostics

Use these labels only when they affect prose quality:

- `WORKFLOW LEAKAGE`: route, gate, audit, or identification labels substitute for the substantive argument.
- `CAVEAT DOMINANCE`: repeated limits organize the paragraph or section.
- `PARALLEL DISCUSSION`: adjacent sections remain thematic lists rather than a cumulative interpretation.
- `RESULT RESTATEMENT`: the discussion repeats findings without changing their meaning.
- `MISSING SYNTHESIS`: important results or processes are not related.
- `CONTRIBUTION COLLAPSE`: cautious revision leaves a safe but substantively weak argument.
- `ADJACENT DOMAINS`: economic, social, institutional, or biophysical material is juxtaposed without a mediation.
- `DEBATE NON-TRANSFORMATION`: prose states findings and limits without changing an interpretation in the literature.
- `EDITORIAL LABEL LEAKAGE`: a journal-family identifier or calibration label appears as manuscript argument.

Do not solve these failures through local rewriting. Preserve the text, report the diagnosis, and invoke or recommend `writing-paper-draft` in `develop_argument` mode.

Do not delete a defensible historical or structural interpretation merely because it is not econometrically identified. Require evidence-bounded wording, specified mediation, timing, scale, and sources. If the necessary support is missing and the claim is central, return it for evidence retrieval or author decision.

## Claim Standard

Treat a major analytical sentence or sentence cluster as incomplete unless it is anchored by at least one of:

- a number,
- a mechanism,
- a citation,
- a place,
- a time period,
- or a named process.

If none are available, either cut the sentence or rewrite it more narrowly.

## Project Vocabulary

Follow the lexical guidance in [references/prose-rules.md](references/prose-rules.md), especially for terms such as `heterogeneity`, `agrarian transformation`, `ecological pressure`, `multiscalar`, `nexus`, and `policy-relevant`.

When a term is too broad, name the variable, scale, geography, mechanism, or policy directly.

Treat project-specific examples in that file as illustrations, not universal vocabulary bans.

## Combination With `alex-urrego-style`

Use `alex-urrego-style` to decide:

- the intellectual framing,
- the historical interpretation,
- the socioecological concepts,
- and the broader Latin American narrative.

Use this skill to decide:

- sentence shape,
- paragraph discipline without mechanical uniformity,
- rhetorical cuts,
- and lexical precision.

The intended combination is:

1. `alex-urrego-style` sets the voice and analytical horizon.
2. `scientific-writing` tightens the prose and removes weak academic habits.
3. `authorial_revision` checks that the final prose reflects manuscript-specific reasoning and documented choices.
4. Do not cut historical texture, citation nuance, or paragraph rhythm merely to make prose shorter.
