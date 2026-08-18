# Agents

The agentic half of the pipeline. Each agent proposes; no agent decides.

## Why prompts are versioned

An approved mapping row records `agent_run_id`, which must resolve to the prompt version
that produced it. Change a prompt without recording it and rows produced before and after
are no longer comparable — provenance silently breaks, and you find out during an audit
rather than during review.

So: every prompt change gets a `CHANGELOG.md` entry with a date and a new version, and
every run records the version it used.

## Structure

```
<agent>/
├── prompt.md        # the instruction — versioned
├── config.yaml      # model, parameters, schema version
└── CHANGELOG.md     # dated version history
```

## Agents

| Agent | Stage | Produces |
|---|---|---|
| `discovery-intake` | Discovery | `summary.md`, source index entries |
| `ia-mapping` | IA Modeling | proposed rows in `mapping.csv` |
| `l3-definition` | L3 Definition | asset definitions and `bindings.csv` rows |

## Adding an agent

An agent earns a folder when its output feeds a gate. Anything that doesn't produce a
reviewable artifact is a helper, not a pipeline agent — keep it out of here so the
provenance chain stays legible.
