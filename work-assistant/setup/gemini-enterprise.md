# Gemini Enterprise Setup

The connected surface. Handles anything touching work data, with permission inheritance
and an audit trail.

## Why work data belongs here

Agents reach Microsoft 365 and Google Workspace sources while honoring the user's own
permissions — an agent can't surface anything the person couldn't already open. That
property, plus centralized governance, is why the connected surface is the right home for
mail, calendar, and document work rather than a locally-wired integration.

## 1. Confirm connectors

Check which sources are enabled for your tenant, and map them to the roles in
`config.md`. Connector coverage varies by tenant and changes often — verify rather than
assume, particularly for third-party task systems, where coverage is thinner than for
mail, calendar, and documents.

For anything without a connector, the fallback order is: MCP server, then ADK custom
tool, then move that skill to the CLI surface.

## 2. Build agents in Agent Designer

Agent Designer builds agents from natural-language description or a visual flow, mixing
generative steps with deterministic nodes where business logic must be reliable. The flow
view is inspectable and testable before approval — use it. For a status or brief agent,
the deterministic parts (which sources, which window, what format) should be nodes, not
prompt instructions.

Reach for ADK instead when logic outgrows a flow, or when you want the agent versioned in
source control alongside this folder.

## 3. Load the context layer

The agent needs `context/` to be useful. Options, in order of preference:

1. Put this folder in a connected document source and reference it from the agent's
   instructions
2. Paste the relevant context into the agent's system instructions — simplest, but goes
   stale and must be re-synced manually
3. Serve it via MCP if you want a single live source shared with the CLI surface

Whichever you choose, `AGENTS.md` operating rules should end up in the agent's
instructions verbatim. They're written to be pasted.

## 4. Schedule and monitor

Agents support schedule- and event-based triggers — use these for `morning-brief`,
`status-rollup`, and `metrics-pulse`. Long-running and scheduled agents surface in the
platform's management view; check it during the first weeks, since a scheduled agent that
silently produces poor output is worse than none.

## 5. Verify guardrails

Before enabling anything that writes or sends:

- Confirm draft-only behavior for mail, chat, and shared documents
- Confirm scope boundaries from `config.md` are enforced, not merely requested
- Run each agent against a known week and check the output by hand
