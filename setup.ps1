# Sets up the skills system on this machine. Run once after cloning, and again
# after every edit of GLOBAL_INSTRUCTIONS.md:
#   git clone https://github.com/alexume/research-skills.git "$env:USERPROFILE\.codex\skills"
#   powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.codex\skills\setup.ps1"
#
# The core lives in ~/.codex/skills. Claude Code and Cline reach it through
# junctions; the global instructions reach each tool as follows:
#   Claude Code: ~/.claude/CLAUDE.md imports GLOBAL_INSTRUCTIONS.md
#   Codex, Cline: generated copies (file symlinks need administrator rights)

$ErrorActionPreference = "Stop"
$core = $PSScriptRoot
$home_ = $env:USERPROFILE
$expected = Join-Path $home_ ".codex\skills"
if ($core -ne $expected) { Write-Warning "Core is at $core, expected $expected" }

# Junctions to the core
foreach ($link in @("$home_\.claude\skills", "$home_\.agents\skills")) {
  $item = Get-Item -LiteralPath $link -Force -ErrorAction SilentlyContinue
  if ($item -and -not $item.LinkType) {
    Write-Warning "$link is a real folder, not a link: move it by hand"
    continue
  }
  if ($item) { cmd /c rmdir "$link" }
  New-Item -ItemType Directory -Force -Path (Split-Path $link) | Out-Null
  cmd /c mklink /J "$link" "$core" | Out-Null
  "junction: $link -> $core"
}

# Global instructions
$source = Join-Path $core "GLOBAL_INSTRUCTIONS.md"
$claude = "$home_\.claude\CLAUDE.md"
$import = "@~/.claude/skills/GLOBAL_INSTRUCTIONS.md"
if (-not (Test-Path $claude)) {
  [System.IO.File]::WriteAllText($claude, "$import`n")
  "written: $claude"
} elseif (-not (Select-String -LiteralPath $claude -SimpleMatch $import -Quiet)) {
  Write-Warning "$claude exists without the import line: add $import"
}

$header = "<!-- Generated copy of skills/GLOBAL_INSTRUCTIONS.md by setup.ps1. Do not edit here. -->`r`n`r`n"
$text = $header + [System.IO.File]::ReadAllText($source)
foreach ($target in @("$home_\.codex\AGENTS.md", "$home_\Documents\Cline\Rules\global_instructions.md")) {
  New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
  [System.IO.File]::WriteAllText($target, $text, (New-Object System.Text.UTF8Encoding $false))
  "copied: $target"
}

# Check
$n = (Get-ChildItem -LiteralPath $core -Directory |
      Where-Object { Test-Path (Join-Path $_.FullName "SKILL.md") }).Count
"$n skills in $core. Restart Claude Code, Codex and Cline to rescan."
