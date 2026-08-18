# Build

What the ETL actually consumes.

## Why a manifest instead of globbing

Globbing the repo means the build changes whenever anyone commits, and "what was in
build 47" becomes unanswerable. The manifest pins subjects to specific reviewed commits,
so a build is reproducible and promotable.

It also lets a subject sit in an approved-but-not-deployed state — normal, and awkward to
express any other way.

## Rules

- **Only `status = approved` rows are consumed.** Filtering happens here, not by deleting
  rows from the CSV.
- **`mapping_commit` pins to a reviewed version.** It should match a commit named in that
  subject's `review.md`.
- **Validation is a required gate.** A manifest referencing an invalid CSV does not build.
- **Never rebuild a `build_id` from a different commit.** Promote by reference; issue a
  new ID for new content.

## Handing to engineering

The contract with the ETL framework is: read `manifest.yaml`, resolve each subject's
mapping at the pinned commit, filter to approved rows, generate config. Nothing in
`3-l2/config/` should be hand-authored — if it is, provenance is broken and this repo's
guarantees no longer hold.
