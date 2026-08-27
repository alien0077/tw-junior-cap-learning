#!/usr/bin/env python3
"""Record the internal math QA boundary on lessons upgraded by QA scripts."""
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
changed = 0
for filename in glob.glob(str(ROOT / "lessons" / "math" / "*.json")):
    path = Path(filename)
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "content-reviewed":
        continue
    note = data.setdefault("provenance", {}).get("authoringNote", "")
    if "Batch-generated draft" not in note:
        continue
    data["provenance"]["authoringNote"] = (
        "Original instructional content authored for this repository; "
        "validated by the repository's explicit math QA batch; "
        "not teacher-reviewed."
    )
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed += 1
print(f"annotated math lessons={changed}")
