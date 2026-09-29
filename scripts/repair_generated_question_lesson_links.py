#!/usr/bin/env python3
"""Repair generated root-question links to existing overview lessons.

Root curriculum nodes currently have no separate lesson records. Keep the root
KG as the assessed concept and add the existing subject overview KG only as the
lesson endpoint required by the repository validator.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = {
    "chinese": ("lesson-chinese-learning-content", "kg-chinese-learning-content"),
    "english": ("lesson-english-learning-content", "kg-english-learning-content"),
    "math": ("lesson-math-learning-content", "kg-math-learning-content"),
    "science": ("lesson-science-learning-content", "kg-science-learning-content"),
}


def main() -> int:
    files = sorted((ROOT / "questions/generated").glob("question-*-root-*.json"))
    changed = []
    for path in files:
        data = json.loads(path.read_text(encoding="utf-8"))
        subject = data["subject"]
        lesson_id, overview_kg = MAP[subject]
        if data.get("lessonId") != lesson_id or overview_kg not in data.get("knowledgeIds", []):
            data["lessonId"] = lesson_id
            data["knowledgeIds"] = list(dict.fromkeys([*data.get("knowledgeIds", []), overview_kg]))
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append(str(path.relative_to(ROOT)))
    print(json.dumps({"changed": len(changed), "files": changed}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
