# IEEE Antenna Figure Workflow Design

**Date:** 2026-09-20

**Status:** Approved design pending implementation planning

## 1. Purpose

Extend the existing `ieee-antennas-paper-workflow` skill with a complete
`scientific-figures` stage for IEEE antenna papers, with first-class profiles
for IEEE TAP and IEEE AWPL.

The figure stage must support the full set of figures commonly required by an
antenna-design paper: quantitative plots, radiation patterns, SAR/current/field
maps, geometry and dimension drawings, prototype and measurement photographs,
and multi-panel assembly. It remains part of the end-to-end paper workflow and
must not become a separate skill.

## 2. Scope

### Included

- TAP and AWPL venue-specific figure profiles.
- Python/Matplotlib as the reproducible plotting and assembly backend.
- Editable draw.io sources for antenna geometry, setup, and mechanism diagrams.
- Origin compatibility through exported CSV and PDF/EPS/SVG artifacts.
- Figure planning, creation, revision, audit, export, caption drafting, and
  manuscript checkpoint integration.
- Evidence and metadata checks specialized for antennas, MIMO, and SAR.
- Style observations derived from a stratified sample of 2025 TAP/AWPL antenna
  papers.
- Reuse of `nature-figure` for general scientific-figure design and rendered QA
  where its rules do not conflict with IEEE or venue-specific requirements.

### Excluded

- A new standalone figure skill.
- Machine-learning-based style imitation or automatic visual style transfer.
- Reliable parsing or editing of Origin `.opju` internals.
- Alteration or invention of HFSS fields, SAR values, scales, geometry,
  measurement conditions, or other scientific evidence.
- Treating observed author practices as official journal requirements.
- Full coverage of propagation, scattering, or computational-electromagnetics
  figure archetypes outside antenna-design papers in the first release.

## 3. Design Principles

1. Scientific evidence controls the figure; visual styling never changes the
   underlying result.
2. Official IEEE and venue instructions outrank corpus observations and
   workflow recommendations.
3. TAP and AWPL use separate profiles. Shared defaults are allowed only where
   the evidence and output contract are genuinely common.
4. Every consequential visual element must remain traceable to raw data,
   author-supplied media, a simulation export, or a verified source.
5. Figures are assessed at final physical column width, not only in a large
   plotting window.
6. Color is preferred, but line style, marker, and luminance provide redundant
   encoding for grayscale printing and common color-vision deficiencies.
7. Vector output is preferred for plots and diagrams. Raster output is used for
   photographs and field maps where vector representation is inappropriate.

## 4. Architecture

The figure stage has four layers.

### 4.1 Evidence Layer

Before drawing, create a Figure Brief that records:

- the single primary conclusion;
- evidence type and source path;
- raw-data or media provenance;
- target venue and final physical width;
- antenna, port, frequency, unit, power, phase, termination, normalization, and
  simulated/measured status where applicable;
- intended panels and each panel's inferential role;
- missing inputs and author checks;
- required editable and final outputs.

Unsupported facts remain `[TO BE PROVIDED]`. Missing evidence conditions block
the affected claim, not unrelated figure work.

### 4.2 Venue Layer

Load either a TAP or AWPL profile. Each profile separates:

- `official-required`: a dated official instruction;
- `corpus-observed`: a reproducible observation from the sampled papers;
- `workflow-recommended`: a recommendation justified by readability,
  reproducibility, or reviewer risk.

TAP may allocate more panels to a complete mechanism and validation chain.
AWPL should use compact evidence architecture without hiding necessary
conditions or making text unreadable.

### 4.3 Figure-Type Layer

Load only the rules for the active archetype:

- S-parameters;
- efficiency and gain;
- radiation patterns;
- ECC and MIMO metrics;
- SAR, electric/magnetic fields, and surface currents;
- parametric studies;
- geometry and dimensions;
- prototype and measurement setup photographs;
- multi-panel assembly.

### 4.4 Execution and QA Layer

- Python/Matplotlib is the primary reproducible backend for data plots and
  figure assembly.
