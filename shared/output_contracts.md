# Output Contracts

Output contracts define the minimum contents required before an artifact can satisfy a stage gate. File existence alone never implies completion.

## Global requirements

Every substantive artifact should state, when applicable:

- purpose and stage;
- inputs and source locations;
- authoring or generation date;
- unresolved decisions and missing evidence;
- links to upstream and downstream artifacts;
- status: draft, review-ready, or gate-ready.

All project artifacts must comply with `project/project_profile.yaml`. Copy and complete `shared/project_profile_template.yaml` at setup. A missing required profile value is an unresolved setup condition, not permission to infer a default silently.

## `project/project_profile.yaml`

- Manuscript language and Quarto source format.
- Required and optional render formats, including PDF engine.
- Figure and table generation, inclusion, identifier, and export rules.
- R code style, pipe, namespace, lint, and formatting requirements.
- Clean-render, citation, and cross-reference failure policy.
- Journal family for argument calibration and target journal overrides when known.

## `project/project_argument_profile.qmd`

- Research question and central empirical, historical, or conceptual tension.
- Selected contribution and alternative contributions considered.
- Debate the manuscript intends to transform.
- Central relations with mediations, actors, timing, scale, evidence, and missing support.
- Claims permitted, contested, and excluded.
- Exact source and evidence requirements for unresolved central bridges.
- Preferred and prohibited project-specific formulations.
- Primary journal family and any secondary audience, used only as backstage calibration.
- Author decisions, decision source, date, and approval status: provisional, author-approved, or superseded.
- Comparison of two to four architectures when materially different contributions remain defensible, including advantages, costs, evidence needs, and risk of contribution loss.

## `project/skill_execution_log.csv`

- Timestamp, workflow stage, and research route.
- Skill invoked and trigger or assigned task.
- Input and output artifact paths.
- Gate evaluated and result: pass, conditional pass, fail, or not assessed.
- Technical exception, unresolved issue, and next owner.
- Keep authorial and interpretive decisions in their substantive logs unless also needed to explain a technical workflow decision.

## `project/setup_manifest.md`

- Project title and short identifier.
- Research question or initial problem.
- Geographic, temporal, and disciplinary scope.
- Candidate routes and current stage.
- Folder and naming conventions.
- Known datasets, source collections, and literature corpus.
- Software and execution assumptions.
- Open risks and next action.

## `project/project_log.md`

- Dated decisions and rationale.
- Changes to question, scope, design, data, or sources.
- Outputs created or superseded.
- Failed approaches and reasons.
- Author decisions required.

## `project/source_inventory.csv`

- Stable source identifier.
- Source type and provenance.
- Location or access path.
- Geographic and temporal coverage.
- Access, rights, and digitization status.
- Relevance and reliability status.
- Processing status and notes.

## `project/reproducibility_plan.md`

- Project root and directory roles.
- Executable entry point and dependency order.
- Raw-data immutability and acquisition boundaries.
- Environment capture and restoration strategy.
- Pipeline architecture and generated-output policy.
- Seed and nondeterminism policy.
- Restricted-data, privacy, credentials, and disclosure strategy.
- Verification responsibility, timing, and completion criteria.

## `literature/literature-review.qmd`

- Initial and refined review question, scope, and relation to `literature/research_question_handoff.qmd`.
- Core research lines, debates, concepts, explanatory traditions, mechanisms, and rivals.
- Foundational works and recent developments.
- Claims, methods, source and data lineages, measurement, scales, and limitations.
- Established, localized, weak, and disputed findings.
- Contradictions, replications, boundary conditions, and unresolved questions.
- Specific contribution space and questions the project cannot answer.
- Search and evidence maturity stated without claiming coverage beyond the protocol.
- Citations linked to `literature/references.bib`.

## `literature/search_strategy.qmd`

