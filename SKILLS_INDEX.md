# Skills Index

Human-readable entry point for selecting skills and locating the governance documents for this research system.

## System Governance

- Routing source of truth: `shared/workflow_registry.yaml`
- Narrative stage definitions: `shared/project_stages.md`
- Artifact completion rules: `shared/output_contracts.md`
- Quality decisions: `shared/stage_gates.md`
- Project publication and code profile: `shared/project_profile_template.yaml`
- Shared R code standard: `shared/r_code_style.md`
- Machine-local paths: `shared/local_config.yaml`
- Current architecture: `ARCHITECTURE_REPORT.md`
- Dated system changes: `SYSTEM_CHANGELOG.md`
- Original pre-change inventory: `PRECHANGE_INVENTORY.txt`
- Full-system validation: `shared/validate_skill_system.py`

The orchestrator must report conflicts between these governance files rather than silently selecting one.

## Workflow At A Glance

| Workflow segment | Routing |
| --- | --- |
| Stages 0-6 | Shared research formation through strategy choice |
| Stage 7 causal | `research-causal-identification` |
| Stage 7 historical-structural | `research-structural-analysis-design` |
| Stage 7 hybrid | Both designs coordinated by `research-strategy-choice` |
| Stage 8 | `research-evidence-discovery-and-acquisition` for all routes |
| Stage 9 | `data-preparation` for all routes |
| Stages 10-11 causal | `implementation-causal-analysis`, with DiD override |
| Stages 10-11 historical-structural | `implementation-historical-structural-analysis` |
| Stages 10-11 hybrid | Both implementations coordinated by the orchestrator |
| Stage 12 | Route-specific interpretation coordinated by `research-mechanism-mapping` |
| Stages 13-19 | Writing, review, replication, submission, and resubmission |

`research-reproducibility-and-replication` is cross-cutting. `implementation-tables-and-appendices` and `implementation-figures` support analytical and publication outputs without defining the research route.

Every project should initialize `project/project_profile.yaml` and `project/skill_execution_log.csv` at Stage 0. The profile declares manuscript language, required renders, PDF engine, figure/table integration, and R code policy. Quarto QMD is the controlled manuscript source and PDF is mandatory under the default profile.

## Intent To Skill Mapping

Usa esta tabla como puente rapido desde una regla o intencion en `.clinerules` hacia la skill mas adecuada.

| Intent / Need | Recommended Skill |
| --- | --- |
| define research architecture | `research-strategy-choice` |
| choose between causal or structural route | `research-strategy-choice` |
| orchestrate full project workflow | `orchestration-research-workflow` |
| design causal strategy | `research-causal-identification` |
| design historical-structural explanation | `research-structural-analysis-design` |
| critically assess historical sources | `research-historical-source-criticism` |
| design and harmonize historical measures | `research-historical-measurement` |
| find and acquire missing datasets or historical sources | `research-evidence-discovery-and-acquisition` |
| generate research hypotheses | `research-hypothesis-generation` |
| refine hypotheses with evidence constraints | `research-hypothesis-refinement` |
| map mechanisms, actors, timing, institutions | `research-mechanism-mapping` |
| verify whether claims are supported by evidence | `research-claim-evidence-mapping` |
| review overall manuscript rigor | `review-reviewer-core` |
| review causal logic and historical coherence | `review-causal-historical-logic` |
| review agrarian and environmental history framing | `review-agrarian-environmental-history` |
| review ecological economics framing | `review-ecological-economics` |
| review doctoral proposal quality | `review-doctoral-proposal` |
| clean and merge datasets | `data-preparation` |
| explore data in R | `data-exploration` |
| implement IV, RDD, panel, and synthetic-control analysis | `implementation-causal-analysis` |
| implement modern DiD and event studies | `implementation-difference-in-differences` |
| implement historical-structural analysis | `implementation-historical-structural-analysis` |
| create traceable tables and analytical appendices | `implementation-tables-and-appendices` |
| design reproducible workflows and replication packages | `research-reproducibility-and-replication` |
| create publication-quality figures | `implementation-figures` |
| run a literature review | `literature-review` |
| extract PDFs or books into structured notes | `knowledge-ingestion` |
| draft paper sections in Quarto | `writing-paper-draft` |
| improve title, abstract, keywords | `writing-title-abstract-keywords` |
| generate academic slides | `writing-beamer-generation` |
| preserve Alex Urrego writing voice | `alex-urrego-style` |
| evaluate journal fit | `submission-journal-fit` |
| draft submission cover letter | `submission-cover-letter` |
| run pre-submission audit | `submission-pre-submission-audit` |
| draft response to reviewers | `revision-response-to-reviewers` |
| consult and reason over KnowledgeWiki | `wiki-consult` |
| refine hypotheses or map claims via wiki | `wiki-consult` |
| draft, edit, or tighten academic prose | `scientific-writing` |
| remove hedging, filler, and vague claims | `scientific-writing` |
| create or refine a Codex skill | `skill-creator` |
| install a skill | `skill-installer` |
| scaffold a plugin | `plugin-creator` |
| consult official OpenAI docs | `openai-docs` |
| generate or edit images | `imagegen` |

