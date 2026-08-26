#!/usr/bin/env python3
"""Record direct official-PDF evidence for English Aa-Ad groupings."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://stv.naer.edu.tw/data/course_outline/pta_18518_3555074_59836.pdf"
CONFIG = {
    "aa": ("PDF viewer P18；A.語言知識／a.字母；Aa-Ⅳ-1。", "high"),
    "ab": ("PDF viewer P18；A.語言知識／b.語音；Ab-Ⅳ-1～Ab-Ⅳ-3。", "high"),
    "ac": ("PDF viewer P18；A.語言知識／c.字詞；Ac-Ⅳ-1～Ac-Ⅳ-4。", "medium"),
    "ad": ("PDF viewer P18；A.語言知識／d.句構；Ad-Ⅳ-1。", "high"),
}


def main() -> None:
    updated = 0
    for key, (locator, confidence) in CONFIG.items():
        unit_path = ROOT / "canonical-units/english" / f"canonical-unit-english-content-{key}.json"
        map_path = ROOT / "canonical-units/english/mappings" / f"unit-map-english-content-{key}.json"
        unit = json.loads(unit_path.read_text())
        unit["source"].update({"type": "official-curriculum", "url": URL, "locator": locator, "confidence": confidence})
        unit_path.write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")
        mapping = json.loads(map_path.read_text())
        mapping["evidence"].update({"type": "official-curriculum", "url": URL, "locator": locator, "confidence": confidence})
        map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")
        updated += 2
    print(f"updated English official evidence files: {updated}")


if __name__ == "__main__":
    main()
