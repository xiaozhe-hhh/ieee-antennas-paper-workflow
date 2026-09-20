---
name: research-paper-workflow
description: Use when planning or executing an end-to-end research-paper workflow, including literature discovery, paper reading, idea development, evidence planning, IEEE antenna writing, scientific figures, LaTeX production, review, natural-language polishing, or research presentations.
---

# Research Paper Workflow

Orchestrate specialized skills; do not merge or duplicate them. Determine the
current stage from the user's request and existing artifacts, invoke only the
skills needed for that stage, and preserve traceability between claims and
sources throughout the workflow.

## Stage Router

Use these stable stage identifiers in checkpoints:

1. `problem-framing`
2. `literature-discovery`
3. `deep-reading`
4. `idea-development`
5. `evidence-planning`
6. `manuscript-writing`
7. `scientific-figures`
8. `latex-production`
9. `review`
10. `humanize`
11. `presentation`

Read [references/skill-routing.md](references/skill-routing.md) to choose a
specialist. For a multi-stage request, read
[references/workflow-sop.md](references/workflow-sop.md). Read
[references/artifact-contracts.md](references/artifact-contracts.md) whenever
one stage hands work to another. Before approving any output, apply
[references/quality-gates.md](references/quality-gates.md).

When progress depends on author-supplied files, parameters, decisions, or
experimental evidence, read
[references/author-material-guide.md](references/author-material-guide.md).
Request only the smallest next evidence bundle, explain how the author should
prepare it, and distinguish material needed to start from material required
before submission.

## Operating Rules

- Start from the latest valid artifact and resume from its checkpoint. Do not
  repeat completed stages unless their inputs changed or a quality gate failed.
- For an end-to-end request, state the detected stage, next deliverable, chosen
  specialist skills, and missing inputs, then continue as far as evidence permits.
- Do not respond to incomplete materials with an undifferentiated master list.
  Inventory what is already available, identify the next blocked claim or stage,
  and issue one numbered author action package from the material guide.
- A stage may call more than one specialist only when their roles are distinct.
- Treat literature-grounded idea generation as hypothesis development, not as
  evidence. Mark proposed mechanisms, experiments, and expected outcomes as
  proposals until the user supplies or generates results.
- Never invent sources, data, dimensions, equations, measurement conditions,
  novelty, or experimental outcomes. Use `[TO BE PROVIDED]` for missing facts.
- Default manuscript language is English. Chinese may be used for planning,
  reading notes, and communication with the user.
- Freeze technical content before `humanize`. After natural-language polishing,
  compare the result with the frozen draft and restore any changed fact.
- External applications and MCP servers are optional capabilities, not embedded
  dependencies. Read [references/skill-sources.md](references/skill-sources.md)
  for installation, licenses, and provenance.

## Checkpoint Contract

At the end of each stage, record: `stage`, `status`, `inputs`, `outputs`,
`skills_used`, `evidence_gaps`, `author_checks`, and `next_stage`. Status is one
of `complete`, `partial`, or `blocked`. A later run must resume from this record.

## Completion

An end-to-end workflow is complete only when citations and quantitative claims
are verified, figures are source-grounded, LaTeX builds without unresolved
references or missing assets, reviewer findings are resolved or accepted, and
the post-humanizer fact audit passes.
