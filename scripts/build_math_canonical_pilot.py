#!/usr/bin/env python3
"""Build a draft canonical-unit pilot for the existing mathematics graph."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM_DIR = ROOT / "curriculum" / "math"
OUT_DIR = ROOT / "canonical-units" / "math"
MAPPING_DIR = OUT_DIR / "mappings"

UNIT_DEFS = {
    "navigation": ("數學課綱分類導航", False),
    "number": ("數與量", True),
    "algebra": ("代數與方程", True),
    "geometry": ("空間與形狀", True),
    "functions": ("函數", True),
    "coordinates": ("坐標幾何", True),
    "data": ("資料與不確定性", True),
}


def cluster(curriculum_id: str) -> str:
    parts = curriculum_id.split("-")
    prefix = parts[3] if len(parts) > 3 else ""
    return {
        "a": "algebra",
        "n": "number",
        "s": "geometry",
        "f": "functions",
        "g": "coordinates",
        "d": "data",
    }.get(prefix, "navigation")


def main() -> None:
    items = [json.loads(path.read_text()) for path in sorted(CURRICULUM_DIR.glob("*.json"))]
    source_url = next((item.get("source", {}).get("url") for item in items if item.get("source", {}).get("url")), "")
    grouped: dict[str, list[str]] = {key: [] for key in UNIT_DEFS}
    for item in items:
        curriculum_id = item["id"]
        grouped[cluster(curriculum_id)].append(curriculum_id)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MAPPING_DIR.mkdir(parents=True, exist_ok=True)
    for key, (title, teachable) in UNIT_DEFS.items():
        unit_id = f"canonical-unit-math-{key}"
        unit = {
            "id": unit_id,
            "subject": "math",
            "title": title,
            "teachable": teachable,
            "gradeRange": ["7", "8", "9"],
            "curriculumIds": grouped[key],
            "status": "draft",
            "source": {
                "type": "canonical-design",
                "url": source_url,
                "locator": "M4 canonical-unit migration pilot; grouped by existing official curriculum ID prefix; publisher and teacher verification pending.",
                "verifiedAt": "2026-08-26",
                "confidence": "low",
            },
        }
        (OUT_DIR / f"{unit_id}.json").write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")

        if not grouped[key]:
            continue
        relation = "classifies" if key == "navigation" else "covers"
        mapping = {
            "id": f"unit-map-math-{key}",
            "subject": "math",
            "unitId": unit_id,
            "curriculumIds": grouped[key],
            "relation": relation,
            "status": "draft",
            "evidence": {
                "type": "canonical-design",
                "url": source_url,
                "locator": "Pilot grouping only; not a claim that publisher chapter boundaries equal official standards.",
                "verifiedAt": "2026-08-26",
                "confidence": "low",
            },
        }
        (MAPPING_DIR / f"unit-map-math-{key}.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")
    print(f"math curriculum nodes: {len(items)}")
    print(f"canonical units: {len(UNIT_DEFS)}")
    print(f"mappings: {sum(bool(ids) for ids in grouped.values())}")


if __name__ == "__main__":
    main()
