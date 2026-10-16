---
name: research-claim-evidence-mapping
description: "Map and audit descriptive, causal, structural, interpretive, historiographic, and methodological claims against their evidence, sources, strength, scale, timing, and limitations. Use before drafting, during interpretation or revision, and before submission when Codex must detect unsupported claims, state the strongest warranted interpretation positively, identify evidence gaps, trigger source retrieval or author decisions, and define the manuscript's safe core claims."
---

# Skill: Claim-Evidence Mapping

You audit the relationship between a paper's claims and its evidence.

This skill is used before drafting, during revision, and before submission. It is essential for avoiding overclaiming and for making papers robust to referee criticism.

## Core principle

Every important claim must have visible evidence, and every piece of evidence must support only the claim it can actually sustain.

## Claim types

Classify each claim as:
- **descriptive**: establishes a pattern or fact,
- **causal**: claims an effect or causal relationship,
- **structural**: explains a historical process or configuration,
- **interpretive**: offers a reading of meaning, mechanism, or implication,
- **historiographic**: positions the paper within a debate,
- **methodological**: justifies data, design, or measurement.

## Workflow

### Step 1: Extract claims
List the main claims from the introduction, results/analysis, discussion, and conclusion.

### Step 2: Match evidence
For each claim, identify:
- table,
- figure,
- model,
- archival source,
- secondary source,
- quote,
- historical fact,
- robustness result.

### Step 3: Assess strength
Classify evidence strength:
- high,
- medium,
- tentative,
- insufficient.

### Step 4: Identify risk
Flag:
- overclaiming,
- missing evidence,
- weak source base,
- scale mismatch,
- temporal mismatch,
- concept-variable mismatch,
- causal language without design,
- literature positioning gap.

### Step 5: Recommend revision
For each weak claim, recommend:
- strengthen evidence,
- retrieve evidence from the project or KnowledgeWiki,
- request a specific source or author decision,
- qualify wording,
- move to discussion,
- reframe as hypothesis,
- park for future work,
- delete.

Use this priority order:

1. retrieve evidence already available;
2. request the exact missing evidence or author decision;
3. state the strongest positive claim the evidence warrants;
4. add one material boundary where it changes interpretation;
5. reframe, park, or delete when the bridge cannot be supported.

Do not use repeated qualification to conceal a missing central premise.

Before narrowing, parking, or deleting a central interpretive or structural claim, test whether the paper retains its promised contribution without it. Distinguish:

- an unsupported overclaim that should be removed;
- a plausible explanatory relation that needs a specific source or additional evidence;
- an authorial choice among defensible contributions.

If narrowing would leave only a descriptive result, an indicator audit, or a contribution materially weaker than the introduction promises, do not treat `narrow` or `park` as a successful resolution. Retrieve available evidence, issue an exact source or author request, and block finalization of the affected architecture.

### Step 6: Classify evidence action

For every insufficient or tentative claim, classify the next action as:

- `retrieve-project`;
- `retrieve-wiki`;
- `request-user-source`;
- `request-author-decision`;
- `precise-placeholder`;
- `narrow`;
- `park`;
- `delete`.

A central claim with `request-user-source` or `request-author-decision` blocks finalization of the affected section, not necessarily the whole manuscript.

Provisional notes without verified locators may orient retrieval but do not close a central evidentiary gap when the claim requires source-verifiable historical or empirical support.

## Output format

```markdown
## Claim-Evidence Map

| Claim | Type | Evidence | Source/Location | Strength | Risk | Evidence action | Strongest warranted wording | Boundary |
|---|---|---|---|---|---|---|---|---|

## Unsupported or Overstated Claims

## Claims Requiring Qualification

## Evidence Gaps

## Source And Author Requests

## Contribution-Preservation Assessment

## Safe Core Claims

## Revision Priorities
```

## Rules

- Be stricter with claims in the abstract, introduction, and conclusion.
- Do not allow the conclusion to make stronger claims than the results.
- Do not allow a causal claim to rest only on descriptive evidence.
- Do not allow a structural claim to rest only on one narrow indicator.
- Do not allow historiographic claims without citations to the relevant debate.
- Prefer a positive evidence-bounded claim over prose organized around negation.
- Consolidate limitations; repeat them only when a new result changes the boundary.
- Invoke `wiki-consult` in `argument_support` mode before asking the user for material that may already exist in the KnowledgeWiki.
- For a user request, name the claim, object, geography, period, evidence type, current coverage, and consequence if the evidence remains unavailable.
- Do not infer author approval from the current draft, a journal-family choice, or a prior gate result.
