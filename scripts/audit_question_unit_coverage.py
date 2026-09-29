#!/usr/bin/env python3
"""Verify every implementation spec has at least three mapped questions."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def aliases(lesson_id: str) -> list[str]:
    values = [lesson_id]
    for suffix in ("-content-a", "-content-b", "-content-j"):
        if lesson_id.endswith(suffix):
            values.append(lesson_id[: -len(suffix)] + suffix.replace("-content", "-content-root"))
    if lesson_id.endswith("-content-j"):
        values.append(lesson_id.replace("-content-j", "-j"))
    return values


def main() -> int:
    specs = []
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        specs.append(yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]["lessonId"].replace("cur-", "lesson-", 1))
    counts = Counter()
    for path in (ROOT / "questions").rglob("*.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        counts[data.get("lessonId", "")] += 1
    rows = []
    for lesson_id in specs:
        mapped = [(candidate, counts[candidate]) for candidate in aliases(lesson_id) if counts[candidate]]
        total = sum(count for _, count in mapped)
        rows.append({"lessonId": lesson_id, "mappedLessonIds": mapped, "questionCount": total, "status": "pass" if total >= 3 else "fail"})
    failures = [row for row in rows if row["status"] == "fail"]
    report = {
        "requiredPerUnit": 3,
        "specCount": len(rows),
        "passed": len(rows) - len(failures),
        "failed": len(failures),
        "failures": failures,
        "status": "pass" if not failures else "fail",
        "aliasPolicy": "root content-a/b and science content-j endpoint aliases are counted only for their exact stable spec family",
    }
    out = ROOT / "implementation/reports/question-unit-coverage.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("requiredPerUnit", "specCount", "passed", "failed", "status")}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
