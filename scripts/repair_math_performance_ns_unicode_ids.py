#!/usr/bin/env python3
"""Remove the accidental Unicode curriculum-code IDs before re-materializing canonical IDs."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
data = json.loads(REPORT.read_text(encoding="utf-8"))
before = len(data["units"])
data["units"] = [item for item in data["units"] if "Ⅳ" not in item["lessonId"]]
data["unitCount"] = len(data["units"])
data["updatedAt"] = "2026-09-21"
REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"removedUnicodeIds": before - len(data["units"]), "unitCount": data["unitCount"]}, ensure_ascii=False))
