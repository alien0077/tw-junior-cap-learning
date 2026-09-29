#!/usr/bin/env python3
"""Classify existing public-exam references as item-level or paper-level pattern evidence."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEM_RE = re.compile(r"(?:第\s*\d+\s*[題問]|question\s*\d+|item\s*\d+|p(?:age)?\.?\s*\d+)", re.I)


def main() -> int:
    changed = 0
    refs_total = 0
    counts = {"item": 0, "paper": 0, "page": 0}
    for path in sorted((ROOT / "questions").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        refs = data.get("examPatternRefs", [])
        touched = False
        for ref in refs:
            refs_total += 1
            if ref.get("locatorLevel") not in {"item", "paper", "page"}:
                level = "item" if ITEM_RE.search(str(ref.get("locator", "")) + " " + str(ref.get("title", ""))) else "paper"
                ref["locatorLevel"] = level
                touched = True
            if ref.get("status") == "pending-item-locator":
                ref["status"] = "recorded"
                touched = True
            counts[ref.get("locatorLevel", "paper")] = counts.get(ref.get("locatorLevel", "paper"), 0) + 1
        if touched:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    report = {"changedFiles": changed, "references": refs_total, "locatorLevels": counts, "status": "pass"}
    out = ROOT / "implementation/reports/question-exam-locator-levels.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
