# Quality Gates

## Evidence Gate

- Every number, citation, equation, dimension, and performance comparison maps
  to user material or a checked primary source.
- Proposed research ideas and expected results are labelled as proposals.
- Missing evidence is `[TO BE PROVIDED]`; absence is never filled by inference.
- Simulation, measurement, calculation, and literature evidence remain distinct.

## Literature Gate

- DOI/title/authors/year/venue are verified against authoritative metadata.
- Secondary summaries support triage only; claims are checked in the original.
- Search logs record date, query, source, filters, and inclusion/exclusion reason.

## Writing Gate

- Claim scope matches evidence scope and limitations remain visible.
- Venue rules and the target audience determine length and structure.
- Antenna work retains frequency, bandwidth definition, polarization, geometry,
  reference plane, units, and simulated/measured status where applicable.

## Figure and LaTeX Gate

- Figure data, labels, units, captions, and panel references agree with the text.
- Editable sources and final exports are retained.
- Antenna figures retain ports, frequencies, coordinate conventions,
  normalization, and simulated/measured status where applicable.
- SAR/current/field figures retain their excitation, power, phase, termination,
  model, spacing, averaging, scale, and normalization conditions as applicable.
- Figures are rendered and inspected at their final physical column width;
  source-file zoom is not a legibility check.
- `FIX BEFORE DELIVERY` and missing scientific conditions block
  submission-ready delivery. `NOT AUDITABLE` must remain visible as a blocker
  when a required rendered check cannot run.
- LaTeX reaches a stable build; rendered pages are visually inspected.
- Unresolved references, missing assets, overflow, and placeholders block submission.

## Humanizer Fact-Safety Gate

Use `humanizer` only after the technical draft is frozen. It may improve syntax,
flow, concision, and naturalness. It must not change numbers, citations, equations,
technical meaning, certainty, novelty scope, limitations, terminology, units, or
simulated/measured labels. Compare before and after versions sentence by sentence;
restore the frozen wording whenever equivalence is uncertain.

Do not use humanizer to evade AI-detection systems or conceal provenance. The
goal is readable academic prose with intact authorship and evidence.

## Release Gate

Release only when all findings are resolved or explicitly accepted by the author,
the fact-safety audit passes, and the manuscript handoff lists no hidden blockers.

