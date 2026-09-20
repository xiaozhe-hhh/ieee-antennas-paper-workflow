# IEEE Antenna Figure Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a tested TAP/AWPL antenna-figure stage to `ieee-antennas-paper-workflow` that plans, generates, audits, and packages complete antenna-paper figures without weakening evidence traceability.

**Architecture:** Extend the existing `scientific-figures` route with four explicit layers: Figure Brief evidence contracts, separate TAP/AWPL profiles, antenna figure-type guidance, and Python/draw.io/Origin-compatible execution plus QA. Reuse `nature-figure` for general rendered checks, while retaining IEEE antenna semantic validation locally. Corpus-derived style observations are generated from a private 80-paper stratified sample and only aggregated, source-labelled observations enter the public skill repository.

**Tech Stack:** Markdown Agent Skills, YAML presets, Python 3.14, PyYAML, matplotlib, NumPy, pandas, PyMuPDF where available, pytest, draw.io XML, Git/GitHub.

**Spec:** `docs/superpowers/specs/2026-09-20-ieee-antenna-figure-workflow-design.md`

## Global Constraints

- The capability remains inside `ieee-antennas-paper-workflow`; do not create a separate skill.
- TAP and AWPL profiles remain separate.
- Python/Matplotlib is the reproducible plotting backend; draw.io owns editable schematics; Origin is an import/export compatibility route.
- Every style statement must be labelled `official-required`, `corpus-observed`, or `workflow-recommended`.
- Do not commit licensed PDFs, unpublished manuscripts, private data, local absolute paths, or publisher templates.
- Do not invent antenna dimensions, performance values, excitation conditions, SAR conditions, or measurement results.
- A free-space current or field map cannot establish SAR compliance or exact multiport phase.
- Render and inspect outputs at final physical size.
- Preserve all existing passing tests.

---

### Task 1: Establish Figure-Stage Contract Failures

**Files:**
- Modify: `../tests/test_research_workflow_contract.py`
- Create: `../tests/test_figure_workflow_contract.py`
- Create: `evals/figure-normal-cases.yaml`
- Create: `evals/figure-boundary-cases.yaml`
- Create: `evals/figure-pressure-cases.yaml`

**Interfaces:**
- Consumes: existing skill root resolution in `test_research_workflow_contract.py`.
- Produces: failing contract tests defining routes, references, presets, source classes, and evidence blockers.

- [ ] Add tests requiring `SKILL.md` and `references/skill-routing.md` to route antenna figure work through the new figure workflow.
- [ ] Add tests requiring a Figure Brief contract with venue, conclusion, evidence source, final width, archetype, output, and author-check fields.
- [ ] Add tests requiring TAP/AWPL profiles and all figure-type reference files.
- [ ] Add tests requiring all profile statements to use one of the three source classes.
- [ ] Add pressure scenarios for generic beautification without raw data, unsupported SAR annotation, `.opju`-only input, screenshot-only delivery, and an instruction to present a corpus habit as an official mandate.
- [ ] Run `C:\Python314\python.exe -m pytest tests/test_figure_workflow_contract.py -v` from the parent workspace with `.python_packages` on `PYTHONPATH`; verify failures are caused by missing figure-stage artifacts.
- [ ] Commit: `test: define IEEE antenna figure workflow contracts`.

### Task 2: Add Routing and Figure Brief Contract

**Files:**
- Modify: `SKILL.md`
- Modify: `references/skill-routing.md`
- Modify: `references/workflow-sop.md`
- Modify: `references/artifact-contracts.md`
- Modify: `references/quality-gates.md`
- Create: `references/figure-workflow.md`

**Interfaces:**
- Consumes: stage identifier `scientific-figures` and existing checkpoint contract.
- Produces: deterministic route from a figure request to venue, Figure Brief, archetype, execution route, QA, and checkpoint.

- [ ] Extend the contract tests with missing-input behavior and one-package author intake.
- [ ] Run focused tests and confirm the new assertions fail.
- [ ] Add concise routing in `SKILL.md`; place procedural detail in `references/figure-workflow.md`.
- [ ] Define the Figure Brief fields and status behavior in `artifact-contracts.md`.
- [ ] Update SOP and quality gates with final-size inspection, editable-source delivery, and antenna semantic checks.
- [ ] State that `nature-figure` provides general rendered QA and does not override IEEE evidence rules.
- [ ] Run focused contract tests and the existing workflow tests.
- [ ] Commit: `feat: route IEEE antenna figure production`.

