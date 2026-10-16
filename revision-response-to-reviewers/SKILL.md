---
name: revision-response-to-reviewers
description: "Plan, draft, and audit rigorous responses to editors and reviewers, linking every comment to a decision, manuscript or analysis change, location, evidence, and residual risk. Use after a journal decision or formal review when Codex must prepare a response letter, revision matrix, change log, or resubmission strategy."
---

# Skill: Response to Reviewers

You help prepare response-to-reviewers documents after a revise-and-resubmit, conditional acceptance, or rejection-with-resubmission invitation.

## Core principle

The response must show that the authors understood the criticism, revised the manuscript concretely, and calibrated claims where evidence is limited.

Use:
- `research-claim-evidence-mapping`
- `review-reviewer-core`
- `review-causal-historical-logic`
- `review-ecological-economics`
- `review-agrarian-environmental-history`
- `writing-paper-draft`
- `research-reproducibility-and-replication`

Read `project/project_profile.yaml` and preserve `revision/revised_manuscript.qmd` as the controlled manuscript source. After accepted changes, regenerate every required format, including `revision/revised_manuscript.pdf` under the default profile. Update table and figure manifests, stable Quarto cross-references, code-quality evidence, and replication records whenever the revision changes analysis or presentation outputs.

## Workflow

### Step 1: Parse decision materials
Separate:
- editor comments,
- reviewer 1 comments,
- reviewer 2 comments,
- reviewer 3 comments,
- mandatory changes,
- optional suggestions.

### Step 2: Classify each comment
Classify comments as:
- contribution/framing,
- literature,
- theory/concepts,
- source/data/method,
- causal identification,
- historical mechanism,
- interpretation/overclaiming,
- tables/figures,
- writing/structure,
- citation/style.

### Step 3: Decide response strategy
For each comment, choose:
- accept and revise,
- accept partially and revise,
- clarify without major revision,
- respectfully disagree,
- cannot address due to evidence/data limits.

### Step 4: Link response to changes
Every substantive response should state:
- what changed,
- where it changed,
- why this addresses the concern,
- whether claims were strengthened, qualified, moved, or removed.

Record technical skill execution in `project/skill_execution_log.csv` and substantive revision decisions in `revision/change_log.md`. Do not use the response letter as the only evidence that a change was implemented.

### Step 5: Maintain tone
Use a professional, concise, non-defensive tone.

## Output format

```markdown
## Overall Response Strategy

## Letter to the Editor

## Response Table

| Reviewer | Comment | Issue Type | Decision | Manuscript Change | Location | Response Draft |
|---|---|---|---|---|---|---|

## Major Revisions Made

## Claims Qualified or Removed

## Additional Evidence or Robustness Added

## Points Respectfully Disputed

## Remaining Risks
```

## Rules

- Do not answer only with promises; link each response to manuscript changes.
- Do not use defensive language.
- Do not ignore editor comments.
- Do not reject a reviewer concern unless the reason is specific and evidence-based.
- If the reviewer identifies overclaiming, prefer claim calibration over rhetorical defense.
- If new analyses are impossible, explain the constraint and revise the claim accordingly.
- Do not declare resubmission ready until the current QMD cleanly produces the profile-required PDF and all citations and cross-references resolve.
