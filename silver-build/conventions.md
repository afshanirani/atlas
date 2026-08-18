# Conventions

## Identifiers

| Thing | Format | Example |
|---|---|---|
| Subject | kebab-case directory under `subjects/` | `clinical-shipment` |
| Subject abbreviation | uppercase, used in IDs | `SHIP` |
| Mapping row | `MAP-<ABBR>-NNNN` | `MAP-SHIP-0001` |
| L3 asset | `L3-<ABBR>-NNNN` | `L3-SHIP-0001` |
| Agent run | `run-YYYY-MM-DD-<n>` | `run-2026-08-17-a` |

IDs are **stable for life**. A row that is rejected keeps its ID; the next proposal gets
a new one. Reusing IDs destroys the audit trail.

## Status vocabularies

**Subject pipeline stage** (`_status.md`)
`discovery` → `ia-modeling` → `l2-implementation` / `l3-definition` → `l3-implementation`
→ `l3-refactoring` → `validation` → `complete`

The two middle stages run in parallel; record both.

**Mapping row status** (`mapping.csv`)
`proposed` — agent output, not yet reviewed
`approved` — consumed by the build
`rejected` — will not be built; `notes` must say why
`deferred` — not now; `notes` must name the trigger for revisiting

**L3 source binding** (`bindings.csv`)
`pre-l2` — reads original sources
`refactor-pending` — L2 available, not yet repointed
`l2` — reads L2 entities

**L3 asset status**
`defined` → `implemented` → `refactored` → `validated`, plus `retired`

## Naming

- Target entities and attributes: `snake_case`
- Source objects and fields: **as they appear in the source**, not normalized — this
  file is a mapping, and normalizing the left-hand side loses the mapping
- Grain: written as a sentence, "one row per …", identical for every row of an entity

## Dates

ISO `YYYY-MM-DD` everywhere. No relative dates in any tracked file — "last sprint" is
unresolvable six months later.

## Editing rules

- **`mapping.csv` is edited through review, not in passing.** Any status change requires
  a corresponding entry in `review.md`.
- **`agent_confidence` is never edited after proposal.** It records what the agent
  claimed, not what turned out to be true.
- **Rows are never deleted.** Reject or defer instead.
- **One CSV per subject.** Never a consolidated file — review scope, merge conflicts, and
  blast radius all point the same way.
