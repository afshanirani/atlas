# L3 Assets

Analytical assets serving gold use cases. Defined and built against pre-L2 sources, then
refactored to consume L2.

## `bindings.csv` is the register

Every asset must be registered **before implementation**. An asset missing from this file
gets missed at fixture capture — and that window does not reopen.

`source_binding` tracks the join state of the pipeline:

- `pre-l2` — reads original sources
- `refactor-pending` — L2 is available, asset not yet repointed
- `l2` — reads L2 entities

## Fixture capture is time-boxed

At the end of L3 Implementation, capture each asset's output to
`validation/fixtures/<subject>/<asset_id>/pre-l2/` and set `fixture_captured=TRUE`.

The acceptance test for refactoring is output equivalence. Without pre-refactor output,
equivalence is unprovable and the Validation gate becomes visual inspection — which is
what this pipeline exists to avoid.

`fixture_captured` cannot honestly become TRUE after the binding changes.

## Semantic alignment

Define assets against the L2 target semantics in `2-ia-model/mapping.csv` even while
reading pre-L2 sources. Divergence here becomes refactor debt, and refactor debt surfaces
as a diff nobody can explain.
