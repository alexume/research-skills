# Stage Gates

Stage gates prevent progression when intellectual, evidentiary, methodological, or production requirements are missing. Gate identifiers are semantic and do not correspond numerically to project stages.

## Gate map

| Gate | Stages | Decision focus |
|---|---|---|
| `G-LITERATURE-ORIENTATION` | 1 | Question refinement and literature-grounded research orientation |
| `G-LITERATURE` | 2 | Literature maturity, coverage, evidence, and positioning |
| `G-HYPOTHESES` | 3 and 5 | Mechanisms, alternatives, and testability |
| `G-EXPLORATION` | 4 | Data/source understanding and quality |
| `G-STRATEGY` | 6 | Causal, historical-structural, or hybrid route |
| `G-DESIGN` | 7 | Identification or structural explanation |
| `G-REQUIREMENTS` | 8 | Verified acquisition and evidentiary coverage |
| `G-PREPARATION` | 9 | Provenance, construction, and validation |
| `G-FEASIBILITY` | 10 | Estimability or explanatory feasibility |
| `G-RESULTS` | 11 | Analytical validity and diagnostic completeness |
| `G-INTERPRETATION` | 12 | Mechanisms, alternatives, and claim calibration |
| `G-DRAFT` | 13 | Manuscript coherence and authorial integrity |
| `G-INTERNAL-REVIEW` | 14-15 | Major-risk resolution |
| `G-JOURNAL-FIT` | 16 | Journal and audience alignment |
| `G-REPLICATION` | 17 | Executability, provenance, and output consistency |
| `G-SUBMISSION` | 18 | Completeness, consistency, and compliance |
| `G-RESUBMISSION` | 19 | Reviewer response and revision traceability |

Every gate returns `pass`, `conditional pass`, `fail`, or `not assessed`. Use `not assessed` when required searches, artifacts, or checks were not examined; never treat it as a pass. A conditional pass must list remaining conditions, responsible artifacts, and a verification criterion.

## `G-LITERATURE-ORIENTATION`

Pass when both question/hypothesis and seed/citation-network discovery tracks have been executed at orientation depth; seed sources have been assessed rather than presumed authoritative; principal research lines, concepts, and rivals are provisionally mapped; and `literature/research_question_handoff.qmd` provides a literature-grounded refined question, mechanisms, provisional hypotheses or propositions, competing explanations, and evidence needs. Conditional pass requires a defensible refined question plus named searches, texts, languages, or traditions whose completion could still alter it. Fail when the output is only a seed bibliography, generic search plan, unchanged topic without rationale, single-tradition framing, or generic absence claim. Return `not assessed` when required discovery or source checks were not executed.

## `G-LITERATURE`

Pass when the review type, protocol, two discovery tracks, executed searches, dates, exports, deduplication, screening, full-text status, source-level appraisal, core research lines, rivals, foundational and recent sources, concepts, evidence lineages, data-source candidates, saturation decision, KnowledgeWiki promotion, and specific contribution space satisfy their contracts. Each core research line must normally contain more than one fully read source, more than one distinguishable position, a serious rival, location-level support for principal findings, and diversity in method, source type, scale, or independently produced evidence where the literature permits. A documented sparse-literature exception narrows the claim but does not convert a seed into a reconstructed debate.

Return conditional pass only when named remaining gaps are bounded, assigned, verifiable, and do not undermine the refined question or central contribution. Fail when the review is merely chronological; searches or exclusions are undocumented; planned platform searches were not executed without a recorded access action; central claims depend on abstracts, snippets, or unread texts; local seeds are treated as authoritative; a core debate has one source or one position; rival or citation-network search is absent; data links are confused with acquired resources; or novelty rests only on "no one has studied X." Return `not assessed` when mandatory tracks, platforms, full-text checks, or extraction were not evaluated.

## `G-HYPOTHESES`

Pass when each core hypothesis or proposition specifies a mechanism, observable implication, competing explanation, required evidence, and uncertainty status. Fail when hypotheses are correlations, mechanisms are implicit, or the project retains too many unfocused claims.