- draw.io owns editable geometry, setup, and mechanism schematics.
- Origin exports are accepted as compatibility inputs. CSV is preferred for
  redrawing; PDF/EPS/SVG can be audited and assembled. An `.opju` file alone is
  insufficient for reproducible processing.
- General rendering, alignment, collision, and export checks may call
  `nature-figure`. IEEE-specific semantic checks remain in this workflow.

## 5. Proposed Repository Structure

```text
references/
|-- figure-workflow.md
|-- figure-style-methodology.md
|-- figure-types/
|   |-- s-parameters.md
|   |-- efficiency-gain.md
|   |-- radiation-patterns.md
|   |-- ecc-mimo.md
|   |-- sar-fields-currents.md
|   |-- parametric-studies.md
|   |-- geometry-dimensions.md
|   `-- prototype-measurement.md
|-- venues/
|   |-- tap-figure-profile.md
|   `-- awpl-figure-profile.md
assets/
|-- figure-presets/
|   |-- tap.yaml
|   `-- awpl.yaml
|-- drawio/
|   `-- antenna-schematic.drawio
scripts/
|-- build_antenna_figure.py
|-- inspect_figure.py
|-- sample_figure_corpus.py
`-- extract_figure_observations.py
evals/
|-- figure-normal-cases.yaml
|-- figure-boundary-cases.yaml
`-- figure-pressure-cases.yaml
```

Implementation may consolidate files when testing shows that a proposed split
does not create a real routing or maintenance boundary. It must preserve the
four architectural layers and the source-class distinction.

## 6. Processing Flow

1. Resolve the target venue as TAP or AWPL.
2. Create or update the Figure Brief.
3. Classify the figure archetype and input type.
4. Validate evidence metadata before plotting.
5. Load the venue profile and only the relevant archetype rules.
6. Generate, revise, or assemble the figure using the selected tool route.
7. Export vector PDF/SVG and a preview PNG; export high-resolution TIFF or PNG
   only when the submission route requires raster output.
8. Run semantic, rendered, grayscale, color-vision, alignment, and export QA.
9. Inspect the complete figure and every panel at final physical size.
10. Return editable source, source-data mapping, final output, preview, QA
    report, and an English caption draft.
11. Register outputs and unresolved author actions in the paper checkpoint.

## 7. Corpus Methodology

Analyze 80 antenna-design papers published in 2025:

- 40 TAP papers;
- 40 AWPL papers.

Use stratified sampling by venue, month, antenna-design subtype, and available
figure archetypes. Include terminal/mobile antennas, arrays and MIMO, low-SAR,
multiband/broadband, reconfigurable, and millimeter-wave designs where the
corpus permits. Normally include no more than two papers from one author team.

For each paper, retain DOI or stable identity, page, figure number, and the
observation record. Extract observable properties including:

- single-column, double-column, and spanning use;
- final physical width and panel count;
- apparent typography, stroke, marker, axis, and legend practices;
- color count and redundant line/marker encodings;
- simulated/measured differentiation;
- radiation-pattern layout and normalization labels;
- geometry views, dimensions, coordinate systems, and units;
- field/current/SAR colorbars and excitation annotations;
- photograph cropping and panel organization;
- caption organization and information density;
- vector, raster, and mixed-media use.

Record the effective sample count for every aggregate observation. Mark fields
that cannot be inferred reliably from publisher PDFs as `not-observable`.
Publisher scaling must not be reported as the author's original plotting
parameter.

## 8. Figure-Type Requirements

### S-Parameters

Require identifiable ports, frequency and units, bandwidth criterion, and
simulated/measured status. Support band shading and threshold lines only when
they clarify a stated criterion. Limit crowding through grouping rather than
indistinguishable colors.

### Efficiency and Gain

Retain percent and dBi units and align reported bands with the S-parameter
evidence. Dual axes require a clear need and must not imply a false correlation.

### Radiation Patterns

Record frequency, plane, coordinate convention, co-/cross-polarization,
normalization, and simulated/measured status. Choose polar or Cartesian form
according to the comparison task, not decoration.

### ECC and MIMO Metrics

Identify the port pair and calculation or measurement source. Thresholds must
be sourced or presented as criteria, not decorative reference lines.

