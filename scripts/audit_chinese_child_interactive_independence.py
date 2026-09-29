#!/usr/bin/env python3
"""Check that the eleven materialized Chinese child lessons have distinct interactions."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    "ab-iv-1", "ab-iv-2", "ab-iv-3", "ab-iv-4", "ab-iv-5", "ab-iv-6", "ab-iv-7", "ab-iv-8",
    "ac-iv-1", "ac-iv-2", "ad-iv-1",
]


def main() -> int:
    rows = []
    for unit_id in TARGETS:
        path = ROOT / "lessons/chinese" / f"lesson-chinese-content-{unit_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        steps = data["interactive"]["steps"]
        signature = "|".join(f"{step['prompt']}::{','.join(step['options'])}::{step['answer']}" for step in steps)
        rows.append({"unitId": unit_id, "signature": signature, "stepCount": len(steps)})
    signatures = [row["signature"] for row in rows]
    duplicates = len(signatures) - len(set(signatures))
    report = {"checked": len(rows), "unique": len(set(signatures)), "duplicateSignatures": duplicates, "status": "pass" if duplicates == 0 else "fail"}
    out = ROOT / "implementation/reports/chinese-child-interactive-independence.json"
    out.write_text(json.dumps({**report, "items": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if duplicates == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
