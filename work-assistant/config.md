# Configuration

The one file to fill in first. Everything else assumes these answers.

`last_verified: TODO`

## Surfaces

| Surface | Product | Used for |
|---|---|---|
| Connected agent platform | Gemini Enterprise | Anything touching work data — mail, calendar, docs, tickets |
| Local terminal agent | Gemini CLI | Local files, personal task system, generation and scaffolding |

## Systems

Name the actual tools. Skills reference these by role, not by product, so swapping a
tool means editing this table rather than rewriting skills.

| Role | Product | Access | In scope? |
|---|---|---|---|
| Mail | TODO | TODO | |
| Calendar | TODO | TODO | |
| Chat | TODO | TODO | |
| Personal task system | TODO | TODO | Which projects/lists only: TODO |
| Ticketing / delivery | TODO | TODO | Which boards: TODO |
| Docs / knowledge base | TODO | TODO | Which spaces: TODO |
| Analytics / BI | TODO | TODO | |
| Design | TODO | TODO | |
| Data platform | TODO | TODO | |

## Scope boundaries

Be explicit. The assistant runs on a work machine; anything listed here as out of scope
must never appear in generated briefs, summaries, or plans.

- **In scope:** TODO
- **Out of scope:** TODO — e.g. personal projects in a shared task system, private lists,
  non-work mailboxes

## Working rhythm

Summarized here; detail lives in `context/cadence.md`.

- **Delivery cadence:** TODO (sprint length, planning day, review day)
- **Reporting cycle:** TODO (weekly, biweekly, monthly — and to whom)
- **Core hours / focus blocks:** TODO
- **When the morning brief should run:** TODO

## Conventions

How work is labeled and structured, so the assistant files things consistently.

- **Priority scheme:** TODO
- **Labels / tags in use and what they mean:** TODO
- **Epic → deliverable structure:** TODO
- **Naming conventions for specs, tickets, docs:** TODO