## `G-EXPLORATION`

Pass when units, coverage, missingness, anomalies, temporal/spatial structure, source production, measurement stability, and provisional patterns are documented. Fail when EDA silently changes the confirmatory question, data quality is unknown, historical categories or boundaries are assumed comparable without audit, or source coverage cannot support refinement.

## `G-STRATEGY`

Pass as causal when treatment, outcome, unit, timing, counterfactual, identifying variation, mechanism, and feasible data are clear. Pass as historical-structural when process, periodization, mechanisms, scales, evidence, and competing interpretations are clear. Pass as hybrid when the bounded causal component and broader structural explanation have an explicit division of labor. Fail when a method is chosen because a regression is possible or claims exceed the available route.

## `G-DESIGN`

Pass when the route-specific design satisfies its contract, variables and sources match concepts, measurement strategies are explicit, assumptions and comparisons are defensible, and limits of inference are stated. Fail when a regression substitutes for identification, a proxy substitutes for a concept without validation, sources cannot support the intended claims, or scale and periodization are incoherent.

## `G-REQUIREMENTS`

Pass when every material design assumption, variable, mechanism, and claim maps to a documented requirement; all blocking evidence is verified and lawfully acquired or has a concrete access route; discovery queries, versions, provenance, rights, coverage, rejected candidates, and fallbacks are recorded; and partial or substitute sources do not silently change the design. Fail when essential evidence is unspecified, only discovered but not verified, inaccessible without a mitigation plan, incompatible with required coverage or measurement, or disconnected from the design.

## `G-PREPARATION`

Pass when raw inputs remain immutable and provenance, source criticism, measurement decisions, scripts, transformations, linkage, derived-variable lineage, validation, exclusions, and outputs are documented. Maintained R code must follow `project/project_profile.yaml` and `shared/r_code_style.md`; `analysis/r_code_quality.md` must record automated checks and justified exceptions. Fail when data construction is undocumented, source values are overwritten, harmonization rules are invented during cleaning, identifiers or merges are unreliable, unresolved anomalies affect central claims, or required code-quality checks fail or remain not assessed.

## `G-FEASIBILITY`

Pass when coverage, support, comparisons, sources, measurement validity, harmonization uncertainty, and inference are adequate for the stated estimand or explanation. Fail when main tests cannot be estimated, source gaps prevent evaluating mechanisms, feasible measures change the concept, or the sample no longer identifies or represents the stated target. For DiD, require audited cohort-time comparisons, pre/post coverage, treatment path, controls, anticipation, overlap, attrition, and spillovers. For historical-structural analysis, require evidence capable of establishing each core pattern, evaluating proposed periodization and mechanism steps, supporting valid comparisons, and confronting at least one serious rival interpretation.

## `G-RESULTS`

Pass when code or analytical procedure matches the final design, diagnostics are complete, source and measurement uncertainty is propagated or disclosed, models or structural decisions and material deviations are registered, and the documented project entry point regenerates results. Tables and figures must trace to analytical objects or evidence through `tables/table_manifest.csv` and `figures/figure_manifest.csv`, use stable identifiers, record main, appendix, or excluded status, and comply with the project profile and shared R standard. Historical-structural results must establish patterns before mechanism claims, assess periodization and comparisons, distinguish independent corroboration from shared-source agreement, and evaluate rivals. Fail when preferred results drive undocumented sample, measurement, periodization, comparison, or specification changes; inference is inappropriate; robustness is unrelated to actual threats; reported outputs depend on manual edits or undeclared steps; or required code, table, or figure checks fail or remain not assessed.

## `G-INTERPRETATION`

