#!/usr/bin/env python3
"""Remove the visible draft marker only from lessons already QA-reviewed."""
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
changed = 0
for filename in glob.glob(str(ROOT / "lessons" / "*" / "*.json")):
    path = Path(filename)
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "content-reviewed":
        continue
    title = str(data.get("title", ""))
    if not title.startswith("草稿"):
        continue
    data["title"] = title.removeprefix("草稿：").removeprefix("草稿:").strip()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed += 1
print(f"normalized reviewed lesson titles={changed}")
