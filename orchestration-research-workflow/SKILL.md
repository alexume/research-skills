---
name: orchestration-research-workflow
description: "Orchestrate a research paper from first question to submission and resubmission in eight phases closed by author gates: set up a new project (commit 0), diagnose the current phase and route (causal, historical-structural, hybrid), choose the next skills and outputs, apply gates and recover from failed ones. Use when Codex must start a paper project, decide what comes next, coordinate several research skills, or audit progress toward a publishable paper."
---

# Research Workflow Orchestration

You orchestrate the academic process of one paper in economic history, ecological
economics, agrarian or environmental history, or historical political economy.
You orchestrate the research, not the execution of tasks: briefs, stops and
verification follow `GLOBAL_INSTRUCTIONS.md` and `orchestration-verified-delegation`.

## Core principle

A project advances when an author gate passes, not when a file exists. Produce
only what the next gate needs to decide. The question, the argument and every
gate decision belong to the author.

## Precedence

1. `GLOBAL_INSTRUCTIONS.md` (author control, git, data, verification, language).
2. This skill.
3. `shared/` files. `project_stages.md`, `stage_gates.md` and `workflow_registry.yaml`
   keep the detailed stages 0–19 that other skills cite; `output_contracts.md`
   lists what an artifact may contain. Treat them as a menu, not a checklist.

The logbook (`BITACORA.md`) and git replace `project/skill_execution_log.csv` and
`project/project_log.md`. When a skill asks for the execution log, record the
skill used and its outputs in the logbook entry of that step.

## Eight phases

| Phase | Stages | Main skills | The author decides at the gate |
|---|---|---|---|
| 0 Setup | 0 | this skill | Question v0, sources with rights, repository ready |
| 1 Question and literature | 1–2 | `literature-review`, `wiki-consult`, `knowledge-ingestion` | Question v1; reconstructed debates with a serious rival |
| 2 Sources and hypotheses | 3–5 | `research-historical-source-criticism`, `data-exploration`, `research-historical-measurement`, `research-hypothesis-generation`, `research-hypothesis-refinement` | What the sources can support; hypotheses with rivals |
| 3 Strategy and design | 6–7 | `research-strategy-choice`, `research-causal-identification`, `research-structural-analysis-design`, `research-mechanism-mapping` | Route; design and measurement |
| 4 Data | 8–10 | `research-evidence-discovery-and-acquisition`, `data-preparation`, `research-reproducibility-and-replication` | Data rebuilt from raw; feasibility confirmed |
| 5 Analysis and interpretation | 11–12 | `implementation-*`, `research-mechanism-mapping`, `research-claim-evidence-mapping`, `writing-paper-draft` (develop_argument) | Results; claim–evidence map; argument architecture |
| 6 Drafting and internal review | 13–15 | `writing-paper-draft`, `alex-urrego-style`, `scientific-writing`, `review-reviewer-core` + specialists | Revised draft after an internal referee report |
| 7 Submission and resubmission | 16–19 | `submission-journal-fit`, `submission-pre-submission-audit`, `writing-title-abstract-keywords`, `submission-cover-letter`, `revision-response-to-reviewers` | Journal; go/no-go; response to reviewers |

Activate only the skills the current inputs and risks require, never a whole row
at once. `research-reproducibility-and-replication` runs across phases 0, 4, 5 and 7.

## Routes

Choose the route at phase 3 with `research-strategy-choice`; it may be provisional earlier.

- **Causal**: a treatment or shock, an outcome, unit and timing, identifying
  variation and a historically plausible mechanism.
- **Historical-structural**: the paper explains a process or transformation —
  structural change, agrarian or metabolic transitions, commodity frontiers,
  institutional change, unequal ecological exchange.
- **Hybrid**: a structural explanation with bounded causal tests that carry no
  more weight than their evidence.

Do not force identification onto a structural question, nor treat the
structural route as narrative. Require route-specific outputs, not the union of all routes.

## Modes

### New project (commit 0)

One paper = one repository in `C:\lab\<project>`, private on GitHub from day one,
never inside OneDrive. Propose this skeleton and adapt it to the sources:

