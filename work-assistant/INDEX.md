# Skill Roster

Automations for a technical PM assistant, split by surface. Descriptions are
implementation-free by design — each states purpose, trigger, inputs, behavior, and
prerequisites, so it can be built as a Gemini Enterprise agent or a Gemini CLI command
without redesign.

Nothing here is implemented yet. Build in the order given in `setup/rollout.md`.

**Surface split follows data gravity:** work data stays on the connected platform with
its permission model and audit trail; local files and personal systems run on the CLI.

---

# Gemini Enterprise agents

Connected to work data. Built in Agent Designer (natural language or visual flow), or
with ADK when logic gets complex. These support scheduling and event triggers natively.

### `morning-brief`
**Purpose.** The day plan no single system can produce. A task list shows what's due; a
calendar shows what's booked. Neither shows what's at stake or what to drop.

**Trigger.** Scheduled each working morning.

**Inputs.** Calendar (today and tomorrow), open tasks and tickets, `context/` for stakes
and dependencies.

**Behavior.** Produces a short brief: today's meetings with prep flags, the two or three
things that actually matter, and an explicit split between deadline-locked and slippable
work. When the day is oversubscribed, names what to cut rather than listing everything.

**Prerequisites.** Calendar connector. Task/ticket source.

---

### `meeting-prep`
**Purpose.** Recurring meetings otherwise start from a blank page and rehash last time.

**Trigger.** Scheduled ahead of calendar events above a threshold, or on demand.

**Inputs.** Event and attendees, prior notes for the same recurring series, open items
tied to the relevant product area, stakeholder context.

**Behavior.** Drafts a prep note: unresolved items carried forward, decisions still
pending, what changed since last time, and questions to raise. For attendees, pulls what
they own and what they're waiting on.

**Prerequisites.** Calendar connector. A decided location for meeting notes.

---

### `meeting-capture`
**Purpose.** Close the loop where notes normally die.

**Trigger.** On demand after a meeting, with notes pasted or referenced.

**Inputs.** Freeform notes, meeting context, attendee list.

**Behavior.** Extracts commitments and proposes tasks with owner, due date, and correct
filing. Separates what this person owes from what others owe them. Flags decisions worth
recording and durable facts worth adding to `context/`. Everything proposed for approval.

**Prerequisites.** Task system write access. Calendar connector to link the source event.

---

### `inbox-triage`
**Purpose.** Convert inbound asks into filed work instead of carried mental load.

**Trigger.** Scheduled once or twice daily, or on demand.

**Inputs.** Mail and chat matching a defined filter.

**Behavior.** Distinguishes genuine asks from noise, drafts tasks with the right filing
and labels, and presents them as a batch to approve. Flags anything that looks
time-sensitive or is from a key stakeholder. Never files silently, never replies.

**Prerequisites.** Mail and chat connectors. A filter definition worth tuning over time.

---

### `status-rollup`
**Purpose.** Assemble recurring status and exec updates from work already tracked
elsewhere, rather than rewriting it by hand every cycle.

**Trigger.** Scheduled before each reporting cycle, or on demand.

**Inputs.** Completed and in-flight work, prior status entries, risk and blocker notes.

**Behavior.** Drafts the update in the established format: progress since last cycle,
what's at risk and why, what's next, decisions needed. Calls out anything that slipped
more than once. Always drafts — never posts without approval.

**Prerequisites.** Docs/knowledge base connector. A confirmed target format.

---

### `stakeholder-digest`
**Purpose.** Different audiences need different slices. Sending everyone the same update
is why updates get ignored.

**Trigger.** On demand, or on the reporting cycle.

**Inputs.** `context/stakeholders.md`, recent progress, open decisions.

**Behavior.** For each stakeholder or group, drafts the slice relevant to what they own
or care about, at the altitude they need. Flags who hasn't heard anything in a while and
who has an unanswered decision request outstanding.

**Prerequisites.** Populated `stakeholders.md`. Mail or chat connector for delivery —
drafts only.

---

### `metrics-pulse`
**Purpose.** Periodic check against targets, so drift is noticed before a review.

**Trigger.** Scheduled on the reporting cadence.

**Inputs.** Analytics or BI source, target definitions.

**Behavior.** Reports movement against targets, flags meaningful changes, and explicitly
distinguishes signal from normal variance. States when a change is too small or too noisy
to interpret rather than narrating it.

**Prerequisites.** Analytics connector. Documented targets — without these it produces
numbers, not insight.

---

# Gemini CLI commands

Local surface. Packaged as an extension with custom commands and `GEMINI.md` context.
Use for filesystem work and any system without a platform connector.

### `epic-scaffold`
**Purpose.** Instantiate a recurring deliverable set in one command. Most PM work has
repeating structures — a discovery set, a launch checklist, a spec package — assembled by
hand every time.

**Trigger.** `/epic-scaffold <template> <name>` plus a target date.

**Inputs.** Template from `context/templates/`, the subject name, target window.

**Behavior.** Creates the parent item and all child deliverables, applies conventions
from `config.md`, and staggers due dates across the window. Prompts for anything
subject-specific rather than inventing it. Reports what it created for review.

**Prerequisites.** Task system write access. At least one template defined.

---

### `sprint-prep`
**Purpose.** Turn grooming from a manual sweep into a reviewable proposal.

**Trigger.** `/sprint-prep`, or scheduled before planning.

**Inputs.** Open items for the area, completion history.

**Behavior.** Groups open work by epic and flags what has slipped more than once, what
has gone longest untouched, and what is blocked and on whom. Proposes a slate sized
against recent throughput. Output is a proposal — it reschedules nothing on its own.

**Prerequisites.** Task or ticket read access, including history.

---

### `weekly-review`
**Purpose.** The retrospective nothing currently produces.

**Trigger.** Scheduled weekly.

**Inputs.** Activity history, `context/`.

**Behavior.** Reports what completed, what slipped and how often, what has gone stale,
and which initiatives saw no movement at all — the last being the one most easily missed.
Prompts for decisions and learnings, and offers to write them to `context/`.

**Prerequisites.** Task history access.

---

### `context-capture`
**Purpose.** The only reliable way decisions and skills get recorded. Both exist in your
head at 5pm and are gone by Friday.

**Trigger.** `/capture`, or at session end.

**Inputs.** A short freeform answer to "what did you learn or decide?"

**Behavior.** Routes durable facts to the right file — an acronym to `glossary.md`, a
capability to `skills.md`, an ownership fact to `stakeholders.md`, a decision with its
rationale to the relevant initiative. Shows a diff before writing. Never edits silently.

**Prerequisites.** Filesystem access only.

---

### `spec-draft`
**Purpose.** Get past the blank page on specs and PRDs, where the structure is known and
only the substance is new.

**Trigger.** `/spec-draft <name>`.

**Inputs.** `context/templates/prd-outline.md`, relevant initiative and stakeholder
context, any research notes provided.

**Behavior.** Produces a structured first draft with sections stubbed and known context
filled in. Explicitly marks what it does not know rather than generating plausible
filler — open questions are the useful output of a first draft.

**Prerequisites.** Filesystem access. A spec template.

---

# Deferred

- **Anything auto-sending to people.** Draft-and-approve only, without exception.
- **Out-of-scope domains.** See `config.md`.
- **Skills without a defined success measure.** If you can't say what a good output looks
  like, the skill isn't specified yet.
