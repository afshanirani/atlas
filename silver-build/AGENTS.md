# Agent Context — silver-build

A human-in-the-loop pipeline for building L2 connected entities and L3 analytical assets
for the global clinical supply operations domain.

Read `pipeline.md` before doing anything. Read `conventions.md` before writing anything.

## Non-negotiables

**You propose. Humans dispose.** Never change a `status` from `proposed`. Never mark
something approved. Never advance a subject's stage in `_status.md`. Those are gate
actions and belong to a named human.

**Approved config is the only build input.** Never write ETL configuration that is not
derived from `approved` rows in a validated `mapping.csv`. If a mapping is needed that
does not exist, propose a row — do not shortcut into the config.

**Every proposed row carries provenance.** `discovery_ref` must resolve to a real anchor
in that subject's discovery material, and `agent_run_id` must be recorded. A row you
cannot cite is a row you should not propose — say so instead.

**Confidence is honest.** `agent_confidence` reflects genuine uncertainty. A low-confidence
proposal with a clear open question is more useful than a confident guess; the review gate
exists to catch exactly this, and inflated confidence defeats it.

**Never delete rows.** Reject or defer with a reason in `notes`.

**Validate before claiming done.** Run
`python3 schemas/validate/validate_mappings.py <subject>` and report the actual result.

## Domain cautions

- Definitional conflicts between source systems are the substance of this work, not
  noise. When discovery shows two systems disagree on what an entity *is*, surface the
  conflict as an open question — do not resolve it by picking one.
- Grain errors are the most expensive mistake available here. If the grain of a source is
  unclear, that is an open question, not something to infer.
- Anything flagged as a critical data element carries downstream quality obligations.
  Flag conservatively and say why.

## Working rules

- Cite discovery, don't paraphrase it from memory
- State what you could not determine — gaps are useful output
- Keep proposals reviewable: a reviewer should be able to check a row against its
  citation in under a minute
