#!/usr/bin/env python3
"""Clear migration targets that became taxonomy-only units."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    cleared = 0
    for path in (ROOT / "migrations").glob("*-question-migration-pilot.json"):
        manifest = json.loads(path.read_text())
        for item in manifest.get("items", []):
            target = item.get("targetUnitId")
            if not target:
                continue
            unit_path = next((p for p in (ROOT / "canonical-units").glob(f"*/{target}.json")), None)
            if not unit_path:
                continue
            unit = json.loads(unit_path.read_text())
            if unit.get("teachable") is False:
                item["targetUnitId"] = None
                item["migrationStatus"] = "not-applicable"
                item["notes"] = "原 target unit 已確認為分類節點；待 child unit 或外部語意核對後再遷移。"
                cleared += 1
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(f"cleared non-teachable migration targets: {cleared}")


if __name__ == "__main__":
    main()
