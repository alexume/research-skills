---
name: research-hypothesis-generation
description: "Generate competing, testable research hypotheses or preliminary propositions from empirical patterns, literature, mechanisms, and historical context. Use when Codex must move from a research problem or exploratory pattern to explicit predictions, alternative explanations, evidence requirements, and provisional identification ideas."
---

# Skill: Hypothesis Generation

You generate research hypotheses for economic history and/or environmental history connecting observed patterns to causal mechanisms.

## Core principle
A good hypothesis must link:
1. **Observed pattern** — empirical regularity (or expected pattern if data not yet analyzed)
2. **Plausible mechanism** — causal process consistent with theory and context
3. **Testable implication** — what should be observable if the hypothesis is correct

## Workflow

### Step 1: Gather inputs
Identify what's available:
- EDA results or descriptive statistics
- `literature/research_question_handoff.qmd`
- mature literature review findings and debate matrix
- `literature/data_source_candidates.csv`
- Historical/institutional context
- Research question

Consume the research-question handoff first when it exists. Preserve the distinction between the initial question, the literature-refined question, and provisional hypothesis candidates. Treat those candidates as inputs to test and formalize, not as hypotheses already approved.

When a KnowledgeWiki exists, prefer its structured layers as inputs: a `Research Brief` from `wiki-consult` if one exists, then `indexes/by_debate.md` and `vocab/debates.yml` (they state the live controversies and who argues what), then the relevant literature notes. Anchor competing hypotheses in opposing debate positions before inventing new ones, and cite notes by slug + bibkey.

If a hypothesis depends on literature that has not passed full-text and extraction maturity, mark the support as provisional and return an exact hypothesis-directed search target to `literature-review`.

If no data is provided, infer plausible patterns from literature and context — clearly label them as inferred.

### Step 2: Map observed patterns
List key empirical regularities. For each:
- What varies? (outcome, across units, over time)
- What co-varies? (potential explanatory factors)
- What is surprising or unexplained?

### Step 3: Propose mechanisms
For each pattern, propose 1-3 causal processes:
- What is the channel from X to Y?
- What institutional or environmental context enables it?
- Is the mechanism immediate or lagged?
- Is it direct or mediated through another variable?

### Step 4: Formulate hypotheses
For each mechanism, write a hypothesis:
- **Format**: "If [mechanism], then [observable implication], because [reasoning]"
- Be specific about direction (increases/decreases), magnitude (if possible), and timing
- Distinguish between main hypotheses and auxiliary/competing ones

### Step 5: Generate competing explanations
For each main hypothesis:
- What alternative mechanism could produce the same pattern?
- What data would discriminate between them?

### Step 6: Map to identification
For each hypothesis, briefly indicate:
- What variation identifies the effect?
- What threats to identification exist?
- What instrument, control, or design might work?

## Output structure

```
### H1: [Short title]
- **Pattern**: [What is observed]
- **Mechanism**: [Proposed causal channel]
- **Prediction**: [Testable implication]
- **Competing**: [Alternative explanation]
- **Identification**: [How to test]
- **Confidence**: high / medium / tentative
```

## Rules
- Generate multiple competing hypotheses when mechanisms are ambiguous
- Distinguish correlation from causation explicitly
- State assumptions behind each hypothesis
- If data is weak, flag uncertainty rather than over-committing
- Never confuse description ("X and Y co-move") with explanation ("X causes Y because...")
- Rank hypotheses by testability, not by how interesting they sound
