#!/usr/bin/env python3
"""Add traceable study-reference URLs to the four content lessons lacking them."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    "lesson-science-content-me": [
        "https://course.cyc.edu.tw/upfile/course109/sub1/14507919853792884.pdf",
        "https://www.naer.edu.tw/upload/1/16/doc/820/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1-%E8%87%AA%E7%84%B6%E7%A7%91%E5%AD%B8%E9%A0%98%E5%9F%9F.pdf",
    ],
    "lesson-social-content-hist-oa-iv-2": [
        "https://www.nani.com.tw/",
        "https://cap.rcpet.edu.tw/",
    ],
    "lesson-social-content-civ-cf": [
        "https://cap.rcpet.edu.tw/index.html",
        "https://www.nani.com.tw/",
    ],
    "lesson-english-fact-opinion": [
        "https://english.nani.com.tw/client/journal",
        "https://cap.rcpet.edu.tw/",
    ],
}


def main() -> None:
    changed = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        lesson_id = data.get("id")
        if lesson_id not in TARGETS:
            continue
        refs = list(dict.fromkeys(TARGETS[lesson_id]))
        data["studyReferences"] = refs
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append({"lessonId": lesson_id, "file": str(path.relative_to(ROOT)), "studyReferences": refs})
    report = {"updatedAt": "2026-09-07", "changedLessons": len(changed), "changed": changed, "rule": "reuse only URLs already present in the lesson's publisherResearch or official public exam/curriculum references"}
    out = ROOT / "implementation/reports/missing-study-reference-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
