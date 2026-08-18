# Validation

Proves the joined pipeline is correct and that refactoring L3 onto L2 was
non-destructive.

## Fixtures

`fixtures/<subject>/<asset_id>/pre-l2/` — output captured **before** the source binding
changed.

This is the expiring artifact of the whole pipeline. Captured at the end of L3
Implementation; impossible to obtain afterward. An asset without a fixture cannot be
proven equivalent, only inspected.

Large payloads are untracked by default — see `.gitignore`. Track a manifest (row counts,
column checksums, capture date) even where the data itself lives elsewhere.

## Equivalence

For each refactored asset, diff current output against its fixture. Every difference gets
classified — an unexplained difference is a blocking finding:

| Classification | Meaning | Action |
|---|---|---|
| Intended change | Refactor deliberately changed semantics | Document in `bindings.csv` notes and the review record |
| Defect fixed | Pre-L2 output was wrong; L2 is right | Record — this is a benefit worth reporting |
| Defect introduced | L2 path is wrong | Blocks the gate |
| Unexplained | Not yet understood | Blocks the gate |

The third and fourth categories are the reason the fixture exists.

## Results

`results/` holds run outputs and is regenerated — untracked. Record the *conclusions* in
the subject's `_status.md` gate row and in the review record, not only in a results file.

## Data quality

`dq_rule` values declared in `mapping.csv` must be implemented and passing at agreed
thresholds before the Validation gate. CDE-flagged attributes carry monitoring
obligations beyond the gate.
