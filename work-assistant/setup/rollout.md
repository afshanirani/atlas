# Rollout

Order matters here. Context before automation; one working skill before a roster.

## Phase 0 — Fill in `config.md` (30 min)

Nothing else works without it. Name the systems, set the scope boundaries, record the
conventions.

## Phase 1 — Seed the context layer (about 1 hour)

In this order — earlier files unblock later ones:

1. `glossary.md` — highest value, lowest effort. Skim two sprints of ticket titles.
2. `products.md` — what each thing is and why it matters
3. `stakeholders.md` — manager, sign-off authorities, recurring attendees
4. `cadence.md` — the rhythm automations key off
5. `initiatives.md` — the *why* and the *blocked-on*
6. `systems.md`, `skills.md` — fill opportunistically

This step determines whether the assistant is genuinely useful or generically pleasant.
It is the whole game. Don't skip ahead.

## Phase 2 — First agent: `morning-brief`

Build it on the connected surface. It's the cheapest real skill — native calendar access,
built-in scheduling, no custom integration — and the one felt daily.

**Run it for a week before building anything else.** It's also the honest test of the
context layer: if the brief reads generic, the problem is the context, not the agent.

## Phase 3 — First CLI command

Pick whichever repeating structure you assemble by hand most often, define it in
`context/templates/`, and build `epic-scaffold` for it. Immediate, measurable time back.

## Phase 4 — Expand deliberately

Add skills only when you notice yourself doing the thing manually a third time. In rough
value order: `meeting-prep`, `sprint-prep`, `status-rollup`, `weekly-review`,
`context-capture`, then the rest.

`context-capture` is worth pulling earlier than its value suggests — it's what keeps the
context layer alive, and a folder that stops being updated stops being trustworthy.

## Phase 5 — Maintenance

- **Monthly:** check `last_verified` dates; anything over 90 days gets reconfirmed or
  deleted. Deleting is fine — a smaller true file beats a larger stale one.
- **Quarterly:** review whether each skill is still used. Delete the ones that aren't.
- **On any org change:** stakeholders and cadence go stale first and fastest.

## How to know it's working

- You stop re-explaining internal shorthand to agents
- The morning brief changes what you do, rather than confirming what you knew
- New skills come from noticing repetition, not from this list
