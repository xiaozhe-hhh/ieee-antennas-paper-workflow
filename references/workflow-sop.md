# End-to-End Research Paper SOP

## 1. Frame the Research Problem

Create a research brief containing the object, application, constraints,
baseline, suspected mechanism, available equipment/data, target venue, and
decision criteria. Separate known observations from assumptions and wishes.

Gate: the problem is testable and the intended contribution is falsifiable.

## 2. Discover Literature

Build database queries from concepts and synonyms; search more than one source;
deduplicate by DOI/title; retain query, date, filters, and inclusion reason.
Use citation chaining for seminal work and recent competing methods.

Gate: every included record is identifiable, and the candidate set covers both
supporting and conflicting work.

## 3. Read and Synthesize

Produce source-grounded Paper Cards. Extract problem, mechanism, geometry or
dataset, conditions, methods, baselines, results, limitations, and reusable
citations. Build a literature matrix before writing narrative related work.

Gate: numerical values point to a page, figure, table, or equation in the source.

## 4. Develop Research Ideas

Derive ideas from unresolved contradictions, missing operating regimes, unfair
comparisons, unexplained mechanisms, measurement gaps, or combinations of
compatible methods. For each idea state novelty hypothesis, physical rationale,
minimum experiment, expected discriminating observation, failure mode, cost,
and closest prior art. Rank by evidence, impact, feasibility, and falsifiability.

Gate: an idea is not promoted to a contribution until results support it.

## 5. Plan Evidence

Create the claim-evidence map before drafting. For each planned claim list the
required simulation, measurement, derivation, ablation, comparison, uncertainty,
and source. Design experiments to distinguish the proposed mechanism from plausible
alternatives, not merely to produce attractive curves.

Gate: unsupported claims are narrowed, removed, or marked `[TO BE PROVIDED]`.

## 6. Write the Manuscript

Choose venue and contribution shape. For TAP/AWPL antenna papers, route to
`ieee-antennas-writing`; AWPL should center one compact contribution, while TAP
requires a fuller mechanism and validation chain. Draft from the claim-evidence
map and keep simulated, measured, calculated, and literature-derived results distinct.

Gate: each consequential sentence has evidence and each section advances the
same engineering argument.

## 7. Produce Scientific Figures

Create a figure brief before drawing. Preserve source data, units, coordinate
systems, legends, panel mappings, and editable originals. Use `nature-figure`
for data figures and `scibox-diagram` for editable mechanism or setup diagrams.

For TAP/AWPL antenna figures, follow `figure-workflow.md`: resolve the venue,
record antenna-specific evidence conditions, select the figure archetype and
tool route, and audit the exported result at final physical width. General
figure tools do not override antenna evidence requirements.

Gate: labels remain readable at final column width and captions can stand alone.

## 8. Build LaTeX

Use the current official venue template and local LaTeX. Keep bibliography and
figure assets beside the manuscript project, compile to convergence, and inspect
the rendered PDF rather than relying only on the log.

Gate: no unresolved citations/references, missing figures, clipped content, or
unreviewed overfull boxes; all `[TO BE PROVIDED]` markers are resolved before submission.

## 9. Review and Verify

Run technical reviewer simulation, claim-evidence audit, citation metadata
verification, terminology/unit checks, and venue compliance review. Record each
finding as resolved, accepted risk, or author action.

Gate: no fabricated citation, unsupported novelty claim, or hidden evidence gap.

## 10. Humanize After Technical Freeze

Save a frozen technical draft, invoke `humanizer` for sentence rhythm, clarity,
and natural academic English, then run a semantic fact diff against the frozen
version. Do not optimize for detector scores or disguise authorship.

Gate: technical meaning, qualification, citations, equations, and numbers are unchanged.

## 11. Prepare Presentation and Archive

Create a talk-specific story from the verified manuscript; do not merely paste
paper paragraphs into slides. Generate PPTX through an available presentation
skill or the optional Office PowerPoint MCP service, render every slide, inspect
for overflow and missing media, and archive the final checkpoint with sources,
data, figures, LaTeX, PDF, reviewer log, and presentation.

