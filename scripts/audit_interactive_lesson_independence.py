#!/usr/bin/env python3
"""Audit interactive steps for every learning-content lesson."""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/interactive-lesson-independence.json"


def main() -> int:
    signatures: dict[str, list[str]] = defaultdict(list)
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("lessonScope") != "learning-content":
            continue
        steps = data.get("interactive", {}).get("steps")
        if not isinstance(steps, list) or not steps:
            signatures["__missing__"].append(str(path.relative_to(ROOT)))
            continue
        canonical = json.dumps(steps, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        signatures[hashlib.sha256(canonical.encode("utf-8")).hexdigest()].append(str(path.relative_to(ROOT)))

    duplicate_groups = [paths for key, paths in signatures.items() if key != "__missing__" and len(paths) > 1]
    missing = signatures.get("__missing__", [])
    report = {
        "lessonCount": sum(len(paths) for paths in signatures.values()) - len(missing),
        "uniqueInteractiveSignatures": len([key for key in signatures if key != "__missing__"]),
        "duplicateGroupCount": len(duplicate_groups),
        "affectedLessonCount": sum(len(paths) for paths in duplicate_groups),
        "missingInteractiveCount": len(missing),
        "duplicateGroups": duplicate_groups,
        "missingInteractiveLessons": missing,
        "status": "pass" if not duplicate_groups and not missing else "fail",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("lessonCount", "uniqueInteractiveSignatures", "duplicateGroupCount", "affectedLessonCount", "missingInteractiveCount", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
