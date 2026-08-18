# Schemas

Contracts that make the CSVs safe to build from. A CSV that has not passed validation
must not reach the ETL.

## Files

- `ia-mapping.schema.json` — the source-to-L2 mapping produced at IA Modeling
- `l3-definition.schema.json` — the L3 asset register, including source binding
- `validate/` — a stdlib-only validator; wire it into CI

## Why CSV

Reviewers open these in a spreadsheet. That is the point — the review gate fails if the
artifact is only readable by engineers.

**Do not maintain a parallel YAML or JSON copy for the ETL.** Two representations drift,
and then there are two answers to what the mapping is. One file, validated on commit,
consumed directly by the build.

## Changing a schema

Adding an optional column is safe. Adding a required column, or narrowing an enum,
invalidates existing rows — so:

1. Add the column as optional and backfill
2. Re-run validation across all subjects
3. Only then make it required

Record the change and its date at the top of this file, since mapping rows produced under
an earlier schema are not directly comparable to later ones.
