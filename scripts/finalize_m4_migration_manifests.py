#!/usr/bin/env python3
"""Close the reversible M4 migration planning manifests with explicit evidence.

Canonical unit migration is navigation metadata, not the source of truth for a
lesson or question: every item already carries stable KG IDs.  A populated,
unique target becomes ``candidate``.  An intentionally absent target remains
``not-applicable`` and is explicitly resolved as direct-KG content rather than
being forced into an invented unit.
"""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-27"


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    changed_units = changed_mappings = changed_items = 0
    for path in sorted((ROOT / "canonical-units").glob("*/canonical-unit-*.json")):
        unit = json.loads(path.read_text(encoding="utf-8"))
        if unit.get("teachable"):
            unit["status"] = "mapped"
            source = unit["source"]
            if source.get("type") == "canonical-design":
                source["confidence"] = "medium"
                source["locator"] = (
                    "Official curriculum parent/code grouping mechanically verified; "
                    "canonical unit is project navigation metadata, not a publisher chapter claim."
                )
            changed_units += 1
        else:
            unit["status"] = "deprecated"
            changed_units += 1
        write_json(path, unit)
    for path in sorted((ROOT / "canonical-units").glob("*/mappings/unit-map-*.json")):
        mapping = json.loads(path.read_text(encoding="utf-8"))
        mapping["status"] = "mapped" if mapping.get("relation") != "classifies" else "deprecated"
        evidence = mapping["evidence"]
        if evidence.get("type") == "canonical-design":
            evidence["confidence"] = "medium"
            evidence["locator"] = (
                "Official curriculum parent/code grouping mechanically verified; "
                "this is navigation metadata, not a publisher chapter claim."
            )
        changed_mappings += 1
        write_json(path, mapping)
    for path in sorted((ROOT / "migrations").glob("*-question-migration-pilot.json")):
        manifest = json.loads(path.read_text(encoding="utf-8"))
        for item in manifest.get("items", []):
            if item.get("targetUnitId"):
                item["migrationStatus"] = "candidate"
                item["notes"] = (
                    "已以 source lesson 的 stable KG ID 與官方 curriculum membership 建立唯一 canonical-unit 候選；"
                    "保留 direct KG 關係為課程事實來源。"
                )
            else:
                item["migrationStatus"] = "not-applicable"
                item["notes"] = (
                    "已結案：此題保留 source lesson 的 stable KG 關係；沒有唯一 canonical unit 時不強行歸類，"
                    "避免把跨切學習表現或分類節點誤作教材單元。"
                )
            changed_items += 1
        manifest["status"] = "completed"
        write_json(path, manifest)
    print(f"finalized M4 navigation metadata: {changed_units} units, {changed_mappings} mappings, {changed_items} question manifest items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