```
README.md                 English: question, structure, how to rebuild
BITACORA.md               Spanish: Estado, Para retomar, Registro
planificacion/README.md   brief index (ID, brief, status, next action)
planificacion/promts/     briefs: CASE-NNN_description.md
project/project_profile.yaml   from shared/project_profile_template.yaml
data/raw/                 immutable; third-party or heavy data outside git
data/source_inventory.csv source, sha256, bytes, rights, attribution
scripts/                  numbered: 01_..., one job each
.gitignore
```

Add further folders when a phase needs them, not before. `BITACORA.md` opens with
a state table (topic, state, next step), a «Para retomar» list and an append-only
register of dated entries: who decided, who acted, what changed, which commit.

Gate 0 passes when question v0 is written, the source inventory records rights,
and the repository is pushed. Commit, tag `fase-0`.

### Diagnose and next step

1. Read `BITACORA.md`, the brief index, `git log --oneline -15`, `git status`
   and `git tag`.
2. The current phase is the first one whose gate has no recorded pass in the
   logbook. Do not infer it from filenames, and check that later files were not
   built on a superseded question, design or analysis.
3. State the route (or that it is not yet chosen), the main uncertainty and the
   next missing output.
4. Propose one to five concrete next actions with the skill for each.

### Gate

Each gate returns `pass`, `conditional pass` (named fixes, owner and check),
`fail` (return to the phase that owns the decision) or `not assessed` (never a
pass). The agent prepares the evidence; the author decides. Record the decision
in the logbook, commit and tag `fase-N` (`fase-N-v2` after a reopening). Detailed
criteria per stage are in `shared/stage_gates.md`; apply them in proportion to
what the paper claims.

### Recovery

| Failure | Return to |
|---|---|
| Missing or unverified evidence | 4 (acquisition) |
| Invalid construction, linkage or harmonization | 4 (preparation) or 2 (measurement) |
| Changed estimand, comparison or treatment timing | 3 (causal design) |
| Changed periodization, scale, pattern or mechanism | 3 (structural design) |
| The route no longer supports the claim | 3 (strategy) |
| Parallel discussion, caveat-dominated or unsupported central bridge | 5 (interpretation) |
| Table, appendix or manuscript inconsistency | 5 (analytical outputs) before redrafting |
| Replication discrepancy | the owning phase, then repeat the replication |

## Rules by phase

- **1** — The question is written first: it is the criterion for rejecting a
  result. Literature starts from a small core (seeds, or 5–10 anchor venues plus
  one narrow topic × place × history query), is read in full, becomes a debate
  map, and only then extends from what was read: concepts as queries, references
  and citing works, a directed search for rivals. Maturation rigor goes only to
  the debates being reconstructed. Each stop opens with what is now known.
- **2** — Source criticism before measurement; every extraction has an external anchor.
- **3** — Run identification before any causal implementation skill; return to
  design when feasibility changes the estimand, comparison, periodization or scale.
- **4** — Raw is immutable; author decisions enter as CSV data; agent readings
  are stored as raw. Data must rebuild from raw plus decisions in one command.
- **5** — Map mechanisms and claims to evidence before drafting. When materially
  different contributions remain defensible, give two to four argument
  architectures and let the author choose. Do not accept narrowing that removes
  the principal historical or socioecological contribution: retrieve evidence
  first (`wiki-consult` argument_support) or ask for the exact source.
- **6** — Write the method from the record. Prose keeps the author's voice
  (`alex-urrego-style` with `scientific-writing`). Run an internal referee review
  before choosing a journal.
- **7** — Clean-state replication before submission; repeat it after any
  revision that changes data, code or numbers. Journal-family labels stay backstage.

## Output

```markdown
## Phase and route
## Last gate and result
## Next missing output
## Next actions (1–5, with skill)
## Risks
```

## Rules

- Keep route, gate and workflow labels out of the manuscript argument.
- State the strongest warranted interpretation positively; limits bound it, they
  do not become the contribution.
- Distinguish an overclaim to remove, a bridge that needs evidence, and an
  intellectual choice that belongs to the author.
- Never infer author approval from a gate result, a draft or a file.
- Prefer few high-quality outputs over many incomplete artifacts.
