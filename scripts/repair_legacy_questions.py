#!/usr/bin/env python3
"""Repair the pre-M4 question baseline to the published question schema."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
LESSON_BY_PREFIX = {
    "chinese-argument": "lesson-chinese-argument-evidence-basics",
    "chinese-source": "lesson-chinese-source-reliability",
    "english-context": "lesson-english-context-clues",
    "english-fact-opinion": "lesson-english-fact-opinion",
    "math-equation": "lesson-math-linear-equation-check",
    "math-factorization": "lesson-math-factorization-common-factor",
    "science-evidence": "lesson-science-evidence-model",
    "science-heat": "lesson-science-specific-heat",
    "social-media": "lesson-social-media-literacy",
    "social-opportunity": "lesson-social-opportunity-cost",
}

for path in sorted((ROOT / "questions").glob("*/*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    data.get("provenance", {}).pop("authoringNote", None)
    old_id = data["id"].split("/")[-1]
    prefix = old_id.rsplit("-", 1)[0].removeprefix("question-")
    lesson_id = LESSON_BY_PREFIX.get(prefix)
    if lesson_id is None:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        continue
    data["id"] = old_id
    data["lessonId"] = lesson_id
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))