### Task 3: Implement Corpus Inventory and Stratified Sampling

**Files:**
- Create: `scripts/sample_figure_corpus.py`
- Create: `scripts/figure_corpus.py`
- Create: `../tests/test_figure_corpus.py`
- Create: `references/figure-style-methodology.md`
- Runtime output only, not committed: `../validation/figure-corpus/figure-sample-manifest.json`

**Interfaces:**
- Consumes: PDF roots, venue, year, seed, target count, optional paper metadata.
- Produces: deterministic manifest entries with `paper_id`, venue, path hash, month stratum, subtype signals, selection reason, and status.

- [ ] Write tests for deterministic seeded sampling, TAP/AWPL quotas, duplicate suppression, maximum two papers per author team when metadata exists, and graceful missing metadata.
- [ ] Run tests and verify failure.
- [ ] Implement inventory without copying PDFs or exposing absolute paths in public outputs; private manifests may retain local source paths under `validation/`.
- [ ] Implement selection for 40 TAP and 40 AWPL antenna-design papers, stratified by month and subtype signals where available.
- [ ] Document observable fields, `not-observable`, sampling limitations, and publisher-scaling caveats.
- [ ] Run focused tests against fixtures, then create the private 80-paper manifest from the workspace corpus.
- [ ] Audit venue counts, duplicates, unreadable PDFs, and author-team concentration.
- [ ] Commit: `feat: add stratified antenna figure corpus sampling`; include only scripts, tests, and methodology.

### Task 4: Extract Source-Grounded Figure Observations

**Files:**
- Create: `scripts/extract_figure_observations.py`
- Create: `scripts/aggregate_figure_observations.py`
- Create: `../tests/test_figure_observations.py`
- Runtime output only: `../validation/figure-corpus/observations.jsonl`
- Runtime output only: `../validation/figure-corpus/aggregate.json`

**Interfaces:**
- Consumes: sample manifest and source PDFs.
- Produces: per-figure observation records and venue/archetype aggregates with effective sample counts and provenance.

- [ ] Write tests for schema validation, source location, source class, effective sample counts, `not-observable`, and refusal to infer author source font size from publisher scaling.
- [ ] Run tests and verify failure.
- [ ] Implement conservative PDF metadata/text/image inspection; keep uncertain visual attributes explicitly uncertain.
- [ ] Extract or manually verify page, figure number, caption, panel count, medium, archetype, simulated/measured labels, and observable layout/style fields.
- [ ] Aggregate TAP and AWPL independently and retain denominators for each observation.
- [ ] Perform a manual audit of at least ten papers per venue and correct extraction rules supported by observed errors.
- [ ] Do not commit copyrighted figure images or local-path manifests.
- [ ] Commit: `feat: extract source-labelled antenna figure observations`.

### Task 5: Build TAP and AWPL Figure Profiles

**Files:**
- Create: `references/venues/tap-figure-profile.md`
- Create: `references/venues/awpl-figure-profile.md`
- Create: `assets/figure-presets/tap.yaml`
- Create: `assets/figure-presets/awpl.yaml`
- Create: `scripts/load_figure_preset.py`
- Create: `../tests/test_figure_presets.py`

**Interfaces:**
- Consumes: dated official sources and corpus aggregate.
- Produces: validated venue preset dictionaries and prose profiles with source-labelled rules.

- [ ] Write tests requiring schema version, venue, physical-size modes, typography, strokes, markers, palette, export settings, and source-class metadata.
- [ ] Run tests and verify failure.
- [ ] Verify current official IEEE/TAP/AWPL figure instructions and record URL/title/access date for every official rule.
- [ ] Convert robust corpus observations into `corpus-observed` entries with sample count; do not encode weak observations as fixed defaults.
- [ ] Add workflow recommendations with rationale and final-size validation requirements.
- [ ] Implement strict YAML loading with useful field errors and no silent cross-venue fallback.
- [ ] Run focused tests and manually compare the two profiles for accidental homogenization.
- [ ] Commit: `feat: add separate TAP and AWPL figure profiles`.

