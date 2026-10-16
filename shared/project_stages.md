# Project Stages

This file defines the standard stages used by the academic production workflow. Skills should use these stages when diagnosing project status, selecting next actions, and checking whether outputs are ready to advance.

Use `workflow_registry.yaml` for machine-readable ownership, routing, inputs, outputs, and gate identifiers. This file provides the narrative definition of each stage.

## 0. Setup
- Purpose: create the project structure, collect initial materials, and define the reproducibility architecture.
- Inputs: research idea, initial references, available datasets or source leads.
- Outputs: `project/setup_manifest.md`, `project/project_profile.yaml`, `project/project_log.md`, `project/skill_execution_log.csv`, `project/source_inventory.csv`, `project/reproducibility_plan.md`, and project folders.

## 1. Literature orientation
- Purpose: assess the seed corpus, execute initial question/hypothesis and seed-network searches, map provisional research lines, and refine the research question within the literature.
- Inputs: topic, initial references, local PDFs, known authors.
- Outputs: `literature/search_strategy.qmd`, `literature/research_question_handoff.qmd`, `literature/references.bib`, `literature/source_discovery_log.csv`, `literature/screening_log.csv`, and `literature/data_source_candidates.csv`.

## 2. Literature maturation
- Purpose: complete and document the search, screening, full-text reading, source appraisal, debate reconstruction, data-source discovery, KnowledgeWiki promotion, saturation assessment, and contribution positioning required by the review type.
- Inputs: research-question handoff, search protocol, seed and discovered corpus, bibliography, and journal target if available.
- Outputs: `literature/literature-review.qmd`, `literature/recent_literature.qmd`, `literature/debate_matrix.csv`, `literature/data_source_candidates.csv`, `literature/references.bib`, and updated discovery, screening, and extraction logs.

## 3. Hypotheses v1
- Purpose: generate competing mechanisms and preliminary hypotheses.
- Inputs: research-question handoff, mature literature review or explicitly bounded orientation evidence, data/source candidates, historical context, and preliminary empirical patterns.
- Outputs: `analysis/hypotheses_v1.qmd`.

## 4. Exploratory data/source assessment
- Purpose: identify empirical patterns, data constraints, source coverage, and anomalies.
- Inputs: datasets, source corpus, codebooks, archival metadata.
- Outputs: `analysis/exploratory.qmd`, `scripts/eda.R`, `analysis/data_source_quality.md`, `analysis/source_criticism.qmd`, `analysis/measurement_strategy.qmd`, `analysis/eda_decision_log.md`, and `project/historical_source_registry.csv` as applicable.

## 5. Hypotheses v2
- Purpose: refine hypotheses against literature, data, sources, and feasibility.
- Inputs: hypotheses v1, EDA, literature, source assessment.
- Outputs: `analysis/hypotheses_v2.qmd`.

## 6. Strategy choice
- Purpose: select the primary research route.
- Inputs: hypotheses v2, EDA, source availability, research question.
- Outputs: `analysis/research_strategy.qmd`.
- Routes: causal, historical-structural, hybrid.

## 7. Design
- Purpose: formalize the empirical or structural design.
- Causal outputs: `analysis/causal_design.qmd`, `analysis/identification_strategy.qmd`.
- Historical-structural outputs: `analysis/structural_analysis_design.qmd`, `analysis/mechanism_map.qmd`.
- Hybrid outputs: both design types plus `analysis/hybrid_integration_plan.md`.
- All routes using constructed historical indicators should also produce `analysis/measurement_strategy.qmd`.

## 8. Requirements and acquisition
- Purpose: identify, search for, verify, and lawfully obtain required data, sources, and contextual evidence.
- Inputs: design outputs.
- Outputs: `analysis/data_requirements.qmd`, `analysis/source_requirements.qmd`, `project/evidence_discovery_log.csv`, `project/acquisition_log.csv`, `project/acquisition_manifest.md`, and verified raw inputs where lawful.

## 9. Preparation
- Purpose: clean data, construct variables, organize sources, document provenance.
- Inputs: acquired data/sources.
- Outputs: `data/clean/`, `data/interim/`, preparation scripts, `analysis/preparation_manifest.md`, `analysis/data_validation.md`, `analysis/r_code_quality.md`, `analysis/computational_environment.md`, `project/historical_source_registry.csv`, `data/metadata/variable_dictionary.csv`, and `data/metadata/measurement_decisions.csv`.

