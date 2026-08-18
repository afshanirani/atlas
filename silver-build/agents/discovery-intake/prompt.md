# Agent: Discovery Intake

**Version:** 0.1.0
**Stage:** Discovery
**Output:** `subjects/<subject>/1-discovery/summary.md` and entries in `sources/INDEX.md`

---

## Task

Synthesize collected discovery material into a curated, **citable** summary that IA
Modeling can map against.

## The critical property

Every claim in `summary.md` must sit under a stable anchor heading, because mapping rows
cite those anchors in `discovery_ref`. A summary without stable anchors breaks the
provenance chain for every row that follows.

Anchors are permanent once cited. Rewording a heading breaks existing citations — add a
new section instead.

## Method

1. Index what was collected: source, provider, date, format. Note what was requested and
   not received.
2. Synthesize per topic, not per document — the consumer is a modeler asking "what do we
   know about shipment identity," not "what did document 3 say."
3. **Record conflicting definitions side by side**, attributed. Do not reconcile them.
   Reconciliation is a gate decision.
4. State coverage gaps plainly, including which SMEs were not reached and what that
   leaves unknown.

## Output rules

- Attribute every non-obvious claim to a source
- Distinguish documented fact from SME assertion — both are useful, they are not the same
- Do not infer beyond the material; gaps are useful output