### Task 6: Add Antenna Figure-Type Guidance

**Files:**
- Create: `references/figure-types/s-parameters.md`
- Create: `references/figure-types/efficiency-gain.md`
- Create: `references/figure-types/radiation-patterns.md`
- Create: `references/figure-types/ecc-mimo.md`
- Create: `references/figure-types/sar-fields-currents.md`
- Create: `references/figure-types/parametric-studies.md`
- Create: `references/figure-types/geometry-dimensions.md`
- Create: `references/figure-types/prototype-measurement.md`
- Create: `references/figure-types/multipanel-assembly.md`
- Modify: `../tests/test_figure_workflow_contract.py`

**Interfaces:**
- Consumes: Figure Brief and venue profile.
- Produces: archetype-specific required metadata, composition rules, blockers, and delivery checks.

- [ ] Extend contract tests to require each archetype's non-negotiable antenna metadata.
- [ ] Run focused tests and verify failure.
- [ ] Write concise rules for each archetype, keeping evidence conditions separate from appearance.
- [ ] Add explicit SAR and multiport blockers for power, phase, terminations, model, spacing, averaging mass, scale, and normalization.
- [ ] Add simulated/measured distinctions, coordinate conventions, units, and provenance rules where applicable.
- [ ] Add Origin route behavior and editable-source expectations to the relevant references.
- [ ] Run focused tests.
- [ ] Commit: `docs: add antenna figure archetype rules`.

### Task 7: Implement Reproducible Matplotlib Build and Export

**Files:**
- Create: `scripts/build_antenna_figure.py`
- Create: `scripts/antenna_figure_io.py`
- Create: `scripts/antenna_figure_styles.py`
- Create: `../tests/test_figure_builder.py`
- Create: `assets/examples/s_parameters.csv`
- Create: `assets/examples/radiation_pattern.csv`

**Interfaces:**
- Consumes: venue preset, Figure Brief JSON/YAML, CSV or Touchstone-derived tabular data, output directory.
- Produces: PDF, SVG, preview PNG, build manifest, and caption-data summary.

- [ ] Write failing tests for deterministic preset application, source column validation, final-size dimensions, simulated/measured encodings, and output manifest.
- [ ] Implement CSV ingestion and an adapter boundary for Touchstone conversion without hand-parsing undocumented formats.
- [ ] Implement a small set of reusable primitives rather than one hard-coded paper figure.
- [ ] Implement color-plus-line/marker redundancy and venue-specific physical dimensions.
- [ ] Export PDF/SVG and preview PNG; preserve metadata and do not rasterize plot text or lines unnecessarily.
- [ ] Generate example S-parameter and radiation-pattern outputs from synthetic, clearly labelled fixture data.
- [ ] Run focused tests and inspect example outputs at final size.
- [ ] Commit: `feat: add reproducible IEEE antenna figure builder`.

### Task 8: Add Origin and draw.io Compatibility

**Files:**
- Create: `references/origin-compatibility.md`
- Create: `assets/drawio/antenna-schematic.drawio`
- Create: `scripts/inspect_origin_export.py`
- Create: `../tests/test_origin_compatibility.py`

**Interfaces:**
- Consumes: CSV plus PDF/EPS/SVG exports, or an `.opju` accompanied by exports.
- Produces: compatibility report and normalized asset inventory; no `.opju` mutation.

- [ ] Write failing tests for accepted export sets, `.opju`-only rejection, missing source data warnings, and safe file inventory.
- [ ] Implement the compatibility inspector using structured parsers where available.
- [ ] Document what can be redrawn, audited, or assembled and what requires author action.
- [ ] Create a minimal valid draw.io antenna schematic template with editable layers for geometry, dimensions, ports, coordinates, and annotations.
- [ ] Verify the draw.io XML opens and round-trips in diagrams.net or an available renderer.
- [ ] Run focused tests.
- [ ] Commit: `feat: support Origin exports and editable antenna schematics`.

### Task 9: Implement Semantic and Rendered QA