- Review type, initial question, search objective, and orientation/maturation phase.
- Databases, repositories, languages, and date coverage.
- Two discovery tracks: question/hypothesis and seed/citation network.
- Exact search strings or persistent seed identifiers by platform.
- Search target identifiers linking every batch to a question, concept, mechanism, rival, hypothesis, measurement problem, or seed.
- Inclusion and exclusion criteria.
- Screening, deduplication, full-text acquisition, data-source discovery, and citation-chasing procedure.
- Search date and stopping rule.
- Executed-by status, imports or exports, amendments, and known access and coverage limitations.

## `literature/research_question_handoff.qmd`

- Initial question and diagnosis of significance, scope, and conceptual coherence.
- Refined question and literature-based rationale for every material change.
- Principal research lines, debates, concepts, mechanisms, actors, periods, scales, and rivals.
- Provisional hypothesis or proposition candidates with observable implications or historical expectations.
- Serious competing explanations and evidence that could discriminate among them.
- Literature, data, archives, and measurements still required.
- Claims currently supportable and not supportable.
- Orientation gate status and exact maturity work remaining.

## `literature/recent_literature.qmd`

- Search window and update date.
- New sources and relevance assessment.
- Changes to debates, methods, or contribution positioning.
- Sources excluded after full assessment and reasons.
- Remaining search gaps.

## `literature/debate_matrix.csv`

- Debate and research-line identifiers.
- Question, concept definition, positions, rivals, claims, and mechanisms.
- Representative fully read sources with evidence and data lineages.
- Evidence, data, method, geography, period, and scale.
- Findings, contradictions, strengths, internal limitations, and transfer limits.
- Unresolved problem, project opportunity, and maturity status.

## `literature/source_discovery_log.csv`

- Stable source identifier, separate `bibkey`, and verified citation fields.
- Discovery track, search target, platform, exact query or seed, batch, and date.
- DOI, OpenAlex ID, Scopus ID, URL, and metadata status.
- Duplicate or version relationship.
- Screening, full-text, local-file, and access status.
- Access limitation, next action, and user-executed or imported-export status.

## `literature/screening_log.csv`

- Stable source identifier.
- Title/abstract and full-text decisions.
- Primary exclusion reason and decision date.
- Reviewer or decision source.
- Full-text availability and unresolved status.

## `literature/extraction_matrix.csv`

- Review role, reading status, extraction status, `source_id`, and separate `bibkey`.
- Source question, claim, concepts, mechanism, actors, evidence, data, method, and measurement.
- Geographic, temporal, population, scalar, and disciplinary scope.
- Finding with page or section location.
- Separate relevance, evidence, design, source-base, measurement, and transparency assessments.
- Internal limitations, transfer limits, and evidence lineage.
- Relation to debates, rivals, hypotheses, data candidates, and project contribution.
- KnowledgeWiki status, note slug, and verification date.

## `literature/data_source_candidates.csv`

- Candidate, publication, and bibliographic identifiers.
- Dataset, archive, official series, code, supplement, map, replication package, or constructed-measure description.
- Creator, custodian, provider, persistent identifier, version, format, and documentation.
- Unit, variables or contents, geography, period, frequency, and resolution.
- Access, licence, verification, acquisition, and local-path status.
- Relation to the question, hypothesis, mechanism, and measurement problem.
- Possible contribution, limitations, priority, next skill, and exact next action.

## `literature/references.bib`

- Stable citation keys for sources that passed metadata verification.
- Metadata verified against the publication, DOI registry, or reliable catalogue.
- DOI, ISBN, pages, issue, publisher, edition, and access fields included only when verified.
- Thematic groups where supported by the bibliography workflow.
- Crosswalk to `source_id` retained in the discovery or extraction matrix rather than encoded by silently changing citation keys.
- Conflicts with the authoritative KnowledgeWiki bibliography resolved or marked `PENDING` before ingestion.

## `analysis/hypotheses_v1.qmd`

- Preliminary hypotheses or structural propositions.
- Pattern or problem motivating each one.
- Mechanism, actors, institutions, timing, and scale.
- Observable implication.
- At least one competing explanation.
- Evidence or data that would discriminate between them.
- Explicitly provisional identification ideas, if any.

## `analysis/exploratory.qmd`

