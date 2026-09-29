#!/usr/bin/env python3
"""Record public-school publisher evidence for social history R-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版主題 Q 歷史選題、踏查與展演定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版現代世界主題探究與地方展演定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 R-Ⅳ-1，採主題選題、史料查證、踏查、討論與展演評量。"),
]
TITLE = "歷 R-Ⅳ-1：從主題 Q 選題深入探究或踏查展演"
CORE = ["主題選題", "現代史料", "地方踏查", "展演溝通"]
REPRESENTATION = "從主題 Q 的帝國主義、戰爭或現代社會議題提出可查證問題，蒐集文本、統計、口述與地方空間資料，形成證據鏈並以展演回應。"
ASSESSMENT = "需檢核問題範圍、來源可信度、訪談與影像授權、推論界線及觀眾回饋，不能以展演形式取代歷史證據。"

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    lesson_id = "lesson-social-content-hist-r-iv-1"
    data["units"] = [x for x in data["units"] if x["lessonId"] != lesson_id]
    data["units"].append({
        "lessonId": lesson_id,
        "title": TITLE,
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": [{
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": locator,
            "accessedAt": "2026-09-21",
            "observedConcepts": [TITLE, *CORE],
            "observedRepresentations": [REPRESENTATION],
            "observedAssessment": [ASSESSMENT],
            "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
        } for publisher, url, locator in SOURCES],
        "fusionReview": {
            "commonCore": CORE,
            "differencesToReview": [REPRESENTATION, ASSESSMENT],
            "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
        },
    })
    data["units"] = sorted(data["units"], key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Six hundred ninety-seven unit samples", "Six hundred ninety-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 1}, ensure_ascii=False))

if __name__ == "__main__":
    main()
