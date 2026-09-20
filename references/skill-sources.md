# External Skills and Tools

Keep external projects independent and record their provenance. Pin a release or
commit before reproducible use; review upstream changes before upgrading.

| Project | Upstream/download | License | Integration policy |
|---|---|---|---|
| Research-Paper-Writing-Skills | Probable archive repository: [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) (inferred from archive name and license owner; verify when GitHub is reachable). Declared methodology source: [pengsida/learning_research](https://github.com/pengsida/learning_research). | MIT (archive copyright Master-cai, 2026) | Install the contained `research-paper-writing` skill independently; use as general writing/idea guidance. |
| humanizer | [blader/humanizer](https://github.com/blader/humanizer) | MIT | Install independently; invoke only after technical freeze and run a fact-diff audit. |
| Office-PowerPoint-MCP-Server | [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) | MIT | Optional separate MCP server for PPTX operations; do not embed the server in this skill. |
| ChatPaper | [kaixindelele/ChatPaper](https://github.com/kaixindelele/ChatPaper) | CC BY-NC-ND 4.0 | Optional external triage tool. Do not copy or adapt its code/content into this skill; verify every extracted fact in the original paper. |

## Research-Paper-Writing Installation

From the extracted `Research-Paper-Writing-Skills-main` repository root on
Linux/macOS or another POSIX shell:

```bash
mkdir -p "$CODEX_HOME/skills"
cp -R research-paper-writing "$CODEX_HOME/skills/"
```

The spelling is `$CODEX_HOME`; `CODEX\_HOME` is only a Markdown escaping form
and must not be typed into the shell. If `CODEX_HOME` is unset, Codex normally
uses `~/.codex`, so the explicit fallback is:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R research-paper-writing "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Windows PowerShell equivalent, run from the extracted repository root:

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
New-Item -ItemType Directory -Force (Join-Path $codexRoot 'skills') | Out-Null
Copy-Item -Recurse -Force '.\research-paper-writing' (Join-Path $codexRoot 'skills')
```

Restart or open a new Codex session after installation so skill discovery refreshes.