- Data and source inventory.
- Unit of observation and coverage.
- Missingness, duplicates, gaps, and anomalies.
- Descriptive patterns with uncertainty and weighting noted.
- Temporal, spatial, and compositional structure.
- Distinction between discovered patterns and confirmatory tests.
- Implications for hypotheses, measurement, and feasibility.
- Decisions that must remain provisional until design selection.

## `analysis/data_source_quality.md`

- Dataset or source identifier.
- Provenance and production purpose.
- Coverage, omissions, and representativeness.
- Definition and classification changes.
- Measurement, digitization, and linkage risks.
- Transformations already applied.
- Claims the material can and cannot support.

## `analysis/source_criticism.qmd`

- Source identity, archival hierarchy, and provenance.
- Creator, production purpose, audience, and institutional context.
- Coverage, selection, survival, omissions, and representativeness.
- Categories, units, internal consistency, and source meanings.
- Digitization, transcription, extraction, coding, and aggregation chain.
- Triangulation and unresolved contradictions.
- Claims supported and not supported by type, period, and scale.
- Access, rights, privacy, uncertainty, and follow-up requirements.

## `project/historical_source_registry.csv`

- Stable source and collection identifiers.
- Archive, repository, location, and citation locator.
- Creator, date, place, type, and production purpose.
- Geographic, temporal, population, and thematic coverage.
- Access, rights, digitization, transcription, and criticism status.
- Known omissions, transformations, reliability dimensions, and linked claims.

## `analysis/measurement_strategy.qmd`

- Concept, observable target, population, unit, geography, period, and frequency.
- Source variables and provenance.
- Concept-to-variable measurement chain.
- Construct validity, coverage, resolution, reliability, and error risks.
- Units, prices, classifications, boundaries, denominators, and time basis.
- Harmonization and aggregation rules.
- Uncertainty flags, ranges, alternative measures, and sensitivity plan.
- Claims supported and not supported.

## `analysis/eda_decision_log.md`

- Exploratory finding or data-quality issue.
- Affected variable, period, geography, group, or source regime.
- Decision, rationale, and responsible downstream skill.
- Whether the decision changes a hypothesis, measure, sample, or design.
- Confirmatory analysis reserved for later.

## `analysis/hypotheses_v2.qmd`

- Three to six core hypotheses or structural propositions.
- Mechanism for each hypothesis or proposition.
- Testable or observable implication.
- Competing explanation.
- Data and source availability.
- Identification or evidence strategy.
- Status: keep, refine, acquire, park, or drop.

## `analysis/research_strategy.qmd`

- Project state.
- Primary route: causal, historical-structural, or hybrid.
- Justification for route selection.
- Feasibility constraints.
- Claims allowed and claims not allowed.
- Required next outputs.
- Gate result: pass, conditional pass, or fail.

## `analysis/causal_design.qmd`

- Causal question, treatment, outcome, unit, timing, and estimand.
- Ideal experiment and counterfactual.
- Treatment-assignment process and comparison units.
- Identifying variation.
- Identifying assumptions in plain language and formal notation.
- Threats, evidence, equations, and required data.
- Inference level, robustness, falsification, and sensitivity plan.
- Recommended implementation skill and method-specific handoff.
- Claims allowed, claims not allowed, and design gate result.

For DiD, also include adoption structure, comparison group, parallel-trends formulation, anticipation, aggregation target, and spillover, attrition, overlap, and cohort-coverage risks.

## `analysis/identification_strategy.qmd`

- Candidate design families considered.
- Identifying variation and assumptions for each candidate.
- Selected strategy and rejected alternatives.
- Historical and institutional plausibility assessment.
- Evidence capable of probing assumptions.
- Consequences of assumption failure.
- Method-specific implementation handoff.

## `analysis/structural_analysis_design.qmd`

- Structural question and historical process.
- Periodization, unit, and scale.
- Core patterns to establish.
- Mechanisms, actors, institutions, and mediations.
- Evidence required and competing interpretations.
- Limits of inference and design gate result.

