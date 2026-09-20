# Research Paper Workflow

An evidence-grounded Codex skill for coordinating a research paper from problem framing and literature discovery through manuscript production, review, and presentation.

This repository contains the orchestration layer. It routes work to specialized skills while preserving claim-to-source traceability, explicit evidence gaps, and resumable stage checkpoints. It does not bundle third-party skills, journal templates, papers, or user research data.

## What It Does

The workflow covers eleven stages:

1. Problem framing
2. Literature discovery
3. Deep reading
4. Research idea development
5. Evidence planning
6. Manuscript writing
7. Scientific figures
8. LaTeX production
9. Technical and citation review
10. Natural-language polishing after technical freeze
11. Presentation and archive preparation

The skill resumes from the latest valid artifact instead of restarting the entire workflow. At each stage it records inputs, outputs, evidence gaps, author checks, and the next stage.

## Core Principles

- Never invent sources, data, dimensions, equations, experimental conditions, novelty, or results.
- Keep simulation, measurement, calculation, and literature evidence distinct.
- Map consequential claims to sources and evidence status before drafting.
- Mark missing facts as `[TO BE PROVIDED]`.
- Treat research ideas and expected outcomes as proposals until supported by results.
- Freeze technical content before style polishing, then verify that facts did not change.
- Request author materials incrementally instead of demanding every possible file at once.

## Installation

### Windows PowerShell

Run from the parent directory of this repository:

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
New-Item -ItemType Directory -Force (Join-Path $codexRoot 'skills') | Out-Null
Copy-Item -Recurse -Force '.\research-paper-workflow' (Join-Path $codexRoot 'skills')
```

### Linux or macOS

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R research-paper-workflow "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Restart Codex or open a new session after installation so skill discovery refreshes.

## Usage

Invoke the skill explicitly:

```text
Use $research-paper-workflow to identify the current stage of my paper and continue from the latest valid artifact.
```

Typical requests include:

```text
Use $research-paper-workflow to build a literature matrix from these papers.
```

```text
Use $research-paper-workflow to audit the evidence needed for each manuscript claim.
```

```text
Use $research-paper-workflow to process these reviewer comments one at a time.
```

English is the default manuscript language. Planning notes and author communication may use another language.

## Author Material Intake

When evidence must come from the author, the skill asks for one small package tied to the next blocked claim. It separates:

- material required now;
- material that would improve the work;
- material required before submission.

The full staged guide is in [references/author-material-guide.md](references/author-material-guide.md). It includes general research materials and a dedicated IEEE antenna/SAR checklist for simulation settings, multiport excitation, measurement conditions, phantom properties, normalization, and raw data.

## Optional Specialist Skills

This skill can route to independently installed specialists, including:

- `research-paper-writing`
- `nature-academic-search` and `nature-literature-pipeline`
- `nature-paper-card` and `nature-reader`
- `ieee-antennas-reader` and `ieee-antennas-writing`
- `nature-figure` and `scibox-diagram`
- `nature-reviewer` and `nature-ref-verifier`
- `humanizer`
- presentation or PowerPoint tooling

Missing specialists do not invalidate the workflow. The fallback behavior and required artifact remain defined in [references/skill-routing.md](references/skill-routing.md).

## Repository Structure

```text
research-paper-workflow/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
`-- references/
    |-- artifact-contracts.md
    |-- author-material-guide.md
    |-- quality-gates.md
    |-- skill-routing.md
    |-- skill-sources.md
    `-- workflow-sop.md
```

## Evidence and Quality Gates

The workflow blocks submission when citations or quantitative claims are unverified, figures cannot be traced to source data, LaTeX has unresolved references or missing assets, or style polishing changes technical meaning.

See:

- [Workflow SOP](references/workflow-sop.md)
- [Artifact contracts](references/artifact-contracts.md)
- [Quality gates](references/quality-gates.md)
- [Skill routing](references/skill-routing.md)

## Privacy and Repository Scope

Do not commit unpublished manuscripts, reviewer correspondence, licensed PDFs, private datasets, credentials, local absolute paths, or publisher templates unless redistribution is explicitly permitted. Keep project evidence outside this skill repository.

## License

No license has been selected yet. Add a `LICENSE` file before encouraging third-party redistribution or modification.