## Research Workflow Skills

### orchestration-research-workflow
Purpose:
- orchestrate end-to-end research workflow
- diagnose stage and select or confirm the route
- dispatch stage owner, method override, and supporting skills in precedence order
- require causal, structural, or hybrid outputs without conflating them
- route failed gates back to acquisition, preparation, design, strategy, or implementation
- connect idea, evidence, writing, and submission

### research-strategy-choice
Purpose:
- choose research architecture
- define scale and causal logic
- identify contribution
- structure hypotheses

### research-causal-identification
Purpose:
- design causal identification strategies
- formalize assumptions
- specify equations and threats
- align questions with methods

### research-structural-analysis-design
Purpose:
- design historical-structural research
- explain processes and transformations
- define periodization and scale
- connect mechanisms with evidence

### research-historical-source-criticism
Purpose:
- reconstruct provenance and source production
- assess coverage, selection, survival, categories, and silences
- trace digitization and transformation chains
- determine which claims a historical source can support

### research-historical-measurement
Purpose:
- translate concepts into historically valid measures
- harmonize units, prices, categories, boundaries, and time
- document variable lineage and measurement uncertainty
- define alternative measures and sensitivity requirements

### research-evidence-discovery-and-acquisition
Purpose:
- convert design requirements into controlled evidence searches
- verify datasets, archival materials, versions, coverage, access, and rights
- acquire lawful raw inputs without confusing discovery with possession
- document failed searches, substitutes, and consequences for design feasibility

### research-hypothesis-generation
Purpose:
- generate testable research hypotheses
- derive expectations from literature and data
- identify competing explanations
- open empirical research paths

### research-hypothesis-refinement
Purpose:
- refine hypotheses against data constraints
- test plausibility and scope
- improve theoretical precision
- align hypotheses with feasible evidence

### research-mechanism-mapping
Purpose:
- map mechanisms, actors, institutions, and timing
- connect patterns to causal processes
- identify rival mechanisms
- organize mechanism-centered explanation

### research-claim-evidence-mapping
Purpose:
- audit claims against evidence
- separate descriptive, causal, and interpretive claims
- detect unsupported assertions
- improve evidentiary discipline

### wiki-consult
Purpose:
- consult, synthesize, and reason over a KnowledgeWiki
- refine hypotheses, brainstorm mechanisms, map claims to evidence
- prepare retrieval packs for cheaper long-context models
- draft memos from wiki indexes, registries, and literature notes
- orchestrate specialized research skills after building wiki context

## Review Skills

### review-reviewer-core
Purpose:
- run core manuscript review
- identify weaknesses in argument and evidence
- structure critical evaluation
- support rigorous feedback

### review-causal-historical-logic
Purpose:
- evaluate causal coherence
- assess historical mechanisms
- test temporal and institutional plausibility
- review mediation, conflict, and agrarian change

### review-agrarian-environmental-history
Purpose:
- evaluate agrarian structures
- assess environmental transformations
- review rural political economy
- situate claims in historical perspective

### review-ecological-economics
Purpose:
- evaluate ecological economics framing
- review material flows and socioecological transitions
- assess environmental accounting logic
- test conceptual coherence

### review-doctoral-proposal
Purpose:
- review doctoral proposal design
- assess question, contribution, feasibility, and risks
- identify supervision priorities
- strengthen proposal architecture

## Data And Analysis Skills

### data-preparation
Purpose:
- clean and transform raw data
- merge sources into analysis-ready datasets
- standardize variables and structures
- support reproducible preprocessing
- apply the shared native-pipe, tidyverse, `styler`, and `lintr` standard

### data-exploration
Purpose:
- run exploratory data analysis in R
- profile variables and distributions
- detect patterns, outliers, and gaps
- inform downstream modeling

