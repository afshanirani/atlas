# silver-build

A human-in-the-loop agentic pipeline for building the **L2 connected-entity layer** and
**L3 analytical assets** for the global clinical supply operations domain.

Agents propose. Humans approve. Only approved, schema-validated configuration reaches the
ETL.

---

## The workflow

```
                                    ┌──► L2 Implementation ──────────┐
                                    │                                │
Discovery ──► IA Modeling ──────────┤                                ├──► L3 Refactoring ──► Validation
                                    │                                │      (to use L2)
                                    └──► L3 Definition ──► L3 Impl ──┘
```

L3 is built against existing sources in parallel with L2 construction, then repointed at
L2. See `pipeline.md` for per-stage entry and exit criteria.

## The central artifact

`subjects/<subject>/2-ia-model/mapping.csv` is three things at once, which is what makes
the review gate work:

| Group | Columns | Purpose |
|---|---|---|
| **Build** | target entity/attribute/grain, source system/object/field, join key, transform rule, CDE flag, DQ rule | Machine-consumable config |
| **Review** | status, reviewer, review date, notes | The human gate |
| **Provenance** | discovery ref, agent confidence, agent run ID | Traceability back to evidence and prompt version |

Three rules follow:

- The ETL consumes **only `status = approved`** rows — filtered at build, not by deleting
- **Rejected and deferred rows stay in the file**, with reasons, so the same mapping isn't
  re-proposed next cycle
- **One CSV per subject**, never consolidated — review scope, merge conflicts, and blast
  radius all point the same way

CSV because reviewers open it in a spreadsheet. That is the point. It is validated
against a JSON schema in CI, and there is deliberately no parallel YAML copy to drift
against.

## Repository layout

```
silver-build/
├── pipeline.md            # stages, gates, exit criteria
├── conventions.md         # IDs, status vocabularies, naming, editing rules
├── AGENTS.md              # agent operating context
├── schemas/               # CSV contracts + stdlib validator
├── agents/                # versioned prompts and configs, with changelogs
├── subjects/              # one directory per subject area, stage-numbered inside
│   └── _template/         # copy this to start a subject
├── build/manifest.yaml    # what the ETL consumes — pinned, promotable
└── validation/            # equivalence fixtures and results
```

## Getting started

```bash
cp -R subjects/_template subjects/<subject-name>
```

Fill in `_status.md`, then work the stages in `pipeline.md`. Validate before every gate:

```bash
python3 schemas/validate/validate_mappings.py <subject-name>
```

## Two things that are easy to get wrong

**Fixture capture is time-boxed.** The acceptance test for refactoring is output
equivalence against pre-refactor output. That output can only be captured at the end of
L3 Implementation, before the binding changes. Miss it and Validation degrades into
visual inspection — the outcome the whole design exists to prevent.

**Prompt versions are part of provenance.** An approved row's `agent_run_id` must resolve
to a prompt version in `agents/*/CHANGELOG.md`. Changing a prompt without recording it
silently breaks comparability between rows produced before and after.

## Handing this to engineering

The contract is narrow and deliberate:

1. Read `build/manifest.yaml`
2. Resolve each subject's `mapping.csv` at the pinned commit
3. Filter to `status = approved`
4. Generate ETL configuration

Nothing under `3-l2/config/` or `4-l3/config/` should be hand-authored. If it is, the
provenance chain is broken and none of this repo's guarantees hold.

`schemas/validate/validate_mappings.py` is stdlib-only and intended as a required CI
check. The model IDs in `agents/*/config.yaml` are marked TODO — set them to whichever
models are sanctioned on the work platform.
