#!/usr/bin/env python3
"""Create a reversible manifest for migrating legacy mathematics questions."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
LESSON_DIR = ROOT / "lessons" / "math"
OUT = ROOT / "migrations" / "math-question-migration-pilot.json"


def unit_for_lesson(lesson_id: str) -> str | None:
    parts = lesson_id.split("-")
    # lesson-math-{content|performance}-{prefix}-...
    prefix = parts[3] if len(parts) > 3 else ""
    key = {"a": "algebra", "n": "number", "s": "geometry", "f": "functions", "g": "coordinates", "d": "data"}.get(prefix)
    return f"canonical-unit-math-{key}" if key else None


def main() -> None:
    lesson_ids = {json.loads(path.read_text())["id"] for path in LESSON_DIR.glob("*.json")}
    items = []
    for path in sorted(QUESTION_DIR.glob("*.json")):
        question = json.loads(path.read_text())
        lesson_id = question["lessonId"]
        if lesson_id not in lesson_ids:
            raise SystemExit(f"question references missing lesson: {question['id']} -> {lesson_id}")
        target = unit_for_lesson(lesson_id)
        if target is None:
            status, notes = "not-applicable", "來源 lesson 對應課綱分類節點；保留原題，暫不遷移至可教學 unit。"
        else:
            status, notes = "pending-review", "候選 unit 僅為 ID 前綴分群，待官方／教師逐項核對後才能升級。"
        items.append({
            "questionId": question["id"],
            "sourceLessonId": lesson_id,
            "targetUnitId": target,
            "migrationStatus": status,
            "notes": notes,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"id": "math-question-migration-pilot", "subject": "math", "status": "in-progress", "items": items}, ensure_ascii=False, indent=2) + "\n")
    print(f"math questions: {len(items)}")
    print(f"pending-review: {sum(item['migrationStatus'] == 'pending-review' for item in items)}")
    print(f"not-applicable: {sum(item['migrationStatus'] == 'not-applicable' for item in items)}")


if __name__ == "__main__":
    main()
