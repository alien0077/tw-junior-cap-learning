#!/usr/bin/env python3
"""Apply only unique KG-derived migration resolutions; leave blocked items untouched."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
audit = {x["questionId"]: x for x in json.loads((ROOT / "migrations/m4-question-resolution.json").read_text())}
changed = 0
for p in (ROOT / "migrations").glob("*-question-migration-pilot.json"):
    d = json.loads(p.read_text())
    for item in d.get("items", []):
        x = audit.get(item["questionId"])
        if x and x["decision"] == "map" and item.get("targetUnitId") is None:
            item["targetUnitId"] = x["targetUnitId"]
            item["migrationStatus"] = "pending-review"
            item["notes"] = x["reason"]
            changed += 1
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print(f"applied unique KG-derived migration resolutions: {changed}")
