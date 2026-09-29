#!/usr/bin/env python3
"""Flag grade-sensitive public-exam pattern refs that need unit-fit review."""
from __future__ import annotations

import collections
from datetime import date
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"


def grade_from_lesson(lesson_id: str, lesson: dict) -> str:
    # Prefer a grade encoded in the stable ID; otherwise use the explicit lesson range.
    matches = re.findall(r"(?:^|-)((?:7|8|9))(?:-|$)", lesson_id)
    if matches:
        return matches[-1]
    grade_range = lesson.get("gradeRange", [])
    if isinstance(grade_range, list) and grade_range and all(str(g) in {"7", "8", "9"} for g in grade_range):
        return "/".join(str(g) for g in grade_range)
    return "unclassified"


def load_lesson_index() -> dict[str, dict]:
    index = {}
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if data.get("id"):
            index[str(data["id"])] = data
    return index


def main() -> None:
    rows = []
    counts = collections.Counter()
    scope_counts = collections.Counter()
    lesson_index = load_lesson_index()
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not any(ref.get("url") == TARGET for ref in data.get("examPatternRefs", [])):
            continue
        lesson = lesson_index.get(str(data.get("lessonId", "")), {})
        grade = grade_from_lesson(str(data.get("lessonId", "")), lesson)
        lesson_scope = str(lesson.get("lessonScope", "unknown"))
        counts[grade] += 1
        scope_counts[lesson_scope] += 1
        rows.append({
            "questionId": data.get("id"),
            "path": str(path.relative_to(ROOT)),
            "lessonId": data.get("lessonId"),
            "inferredGrade": grade,
            "sourceGradeCompatible": "9" in grade.split("/"),
            "lessonScope": lesson_scope,
            "referenceMode": "pattern-only",
        })
    mismatch_count = sum(1 for row in rows if row["inferredGrade"] != "unclassified" and not row["sourceGradeCompatible"])
    unclassified_count = counts["unclassified"]
    grade_status = "pass-grade-compatibility" if mismatch_count == 0 and unclassified_count == 0 else "review-queue"
    out = {
        "status": grade_status,
        "auditedAt": date.today().isoformat(),
        "sourceUrl": TARGET,
        "sourceGrade": "9",
        "totalRefs": len(rows),
        "countsByInferredGrade": dict(counts),
        "countsByLessonScope": dict(scope_counts),
        "potentialGradeMismatchRefs": mismatch_count,
        "sourceGradeCompatibleRefs": sum(1 for row in rows if row["sourceGradeCompatible"]),
        "unclassifiedRefs": unclassified_count,
        "rows": rows,
        "boundary": "這是來源適配 triage，不是答案錯誤判定；pattern-only 可保留作能力研究，但顯式不同年級與未分類節點必須在逐題內容／來源 QA 中重新核對。",
    }
    target = ROOT / f"implementation/reports/public-exam-source-unit-fit-queue-{date.today():%Y%m%d}.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("status", "totalRefs", "countsByInferredGrade", "countsByLessonScope", "potentialGradeMismatchRefs", "sourceGradeCompatibleRefs", "unclassifiedRefs")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