## `analysis/mechanism_map.qmd`

- Pattern, mechanism, actors, institutions, timing, and scale.
- Evidence, source, and strength of support.
- Alternative explanation and discriminating evidence.
- Relational synthesis across the few mechanisms or processes with the highest explanatory yield.
- Argumentative payoff and evidence action for every weak central bridge.
- Contribution-preservation assessment before narrowing, parking, or deleting a central mechanism.
- Explicit mediation test when integration across economic, social, institutional, or biophysical domains is claimed.
- Weak links and evidence still required.

## `analysis/hybrid_integration_plan.md`

- Broader structural question and bounded causal question.
- Division of evidentiary labor between components.
- Claims supported by each component.
- Shared mechanisms, scales, and temporal boundaries.
- Integration sequence and overclaiming risks.

## `analysis/data_requirements.qmd`

- Variables, units, periods, geography, and resolution required.
- Measurement and harmonization requirements.
- Minimum coverage and support conditions.
- Preferred and fallback sources.
- Access, rights, cost, and feasibility constraints.
- Link to the design assumption or claim each item supports.

## `analysis/source_requirements.qmd`

- Historical claim or mechanism requiring evidence.
- Source type, archive, collection, or registry needed.
- Geographic and temporal coverage.
- Expected evidentiary role and limitations.
- Access, digitization, transcription, and permission requirements.
- Priority and fallback source strategy.

## `project/acquisition_log.csv`

- Requirement identifier.
- Requested dataset or source.
- Provider, archive, or repository.
- Request and access dates.
- Access, licensing, and permission status.
- Acquired version and storage location.
- Coverage differences from the requirement.
- Next action.

## `project/evidence_discovery_log.csv`

- Stable requirement, search, and candidate identifiers.
- Repository, catalogue, provider, or platform.
- Exact query, filters, language, and search date.
- Historical names, geographic terms, and coverage constraints used.
- Results reviewed and candidate stable identifiers.
- Candidate disposition: verify, request, acquire, reject, duplicate, or unavailable.
- Rejection reason, next action, and stopping decision.

## `project/acquisition_manifest.md`

- Acquisition scope, responsible design requirements, and gate status.
- Verified sources and datasets with provider, custodian, version, and stable identifiers.
- Geographic, temporal, population, variable, and file coverage.
- Access route, acquisition date, format, size, checksum, and documentation.
- License, privacy, confidentiality, redistribution, and citation requirements.
- Status: discovered, verified, requested, acquired, restricted, unavailable, or rejected.
- Requirement coverage: satisfied, partial, substitute, or failed.
- Design, measurement, population, or claim consequences of gaps and substitutions.

## `analysis/preparation_manifest.md`

- Immutable raw inputs and locations.
- Scripts and execution order.
- Cleaning, linkage, harmonization, and variable-construction decisions.
- Row, key, coverage, and merge validation.
- Data dictionary and derived-variable lineage.
- Exclusions, unresolved anomalies, and known limitations.
- Clean and interim outputs.

## `data/metadata/variable_dictionary.csv`

- Stable variable name, label, role, type, and allowed values.
- Concept, unit, denominator, price basis, geography, and time basis.
- Source variables and source identifiers.
- Formula, transformation stage, and missing-value behavior.
- Validity, uncertainty, flags, and intended analytical use.

## `data/metadata/measurement_decisions.csv`

- Stable decision identifier.
- Measurement problem and affected variables.
- Chosen rule, alternatives, and rationale.
- Source, formula, conversion factor, crosswalk, or deflator.
- Valid domain, uncertainty, sensitivity version, and approval status.

## `analysis/data_validation.md`

- Schemas, keys, cardinalities, and allowed-value checks.
- Row, temporal, geographic, population, and group coverage.
- Merge results and unmatched distributions.
- Arithmetic, range, total-conservation, and temporal-ordering checks.
- Source-to-clean spot checks.
- Blocking, material, and informational failures.
- Final validation status and unresolved limitations.

## `analysis/computational_environment.md`

