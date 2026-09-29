#!/usr/bin/env python3
"""Audit the unit-specific data actually available to the visual renderer."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    rows = []
    errors = []
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        blocks = spec.get("interactiveBlocks", [])
        block = blocks[0] if blocks else {}
        row = {
            "lessonId": spec.get("lessonId"),
            "subject": spec.get("subject"),
            "component": block.get("component"),
            "coreConcept": (spec.get("coreConcepts") or [None])[0],
            "visualizations": spec.get("visualizations", []),
            "studentActions": block.get("studentActions", []),
            "visualRules": block.get("visualRules", []),
            "misconceptionChecks": block.get("misconceptionChecks", []),
            "capTransfer": spec.get("capTransfer", {}),
        }
        required = ["component", "coreConcept", "visualizations", "studentActions", "visualRules", "misconceptionChecks", "capTransfer"]
        missing = [key for key in required if not row.get(key)]
        if missing:
            errors.append({"lessonId": spec.get("lessonId"), "missing": missing})
        rows.append(row)
    summary = {
        "status": "pass" if not errors else "pending",
        "unitCount": len(rows),
        "unitsWithRendererData": len(rows) - len(errors),
        "errors": len(errors),
        "note": "This proves data-backed semantic and diagnostic bodies are available to the renderer; it does not replace visual design, subject correctness or pedagogical review.",
    }
    out = ROOT / "implementation/reports/unit-visualization-bodies.json"
    out.write_text(json.dumps({"summary": summary, "units": rows, "errors": errors}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
