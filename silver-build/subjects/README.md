# Subjects

One directory per subject area moving through the pipeline. The unit of work is *a
subject traversing the stages*, not *all subjects at one stage* — so stage position is
visible from the filesystem.

## Starting a subject

```bash
cp -R subjects/_template subjects/<subject-name>
```

Then fill in `_status.md` — subject abbreviation, owner, and stage. The abbreviation is
used in every ID for that subject and cannot change later.

`_template` is skipped by the validator; real subjects are not.

## Layout

```
<subject>/
├── _status.md              # stage, owner, gate history
├── 1-discovery/
│   ├── sources/INDEX.md    # what was collected, from whom, when
│   └── summary.md          # curated synthesis — mapping rows cite its anchors
├── 2-ia-model/
│   ├── mapping.csv         # the central artifact
│   ├── review.md           # the gate record
│   └── open-questions.md
├── 3-l2/config/            # ETL config, derived from approved rows only
└── 4-l3/
    ├── definitions/        # view definitions
    ├── config/
    └── bindings.csv        # asset register and source binding state
```

## Rules

- **Nothing is built from outside an approved CSV row.** Config that has no corresponding
  approved mapping means the pipeline was bypassed.
- **Discovery anchors are permanent once cited.** Rewording a heading in `summary.md`
  breaks every `discovery_ref` pointing at it.
- **`_status.md` is updated by humans at gates**, not by agents in passing.
