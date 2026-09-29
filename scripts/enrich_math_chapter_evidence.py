#!/usr/bin/env python3
"""Enrich math lesson publisher records from exact existing mapping evidence.

Only lessons whose Knowledge ID is found in all three publisher mappings are
updated. No textbook text, examples, answers, or publisher status is copied or
promoted; this is chapter-location evidence enrichment.
"""
from __future__ import annotations

import json
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHERS = ("nani", "kanghsuan", "hanlin")


def collect_mappings():
    by_kg = {}
    for path in glob.glob(str(ROOT / "textbook-mapping" / "math" / "*.json")):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for volume in data.get("volumes", []):
            for entry in volume.get("entries", []):
                for kg in entry.get("knowledgeIds", []):
                    by_kg.setdefault(kg, {}).setdefault(data.get("publisher"), []).append({
                        "path": str(Path(path).relative_to(ROOT)),
                        "source": data.get("source", {}),
                        "entry": entry,
                    })
    return by_kg


def main():
    mappings = collect_mappings()
    updated = []
    for path in sorted((ROOT / "lessons" / "math").glob("*.json")):
        lesson = json.loads(path.read_text(encoding="utf-8"))
        candidates = {}
        for kg in lesson.get("knowledgeIds", []):
            for publisher, rows in mappings.get(kg, {}).items():
                candidates.setdefault(publisher, []).extend(rows)
        if not all(publisher in candidates for publisher in PUBLISHERS):
            continue
        records = {row.get("publisher"): row for row in lesson.get("publisherResearch", [])}
        if not all(publisher in records for publisher in PUBLISHERS):
            continue
        for publisher in PUBLISHERS:
            mapping = candidates[publisher][0]
            source = mapping["source"]
            entry = mapping["entry"]
            record = records[publisher]
            source_url = source.get("url")
            if not source_url:
                continue
            record["sourceUrl"] = source_url
            record["chapterLocator"] = (
                f"{entry.get('chapterCode', '')} {entry.get('chapterLabel', '')}; "
                f"{source.get('locator', '')}；mapping file {mapping['path']}"
            ).strip()
            record["reviewedAt"] = "2026-09-07"
            record["outcome"] = (
                record.get("outcome", "").rstrip("。")
                + f"；本次以既有 mapping 的可追溯章節條目補強定位：{entry.get('chapterLabel', '')}。"
            )
            record["copyrightBoundary"] = (
                record.get("copyrightBoundary", "").rstrip("。")
                + " 本次只補記章節定位與來源 metadata，不複製教材文字、圖片、題目、答案或版面。"
            )
        lesson["publisherResearch"] = [records[p] for p in PUBLISHERS]
        for record in lesson.get("versionResearch", []):
            publisher = record.get("publisher")
            if publisher not in candidates:
                continue
            mapping = candidates[publisher][0]
            source_url = mapping["source"].get("url")
            if source_url:
                record["sourceLocator"] = f"{source_url}；{mapping['entry'].get('chapterCode', '')} {mapping['entry'].get('chapterLabel', '')}；{mapping['source'].get('locator', '')}"
                record["reviewedAt"] = "2026-09-07"
        path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        updated.append({"lessonId": lesson.get("id"), "title": lesson.get("title"), "publishers": list(PUBLISHERS)})
    report = {
        "updatedAt": "2026-09-07",
        "updatedLessonCount": len(updated),
        "lessons": updated,
        "status": "chapter-location-enriched-pending-fusion-review",
        "boundary": "Existing school-plan and official publisher mapping metadata only; no publisher text was copied and no global publisherEvidence/spec status was promoted.",
    }
    out = ROOT / "implementation" / "reports" / "math-chapter-evidence-enrichment.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"updatedLessonCount": len(updated), "status": report["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