### SAR, Fields, and Currents

Record active ports, frequency, input or accepted power, amplitude/phase vector,
inactive-port terminations, model, spacing, averaging mass, color scale, and
normalization as applicable. A free-space current or field map cannot establish
SAR compliance or an exact multiport phase relationship.

### Parametric Studies

Identify the controlled variable, unchanged conditions, baseline, and selected
design. The figure should reveal a discriminating trend, not only a collection
of curves.

### Geometry and Dimensions

Use the minimum necessary top, side, sectional, and detail views. Preserve
coordinate system, dimensions, units, materials, feed/port locations, matching
components, and scale relationships. The editable source is mandatory.

### Prototype and Measurement Photographs

Preserve factual image content. Cropping, exposure correction, background
cleanup, labels, and assembly must not conceal connections, fixtures, spacing,
or measurement conditions. Record instrument, distance, calibration, and setup
metadata in the Figure Brief or caption when relevant.

### Multi-Panel Assembly

Use consistent panel labels, plot-area alignment, gutters, legends, colorbars,
and terminology. Panels must have distinct evidentiary roles and answer one
Results-level question.

## 9. Deliverable Contract

Each completed figure package contains:

- Figure Brief;
- editable source or plotting script;
- raw-data and media source paths with descriptions;
- final PDF or SVG where appropriate;
- preview PNG;
- required raster export where applicable;
- machine-readable or Markdown QA report;
- English caption draft;
- checkpoint entry listing evidence gaps and author checks.

## 10. Automated and Human QA

Automated checks should cover, where technically observable:

- final-size text legibility;
- collisions among axes, labels, legends, annotations, and panels;
- line, marker, and color distinguishability;
- grayscale and common color-vision-deficiency robustness;
- required units, frequencies, ports, and simulated/measured labels;
- raster resolution at target physical size;
- vector preservation in PDF/SVG;
- panel alignment and repeated gutters;
- consistency between Figure Brief, caption, and figure labels.

Automated checks do not replace visual inspection. Inspect each panel and the
complete composition at final physical size. Any `FIX BEFORE DELIVERY`, missing
scientific condition, unresolved collision, or unauditable required output
blocks delivery as submission-ready.

## 11. Validation Strategy

Use skill-development TDD:

1. Establish baseline failures with realistic requests that tempt generic
   styling, unsupported SAR annotation, screenshot-only delivery, or confusion
   between official rules and corpus observations.
2. Add contract tests for routing, source classes, required Figure Brief fields,
   venue profiles, and archetype references.
3. Add deterministic unit tests for corpus sampling, preset loading, metadata
   validation, and inspection results.
4. Test at least four real antenna figure classes end to end, including an
   S-parameter plot, radiation pattern, SAR/current/field case, and geometry or
   prototype composition.
5. Verify both TAP and AWPL profiles independently.
6. Run the existing full test suite and retain all prior passing behavior.

## 12. Implementation Sequence

1. Baseline scenarios and failing tests.
2. Figure-stage routing and Figure Brief contract.
3. Corpus sampling and observation extraction.
4. TAP and AWPL venue profiles.
5. Antenna figure-type references.
6. Python/Matplotlib presets and export interface.
7. Origin compatibility and draw.io template.
8. Automated semantic and rendered QA.
9. Real-data end-to-end validation.
10. Global skill synchronization, Chinese README update, full regression tests,
    and GitHub publication.

## 13. Acceptance Criteria

- The capability remains inside `ieee-antennas-paper-workflow` and routes
  through its `scientific-figures` stage.
- TAP and AWPL profiles can be selected independently.
- At least four real antenna figure classes can be generated or normalized from
  source materials.
- Every style statement is identified as `official-required`,
  `corpus-observed`, or `workflow-recommended`.
- Every completed figure package contains editable source, final vector or
  appropriate raster output, preview, provenance, caption draft, and QA result.
- Missing units, excitation conditions, raw data, or SAR conditions prevent an
  unsupported submission-ready claim.
- Existing tests remain green and figure-stage coverage is added.
- The global installed skill and GitHub repository are synchronized with the
  validated workspace version.
