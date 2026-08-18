# Work Assistant

A portable scaffold for a personal-assistant agent supporting a **technical product
manager**. Tracks priorities, meetings, and commitments; automates the repetitive parts
of the role.

Targets **Gemini Enterprise** (connected work data) and **Gemini CLI** (local work), but
the context layer is plain markdown and works with any agent tooling.

**Status:** template. Context files are structured but empty; skills are described but
not built.

---

## What this is

Three things:

1. **A context layer** (`context/`) — the durable facts an agent needs: products,
   initiatives, stakeholders, cadence, systems, glossary, and the templates behind
   repeating work. Without it, every session starts by re-explaining your own acronyms.

2. **A skill roster** (`INDEX.md`) — twelve automations described with purpose, trigger,
   inputs, behavior, and prerequisites. Split by surface. Deliberately
   implementation-free, so each can be built as a Gemini Enterprise agent or a Gemini CLI
   command without redesign.

3. **A rollout plan** (`setup/`) — how to stand it up, in an order that front-loads the
   part that actually matters.

## Start here

1. Fill in `config.md` — 30 minutes, and nothing works without it
2. Seed `context/` following `setup/rollout.md` — about an hour, and it is the whole game
3. Build `morning-brief` first; run it a week before adding anything else

## Design principles

**Context before automation.** A well-built skill on an empty context layer produces
confident, generic output. The reverse — good context, one crude skill — is immediately
useful.

**Every fact carries `last_verified`.** Anything over 90 days is treated as unverified.
Stale context is worse than missing context, because agents cite it with confidence.

**Unknowns stay marked.** A `TODO` is an honest answer. A guessed acronym expansion
propagates into everything downstream.

**Draft, don't send.** Creating tasks and local files is routine. Anything other people
read requires explicit approval, every time.

**Not everything is a fact.** If it wouldn't need explaining to a new colleague, it's a
task — leave it in the task system.

**Capture as a by-product.** The context layer grows from real work via
`context-capture`, never from scheduled data-entry sessions. Those don't happen twice.

## Layout

```
work-assistant/
├── AGENTS.md              # canonical agent context — the entry point
├── GEMINI.md              # pointer to AGENTS.md (Gemini CLI)
├── CLAUDE.md              # pointer to AGENTS.md (Claude)
├── config.md              # your systems, scope, conventions — fill in first
├── INDEX.md               # skill roster, split by surface
├── context/
│   ├── glossary.md        # internal shorthand
│   ├── products.md        # what's owned and why it matters
│   ├── initiatives.md     # active workstreams, blockers, decisions
│   ├── stakeholders.md    # who owns, decides, needs informing
│   ├── cadence.md         # the recurring rhythm automations key off
│   ├── systems.md         # tool stack and assistant guardrails per system
│   ├── skills.md          # capability growth
│   └── templates/
│       ├── epic-template.md
│       ├── prd-outline.md
│       └── status-update.md
└── setup/
    ├── gemini-enterprise.md
    ├── gemini-cli.md
    └── rollout.md
```

## Portability

`AGENTS.md` is the canonical context file, with thin tool-specific pointers alongside it.
Nothing in `context/` is tool-specific — only the packaging in `setup/` and the surface
split in `INDEX.md` assume Gemini. Retargeting means rewriting those two, not the folder.
