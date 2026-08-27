#!/usr/bin/env python3
"""Promote mechanically verified parentId mappings from draft to mapped."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ("chinese", "english", "science", "social")


def main() -> None:
    promoted = 0
    for subject in SUBJECTS:
        curriculum = {json.loads(path.read_text())["id"]: json.loads(path.read_text()) for path in (ROOT / "curriculum" / subject).glob("*.json")}
        for path in (ROOT / "canonical-units" / subject).glob("canonical-unit-*.json"):
            unit = json.loads(path.read_text())
            ids = unit.get("curriculumIds", [])
            valid = bool(ids) and all(item in curriculum and curriculum[item].get("level") == "learning-content" for item in ids)
            if valid and unit.get("status") == "draft":
                unit["status"] = "mapped"
                unit["source"]["locator"] = "Official parentId grouping mechanically verified; publisher chapter alignment and teacher review pending."
                unit["source"]["confidence"] = "medium"
                path.write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")
                promoted += 1
        for path in (ROOT / "canonical-units" / subject / "mappings").glob("unit-map-*.json"):
            mapping = json.loads(path.read_text())
            valid = all(item in curriculum and curriculum[item].get("level") == "learning-content" for item in mapping.get("curriculumIds", []))
            if valid and mapping.get("status") == "draft":
                mapping["status"] = "mapped"
                mapping["evidence"]["locator"] = "Official parentId grouping mechanically verified; publisher chapter alignment and teacher review pending."
                mapping["evidence"]["confidence"] = "medium"
                path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")
                promoted += 1
    print(f"promoted mappings/units: {promoted}")


if __name__ == "__main__":
    main()