- R, Quarto, operating system, locale, and external program versions.
- Package lockfile, snapshot method, restoration command, and status.
- System libraries, extensions, fonts, or binaries outside the lockfile.
- Environment-variable names and purposes without secret values.
- Hardware, runtime, network, and access requirements.
- Commands for environment restoration, pipeline execution, rendering, and validation.
- Known platform-dependent behavior and mitigation.

## `analysis/r_code_quality.md`

Required at milestones whose gate calls for code-quality verification. Bounded
edits report checks in the existing task closure under `r_code_style.md`; they
do not create this report solely because an R file changed. Consolidate relevant
results and exceptions when closing the milestone.

- R paths and Quarto chunks assessed, with exclusions.
- Applied project profile and shared R standard version or date.
- `styler` and `lintr` versions, commands, and results.
- Documented exceptions with file, location, reason, and owner.
- Unresolved errors or warnings and affected outputs.
- Result: pass, conditional pass, fail, or not assessed.

## `analysis/feasibility.qmd`

- Design and target estimand or explanation being audited.
- Available sample, sources, and identifying comparisons.
- Coverage, missingness, support, and composition diagnostics.
- Inference feasibility for quantitative designs.
- Required design, measurement, or sample revisions.
- Claims or estimands that remain feasible and those that do not.
- Gate result: pass, conditional pass, or fail.

For DiD, also include cohort-time support, pre/post coverage, treatment reversals, comparison-group availability, overlap, anticipation, attrition, and spillover risks.

For historical-structural analysis, also include evidence coverage for every core pattern and mechanism step, source and measurement comparability across proposed periods and cases, ability to evaluate rival interpretations, periodization or scale revisions, and claims that remain supportable.

## `analysis/inference_plan.qmd`

- Target estimand and assignment mechanism.
- Sampling, assignment, and observational dependence levels.
- Standard-error, clustering, randomization, bootstrap, or spatial procedure.
- Cluster count, finite-sample corrections, and weak-inference risks.
- Confidence interval and simultaneous-band plan.
- Multiplicity and prespecified outcome-family treatment.
- Method-specific weak identification or design uncertainty.
- Seeds and computational requirements for stochastic procedures.

## `analysis/model_registry.csv`

- Stable model identifier and status: main, diagnostic, sensitivity, exploratory, or invalid.
- Estimand, target population, sample, and exclusion rules.
- Estimator, formula, fixed effects, controls, weights, and timing choices.
- Inference procedure, cluster level, and random seed where relevant.
- Package, function, version-relevant arguments, and fitted-object location.
- Corresponding table, figure, appendix, and manuscript claim.
- Prespecification status, execution status, and gate disposition.

## `analysis/specification_log.csv`

- Stable decision and model identifiers.
- Date and analytical stage.
- Material change to sample, variable, estimator, specification, or inference.
- Reason, evidence, and whether the change was prespecified.
- Affected estimand, population, output, or claim.
- Previous and replacement model identifiers.
- Decision owner, result status, and unresolved risk.

## `analysis/results.qmd`

- Research question and target estimand or pattern.
- Estimator or analytical procedure, sample, and comparison.
- Main result with uncertainty or evidence strength.
- Diagnostics, robustness, and sensitivity.
- Link to hypotheses and mechanisms.
- Alternative explanations.
- Limits of inference and unresolved results.

For DiD, also report group-time support, prespecified aggregations and weights, simultaneous bands when available, pre-treatment evidence without treating it as proof, and sensitivity to material parallel-trends violations.

## `analysis/structural_patterns.qmd`

- Structural question and approved design handoff.
- Evidence base, source regimes, measurement, and comparability.
- Temporal, spatial, compositional, institutional, and socioecological patterns.
- Proposed and empirically assessed periodization.
- Cross-period, cross-case, or multiscalar comparisons and their leverage.
- Source triangulation, independence, contradictions, and uncertainty.
- Mechanism sequences, actor and institutional evidence, and counterevidence.
- Rival interpretations and discriminating evidence.
- What is established, supported, plausible, unresolved, and not established.
- Feasibility and results gate decisions.

