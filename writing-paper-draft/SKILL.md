---
name: writing-paper-draft
description: "Develop arguments, draft, or restructure academic paper sections from research materials in economic history, environmental history, ecological economics, agrarian studies, and related fields. Use when Codex must connect results into a cumulative interpretation, turn evidence or an argument map into a coherent manuscript, deepen a discussion, or revise an architecture while preserving claim-evidence limits and the author's intellectual choices."
---

# Academic Paper Drafting

Draft academic prose from an established research design, evidence base, or argument map.

Use `alex-urrego-style` for intellectual framing and authorial calibration.
Use `scientific-writing` for local prose revision.
Use `research-claim-evidence-mapping` when the permitted claims are uncertain.
Use `wiki-consult` in `argument_support` mode when a central interpretive bridge needs literature or historical-source support.

Read:

- `project/project_profile.yaml` for manuscript language, required render formats, PDF engine, and table/figure inclusion rules;
- `../shared/output_contracts.md` for the draft contract.
- `../shared/stage_gates.md` before treating a draft as ready;
- `../shared/journal_families.md` when `journal_family` is declared or must be selected.

For argument development, read [references/project-argument-profile.md](references/project-argument-profile.md). Keep project-specific intellectual choices in `project/project_argument_profile.qmd`, not in reusable skill instructions.

If the project profile is missing or incomplete, create or complete it from `../shared/project_profile_template.yaml` before drafting. Do not infer the manuscript language from existing prose when the profile is available.

Use `implementation-tables-and-appendices` when drafting from analytical outputs. Treat `tables/table_manifest.csv` and `appendix/analytical_appendix.qmd` as controlled evidence interfaces; do not copy unregistered console values or create manuscript-only versions of results.
Treat `figures/figure_manifest.csv` the same way. Cite included outputs with stable Quarto cross-references such as `@tbl-main-results` and `@fig-event-study`. Use raw LaTeX inclusion only when the project profile or target journal explicitly requires it.

## Select the Intervention Mode

Choose one mode before intervening.

### `develop_argument`

Use when evidence and results exist but the argument is shallow, fragmented, parallel, dominated by caveats, or insufficiently connected across mechanisms, scales, periods, or debates.

Read and apply [references/argument-development.md](references/argument-development.md).
Produce or update `analysis/discussion_argument_map.qmd` before drafting polished discussion prose. Do not treat fluency as a substitute for a resolved interpretive architecture.
When the central contribution or debate remains unresolved, propose alternative architectures and produce or update `project/project_argument_profile.qmd` before the discussion map. Do not choose among defensible contributions on the author's behalf.

### `draft_from_evidence`

Use when drafting new prose from:

- notes,
- tables or figures,
- archival extracts,
- a literature synthesis,
- a mechanism map,
- or a claim-evidence map.

Do not invent connective claims merely to make the narrative smoother.
Mark unresolved evidence, citations, or interpretation as explicit placeholders.

### `revise_author_text`

Use when the user supplies prose they wrote.

Preserve:

- the author's analytical sequence,
- historically meaningful detail,
- distinctive vocabulary,
- paragraph rhythm,
- and justified ambiguity.

Intervene only where argument, precision, coherence, or readability requires it.
Do not normalize the text into a generic journal voice.

### `restructure_draft`

Use when a complete or partial draft exists but its architecture is weak.

First reconstruct:

- the research question,
- the paper's strongest defensible contribution,
- the evidence sequence,
- the mechanism or interpretive logic,
- and the limits of inference.

Then move, merge, split, or cut material.
Do not line-edit heavily until the argument order is stable.

## Drafting Workflow

1. Identify the section type and intervention mode.
2. Resolve the journal family or record why it remains undecided; use the family as an editorial calibration, not as a prose template.
3. State the section's analytical job in one sentence.
4. List the claims the section must establish and the evidence available for each.
5. For `develop_argument`, build the relational synthesis, alternative architectures when needed, contribution-preservation test, and evidence actions before prose; stop there unless drafting is also requested.
6. For full-paper or discussion drafting, consume `project/project_argument_profile.qmd`, `analysis/interpretation.qmd`, and `analysis/discussion_argument_map.qmd`; if a required artifact is missing, run `develop_argument` first. Require `author-approved` profile status when the author had to choose among materially different contributions. Use an explicit provisional placeholder only when the user requests drafting before the interpretation gate can pass.
7. Decide the most effective order for this specific argument.
8. Draft paragraphs around analytical moves, not around a fixed sentence count.
9. Check transitions, claim-evidence fit, historical continuity, and leakage of internal workflow categories.
10. Check that claimed interdisciplinary relations are mediated rather than merely placed in adjacent paragraphs, and that the discussion changes the relevant debate rather than only auditing indicator limits.
11. Verify all table, figure, and appendix references against their stable identifiers.
12. Render every format required by the project profile; PDF is mandatory under the default profile.
13. Run the authorial revision and draft gates before presenting the text as final.
14. Record technical skill use in `project/skill_execution_log.csv`; reserve `paper/authorial_revision_log.md` for intellectual and authorial decisions.

