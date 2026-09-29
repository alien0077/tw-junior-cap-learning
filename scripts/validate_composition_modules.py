#!/usr/bin/env python3
"""Validate the composition module registry without inventing module content."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ["審題立意", "選材", "組織", "段落", "敘事", "描寫", "抒情", "說明", "議論", "開頭結尾", "銜接修辭", "修改", "限時寫作"]


def main() -> int:
    contract = json.loads((ROOT / "implementation/composition/composition-contract.json").read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "implementation/composition/module-registry.json").read_text(encoding="utf-8"))
    labels = [module["label"] for module in registry["modules"]]
    errors = []
    if contract["modules"] != EXPECTED:
        errors.append("composition contract module list differs from guide")
    if labels != EXPECTED:
        errors.append("registry module list differs from guide")
    if len({module["id"] for module in registry["modules"]}) != len(EXPECTED):
        errors.append("registry IDs are not unique")
    content = json.loads((ROOT / "implementation/composition/module-content.json").read_text(encoding="utf-8"))
    content_by_id = {module["id"]: module for module in content["modules"]}
    for module in registry["modules"]:
        if module["status"] not in {"content-pending", "content-authored-draft", "content-reviewed-draft"}:
            errors.append(f"module status is invalid: {module['id']}")
        if module["requiredArtifacts"] != ["prompt", "diagnostic", "firstHint", "transfer"]:
            errors.append(f"required artifacts incomplete: {module['id']}")
    for module in registry["modules"]:
        row = content_by_id.get(module["id"])
        if not row or not all(str(row.get(key, "")).strip() for key in module["requiredArtifacts"]):
            errors.append(f"source-aware content artifact missing: {module['id']}")
    if len(content_by_id) != len(EXPECTED) or set(content_by_id) != {module["id"] for module in registry["modules"]}:
        errors.append("module content IDs do not match registry")
    status_counts = {}
    for module in registry["modules"]:
        status_counts[module["status"]] = status_counts.get(module["status"], 0) + 1
    report = {"moduleCount": len(registry["modules"]), "expected": len(EXPECTED), "errors": errors, "status": "passed" if not errors else "failed", "contentStatuses": status_counts, "sourceRefs": len(content.get("sourceRefs", []))}
    out = ROOT / "implementation/reports/composition-modules.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
