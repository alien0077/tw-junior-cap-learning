#!/usr/bin/env python3
"""Repair legacy publisher-sample IDs against actual lesson files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
REMAP = {
    "lesson-chinese-root-a": "lesson-chinese-content-root-a",
    "lesson-chinese-root-b": "lesson-chinese-content-root-b",
}
REMOVE = {
    "lesson-science-content-j",
    "lesson-social-content-geo-aa-1",
    "lesson-social-content-geo-aa-2",
    "lesson-social-content-geo-aa-3",
    "lesson-social-content-geo-aa-4",
}

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = []
    removed = []
    remapped = []
    seen = set()
    for item in data["units"]:
        old = item["lessonId"]
        if old in REMOVE:
            removed.append(old)
            continue
        new = REMAP.get(old, old)
        if new in seen:
            raise SystemExit(f"duplicate lesson ID after repair: {new}")
        if new != old:
            item = dict(item)
            item["lessonId"] = new
            remapped.append({"from": old, "to": new})
        seen.add(new)
        units.append(item)
    data["units"] = sorted(units, key=lambda x: x["lessonId"])
    data["unitCount"] = len(units)
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred nineteen unit samples", "Seven hundred fourteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": len(units), "remapped": remapped, "removed": removed}, ensure_ascii=False))

if __name__ == "__main__":
    main()
