#!/usr/bin/env python3
"""Validate mapping and L3 definition CSVs against their JSON schemas.

Standard library only — no install step, so CI and laptops behave identically.

Usage:
    python schemas/validate/validate_mappings.py              # all subjects
    python schemas/validate/validate_mappings.py <subject>    # one subject

Exits non-zero if any file fails. Wire into CI as a required check.
"""

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas"
SUBJECTS = ROOT / "subjects"

TARGETS = [
    ("2-ia-model/mapping.csv", "ia-mapping.schema.json"),
    ("4-l3/bindings.csv", "l3-definition.schema.json"),
]


def load_schema(name):
    with open(SCHEMA_DIR / name) as fh:
        return json.load(fh)


def check_value(col, value, spec):
    """Return an error string, or None if the value is acceptable."""
    if value == "":
        return None  # emptiness is handled by required/requiredWhenApproved

    if "enum" in spec and value not in spec["enum"]:
        return f"{col}={value!r} not in {spec['enum']}"

    if "pattern" in spec and not re.match(spec["pattern"], value):
        return f"{col}={value!r} does not match {spec['pattern']}"

    if spec.get("type") == "number":
        try:
            num = float(value)
        except ValueError:
            return f"{col}={value!r} is not numeric"
        if "minimum" in spec and num < spec["minimum"]:
            return f"{col}={num} below minimum {spec['minimum']}"
        if "maximum" in spec and num > spec["maximum"]:
            return f"{col}={num} above maximum {spec['maximum']}"

    return None


def validate_file(path, schema):
    errors = []
    props = schema.get("properties", {})
    required = schema.get("required", [])
    req_approved = schema.get("requiredWhenApproved", [])
    unique_cols = schema.get("unique", [])
    seen = {col: {} for col in unique_cols}

    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return [f"{path}: file is empty"]

        expected = schema.get("columnOrder", list(props))
        missing_cols = [c for c in expected if c not in reader.fieldnames]
        if missing_cols:
            errors.append(f"{path}: missing columns {missing_cols}")
            return errors

        unknown = [c for c in reader.fieldnames if c not in props]
        if unknown:
            errors.append(f"{path}: unknown columns {unknown}")

        grains = {}
        for lineno, row in enumerate(reader, start=2):
            where = f"{path}:{lineno}"

            for col in required:
                if not (row.get(col) or "").strip():
                    errors.append(f"{where}: required column {col!r} is empty")

            if (row.get("status") or "") == "approved":
                for col in req_approved:
                    if not (row.get(col) or "").strip():
                        errors.append(
                            f"{where}: {col!r} is required once status=approved"
                        )

            for col, spec in props.items():
                problem = check_value(col, (row.get(col) or "").strip(), spec)
                if problem:
                    errors.append(f"{where}: {problem}")

            for col in unique_cols:
                val = (row.get(col) or "").strip()
                if not val:
                    continue
                if val in seen[col]:
                    errors.append(
                        f"{where}: duplicate {col}={val!r} "
                        f"(first seen line {seen[col][val]})"
                    )
                else:
                    seen[col][val] = lineno

            # Grain must be consistent across every row for a target entity —
            # an inconsistency here is a modeling error, not a typo.
            entity = (row.get("target_entity") or "").strip()
            grain = (row.get("target_grain") or "").strip()
            if entity and grain:
                if entity in grains and grains[entity][0] != grain:
                    errors.append(
                        f"{where}: target_grain {grain!r} for entity {entity!r} "
                        f"conflicts with {grains[entity][0]!r} at line {grains[entity][1]}"
                    )
                else:
                    grains.setdefault(entity, (grain, lineno))

    return errors


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    if not SUBJECTS.exists():
        print("no subjects/ directory found", file=sys.stderr)
        return 1

    all_errors = []
    checked = 0

    for subject in sorted(SUBJECTS.iterdir()):
        if not subject.is_dir() or subject.name.startswith("_"):
            continue
        if only and subject.name != only:
            continue

        for rel, schema_name in TARGETS:
            path = subject / rel
            if not path.exists():
                continue
            checked += 1
            all_errors.extend(validate_file(path, load_schema(schema_name)))

    if not checked:
        target = only or "any subject"
        print(f"No CSVs found for {target} — nothing to validate.")
        return 0

    if all_errors:
        for err in all_errors:
            print(f"FAIL {err}")
        print(f"\n{len(all_errors)} problem(s) across {checked} file(s).")
        return 1

    print(f"OK — {checked} file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
