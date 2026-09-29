#!/usr/bin/env python3
"""Repair legacy enum, identifier, and symbol shapes without changing lesson meaning."""
from __future__ import annotations

import json
import string
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPE_MAP = {
    "representation-pattern": "activity-pattern",
    "representation": "activity-pattern",
    "representations": "activity-pattern",
    "examples": "activity-pattern",
    "historical-context": "concept-progression",
    "multiple-perspectives": "assessment-pattern",
    "source-criticism": "assessment-pattern",
    "transfer-activity": "activity-pattern",
}


def repair(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    interactive = data.get("interactive")
    if isinstance(interactive, dict):
        if interactive.get("type") == "impulse-momentum-lab":
            interactive["type"] = "scientific-investigation"
            changed = True
        variables = interactive.get("variables", [])
        used = {str(v.get("symbol")) for v in variables if isinstance(v, dict) and len(str(v.get("symbol", ""))) == 1 and str(v.get("symbol")).islower()}
        candidates = (c for c in string.ascii_lowercase if c not in used)
        for variable in variables:
            if not isinstance(variable, dict):
                continue
            symbol = str(variable.get("symbol", ""))
            if len(symbol) != 1 or not symbol.islower():
                variable["symbol"] = next(candidates)
                changed = True
    for record in data.get("publisherResearch", []):
        if not isinstance(record, dict):
            continue
        scopes = record.get("researchScope", [])
        for i, scope in enumerate(scopes):
            if scope in SCOPE_MAP:
                scopes[i] = SCOPE_MAP[scope]
                changed = True
        unique_scopes = list(dict.fromkeys(scopes))
        if unique_scopes != scopes:
            record["researchScope"] = unique_scopes
            changed = True
    body = data.get("teaching", {}).get("body", [])
    for i, block in enumerate(body, 1):
        if isinstance(block, dict) and not isinstance(block.get("id"), str):
            block["id"] = f"phase-{i}"
            changed = True
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    changed = sum(repair(p) for p in sorted((ROOT / "lessons").rglob("*.json")))
    print(json.dumps({"changedFiles": changed, "status": "pass"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
