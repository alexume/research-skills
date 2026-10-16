# research-skills

The skills system and global instructions shared by every agent tool the author
uses (Claude Code, Codex, Cline). Everything needed to install, use, maintain and
continue migrating the system is in this repository.

## Where it lives

| Path | What it is |
|---|---|
| `~/.codex/skills` | The core: this repository (private remote `alexume/research-skills`) |
| `~/.claude/skills` | Junction to the core, for Claude Code |
| `~/.agents/skills` | Junction to the core, for Cline |
| `~/.claude/CLAUDE.md` | One line importing `GLOBAL_INSTRUCTIONS.md` |
| `~/.codex/AGENTS.md` | Generated copy of `GLOBAL_INSTRUCTIONS.md`, for Codex |
| `~/Documents/Cline/Rules/global_instructions.md` | Generated copy, for Cline |

Editing through any of the three skill paths edits the same files. Commit and
push from `~/.codex/skills`.

## Contents

- `GLOBAL_INSTRUCTIONS.md` — rules for every session: author control, git, data
  and pipeline, verification, briefs, the path from question to paper, language.
- `SKILLS_INDEX.md` — which skill to use for which task.
- `orchestration-research-workflow/` — a paper in eight phases closed by author
  gates; start a new project here (commit 0).
- `shared/` — stages, gates, contracts, R code style and examples, project profile template.
- `SYSTEM_CHANGELOG.md` — dated changes to the system. `ARCHITECTURE_REPORT.md` —
  architecture as of July 2026.
- `setup.ps1` — junctions, CLAUDE.md import and the copies for Codex and Cline.

Not versioned (see `.gitignore`): tool-managed folders (`.system/` by Codex,
`synced/` by the Claude app, `.cache/`, `.vscode/`) and an old backup.

## Install on a new machine

1. Close Claude Code, Codex and Cline.
2. If old links to OneDrive exist, remove the links only (not their content):
   `cmd /c rmdir "%USERPROFILE%\.codex\skills"`, and the same for
   `.claude\skills` and `.agents\skills`.
3. `git clone https://github.com/alexume/research-skills.git "%USERPROFILE%\.codex\skills"`
4. `powershell -ExecutionPolicy Bypass -File "%USERPROFILE%\.codex\skills\setup.ps1"`
5. Restart the tools; each should list the skills and quote `GLOBAL_INSTRUCTIONS.md`.

## Daily use

- Edit a skill → commit and push.
- Edit `GLOBAL_INSTRUCTIONS.md` → run `setup.ps1` (Codex and Cline read copies),
  then commit and push.
- `git pull` before working only if the system changed elsewhere (another
  machine, or the GitHub web editor).
- Record material changes in `SYSTEM_CHANGELOG.md`.

## Pending

1. **Second computer.** It still reads the frozen OneDrive copy
   (`AlexF/SKILLS_IA/codex/skills`). Migrate it with the steps above. When no
   machine uses the OneDrive copy, archive or delete `AlexF/SKILLS_IA`
   (including the obsolete `bootstrap_symlinks.ps1` and `agent/skills`).
2. **Research projects in OneDrive.** Migrate one at a time:
   - Start with a read-only inventory of `AlexF/Proyectos`: size, git status,
     raw data versus code and documents, third-party data and rights.
   - For each project: a repository in `C:\lab\<project>`, private on GitHub;
     heavy or third-party data outside git, with a manifest and sha256; set it up
     with the new-project mode of `orchestration-research-workflow` and record
     the migration as its first logbook entry.
   - `shared/local_config.yaml` still points the KnowledgeWiki to OneDrive
     (`AlexF/Bibliografía/KnowledgeWiki`); update it when the wiki moves.
3. **Stray copies to delete when convenient**: `~/.agents/Cuxlsjvs`,
   `~/.codex/skills_guardar`, `~/.claude/skills_guardar`.