Pass when `project/project_argument_profile.qmd`, `analysis/interpretation.qmd`, and `analysis/discussion_argument_map.qmd` connect results to mechanisms, actors, institutions, infrastructures or practices where relevant, timing, scale, literature, alternatives, and evidence strength. The interpretation must identify the strongest warranted answer, select consequential relations among results or processes, state their mediations and argumentative payoff, assess whether evidence actions preserve the promised contribution, and assign evidence actions to weak bridges. When materially different contributions remain defensible, the profile must record the alternatives and an explicit author selection or revision before pass. Pass requires a journal family or target journal, or an explicit author decision that temporarily leaves it unresolved. Fail when interpretation remains a collection of parallel mechanisms, claimed domains are merely adjacent, discussion repeats results, historical context is decorative, workflow categories replace substantive reasoning, limitations organize the contribution, the remaining argument only audits an indicator or design without transforming a debate, a dialectic is forced, or a central bridge is narrowed or parked despite contribution collapse without a retrieval or exact source or author request.

## `G-DRAFT`

Pass when the manuscript delivers what the introduction promises, methods and sources are transparent, claims trace to evidence, the discussion realizes the author-approved project argument profile and approved argument map, tables, figures, and the analytical appendix match registered outputs, unresolved issues are visible, and authorial choices have been reviewed. The framing must be calibrated to the declared journal family or target journal without imitating a house style or exposing calibration labels in prose. The QMD must be the controlled manuscript source, use the language declared in `project/project_profile.yaml`, cite registered table and figure identifiers through stable Quarto cross-references, and render every required format. PDF is mandatory under the default profile and must be current, legible, and free of unresolved citation or cross-reference warnings. `paper/authorial_revision_log.md` records intellectual intervention; `project/skill_execution_log.csv` separately records technical skill use. Fail when fluent prose introduces unsupported claims, workflow, route, or journal-family labels become recurring argument, caveats displace the positive interpretation, discussion sections remain parallel summaries, claimed domains remain adjacent without mediation, the discussion does not transform its stated debate, contribution language is generic, appendix evidence contradicts the main text without discussion, the conclusion exceeds results, a blocking source or author request is unresolved, a required render is absent or stale, or a required check remains not assessed.

## `G-INTERNAL-REVIEW`

Pass when major reviewer risks have explicit dispositions, revisions trace to evidence or author decisions, and blocking problems are resolved. Fail when revision focuses on prose while leaving design, evidence, mechanism, or contribution failures untouched.

## `G-JOURNAL-FIT`

Pass when the selected journal family and target journal align with the manuscript's audience, contribution, method, sources, length, argumentative architecture, and likely objections. Any change of family must state the required intellectual reframing. Fail when family selection is an undifferentiated blend, fit depends on substantial uncompleted redesign, house-style imitation substitutes for argument, or journal prestige substitutes for audience relevance.

## `G-REPLICATION`

Pass when a clean checkout or package copy restores the documented environment, executes from the stated entry point using only declared inputs, and reproduces all reported estimates, structural summaries, tables, figures, appendices, manuscript numbers, and project-profile render formats within prespecified tolerances. Table and figure manifests, R code-quality results, the analytical appendix, the skill-execution log, and the required PDF must agree with model, specification, structural evidence, and replication records. Restricted-data projects pass only when access limitations, executable code, metadata, verification responsibilities, and any authorized verification are documented. Fail when central outputs differ, dependencies or inputs are undeclared, execution requires undocumented author knowledge, the package exposes protected material, required renders or checks are absent or not assessed, or no independent clean-state verification has occurred.

## `G-SUBMISSION`

Pass only after `G-REPLICATION` passes or receives a bounded conditional pass, and when claims, evidence, manuscript, current PDF, tables, figures, citations, appendices, disclosures, permissions, replication-package status, project profile, and journal requirements are consistent. A required audit domain marked not assessed prevents pass. Fail when a central claim is unsupported, files disagree, required permissions are missing, the replication status is unresolved, the PDF is stale or noncompliant, or the audit returns no-go.

## `G-RESUBMISSION`

Pass when every editor and reviewer comment has a documented decision, corresponding change or reasoned rejection, location, verification, and consistent revised artifact. Any changed analysis must also be rerun from the documented entry point and propagated through the replication manifest and verification report. Fail when responses claim changes not present in the manuscript, new analyses are not propagated through tables, figures, discussion, and supplements, or the revised package is not reverified.
