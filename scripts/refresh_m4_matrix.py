#!/usr/bin/env python3
"""Refresh coverage status from materialized lesson/question files."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
matrix_path = ROOT / "data/m4-coverage-matrix.json"
matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
question_counts = {}
for question_path in (ROOT / "questions").glob("*/*.json"):
    question = json.loads(question_path.read_text(encoding="utf-8"))
    lesson_id = question.get("lessonId")
    if lesson_id:
        question_counts[lesson_id] = question_counts.get(lesson_id, 0) + 1
for row in matrix["rows"]:
    if not row.get("lessonId"):
        continue
    lesson_path = ROOT / "lessons" / row["subject"] / f"{row['lessonId']}.json"
    if not lesson_path.exists():
        continue
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    row["questionCount"] = question_counts.get(row["lessonId"], 0)
    row["interactiveStatus"] = (
        "complete" if row["subject"] in {"math", "science"} and len(lesson.get("interactive", {}).get("steps", [])) >= 3
        else "not-required" if row["subject"] not in {"math", "science"} else "pending"
    )
matrix["summary"]["questionsCovered"] = sum(r.get("questionCount", 0) >= 10 for r in matrix["rows"])
matrix["summary"]["interactivePending"] = sum(r.get("interactiveStatus") == "pending" for r in matrix["rows"])
matrix_path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("refreshed", len(matrix["rows"]), "coverage rows")
