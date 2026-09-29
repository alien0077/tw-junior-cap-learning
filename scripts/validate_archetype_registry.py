#!/usr/bin/env python3
"""Validate archetype routing without treating routing as content QA."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    registry = json.loads((ROOT / "implementation/archetype-registry.json").read_text(encoding="utf-8"))
    components = set(json.loads((ROOT / "implementation/component-registry.json").read_text(encoding="utf-8"))["components"])
    archetypes = registry["archetypes"]
    errors = []
    seen = {}
    for archetype_id, entry in archetypes.items():
        if not entry.get("components") or not entry.get("subjects"):
            errors.append({"archetype": archetype_id, "error": "components and subjects are required"})
        for component in entry.get("components", []):
            if component not in components:
                errors.append({"archetype": archetype_id, "component": component, "error": "unknown component"})
            if component in seen:
                errors.append({"component": component, "error": "assigned to multiple archetypes", "previous": seen[component], "current": archetype_id})
            seen[component] = archetype_id
    missing = sorted(components - set(seen))
    errors.extend({"component": component, "error": "unassigned component"} for component in missing)

    counts = defaultdict(Counter)
    unit_count = 0
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        unit_count += 1
        for block in spec["interactiveBlocks"]:
            component = block["component"]
            archetype = seen.get(component)
            if not archetype:
                errors.append({"lessonId": spec["lessonId"], "component": component, "error": "no archetype"})
                continue
            counts[archetype][spec["subject"]] += 1
            if spec["subject"] not in archetypes[archetype]["subjects"]:
                errors.append({"lessonId": spec["lessonId"], "subject": spec["subject"], "component": component, "archetype": archetype, "error": "subject not allowed"})

    report = {
        "archetypeCount": len(archetypes),
        "componentCount": len(components),
        "unitCount": unit_count,
        "assignedComponents": len(seen),
        "counts": {key: dict(value) for key, value in sorted(counts.items())},
        "errors": errors,
        "status": "passed" if not errors and unit_count == 1027 else "failed",
        "note": "Archetype routing is structural evidence only; independent unit content, visualization and pedagogical QA remain separate gates.",
    }
    out = ROOT / "implementation/reports/archetype-coverage.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"archetypeCount": report["archetypeCount"], "componentCount": report["componentCount"], "unitCount": unit_count, "assignedComponents": len(seen), "errors": len(errors), "status": report["status"]}, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