## Section Contracts

These are functional requirements, not fixed templates.
The order and number of paragraphs should follow the manuscript's argument.

### Introduction

An introduction should make legible:

- the historical or analytical problem,
- the empirical object, geography, and period,
- the question or proposition,
- the evidence or approach,
- the strongest defensible contribution,
- and the relation to relevant debates.

A hook, numbered contributions, or a roadmap may be used when they help.
Do not include them automatically.
Do not manufacture a literature gap when the contribution is a reinterpretation, new evidence, a new scale, or a new connection between established debates.

### Literature and Historiography

Organize the discussion around:

- disagreements,
- explanatory traditions,
- changing evidence,
- concepts,
- or unresolved historical problems.

Chronology is legitimate when the evolution of interpretation is itself the object.
Do not end every subsection with a formula announcing the paper's contribution.
Make the relationship between the literature and the manuscript's question visible through the argument.

### Historical Context

Use context to establish conditions, institutions, actors, timing, or constraints required by the explanation.
Do not treat context as a detached background summary.
Retain historical texture when it changes how the evidence should be interpreted.

### Sources, Data, and Method

Explain:

- provenance,
- coverage,
- construction,
- inclusion and exclusion decisions,
- source criticism,
- measurement,
- analytical procedure,
- and limits.

The section's form should match the research route.
Do not force equations or identification language onto historical-structural work.
Do not hide inferential limits in footnotes.

### Results, Patterns, and Analysis

Organize around the research question, propositions, mechanisms, or historical sequence.

Each analytical unit should connect:

- the empirical result or pattern,
- its evidentiary strength,
- its historical interpretation,
- relevant alternatives,
- and its limits.

Do not force every paragraph into `finding -> statistic -> robustness -> implication`.
Use that sequence only when it fits the evidence.

### Discussion

Explain what the results change in the relevant debate.
Build a cumulative interpretation rather than a sequence of result summaries or parallel themes. Relate patterns where the evidence supports tension, co-constitution, mediation, displacement, accumulation, feedback, comparison, or scalar transformation. Distinguish:

- what the evidence establishes,
- what it supports interpretively,
- what remains plausible but untested,
- and what should not be claimed.

State the strongest warranted interpretation positively before its boundary. Consolidate limitations deliberately; do not let repeated statements about what the design does not identify become the discussion's organizing logic.
Do not treat a defensible historical or structural explanation as invalid merely because the project does not identify it econometrically. Match its wording to its sources, mediations, period, and scale. If the evidence is insufficient and narrowing would remove the discussion's main payoff, request the exact evidence or author decision before drafting.

### Conclusion

Return to the question and state the answer at the level supported by the manuscript.
Synthesize rather than repeat the results section.
Include limitations or future research only when they clarify the contribution or remaining uncertainty.
Do not introduce stronger claims or new evidence.

## Research Routes

### Causal

Keep the estimand, identifying variation, assumptions, historical mechanism, and external validity distinct.
Do not let formal identification replace historical plausibility.

### Historical-Structural

Build the explanation through periodization, patterns, actors, institutions, mechanisms, and competing interpretations.
Narrative is analytical when it establishes sequence and mechanism.
It is not a substitute for evidence.

### Hybrid

Use bounded causal evidence to test a specific mechanism.
Let the broader structural interpretation rest on the full historical evidence base.
Do not generalize a partial estimate into the paper's entire explanation.

Treat route labels and workflow decisions as internal analytical controls. Mention identification, route choice, or evidentiary classification in manuscript prose only when they are substantively necessary for the reader's evaluation of method or inference; never use them as a recurring contribution claim.

## Prose Rules

- Prefer claim-first prose when it improves clarity, but preserve narrative sequencing when chronology carries the explanation.
- Let paragraph length vary with analytical function.
- Let sentence length vary with the relation between evidence and interpretation.
- Use signposting only when the reader needs orientation.
- Prefer concrete places, actors, periods, quantities, sources, and mechanisms over abstract academic language.
- Do not use numbered lists inside prose merely to create an appearance of structure.
- Do not repeat the same transition pattern across consecutive paragraphs.
- Do not expose internal workflow categories as manuscript argument.
- Do not expose journal-family identifiers or calibration labels in manuscript prose. Translate them into the substantive debate, audience, or implication.
- Do not repeat inferential disclaimers when one well-placed boundary statement is sufficient.
- Never invent citations, archival references, results, or source details.

## Output

Use the project structure requested by the user.
If none is specified, draft in Quarto and follow the `paper/first_draft.qmd` and `paper/first_draft.pdf` contracts in `../shared/output_contracts.md`. The QMD is the controlled source; generated HTML or PDF files are outputs and must never be edited independently.

Do not declare the draft complete until a clean render produces every required format without unresolved citation or cross-reference warnings. Report an unavailable TeX engine, missing font, or render failure as a failed or not-assessed requirement rather than silently substituting HTML.

For review drafts, line numbers and 1.5 spacing may be useful, but formatting is secondary to a defensible argument.
