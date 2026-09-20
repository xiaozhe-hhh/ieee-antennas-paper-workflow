# IEEE Antenna Figure Workflow

Use this workflow for the `scientific-figures` stage of a TAP or AWPL antenna
paper. The figure must communicate one evidence-bounded conclusion and remain
traceable to raw data, author-supplied media, a simulation export, or a verified
source.

## 1. Resolve the Figure Contract

Create or update a Figure Brief before drawing. Resolve:

- target venue: `tap` or `awpl`;
- primary conclusion and figure archetype;
- evidence source, source location, and raw data or media provenance;
- final physical width and intended manuscript position;
- panels and their distinct inferential roles;
- editable source and required export formats;
- antenna-specific conditions and simulated/measured status;
- evidence gaps and author checks.

For another IEEE venue, verify its current official instructions. Do not inherit
TAP or AWPL limits by analogy.

## 2. Validate Evidence Before Styling

Retain units, frequencies, ports, coordinate conventions, bandwidth criteria,
normalization, and simulation/measurement labels where applicable. For active
or multiport results, retain power definition, amplitude/phase vector, and
inactive-port terminations.

SAR evidence also requires the human or phantom model, tissue properties,
spacing and orientation, averaging mass, excitation, power normalization,
mesh/solver conditions, and color scale as applicable. A free-space current or
field map cannot prove SAR compliance or an exact multiport phase relationship.
Block those claims until the required evidence exists.

## 3. Select the Tool Route

- Use Python/Matplotlib for reproducible data plots and figure assembly.
- Use draw.io for editable geometry, setup, and mechanism schematics.
- Prefer CSV from Origin when a plot must be redrawn. PDF, EPS, or SVG exports
  may be audited and assembled when accompanied by provenance.
- An `.opju` file alone is not a reproducible delivery package. Request raw data
  and a vector export; do not claim access to unsupported Origin internals.
- A screenshot is review material, not raw data. Do not infer exact values from
  pixels unless the output is explicitly labelled approximate digitization.

Use `nature-figure` for general figure composition and rendered QA when
available. Its general style rules do not override this workflow's IEEE antenna
semantics or venue source precedence.

## 4. Apply Source-Labelled Style Rules

Apply rules in this order:

1. `official-required`: dated IEEE or venue instructions;
2. `corpus-observed`: reproducible observations with effective sample counts;
3. `workflow-recommended`: readability and reproducibility recommendations.

Never restate a corpus habit as an official requirement. TAP and AWPL profiles
remain separate.

## 5. Export and Inspect

Prefer PDF/SVG for plots and diagrams. Use high-resolution raster output for
photographs and field maps when vector output is inappropriate. Inspect every
panel and the full composition at final physical width. Check legibility,
collisions, panel alignment, grayscale and color-vision distinguishability,
units, labels, and consistency with the Figure Brief and caption.

## 6. Delivery Package

Return:

- Figure Brief;
- raw-data/media mapping;
- editable source or plotting script;
- final PDF or SVG, or an appropriate raster master;
- preview PNG;
- English caption draft;
- semantic and rendered QA report;
- checkpoint update with evidence gaps and author checks.

Request one smallest next author evidence package when inputs are incomplete.
Continue source-grounded panels where possible; block only unsupported claims.