## `analysis/structural_evidence_matrix.csv`

- Stable pattern, mechanism, rival, evidence, source, and claim identifiers.
- Period, geography, population, sector, actor, institution, and scale.
- Exact source locator and measurement or coding decision.
- Evidentiary role: direct, indirect, contrastive, illustrative, or insufficient.
- Independence from other evidence and source-production relationship.
- Support, contradiction, uncertainty, and observation limitations.
- Linked analytical output, table, figure, appendix, and manuscript claim.

## `analysis/structural_analysis_log.csv`

- Stable decision identifier and date.
- Design object affected: periodization, scale, comparison, pattern, mechanism, source, or claim.
- Original and revised decision.
- Evidence, source, measurement, or feasibility reason.
- Whether the change was anticipated or emerged during implementation.
- Affected outputs and claims.
- Decision owner, status, and unresolved risk.

## `tables/table_manifest.csv`

- Stable table and panel identifiers, title, purpose, and status: main, appendix, or excluded.
- Linked claims, model/specification identifiers, or structural evidence identifiers.
- Source data, sample, population, period, geography, unit, and measurement basis.
- Displayed statistics, uncertainty, precision, and ordering.
- Notes, abbreviations, sources, and material limitations.
- Generation script or pipeline target and machine-readable table-data location.
- Required output formats and manuscript cross-references.
- Replication hash or comparison rule and audit status.

## `figures/figure_manifest.csv`

- Stable figure and panel identifiers, title, purpose, and status: main, appendix, or excluded.
- Linked claim, result, model, specification, or structural evidence identifiers.
- Source data or object, generation script or pipeline target, and output paths.
- Caption, notes, units, accessibility treatment, and material limitations.
- Required export formats and Quarto manuscript cross-reference.
- Replication hash or visual comparison rule and audit status.

## `appendix/analytical_appendix.qmd`

- Data, source, access, and measurement documentation needed beyond the manuscript.
- Route-specific design and estimator or analytical procedure details.
- Additional descriptive, structural, or comparative evidence.
- Diagnostics, falsification, and sensitivity tied to registered threats.
- Alternative specifications, constructions, boundaries, periods, or source regimes.
- Heterogeneity, mechanism, counterevidence, and rival interpretations.
- Stable table and figure identifiers with manuscript cross-references.
- Reproducibility, restricted-data, and package-access notes.
- Material failures and null or contradictory evidence retained visibly.

## `analysis/claim_evidence_map.qmd`

- Claim and claim type.
- Evidence and source location.
- Strength, limitation, and risk.
- Scale and temporal fit.
- Strongest positive wording warranted by the evidence and one material boundary where needed.
- Evidence action: retrieve from project, retrieve from KnowledgeWiki, request a source, request an author decision, use a precise placeholder, narrow, park, or delete.
- Distinction among unsupported overclaim, supportable explanatory bridge with missing evidence, and authorial choice.
- Contribution-preservation assessment for every narrowed, parked, or deleted central claim.

## `analysis/interpretation.qmd`

- Main answer to the research question.
- Results or patterns being interpreted.
- Mechanisms, actors, institutions, timing, and scale.
- Competing explanations.
- Relation to literature and historiography.
- What is established, supported, plausible, or unresolved.
- External-validity and historical-generalization limits.
- Debate transformation: what the combined evidence changes, rather than only what the indicator or design cannot establish.
- Contribution-preservation assessment and unresolved source or author requests.

## `analysis/discussion_argument_map.qmd`

