# Agent: L3 Definition

**Version:** 0.1.0
**Stage:** L3 Definition
**Output:** definitions under `4-l3/definitions/` and rows in `4-l3/bindings.csv`

---

## Task

Define the analytical assets serving a use case, and register each in `bindings.csv`.

## The binding problem

L3 assets are defined and built **before L2 exists**, then refactored to consume it. So
every asset starts at `source_binding: pre-l2` and must later move to `l2`.

Two consequences you are responsible for:

1. **Align semantics with the L2 targets now**, even though the asset does not yet read
   from L2. Check `2-ia-model/mapping.csv` for the target entity and attribute definitions
   and match them. Divergence here becomes refactor debt, and refactor debt surfaces as
   an unexplainable diff at Validation.

2. **Every asset must be registered before implementation** so that fixture capture is
   tracked. An asset absent from `bindings.csv` will be missed at fixture capture, and
   that window does not reopen.

## Method

1. State grain explicitly per asset, and check it against the L2 grain it will eventually
   read from. A mismatch is a finding — raise it.
2. Name the consumers and the success measure. An asset with neither is not yet specified.
3. Record current source objects, since these are what the refactor will replace.
4. Set `fixture_captured=FALSE` at definition; only implementation sets it TRUE.

## Output rules

- `source_binding` is `pre-l2` at definition unless L2 already exists for that entity
- `status` is `defined`; never set `implemented` or beyond
- Flag any semantic divergence from the L2 mapping rather than quietly accommodating it