### implementation-causal-analysis
Purpose:
- implement causal inference analyses
- support IV, RDD, panel, and synthetic-control methods
- translate design into executable analysis
- connect identification with estimation, inference, diagnostics, and sensitivity

### implementation-difference-in-differences
Purpose:
- implement canonical and staggered DiD designs
- estimate and aggregate group-time treatment effects
- audit parallel trends, anticipation, overlap, and cohort support
- connect DiD estimation with causal and historical interpretation

### implementation-historical-structural-analysis
Purpose:
- execute approved historical-structural and hybrid designs
- establish temporal, spatial, compositional, institutional, and socioecological patterns
- assess periodization, comparisons, triangulation, mechanisms, and rival interpretations
- produce reproducible structural evidence matrices, analysis logs, and pattern reports

### implementation-tables-and-appendices
Purpose:
- generate publication tables from registered analytical objects and evidence
- organize main and appendix outputs by argumentative and diagnostic purpose
- standardize notes, uncertainty, provenance, and multi-format rendering
- audit consistency across manuscript, appendix, pipeline, and replication package
- maintain stable Quarto cross-references and main, appendix, or excluded manifest status

### research-reproducibility-and-replication
Purpose:
- design the reproducibility architecture from project setup
- capture computational environments, pipelines, seeds, models, and analytical decisions
- assemble lawful full or restricted-data replication packages
- run clean-state verification before submission and after analytical revisions
- verify profile-required renders, manifests, R code quality, and technical skill execution

### implementation-figures
Purpose:
- create publication-quality figures
- use consistent ggplot2 styling
- communicate patterns clearly
- prepare academic visual outputs
- maintain `figures/figure_manifest.csv` and stable Quarto cross-references
- export profile-required vector or raster formats and verify the rendered PDF
- apply `cedric-scherer-aesthetics.qm` as the operational aesthetic synthesis
- preserve its extracted and scraped source material under `implementation-figures/references/` for provenance and selective updates

## Literature And Writing Skills

### literature-review
Purpose:
- run systematic literature review
- search and evaluate sources
- synthesize debates and gaps
- build literature-grounded positioning

### writing-paper-draft
Purpose:
- draft academic paper sections in Quarto
- structure argument and evidence
- maintain scholarly flow
- support section-level writing
- use the declared manuscript language and generate every required render, including PDF by default
- separate authorial decisions from technical skill-execution records

### writing-title-abstract-keywords
Purpose:
- create titles, abstracts, and keywords
- sharpen contribution framing
- calibrate manuscript front matter to journals
- improve discoverability

### writing-beamer-generation
Purpose:
- generate Quarto Beamer presentations
- structure slide progression
- support academic talks
- turn research into presentation format

### alex-urrego-style
Purpose:
- preserve academic voice
- maintain economic history and ecological economics tone
- avoid generic AI writing
- align prose with authorial style

### scientific-writing
Purpose:
- apply scientific writing rules for academic prose in social and environmental science
- draft, edit, tighten, or review article prose
- remove throat-clearing, stacked hedging, vague abstraction, and empty contribution claims
- enforce claim-first paragraphs, evaluable statements, and lexical precision

## Submission Skills

### submission-journal-fit
Purpose:
- assess journal fit
- anticipate reviewer objections
- guide reframing for target outlets
- improve submission strategy
- propagate journal-specific language, render, table, figure, and disclosure requirements into the project profile

### submission-cover-letter
Purpose:
- draft concise journal-calibrated cover letters
- present contribution clearly
- support submission package quality
- align tone with editorial expectations

### submission-pre-submission-audit
Purpose:
- run final submission audit
- review claims, methods, tables, figures, and citations
- detect readiness gaps
- reduce preventable submission problems
- audit the current PDF, manifests, R code quality, project profile, and technical execution log

### revision-response-to-reviewers
Purpose:
- plan revision strategy
- draft responses to reviewers
- link comments to manuscript changes
- improve revision coherence
- regenerate the profile-required revised PDF and reverify affected analytical outputs

## System Skills

### skill-creator
Purpose:
- create or improve Codex skills
- define structure, workflow, and instructions
- support new skill authoring

### skill-installer
Purpose:
- install skills into Codex
- list curated skills
- add skills from repositories

### plugin-creator
Purpose:
- scaffold Codex plugins
- create plugin manifests and structure
- support local plugin setup

### openai-docs
Purpose:
- consult current official OpenAI documentation
- support API and product implementation
- ground answers in authoritative docs

### imagegen
Purpose:
- generate or edit bitmap images
- create visual assets from prompts
- transform existing images when needed
