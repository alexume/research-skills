---
name: submission-pre-submission-audit
description: "Conduct the final go, conditional-go, or no-go audit of an academic manuscript's contribution, claims, evidence, design, sources, literature, tables, figures, citations, disclosures, reproducibility status, and journal compliance. Use immediately before assembling or uploading a submission package."
---

# Skill: Pre-Submission Audit

You perform the final audit before a manuscript is submitted to a journal.

This is the final substantive audit before the submission package is assembled. It consumes a separate clean-state replication decision rather than treating code availability as reproducibility.

Read `project/project_profile.yaml`, `project/skill_execution_log.csv`, `analysis/r_code_quality.md`, `tables/table_manifest.csv`, and `figures/figure_manifest.csv`. Audit the current QMD source and every render required by the profile; PDF is mandatory under the default profile.

## Core principle

A manuscript should not be submitted because it is complete. It should be submitted because its claims, evidence, framing, and journal fit are aligned.

## Workflow

### Step 1: Contribution audit
Check:
- research question is clear,
- contribution is explicit,
- novelty is credible,
- claims are not inflated,
- introduction and conclusion match.

### Step 2: Claim-evidence audit
Use or request `research-claim-evidence-mapping`.

Check:
- every major claim has evidence,
- causal claims have design support,
- structural claims have mechanism and evidence,
- historiographic claims have citations,
- conclusion does not exceed results.

### Step 3: Design and method audit
For causal papers:
- treatment, outcome, unit, timing, and identifying variation are clear,
- assumptions are stated,
- robustness and falsification are included,
- standard errors and fixed effects are justified.

For historical-structural papers:
- periodization is clear,
- patterns are established,
- mechanisms are mapped,
- competing interpretations are addressed,
- source limits are acknowledged.

For hybrid papers:
- causal and structural claims are separated,
- bounded estimates are not overgeneralized,
- interpretation integrates evidence without overstating it.

### Step 4: Literature audit
Check:
- relevant debates are represented,
- citations are current where needed,
- contribution is positioned specifically,
- no straw-man literature gap is used.

### Step 5: Tables and figures audit
Activate `implementation-tables-and-appendices` and `implementation-figures` as needed.

Check:
- each table/figure has a purpose,
- titles and captions are clear,
- units are reported,
- figures do not overstate patterns,
- tables support the argument,
- the table manifest matches main and appendix outputs,
- every displayed value traces to a registered model, structural evidence object, or documented transformation,
- failed diagnostics and material sensitivities are not hidden in or omitted from the appendix.
- every table and figure has a stable Quarto cross-reference and a manifest status of main, appendix, or excluded;
- the required PDF contains the registered main outputs and renders them legibly;
- raw LaTeX inclusion is used only when explicitly required by the profile or journal.

### Step 6: Citation and bibliography audit
Check:
- all cited works are in bibliography,
- all bibliography entries are cited or intentionally retained,
- citation style is consistent,
- page numbers are included for specific textual claims when needed.

### Step 7: Journal readiness
Use `submission-journal-fit` if not already completed.

Check:
- target journal is plausible,
- manuscript is framed for that audience,
- likely reviewer objections have been addressed.

### Step 8: Reproducibility and replication audit

Activate `research-reproducibility-and-replication`. Check:

- the computational environment is documented and restorable;
- one documented entry point regenerates the required analytical outputs;
- raw inputs, transformations, models, specifications, tables, figures, and manuscript numbers have traceable provenance;
- structural evidence, analysis decisions, table manifest entries, and appendix outputs are traceable when applicable;
- restricted or archival data are handled lawfully and their access limitations are explicit;
- `replication/README.md` and `replication/manifest.csv` match the package contents;
- an independent clean-state run is recorded in `replication/run_log.md`;
- `replication/verification_report.md` compares all central outputs with declared tolerances;
- no credentials, personal data, absolute local paths, or undocumented manual steps remain.
- maintained R code follows the declared native-pipe and tidyverse-style policy, with `styler` and `lintr` results recorded;
- the QMD regenerates every profile-required format from a clean state and the PDF is current;
- `project/skill_execution_log.csv` supports technical execution claims, while `paper/authorial_revision_log.md` contains substantive authorial decisions rather than acting as a skill checklist.

Apply `G-REPLICATION` before the final `G-SUBMISSION` decision. A failed replication gate is a no-go. A conditional pass must be bounded, must not affect a central claim, and must name the fix and re-verification criterion.

For each audit domain report `pass`, `conditional pass`, `fail`, or `not assessed`. `Not assessed` means evidence was unavailable or the check was not performed; it is never equivalent to pass and prevents a final Go when the domain is required.

## Output format

```markdown
## Overall Decision
Go / Conditional Go / No-Go

## Contribution Audit

## Claim-Evidence Audit

## Method or Structural Design Audit

## Literature Audit

## Tables and Figures Audit

## Citation and Bibliography Audit

## Reproducibility and Replication Audit

## Journal Readiness

## Required Fixes Before Submission

## Residual Risks

## Final Recommendation
```

## Decision rules

### Go
Use only when:
- contribution is clear,
- evidence supports claims,
- journal fit is plausible,
- the replication gate has passed,
- remaining problems are minor.
- no required audit domain is not assessed.

### Conditional Go
Use when:
- paper is nearly ready,
- specific limited fixes remain,
- risks are manageable,
- any replication exception is bounded and has a verification criterion.

### No-Go
Use when:
- contribution is unclear,
- claims exceed evidence,
- design is not defensible,
- literature positioning is weak,
- journal fit is implausible,
- the analysis or central reported outputs cannot be reproduced.
- a required PDF, manifest, code-quality check, project profile, or execution log is missing or not assessed.

## Rules

- Be stricter with abstract, introduction, and conclusion than with internal sections.
- Do not allow submission if the main claim is unsupported.
- Do not allow journal fit to compensate for weak evidence.
- Do not allow code availability to substitute for a clean-state verification.
- Do not infer skill use from prose, filenames, or the authorial revision log.
- Do not accept an optional HTML render in place of a required PDF.
- Provide a prioritized fix list, not a generic list of comments.
