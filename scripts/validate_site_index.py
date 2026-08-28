#!/usr/bin/env python3
"""Validate the M5 deployment index without making network requests."""
from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    index_path = ROOT / "site" / "data-index.json"
    index = read_json(index_path)
    errors: list[str] = []
    if index.get("version") != 2:
        errors.append("index version must be 2")
    revision = str(index.get("sourceRevision", ""))
    if not revision or revision == "main":
        errors.append("site index must pin an immutable source revision")
    lessons = index.get("lessons", [])
    if not lessons:
        errors.append("site index has no active lessons")
    ids = set()
    for lesson in lessons:
        lesson_id = lesson.get("id")
        if lesson_id in ids:
            errors.append(f"duplicate lesson in site index: {lesson_id}")
        ids.add(lesson_id)
        source = read_json(ROOT / lesson["path"])
        if source.get("reviewStatus") == "deprecated":
            errors.append(f"deprecated lesson exposed: {lesson_id}")
        if len(lesson.get("questionPaths", [])) < 10:
            errors.append(f"lesson has fewer than 10 active question paths: {lesson_id}")
        for question_path in lesson.get("questionPaths", []):
            question = read_json(ROOT / question_path)
            if question.get("reviewStatus") == "deprecated":
                errors.append(f"deprecated question exposed: {question.get('id')}")
            if question.get("lessonId") != lesson_id:
                errors.append(f"question belongs to another lesson: {question.get('id')}")
    if index.get("validation", {}).get("lessonCount") != len(lessons):
        errors.append("lesson count differs from index validation block")
    if errors:
        print("\n".join(errors))
        return 1
    print(
        "site index validated: "
        f"{len(lessons)} lessons, "
        f"{sum(len(x['questionPaths']) for x in lessons)} question paths, "
        f"revision {revision}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
