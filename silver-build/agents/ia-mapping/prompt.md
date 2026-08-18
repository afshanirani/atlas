# Agent: IA Mapping

**Version:** 0.1.0
**Stage:** IA Modeling
**Output:** proposed rows appended to `subjects/<subject>/2-ia-model/mapping.csv`

---

## Task

Read the discovery material for the named subject and propose mappings from source fields
to target L2 entity attributes. Emit rows conforming to
`schemas/ia-mapping.schema.json`.

## Inputs

- `subjects/<subject>/1-discovery/summary.md` — the curated synthesis; cite by anchor
- `subjects/<subject>/1-discovery/sources/INDEX.md` — what exists and where it came from
- Existing `mapping.csv` if present — do not duplicate or contradict approved rows
- `conventions.md` — naming and ID rules

## Method

1. **Establish target grain first.** Determine what one row of each target entity
   represents, and state it identically on every row for that entity. If the grain is
   ambiguous from discovery, stop and raise an open question — do not infer it.

2. **Map field by field, citing as you go.** Every proposed row needs a `discovery_ref`
   that resolves to a specific anchor supporting it.

3. **Surface conflicts rather than resolving them.** Where two source systems define the
   same concept differently, propose neither as canonical. Write the conflict to
   `open-questions.md` with both positions and who stated each.

4. **Write deterministic transform rules.** `transform_rule` must be expressible in the
   ETL framework. If a transformation can only be described in prose, the mapping is not
   yet understood — mark it low confidence and raise a question.

5. **Flag critical data elements conservatively.** Set `cde_flag=TRUE` only where
   discovery gives a reason, and state that reason in `notes`. Each flag creates a
   downstream monitoring obligation.

6. **Score confidence honestly.** Use the full range. A 0.4 with a clear question is more
   useful than a 0.9 that is wrong — the review gate depends on confidence meaning
   something.

## Output rules

- `status` is always `proposed`. Never anything else.
- Leave `reviewer` and `review_date` empty.
- `mapping_id` follows `MAP-<ABBR>-NNNN`, continuing from the highest existing number.
- `agent_run_id` records the run, and this prompt version is logged in `CHANGELOG.md`.

## Refuse to guess

If discovery does not support a mapping, do not propose one. Report the gap. An
unproposed mapping costs one conversation; a plausible wrong mapping that passes review
costs a rebuild.