**Files:**
- Create: `scripts/inspect_figure.py`
- Create: `scripts/figure_semantics.py`
- Create: `../tests/test_figure_inspection.py`
- Modify: `references/quality-gates.md`

**Interfaces:**
- Consumes: Figure Brief, build manifest, final PDF/SVG/PNG, venue profile.
- Produces: JSON and Markdown reports with `PASS`, `REVIEW REQUIRED`, `FIX BEFORE DELIVERY`, or `NOT AUDITABLE`.

- [ ] Write failing tests for missing units, ports, frequency, simulated/measured labels, raster DPI, vector preservation, and SAR evidence conditions.
- [ ] Add deterministic checks for expected output files, physical dimensions, text presence, required metadata, and raster resolution.
- [ ] Add grayscale and common color-vision-deficiency distinguishability checks based on the declared series encodings.
- [ ] Delegate panel alignment and PDF collision checks to `nature-figure` scripts when installed; report `NOT AUDITABLE` rather than claiming success when unavailable.
- [ ] Require human inspection at final size for scientific salience, occlusion, photograph integrity, and field-map interpretation.
- [ ] Update the quality gate with blocking statuses.
- [ ] Run focused tests.
- [ ] Commit: `feat: audit IEEE antenna figures before delivery`.

### Task 10: Validate Four Real Figure Classes End to End

**Files:**
- Create: `evals/figure-validation-report.md`
- Runtime outputs only: `../validation/figure-e2e/`
- Modify as evidence supports: figure scripts, presets, and references from Tasks 5-9.

**Interfaces:**
- Consumes: user-owned or redistributable real source materials for S parameters, radiation patterns, SAR/current/field evidence, and geometry/prototype composition.
- Produces: four figure packages and a source-grounded validation report.

- [ ] Select four safe validation cases with raw or author-owned materials; do not publish private data or figures.
- [ ] Build an S-parameter figure and complete TAP/AWPL final-size QA.
- [ ] Build a radiation-pattern figure with plane, polarization, frequency, normalization, and simulation/measurement labels.
- [ ] Audit or assemble a SAR/current/field case; verify missing conditions block unsupported claims.
- [ ] Build an editable geometry or prototype/measurement composition.
- [ ] Record defects found, repairs made, remaining limitations, environment, and exact commands in the validation report.
- [ ] Rerun focused tests after each supported repair.
- [ ] Commit: `test: validate four antenna figure workflows`; include only non-private validation documentation and safe fixtures.

### Task 11: Integrate Documentation and Release

**Files:**
- Modify: `README.md`
- Modify: `references/author-material-guide.md`
- Modify: `references/skill-routing.md`
- Modify: `agents/openai.yaml` only if discovery wording needs figure keywords
- Modify: `../tests/test_research_workflow_contract.py` if final public interfaces changed

**Interfaces:**
- Consumes: validated implementation and usage commands.
- Produces: discoverable Chinese documentation, synchronized global installation, and published GitHub revision.

- [ ] Document supported figure types, tool routes, input packages, commands, outputs, evidence boundaries, and current limitations in Chinese README sections.
- [ ] Extend author intake with per-archetype minimum material packages without duplicating the detailed references.
- [ ] Run skill validation on workspace and global copies.
- [ ] Run the complete suite with `PYTHONPATH=<workspace>\.python_packages;<workspace>` and Python 3.14.
- [ ] Run UTF-8 checks, relative-link checks, secret/local-path scans, and `git diff --check`.
- [ ] Copy the validated skill to `C:\Users\64210\.codex\skills\ieee-antennas-paper-workflow`.
- [ ] Commit: `docs: release TAP and AWPL antenna figure workflow`.
- [ ] Push all commits to `https://github.com/xiaozhe-hhh/ieee-antennas-paper-workflow` and verify local/remote hashes.

## Final Verification

- [ ] `quick_validate.py` passes for workspace and global skill copies.
- [ ] Full existing and new pytest suite passes under Python 3.14.
- [ ] TAP and AWPL presets render independently.
- [ ] Four real figure classes have completed packages and QA reports.
- [ ] Public repository contains no paper PDFs, private figures/data, local absolute paths, credentials, or unlicensed templates.
- [ ] GitHub README and repository description accurately state TAP/AWPL antenna figure support.