- Central empirical, historical, or conceptual tension or problem.
- Strongest positive interpretation warranted by the evidence.
- Selected relations among results or processes: tension, co-constitution, mediation, displacement, accumulation, feedback, comparison, sequence, or scalar transformation as applicable.
- Actors, institutions, infrastructures, technologies, practices, timing, and scale required by each relation.
- Serious rivals and material boundaries.
- Section architecture with analytical job, evidence, relational move, debate payoff, and transition.
- Evidence actions: retrieve from project, retrieve from KnowledgeWiki, request a source, request an author decision, use a precise placeholder, narrow, park, or delete.
- Internal workflow language that must not appear as manuscript argument.
- Journal-family calibration and unresolved editorial decisions.
- Reference to the selected architecture and approval status in `project/project_argument_profile.qmd`.
- Contribution-preservation assessment for central bridges proposed for narrowing, parking, or deletion.
- Integration test for every claimed relation across economic, social, institutional, or biophysical domains.
- Exact source or author requests when a safer formulation would collapse the promised contribution.

## `paper/first_draft.qmd`

- Title and abstract draft.
- Introduction with problem, question, contribution, and scope.
- Literature and historiographic positioning.
- Sources, data, measurement, and methods.
- Results or structural patterns.
- Interpretation, discussion, and conclusion.
- Bibliography and citations.
- Stable Quarto cross-references for every included table and figure.
- Language, source format, and rendering configuration consistent with `project/project_profile.yaml`.
- Framing and discussion calibrated to the declared journal family or target journal without using a reusable prose template.
- Realization of the passed `analysis/discussion_argument_map.qmd`, with deviations recorded as authorial decisions.
- Realization of the author-approved `project/project_argument_profile.qmd` when architecture selection was required.
- No workflow, route, evidence-classification, journal-family, or editorial-calibration labels used as manuscript argument.
- Consolidated limitations that do not force each discussion paragraph into a finding-then-disclaimer cadence.
- Explicit placeholders for unresolved evidence, citations, or author decisions.

## `paper/first_draft.pdf`

- Generated from the current `paper/first_draft.qmd`, never edited independently.
- Uses the profile's PDF engine, manuscript language, bibliography, and layout requirements.
- Contains no unresolved citation or cross-reference warnings.
- Includes only registered main-text tables and figures, with legible captions, notes, and units.
- Records a successful clean-render command in the project or replication log.

## `paper/authorial_revision_log.md`

- Intervention mode and source materials used.
- Author-written references used for calibration.
- Major interpretive decisions confirmed by the author.
- Claims qualified, moved, or removed.
- Unresolved decisions requiring author review.
- Authorial revision gate result.
- Do not use this artifact as evidence that a skill ran; record technical invocation in `project/skill_execution_log.csv`.

## `paper/referee_report.qmd`

- Reconstructed question, contribution, design, evidence, and claims.
- Core weaknesses ordered by severity.
- Disciplinary and methodological assessment.
- Major and minor revisions.
- Journal-fit risks and final assessment.

## `paper/revision_priorities.md`

- Prioritized issue.
- Severity and affected claim or section.
- Required evidence, analysis, or rewrite.
- Dependencies and completion criterion.
- Status and author decision.

## `paper/revision_log.md`

- Revision identifier and source comment.
- Decision: accept, partial, reject, or defer.
- Manuscript or analysis change.
- Location and supporting artifact.
- Remaining risk.

## `paper/revised_manuscript.qmd`

- Satisfy the complete `paper/first_draft.qmd` contract.
- Incorporate resolved internal-review priorities.
- Preserve explicit placeholders for unresolved issues.
- Link major changes to `paper/revision_log.md`.

## `paper/revised_manuscript.pdf`

- Satisfy the complete `paper/first_draft.pdf` contract.
- Be generated from the current `paper/revised_manuscript.qmd` after accepted revisions.
- Resolve all required-format, citation, table, figure, and cross-reference checks.

## `submission/journal_fit.qmd`

- Primary journal family and any justified secondary audience.
- Candidate journals and fit.
- Audience and contribution alignment.
- Methodological, historiographic, and format expectations.
- Required reframing and likely reviewer objections.
- Submission sequence and recommendation.

## `paper/title_abstract_keywords.qmd`

- Three to five candidate titles with rationale.
- Recommended title.
- Journal-calibrated abstract.
- Five to eight keywords.
- One-sentence contribution statement.
- Claim calibration and audience fit.

## `submission/cover_letter.qmd`

