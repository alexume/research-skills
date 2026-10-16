---
name: research-strategy-choice
description: "Choose whether a research project should follow a causal, historical-structural, or hybrid strategy based on its question, mechanisms, data, sources, identification strength, and defensible claims. Use after hypothesis refinement and exploratory assessment when the primary research route is unresolved or must be reconsidered after feasibility problems."
---

# Skill: Research Strategy Choice

You decide whether a research project should be developed as a causal paper, a historical-structural paper, or a hybrid paper.

## Core principle

The research strategy must match the strongest defensible claim, not the most ambitious claim.

## Strategy types

### Causal
Use when the paper can credibly estimate or identify an effect.

Required:
- treatment or shock,
- outcome,
- unit of analysis,
- timing,
- counterfactual logic,
- identifying variation,
- plausible mechanism,
- sufficient data.

Allowed claims:
- bounded causal effects,
- mechanism-consistent interpretation,
- heterogeneity where supported.

Forbidden claims:
- total historical explanation from a narrow estimate,
- causal language without identifying assumptions,
- universal extrapolation across periods or regions.

### Historical-structural
Use when the paper explains a transformation, process, structure, or pattern using historical evidence and theoretically grounded mechanisms.

Required:
- process to explain,
- periodization,
- scale,
- core patterns,
- mechanisms,
- sources or indicators,
- competing interpretations.

Allowed claims:
- historically grounded structural explanation,
- process tracing across periods,
- mechanism plausibility,
- interpretation of patterns.

Forbidden claims:
- isolated causal effects without design,
- description without mechanism,
- broad structural claims unsupported by evidence.

### Hybrid
Use when the paper combines structural explanation with one or more bounded causal tests.

Required:
- explicit division of labor between structural and causal components,
- bounded causal question,
- broader structural process,
- claim calibration.

Allowed claims:
- structural explanation supported by multiple evidence types,
- causal evidence for one mechanism or sub-process,
- integrated interpretation.

Forbidden claims:
- treating one estimate as proof of the whole structural process,
- mixing causal and structural language without boundaries.

## Workflow

### Step 1: Define the main research claim
State the strongest claim the project seems to want to make.

### Step 2: Audit evidence and design
Assess:
- data availability,
- source availability,
- temporal coverage,
- spatial coverage,
- identification strength,
- mechanism clarity,
- literature positioning.

### Step 3: Classify route
Use this table:

| Criterion | Causal | Historical-structural | Hybrid |
|---|---|---|---|
| Identification | strong | not required | partial |
| Mechanism | explicit | explicit | explicit |
| Quantitative data | central | useful | central for one part |
| Historical sources | contextual or evidentiary | central | central |
| Main result | estimated effect | explanation of process | effect plus process |
| Main risk | overclaiming | description without mechanism | imbalance |

### Step 4: Define claims
Separate:
- claims the project can make,
- claims it cannot make,
- claims requiring additional evidence.

### Step 5: Recommend next outputs
Assign outputs from `shared/output_contracts.md`.

## Output format

```markdown
## Recommended Primary Strategy

## Secondary Strategy

## Justification

## Feasibility Constraints

## What Can Be Claimed

## What Cannot Be Claimed

## Evidence Needed

## Required Next Outputs

## Stage Gate Result
```

## Rules

- Be conservative about causal claims.
- Do not demote historical-structural papers to “descriptive” if they have mechanisms, periodization, and evidence.
- Do not recommend a causal route only because regression is possible.
- A weak causal design plus a strong structural explanation should usually become hybrid or historical-structural.
- If no route is ready, return the project to literature, hypotheses, or EDA/source assessment.
