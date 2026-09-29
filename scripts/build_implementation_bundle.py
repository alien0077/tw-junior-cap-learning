#!/usr/bin/env python3
"""Compile extracted YAML unit specs into a browser-readable JSON bundle."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    files = sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml"))
    units = []
    lessons_by_id = {}
    for lesson_path in sorted((ROOT / "lessons").glob("*/*.json")):
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        lesson_id = lesson.get("id")
        if lesson_id:
            lessons_by_id[lesson_id] = lesson
    for path in files:
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        curriculum_id = spec.get("lessonId")
        lesson_id = curriculum_id.replace("cur-", "lesson-", 1) if isinstance(curriculum_id, str) and curriculum_id.startswith("cur-") else curriculum_id
        lesson = lessons_by_id.get(lesson_id)
        if lesson is not None:
            spec["authoredLesson"] = lesson
        spec["authoredLessonId"] = lesson_id
        spec["authoredLessonAttached"] = lesson is not None
        units.append(spec)
    out = ROOT / "implementation/unit-specs.bundle.json"
    out.write_text(json.dumps({"specVersion": "1.0", "units": units}, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    attached = sum(1 for unit in units if unit.get("authoredLessonAttached"))
    missing = [unit.get("lessonId") for unit in units if not unit.get("authoredLessonAttached")]
    print(json.dumps({"units": len(units), "lessonsAttached": attached, "lessonsMissing": len(missing), "missingLessonCurriculumIds": missing, "output": str(out)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
