#!/usr/bin/env python3
"""Route explicitly identified calligraphy questions to the unique child unit."""
import json
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "migrations/chinese-question-migration-pilot.json"
data = json.loads(path.read_text())
for item in data["items"]:
    if item["sourceLessonId"] == "lesson-chinese-calligraphy-appreciation":
        item["targetUnitId"] = "canonical-unit-chinese-content-ab-calligraphy"
        item["migrationStatus"] = "pending-review"
        item["notes"] = "官方 Ab-Ⅳ-8 唯一對應；child unit 已建立，仍待逐題語意審核。"
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print("updated calligraphy migration items")
