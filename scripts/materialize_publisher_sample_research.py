#!/usr/bin/env python3
"""Materialize chapter-sample evidence into lesson publisherResearch fields."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

def main():
    samples = json.loads(REPORT.read_text(encoding="utf-8")).get("units", [])
    lesson_index = {}
    for path in (ROOT / "lessons").glob("*/*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            lesson_index[data["id"]] = (path, data)
    changed = 0
    updated_records = 0
    for sample in samples:
        lesson_id = sample.get("lessonId")
        resolved = lesson_index.get(lesson_id)
        if resolved is None and isinstance(lesson_id, str) and lesson_id.startswith("lesson-"):
            resolved = lesson_index.get(lesson_id)
        if resolved is None:
            continue
        path, lesson = resolved
        records = {str(item.get("publisher")): item for item in lesson.get("publisherResearch", []) if isinstance(item, dict) and item.get("publisher")}
        for source in sample.get("sources", []):
            publisher = source.get("publisher")
            if publisher not in {"nani", "kanghsuan", "hanlin"}:
                continue
            record = dict(records.get(publisher, {}))
            record.update({
                "publisher": publisher,
                "edition": f"{publisher} 公立校方章節級交叉證據（{lesson.get('subject', 'unknown')}）",
                "subject": lesson.get("subject"),
                "chapterLocator": source.get("locator") or f"{lesson.get('title', lesson_id)}；章節級樣本定位。",
                "sourceUrl": source.get("sourceUrl"),
                "access": "public-open",
                "reviewedAt": source.get("accessedAt", "2026-09-21"),
                "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"],
                "outcome": f"記錄{publisher}公立校方或官方公開結構對「{lesson.get('title', lesson_id)}」的章節定位、概念表徵與評量方向；正文、例題、題目、答案與互動仍為本專案獨立撰寫，三版本融合審查尚未完成。",
                "copyrightBoundary": "只保留公開章節定位、教學結構與評量方向；不複製出版社或校方教材正文、圖片、題目、答案、影音或版面。",
            })
            records[publisher] = record
            updated_records += 1
        ordered = sorted(records.values(), key=lambda item: str(item.get("publisher", "")))
        if ordered != lesson.get("publisherResearch", []):
            lesson["publisherResearch"] = ordered
            path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(json.dumps({"changedLessons": changed, "updatedPublisherRecords": updated_records, "sampleUnitsSeen": len(samples)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
