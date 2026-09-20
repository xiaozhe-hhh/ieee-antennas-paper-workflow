# Artifact Contracts

Every artifact begins with its identifier, creation date, source paths, status,
and producing skill. Use Markdown or a structured equivalent that preserves
these fields.

## Research Brief

Fields: research question, object/system, application, constraints, known facts,
assumptions, candidate contribution, resources, target venue, success criteria.

## Paper Card

Fields: bibliographic identity, research problem, method/mechanism, setup and
conditions, quantitative results with source locations, limitations, relevance,
and citation status.

## Literature Matrix

One row per paper: verified identity, taxonomy, method, frequency/application
range, geometry/dataset, evidence type, baselines, key results, limitations,
and relationship to the proposed work.

## Claim-Evidence Map

One row per claim: exact claim, evidence required, supplied source/location,
evidence type, status (`solid`, `partial`, `unclear`, `missing`), allowed wording,
and author action.

## Figure Brief

Fields: identifier, target venue, primary conclusion, evidence source and
location, evidence type, raw-data or media provenance, final physical width,
figure archetype, panels and inferential roles, antenna/port/frequency/unit
metadata, power/phase/termination/normalization conditions where applicable,
simulated or measured status, axes, annotations, caption facts, editable source,
export formats, evidence gaps, author checks, and visual/semantic QA result.

Status is `complete`, `partial`, or `blocked`. A missing condition blocks only
the claim or panel that requires it; unrelated, source-grounded work may proceed.

## Manuscript Handoff

Fields: venue, manuscript version, frozen technical draft, LaTeX project path,
figure inventory, bibliography path, unresolved placeholders, author checks,
build result, reviewer findings, humanizer fact-diff result, and next stage.

## Checkpoint

```yaml
stage: deep-reading
status: partial
inputs: []
outputs: []
skills_used: []
evidence_gaps: []
author_checks: []
next_stage: idea-development
```