- Target journal and editor if known.
- Manuscript title and contribution summary.
- Fit with journal scope and audience.
- Evidence, method, and source base.
- Originality and non-submission statement.
- Ethical, data, funding, and conflict notes where relevant.

## `submission/pre_submission_audit.qmd`

- Contribution, claim-evidence, method, literature, and source audit.
- Tables, figures, citations, bibliography, and appendix audit.
- Data, code, permissions, ethics, and reproducibility status.
- Journal compliance and likely reviewer objections.
- Project-profile, required PDF render, table and figure manifest, R code-quality, and skill-execution-log status.
- Prioritized final risk list.
- Audit result for each domain: pass, conditional pass, fail, or not assessed.
- Go, conditional go, or no-go decision; a required domain marked not assessed cannot support go.

## `submission/final_fix_list.md`

- Blocking and non-blocking fixes.
- Responsible artifact and location.
- Verification criterion.
- Status and final approver.

## `replication/README.md`

- Citation, authorship, contact, license, package version, and release date.
- Package classification: full, partial, executable without data, or documentation-only.
- Data sources, rights, access conditions, and restricted-data procedure.
- Software, system dependencies, hardware, and expected runtime.
- Exact restoration, execution, rendering, and validation commands.
- Expected outputs, locations, and links to paper tables, figures, and appendices.
- Manual, licensed, network-dependent, or nondeterministic steps.
- Known deviations, disclosure controls, and package limitations.

## `replication/manifest.csv`

- Stable file identifier and project-relative path.
- Role: input, code, environment, intermediate, output, or documentation.
- Source or generating command/target.
- Version or cryptographic hash where applicable.
- Sharing, license, confidentiality, and required-status fields.
- Corresponding table, figure, appendix, result, or manuscript claim.
- Verification comparison rule, tolerance, and result.

## `replication/run_log.md`

- Package version, verifier, date, platform, and clean-state description.
- Environment restoration commands and outcomes.
- Execution commands, exit status, warnings, errors, and elapsed time.
- Inputs used and any restricted, network, or manual steps.
- Outputs generated and checks performed.
- Deviations from the README and unresolved execution issues.

## `replication/verification_report.md`

- Verification scope, verifier independence, date, and package version.
- Clean environment, declared inputs, and execution protocol.
- Comparison of estimates, sample sizes, tables, figures, appendices, and manuscript numbers.
- Hashes or justified numeric and visual tolerances.
- Discrepancies, causes, affected claims, and corrections.
- Restricted-data or platform limitations distinguished from package failures.
- Gate result: pass, conditional pass, or fail, with blocking actions and verification criteria.

## `submission/submission_manifest.md`

- Final manuscript and supplemental files.
- Version and generation date.
- Journal-specific requirements and compliance status.
- Data, code, appendix, disclosure, and permission files.
- Files intentionally excluded and reasons.

## `revision/response_to_reviewers.qmd`

- Editor summary response.
- Reviewer-by-reviewer table.
- For each comment: concern, decision, change, location, and response.
- Concessions, rejections, and partial acceptances distinguished.
- Updated claim-evidence or robustness notes.

## `revision/change_log.md`

- Reviewer or editor source.
- Requested and implemented change.
- Manuscript, analysis, table, or figure location.
- New evidence or computation.
- Verification and residual risk.

## `revision/revised_manuscript.qmd`

- Satisfy the complete manuscript contract.
- Incorporate all accepted editor and reviewer changes.
- Keep rejected or deferred requests traceable to the response letter.
- Maintain consistency with updated analysis, tables, figures, and supplements.

## `revision/revised_manuscript.pdf`

- Satisfy the complete revised-manuscript PDF contract.
- Be generated from the current `revision/revised_manuscript.qmd` after all accepted reviewer changes.
- Resolve citations, cross-references, tables, figures, and journal-specific PDF requirements.

## `revision/resubmission_manifest.md`

- Revised manuscript and response letter.
- Tracked and clean versions when required.
- Updated supplements, data, code, tables, and figures.
- Journal requirements and completion status.
- Final consistency check.
