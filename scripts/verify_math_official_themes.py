#!/usr/bin/env python3
"""Record official curriculum evidence for the six junior-high math themes."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = next(json.loads(p.read_text())["source"]["url"] for p in (ROOT / "curriculum/math").glob("*.json"))
THEMES = {
    "number": ("數與量（N）", "PDF viewer P80-P81；附錄三 P74-P79；國民中學七至九年級主題：數與量（N）。"),
    "algebra": ("代數與方程", "PDF viewer P80-P81；國民中學七至九年級主題：代數（A）；本 unit title 為本專案教學標籤。"),
    "geometry": ("空間與形狀", "PDF viewer P80-P81；國民中學七至九年級主題：空間與形狀（S）。"),
    "functions": ("函數", "PDF viewer P80-P81；國民中學八至九年級主題：函數（F）。"),
    "coordinates": ("坐標幾何", "PDF viewer P80-P81；國民中學七至九年級主題：坐標幾何（G）。"),
    "data": ("資料與不確定性", "PDF viewer P80-P81；國民中學七至九年級主題：資料與不確定性（D）。"),
}


def main() -> None:
    updated = 0
    for key, (title, locator) in THEMES.items():
        unit_path = ROOT / "canonical-units/math" / f"canonical-unit-math-{key}.json"
        map_path = ROOT / "canonical-units/math/mappings" / f"unit-map-math-{key}.json"
        unit = json.loads(unit_path.read_text())
        unit["title"] = title
        unit["source"].update({"type": "official-curriculum", "url": URL, "locator": locator, "confidence": "high"})
        unit_path.write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")
        mapping = json.loads(map_path.read_text())
        mapping["evidence"].update({"type": "official-curriculum", "url": URL, "locator": locator, "confidence": "high"})
        map_path.write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")
        updated += 2
    print(f"updated math official theme evidence files: {updated}")


if __name__ == "__main__":
    main()
