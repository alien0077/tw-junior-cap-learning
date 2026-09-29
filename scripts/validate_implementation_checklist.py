#!/usr/bin/env python3
"""Validate that the P0-P9 checklist is complete as a report, not as a completion claim."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKLIST = ROOT / "implementation/reports/guide-checklist.json"


def evidence_path(value: str) -> Path | None:
    if not isinstance(value, str) or value.startswith("http") or value.startswith("npm ") or value.startswith("1027") or value.startswith("596") or value.startswith("headless") or value.startswith("spec ") or value.startswith("browser ") or value.startswith("ordered") or value.startswith("16 ") or value.startswith("320"):
        return None
    candidate = value.split()[0]
    if candidate.startswith("scripts/") or candidate.startswith("implementation/") or candidate.startswith(".github/"):
        return ROOT / candidate
    return None


def main() -> int:
    doc = json.loads(CHECKLIST.read_text(encoding="utf-8"))
    errors = []
    items = doc.get("items", {})
    expected = [f"P{i}" for i in range(10)]
    if list(items) != expected:
        errors.append(f"P0-P9 keys mismatch: {list(items)}")
    for item_id in expected:
        item = items.get(item_id, {})
        if not item.get("status"):
            errors.append(f"{item_id} has no status")
        if not item.get("evidence"):
            errors.append(f"{item_id} has no evidence")
        if not item.get("pending") and item.get("status") != "implemented":
            errors.append(f"{item_id} has no pending list")
        for evidence in item.get("evidence", []):
            path = evidence_path(evidence)
            if path is not None and not path.exists():
                errors.append(f"{item_id} evidence path missing: {evidence}")
    for key in ["composition", "questionCoverage", "qaContract"]:
        if not isinstance(doc.get(key), dict) or not doc[key].get("status"):
            errors.append(f"{key} report status missing")
    if doc.get("eligibleUnits") != 0 or doc.get("pendingUnits") != 1027:
        errors.append("completion counters changed without explicit gate review")
    report = {"expectedItems": expected, "actualItems": list(items), "errors": errors, "status": "passed" if not errors else "failed", "completionCounters": {"eligibleUnits": doc.get("eligibleUnits"), "pendingUnits": doc.get("pendingUnits")}}
    out = ROOT / "implementation/reports/checklist-validation.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
