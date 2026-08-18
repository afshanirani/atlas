# Systems

The tool stack, by role. `config.md` names the products; this file records how they're
actually used and what the assistant may do with each.

`last_verified: TODO`

## Template

```
## <System>

- **Role:** mail | calendar | chat | tasks | ticketing | docs | analytics | design | data
- **Used for:** what actually lives here, specifically
- **Access:** read | read-write | none | via connector | via API
- **Assistant may:** read | draft | write with approval | never touch
- **Conventions:** naming, structure, where things belong
- **last_verified:** YYYY-MM-DD
```

## Notes

- **"Assistant may" is a guardrail, not documentation.** Set it deliberately per system.
  Default to draft-only for anything other people read.
- **Note where the same information lives in two places** and which one is authoritative.
  Duplicate sources of truth are where assistants produce confidently wrong answers.
- Record the *conventions*, not just the tool. Knowing specs live in a docs system is
  useless without knowing how they're named and where they belong.
