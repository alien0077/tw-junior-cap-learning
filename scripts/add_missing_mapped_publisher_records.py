#!/usr/bin/env python3
"""Add publisherResearch records only where existing mapping evidence is exact."""
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHERS = {"nani", "kanghsuan", "hanlin"}


def mapping_index():
    index = {}
    for path in glob.glob(str(ROOT / "textbook-mapping" / "*" / "*.json")):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        for volume in data.get("volumes", []):
            for entry in volume.get("entries", []):
                for kg in entry.get("knowledgeIds", []):
                    index.setdefault(kg, {}).setdefault(data.get("publisher"), []).append((data, entry, str(Path(path).relative_to(ROOT))))
    return index


def main():
    index = mapping_index()
    added = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        records = {record.get("publisher"): record for record in data.get("publisherResearch", [])}
        missing = []
        for publisher in PUBLISHERS - set(records):
            matches = []
            for kg in data.get("knowledgeIds", []):
                matches.extend(index.get(kg, {}).get(publisher, []))
            if matches:
                missing.append((publisher, matches[0]))
        if not missing:
            continue
        for publisher, (mapping, entry, mapping_path) in missing:
            source = mapping.get("source", {})
            if not source.get("url"):
                continue
            records[publisher] = {
                "publisher": publisher,
                "edition": f"{publisher} 公開章節 mapping metadata（{mapping.get('academicYear', '現行')}）",
                "subject": data.get("subject"),
                "chapterLocator": f"{entry.get('chapterCode', '')} {entry.get('chapterLabel', '')}；{source.get('locator', '')}；mapping file {mapping_path}",
                "sourceUrl": source["url"],
                "access": "public-open",
                "reviewedAt": "2026-09-07",
                "researchScope": ["teaching-sequence", "concept-progression", "activity-pattern", "assessment-pattern"],
                "outcome": "公開 mapping 可核對本課對應的版本章節名稱與教材定位；此記錄只保存章節 metadata，不宣稱已取得或讀完出版社完整教材。",
                "copyrightBoundary": "只使用校方／出版社公開 mapping 的章節定位與版本 metadata；不複製教材正文、圖片、例題、習題、答案或版面，lesson 內容維持原創。",
            }
        data["publisherResearch"] = [records[p] for p in sorted(records)]
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        added.append({"lessonId": data.get("id"), "path": str(path.relative_to(ROOT)), "publishers": [publisher for publisher, _ in missing]})
    report = {"updatedAt": "2026-09-07", "updatedLessonCount": len(added), "recordsAdded": sum(len(row["publishers"]) for row in added), "lessons": added, "status": "mapped-publisher-records-added-pending-fusion"}
    (ROOT / "implementation" / "reports" / "mapped-publisher-record-additions.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("updatedLessonCount", "recordsAdded", "status")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
