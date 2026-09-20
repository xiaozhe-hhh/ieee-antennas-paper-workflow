# TAP/AWPL Figure Style Methodology

## Scope

Build separate observational profiles from 40 TAP and 40 AWPL antenna-design
papers published in 2025. Sampling is stratified by venue and, where observable,
month and antenna subtype. A title signal only establishes sampling eligibility;
it does not establish scientific relevance or quality. A human reviews the
selected set before style extraction.

## Sampling Record

The private manifest may retain local source paths during validation. Public
records contain only a relative identifier, path hash, venue, title, available
month, subtype signal, selection reason, and parse status. Licensed PDFs and
local absolute paths never enter the public skill repository.

When author metadata is available, normally select no more than two papers from
one author team. When it is absent, record that limitation instead of inferring
authors from filenames.

## Observable Fields

Record DOI or stable identity, page, figure number, caption, panel count,
apparent final width, medium, archetype, simulated/measured encoding, legend
placement, color/line/marker encoding, geometry views, colorbars, photograph
organization, and caption structure when reliably observable.

Use `not-observable` when publisher scaling, rasterization, missing metadata, or
PDF structure prevents a defensible observation. Do not report apparent PDF
font size, line width, or image resolution as the author's original source
setting.

## Evidence Classes

- `official-required`: verified against a dated official source.
- `corpus-observed`: computed from retained source locations with an effective
  sample count.
- `workflow-recommended`: justified by readability, reproducibility, or
  reviewer risk.

Official instructions outrank corpus observations. TAP and AWPL aggregates are
never pooled when doing so would hide venue differences.
