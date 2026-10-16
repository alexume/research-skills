---
name: research-hypothesis-refinement
description: "Refine, triage, rank, merge, or park research hypotheses by confronting them with data, sources, literature, mechanism clarity, testability, and identification constraints. Use after initial hypotheses and exploratory assessment when Codex must produce a tractable set of core hypotheses or propositions for strategy choice and design."
---

# Skill: Hypothesis Refinement

You refine research hypotheses by stress-testing them against evidence, feasibility, and identification constraints.

## Purpose
Take initial hypotheses (from `research-hypothesis-generation`) and sharpen them: drop untestable ones, merge redundant ones, decompose complex ones, and align surviving hypotheses with available data and identification strategies.

When `literature/research_question_handoff.qmd`, `literature/debate_matrix.csv`, or `literature/data_source_candidates.csv` exists, use them to distinguish literature plausibility from empirical feasibility. If a surviving hypothesis lacks a serious rival, boundary search, or mature source support, reactivate `literature-review` for a targeted update before finalizing it.

## Workflow

### Step 1: Audit existing hypotheses
For each hypothesis, assess:

| Criterion | Question | Rating |
|-----------|----------|--------|
| **Testability** | Can it be falsified with available data? | yes / partial / no |
| **Mechanism clarity** | Is the causal channel specific enough? | clear / vague / missing |
| **Data availability** | Do we have the variables needed? | available / constructible / missing |
| **Identification** | Is there a plausible design to estimate the effect? | strong / weak / none |
| **Distinctiveness** | Does it predict something different from alternatives? | distinct / overlapping |

### Step 2: Triage
Classify each hypothesis into:
- **Keep**: testable, clear mechanism, data available
- **Refine**: partially testable, needs decomposition or proxy construction
- **Acquire**: testable but requires additional data not yet in the project. Specify exactly what data is needed, where it might be found, and how difficult acquisition would be (easy/moderate/hard)
- **Park**: interesting but not testable with current data AND additional data is not realistically obtainable (document for future work)
- **Drop**: redundant, too vague, or unfalsifiable

### Step 3: Refine surviving hypotheses
For each "Keep" or "Refine" hypothesis:

1. **Sharpen the mechanism**: Make the causal channel more specific
   - Bad: "Disease affects mortality"
   - Good: "Yellow fever epidemics increase infant mortality among enslaved populations within 6 months of outbreak onset"

2. **Specify the prediction**: What coefficient sign, magnitude, or pattern would confirm/reject?
   - "If H1 is correct, β₁ > 0 and the effect should be larger in port cities"

3. **Identify the discriminating test**: What observation would distinguish this hypothesis from its competitor?
   - "H1 predicts a contemporaneous effect; H2 predicts a lagged effect. An event-study design discriminates."

4. **Map to variables**: 
   | Role | Variable | Source | Available? |
   |------|----------|--------|------------|

5. **Align with identification strategy**: Which equation from `research-causal-identification` tests this hypothesis?

### Step 4: Organize into tiers
Group refined hypotheses by priority:

- **Tier 1 (core)**: Central to the paper's contribution, strong identification available
- **Tier 2 (supporting)**: Reinforces core findings, weaker identification but informative
- **Tier 3 (exploratory)**: Worth documenting, requires future data or methods

### Step 5: Produce updated hypothesis table

```
| ID | Hypothesis | Mechanism | Test | Tier | Status | Data needed |
|----|-----------|-----------|------|------|--------|-------------|
| H1 | ... | ... | Eq. 7 | 1 | keep | — |
| H2 | ... | ... | Eq. 13 | 1 | keep | — |
| H3 | ... | ... | Eq. 5 | 2 | acquire | Epidemic records for Matanzas 1770s |
| H4 | ... | ... | — | 3 | park | — |
```

## Rules
- Be ruthless: parking a hypothesis is better than testing it badly
- Every surviving hypothesis must map to at least one estimating equation
- Distinguish between "we can't test this" and "we can test this but the data is noisy"
- When merging hypotheses, explain what was lost and what was gained
- Document parked hypotheses with clear conditions for when they become testable
- The final output should be a tractable set (3-6 core hypotheses), not an exhaustive list
