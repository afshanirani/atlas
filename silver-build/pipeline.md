# Pipeline

The human-in-the-loop agentic workflow for building L2 connected entities and L3
analytical assets.

```
                                    ┌──► L2 Implementation ──────────┐
                                    │                                │
Discovery ──► IA Modeling ──────────┤                                ├──► L3 Refactoring ──► Validation
                                    │                                │      (to use L2)
                                    └──► L3 Definition ──► L3 Impl ──┘
```

L3 is built against pre-L2 sources in parallel with L2 construction, then refactored to
consume L2. The two branches converge at refactoring; validation covers the joined result.

**Why this matters for the repo:** the fork means every L3 asset has a *source binding*
that changes mid-lifecycle, and the join means validation has to prove the change was
non-destructive. Both are tracked explicitly — see `4-l3/bindings.csv` per subject and
`validation/`.

---

## Stage 1 — Discovery

**Goal.** Assemble the raw understanding of a subject area: source systems, existing
definitions, SME knowledge, current-state process.

**Inputs.** System documentation, data dictionaries, extracts, SME interviews, existing
reports and their definitions.

**Outputs.**
- `1-discovery/sources/` — the raw material (see `.gitignore` note on confidentiality)
- `1-discovery/sources/INDEX.md` — what was collected, from whom, when
- `1-discovery/summary.md` — the curated, citable synthesis

**Exit criteria.**
- [ ] Every source system in scope has an entry in the source index
- [ ] `summary.md` has stable anchors that mapping rows can cite
- [ ] Known conflicts in definitions are recorded, not resolved — resolution is IA's job
- [ ] SME coverage is stated, including who was *not* reached

**Gate.** Subject lead confirms coverage is sufficient to model against.

---

## Stage 2 — IA Modeling

**Goal.** Turn discovery into a reviewed, machine-consumable mapping from sources to
target entities and attributes.

**Inputs.** `1-discovery/summary.md` and indexed sources.

**Agent.** `agents/ia-mapping/` proposes mapping rows with confidence and provenance.

**Outputs.**
- `2-ia-model/mapping.csv` — the central artifact
- `2-ia-model/review.md` — the gate record
- `2-ia-model/open-questions.md` — what modeling could not resolve

**Exit criteria.**
- [ ] `mapping.csv` passes `schemas/validate`
- [ ] Every row is `approved`, `rejected`, or `deferred` — none left `proposed`
- [ ] Every approved row carries `reviewer`, `review_date`, and a resolvable
      `discovery_ref`
- [ ] Grain is stated and consistent per target entity
- [ ] Open questions are either closed or explicitly deferred with an owner

**Gate.** Named reviewer approves. Business definitions require business sign-off, not
just data review — record both in `review.md`.

---

## Stage 3a — L2 Implementation

**Goal.** Build the connected-entity layer from approved mappings.

**Inputs.** `mapping.csv` rows where `status = approved`, via `build/manifest.yaml`.

**Outputs.** `3-l2/config/` — configuration consumed by the ETL framework.

**Exit criteria.**
- [ ] Config derives from approved rows only — no hand-authored mappings outside the CSV
- [ ] Entity loads reconcile to source counts within agreed tolerance
- [ ] Declared `dq_rule` values are implemented and reporting
- [ ] CDE-flagged attributes have quality monitoring in place

**Gate.** Data engineering confirms the build is reproducible from config alone.

---

## Stage 3b — L3 Definition

**Goal.** Define the analytical assets for a use case, independent of whether L2 exists yet.

**Inputs.** Use-case requirements; discovery; available sources.

**Outputs.** `4-l3/definitions/` — view definitions with declared grain and semantics.

**Exit criteria.**
- [ ] Each asset states its grain, intended consumers, and success measure
- [ ] Each asset registered in `bindings.csv` with `source_binding: pre-l2`
- [ ] Business definitions align with the L2 targets in `mapping.csv` even where the
      asset does not yet read from L2 — divergence here becomes refactor debt

**Gate.** Use-case owner approves semantics.

---

## Stage 4 — L3 Implementation

**Goal.** Build the L3 assets against currently available sources.

**Outputs.** `4-l3/config/`; deployed views.

**Exit criteria.**
- [ ] Assets deployed and consumable
- [ ] **Pre-refactor outputs captured as fixtures** — see below

> **This is the expiring step.** The acceptance test for refactoring is output
> equivalence, which is only provable against outputs captured *before* the source
> binding changes. Capture fixtures at the end of this stage or the Validation gate
> degrades into visual inspection.

**Gate.** Fixtures captured and recorded in `validation/fixtures/<subject>/`.

---

## Stage 5 — L3 Refactoring

**Goal.** Repoint L3 assets from their original sources to L2 entities.

**Inputs.** Built L2 entities; existing L3 definitions; fixtures.

**Outputs.** Updated `4-l3/definitions/` and `4-l3/config/`; `bindings.csv` updated.

**Exit criteria.**
- [ ] Every asset in `bindings.csv` is `l2` or has a recorded reason for remaining `pre-l2`
- [ ] Semantic differences discovered during refactoring are logged — these are the real
      findings of the whole exercise
- [ ] No asset silently changed meaning; any intended change is documented as such

**Gate.** Refactor review confirms each binding change and its equivalence result.

---

## Stage 6 — Validation

**Goal.** Prove the joined result is correct and the refactor was non-destructive.

**Inputs.** Fixtures, current outputs, mapping CSV, DQ results.

**Outputs.** `validation/results/`.

**Exit criteria.**
- [ ] Equivalence diff run for every refactored asset; all differences explained
- [ ] Explained differences classified: defect fixed, defect introduced, or intended change
- [ ] DQ rules from `mapping.csv` passing at agreed thresholds
- [ ] Sign-off recorded with reviewer, date, and build manifest version

**Gate.** Subject marked complete in `_status.md`.

---

## Principles

**Approved config is the only build input.** If something is built that isn't in an
approved CSV row, the pipeline has been bypassed and provenance is broken.

**Rejected is a record, not a deletion.** Rejected and deferred rows stay in the CSV so
the same mapping isn't re-proposed next cycle.

**Agents propose; humans dispose.** No stage transition happens on agent output alone.
Every gate has a named human and a written record.

**Provenance survives the people.** Every approved row resolves to a discovery citation
and an agent run; every agent run resolves to a prompt version.
