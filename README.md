# atlas

Context, skills, and configurations to share.

Reusable scaffolds for agent-assisted work. Each folder is self-contained and can be
copied out on its own — the shared idea is that **the context layer is the valuable part**
and the automation is what you build on top of it.

---

## What's here

### [`work-assistant/`](work-assistant/) — personal assistant scaffold for a technical PM

A context layer plus a roster of automations for someone running products and a delivery
cadence. Structured but unfilled: the files define *what to record and why it matters*,
not what any particular person's work looks like.

- `config.md` — name your systems and scope boundaries; fill this in first
- `context/` — glossary, products, initiatives, stakeholders, cadence, systems, skills
- `INDEX.md` — twelve skills described with purpose, trigger, inputs, and prerequisites,
  split across a connected platform surface and a local CLI surface
- `setup/` — phased rollout that front-loads context before automation

**Start with** `setup/rollout.md`. The hour spent seeding `context/` is what separates a
useful assistant from a generically pleasant one.

### [`silver-build/`](silver-build/) — human-in-the-loop pipeline for a data foundation

An agentic workflow for building a connected-entity layer (L2) and the analytical assets
that consume it (L3). Agents propose; humans approve; only approved, schema-validated
configuration reaches the ETL.

- `pipeline.md` — six stages with entry/exit criteria and named gates
- `schemas/` — the mapping contract, plus a stdlib-only validator meant to run in CI
- `agents/` — versioned prompts with changelogs, so provenance survives prompt changes
- `subjects/_template/` — copy to start a subject through the pipeline

**Start with** `README.md` there, then copy the template.

---

## Shared conventions

Both scaffolds follow the same few rules, which are the actually portable part:

**`AGENTS.md` is canonical.** Tool-specific files (`GEMINI.md`, `CLAUDE.md`) are thin
pointers to it, so the same folder works across agent tooling without duplication.

**Context is markdown, and the filename is the identifier.** No database, no embedding
store, no entity-resolution problem. Files are diffable, reviewable, and editable by hand
in five seconds when an agent gets something wrong.

**Every durable fact carries a verification date.** Anything past its shelf life is
treated as unverified rather than true. Stale context is worse than missing context,
because agents cite it confidently.

**Unknowns stay marked.** A `TODO` is an honest answer. A guessed acronym expansion
propagates into everything downstream.

**Agents propose, humans dispose.** Drafting and local file creation are routine.
Anything other people read, and any state transition at a gate, needs a named human and a
written record.

**Capture as a by-product.** Context grows from real work, not from scheduled data-entry
sessions. Those don't happen twice.

---

## Using these

Copy the folder you need and fill in the `TODO` markers — they mark exactly the decisions
that can't be made generically. Neither scaffold assumes a particular employer, tool
vendor, or domain beyond what its own README states.