## 10. Feasibility and design update
- Purpose: verify estimability or explanatory feasibility before full implementation.
- Inputs: clean data/source corpus, design files.
- Outputs: `analysis/feasibility.qmd`, `analysis/inference_plan.qmd`, updated design.
- Route logic: causal feasibility is owned by the selected causal implementation skill; historical-structural feasibility by `implementation-historical-structural-analysis`; hybrid feasibility coordinates both.

## 11. Implementation
- Purpose: run models or produce structural empirical analysis.
- Inputs: final design, clean data/sources.
- Causal outputs: `analysis/results.qmd`, model and specification registries, fitted objects, scripts, tables, and figures.
- Historical-structural outputs: `analysis/structural_patterns.qmd`, `analysis/structural_evidence_matrix.csv`, `analysis/structural_analysis_log.csv`, scripts, tables, figures, and maps as applicable.
- Shared quality and presentation outputs: `analysis/r_code_quality.md`, `tables/table_manifest.csv`, and `figures/figure_manifest.csv`.

## 12. Interpretation
- Purpose: connect results or patterns to mechanisms, literature, historical context, and a cumulative discussion argument.
- Inputs: causal results and/or structural patterns, mechanism map, literature.
- Process: complete mechanism and claim-evidence mapping, compare alternative architectures when the contribution remains open, obtain author approval for materially different choices, then use `writing-paper-draft` in `develop_argument` mode; invoke `wiki-consult` in `argument_support` mode for retrievable central gaps.
- Outputs: `project/project_argument_profile.qmd`, route-appropriate updates to `analysis/results.qmd` and/or `analysis/structural_patterns.qmd`, plus `analysis/interpretation.qmd`, `analysis/discussion_argument_map.qmd`, and `analysis/claim_evidence_map.qmd`.

## 13. First draft
- Purpose: assemble a coherent paper.
- Inputs: all analysis outputs, including the author-approved project argument profile, passed interpretation and discussion argument map, plus the declared journal family or target journal.
- Outputs: `paper/first_draft.qmd`, `paper/first_draft.pdf`, `paper/authorial_revision_log.md`, and `appendix/analytical_appendix.qmd`.

## 14. Internal referee review
- Purpose: critique the draft as a referee, coauthor, or editor.
- Inputs: draft, target journal if available.
- Outputs: `paper/referee_report.qmd` and `paper/revision_priorities.md`.

## 15. Revision
- Purpose: implement major revisions and strengthen contribution, evidence, and structure.
- Inputs: referee report, draft, analysis outputs, and an updated discussion argument map when the revision changes interpretation or architecture.
- Outputs: `paper/revised_manuscript.qmd`, `paper/revised_manuscript.pdf`, `paper/revision_log.md`, and updated `appendix/analytical_appendix.qmd` when evidence or analysis changes.

## 16. Journal fit
- Purpose: select journal and adjust framing.
- Inputs: revised draft, contribution, journal profiles.
- Outputs: `submission/journal_fit.qmd`.

## 17. Pre-submission audit
- Purpose: final consistency, publishability, reproducibility, and independent replication check.
- Inputs: manuscript QMD and current PDF, project profile, figures and figure manifest, tables and table manifest, analytical appendix, bibliography, code-quality report, skill-execution log, code, data documentation, and computational environment.
- Outputs: `submission/pre_submission_audit.qmd`, `submission/final_fix_list.md`, `replication/README.md`, `replication/manifest.csv`, `replication/run_log.md`, and `replication/verification_report.md`.

## 18. Submission package
- Purpose: prepare final manuscript, cover letter, abstract, keywords, and supplemental files.
- Inputs: audited manuscript.
- Outputs: final submission package, verified replication materials, `paper/title_abstract_keywords.qmd`, `submission/cover_letter.qmd`, `submission/submission_manifest.md`, and updated `replication/manifest.csv`.

## 19. Revision and resubmission
- Purpose: respond to reviewers and revise the manuscript after editorial feedback.
- Inputs: decision letter, reviewer reports, manuscript, analysis outputs, revision log.
- Outputs: `revision/response_to_reviewers.qmd`, `revision/revised_manuscript.qmd`, `revision/revised_manuscript.pdf`, `revision/change_log.md`, `revision/resubmission_manifest.md`, updated `appendix/analytical_appendix.qmd`, and reverified replication manifest, run log, and verification report when analyses change.
