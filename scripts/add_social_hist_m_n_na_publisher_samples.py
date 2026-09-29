#!/usr/bin/env python3
"""Record public-school publisher evidence for social history M, N and Na."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史探究展演、古代文化遺產與多元並立文化定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史探究、古代文明與多元文化發展定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 M、N、Na 的探究展演、古代文化遺產與多元並立，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("m", "M：歷史考察（四）", ["探究設計", "文化遺產", "地方踏查", "展演與反思"], "從古代文化遺產或地方記憶選定問題，建立遺址、器物、文本與口述資料的證據鏈，再以展演回應問題並揭露研究限制。", "展演形式不能取代證據；需說明保存狀況、資料來源、詮釋取捨與當代社群的權利。"),
    ("n", "N：古代文化的遺產", ["古代文明", "文化遺產", "制度與思想", "跨域傳播"], "比較古代制度、思想、技術與藝術如何留下可辨識的文化遺產，並追蹤它們在不同時代與地區被保存、轉譯或重新使用的過程。", "不能把遺產當作靜止的名物清單；需辨識保存者、使用者、權力關係與後世重新賦義。"),
    ("na", "Na：多元並立古代文化", ["多元文明", "區域互動", "文化交流", "比較視角"], "用城市、文字、宗教、科技與制度資料比較多個古代文化並立的條件，分析交流如何帶來借用、混合與衝突，而非只有單向傳播。", "比較時不能只看相似表面；要控制時間、地理與社會層次，並說明哪些差異來自資料不足。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id,
            "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {
                    "publisher": publisher,
                    "sourceUrl": url,
                    "sourceKind": "public-school-course-plan-identifying-publisher-material",
                    "locator": locator,
                    "accessedAt": "2026-09-21",
                    "observedConcepts": [title, *core],
                    "observedRepresentations": [representation],
                    "observedAssessment": [assessment],
                    "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
                }
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {
                "commonCore": core,
                "differencesToReview": [representation, assessment],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Six hundred seventy-nine unit samples", "Six hundred eighty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
