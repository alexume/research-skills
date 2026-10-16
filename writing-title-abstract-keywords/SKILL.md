---
name: writing-title-abstract-keywords
description: "Create and evaluate journal-calibrated academic titles, abstracts, keywords, and concise contribution statements while preserving claim-evidence limits. Use when a manuscript has a stable question, design, results, and target audience and Codex must prepare discovery metadata or submission-facing summaries."
---

# Skill: Title, Abstract, and Keywords

You help prepare the front matter of an academic manuscript for submission.

Use this skill after a draft exists, or earlier when the user needs to clarify the manuscript's contribution and target audience.

Use `alex-urrego-style` when the manuscript requires authorial or domain-specific calibration.
Use `scientific-writing` in `authorial_revision` mode before finalizing the abstract.

## Core principle

The title and abstract must promise only what the manuscript can deliver. They should make the contribution legible without inflating the evidence.

Use:
- `../shared/journal_profiles.md`
- `../shared/output_contracts.md`
- `submission-journal-fit`
- `research-claim-evidence-mapping`

## Workflow

### Step 1: Diagnose manuscript profile
Identify:
- field and target journal,
- main research question,
- empirical object,
- geography and period,
- method or evidence base,
- strongest defensible contribution,
- claims that should not appear in the abstract.

### Step 2: Draft candidate titles
Produce 3-5 genuinely distinct title options chosen for the manuscript.
Possible functions include:

- naming the historical object,
- foregrounding a mechanism,
- marking a comparison,
- identifying a turning point,
- or signaling a historiographic intervention.

For each title, state:
- strength,
- risk,
- best target audience.

Do not generate one option per category mechanically.
Do not use a colon in every option.

### Step 3: Draft abstract
The abstract must make the following functions legible:

- the problem or debate,
- the empirical object, geography, and period,
- the evidence or method,
- the main finding or argument,
- and the contribution.

These functions do not require six sentences or a fixed order.
Let the order follow the manuscript's strongest logic.
State limits when they materially change how the finding should be read.

### Step 4: Calibrate claims
Check whether the abstract:
- avoids causal language unsupported by design,
- distinguishes pattern from explanation,
- does not overgeneralize beyond the case,
- identifies historical period and scale,
- names the evidence base.

Also check:

- whether consecutive sentences follow a repetitive template,
- whether generic gap or contribution language can be replaced by the actual historical finding,
- whether the abstract preserves the manuscript's distinctive analytical object,
- and whether every sentence can be traced to the manuscript.

### Step 5: Select keywords
Provide 5-8 keywords that balance:
- field terms,
- empirical object,
- geography,
- method or evidence,
- theoretical debate.

## Output format

```markdown
## Manuscript Profile

## Candidate Titles

| Title | Strength | Risk | Best Audience |
|---|---|---|---|

## Recommended Title

## Abstract

## Keywords

## One-Sentence Contribution

## Claims Excluded from the Abstract

## Journal Calibration Notes
```

## Rules

- Do not use a causal title unless the design supports a causal claim.
- Do not promise general theory from a narrow case unless the manuscript explicitly supports that move.
- Avoid vague titles built only from concepts.
- Prefer concrete historical objects, period, geography, and mechanism.
- Make keywords useful for discovery, not decorative.
- Do not optimize titles or abstracts for AI detectors.
- Do not smooth away uncertainty, historical specificity, or authorial rhythm merely to make the abstract more uniform.
