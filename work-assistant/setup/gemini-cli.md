# Gemini CLI Setup

The local surface. Filesystem work, generation, and any system without a platform
connector.

## Why a second surface

Some work has no business going through a connected platform — drafting local files,
scaffolding, capturing notes — and some systems simply won't have connectors. The CLI
covers both, and reads this folder's context directly with no sync step.

## 1. Install and configure

Follow the enterprise deployment guidance for a managed environment; settings can be
centrally applied rather than configured per machine. Confirm with whoever administers it
which model access and tool permissions apply.

## 2. Context loading

Gemini CLI reads `GEMINI.md` from the working directory, which points at `AGENTS.md`.
Two options:

- **Run from this folder** — simplest, works immediately
- **Reference it globally** so context loads regardless of directory — preferred, since
  the assistant is useful outside this folder

## 3. Package as an extension

Extensions bundle custom commands, MCP servers, context files, and sub-agents into one
installable unit. That's the right container for this roster: everything version-controlled
together, installable on another machine in one step.

Structure:

```
extension/
├── gemini-extension.json
├── GEMINI.md              # or a pointer to this folder's AGENTS.md
└── commands/
    ├── epic-scaffold.toml
    ├── sprint-prep.toml
    ├── weekly-review.toml
    ├── capture.toml
    └── spec-draft.toml
```

Custom commands are TOML files encapsulating multi-step prompts behind a slash command.
Start with one, use it for a week, then add more — a roster of untested commands is worse
than two that work.

## 4. Connect the task system

The CLI commands need read-write access to whichever task system `config.md` names.
Either an MCP server for it, or direct API calls wrapped in a small script. Confirm this
is acceptable under your organization's tooling policy before wiring it up, particularly
if the task system is a personal account.

## 5. Scope enforcement

If the task system holds anything out of scope, enforce the filter in the command itself —
not as an instruction in a prompt. Prompt-level scoping fails quietly.
