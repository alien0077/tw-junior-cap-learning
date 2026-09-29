#!/usr/bin/env python3
"""Validate every canonical lesson directly against schemas/lesson.schema.json."""
from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    schema = json.loads((ROOT / "schemas/lesson.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    failures = []
    paths = sorted((ROOT / "lessons").glob("*/*.json"))
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))
        if errors:
            failures.append({
                "file": str(path.relative_to(ROOT)),
                "errors": [error.message for error in errors[:10]],
            })
    report = {
        "schema": "schemas/lesson.schema.json",
        "checked": len(paths),
        "failed": len(failures),
        "failures": failures,
        "status": "pass" if not failures else "fail",
    }
    out = ROOT / "implementation/reports/lesson-schema-direct-audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("checked", "failed", "status")}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
