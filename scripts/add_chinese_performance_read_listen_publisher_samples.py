#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese reading and listening units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版閱讀總綱、同理聆聽與聲情辨識定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版閱讀學習、聆聽歸納與情境回應定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列閱讀、1-Ⅳ-1、1-Ⅳ-2，採聆聽記錄、聲情判讀、文本閱讀與紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-performance-5", "閱讀", ["閱讀理解", "文本策略", "證據整合", "跨文本"], "依文本目的、文體與問題選擇定位、預測、提問、統整、查證和反思策略，將字句、段落、圖表及背景知識整合成可驗證理解。", "閱讀不是只找關鍵字；需回指文本證據，說明策略選擇與推論限制，並辨認不同文本的立場。"),
    ("lesson-chinese-performance-1-iv-1", "1-Ⅳ-1：同理聆聽並記錄歸納", ["聆聽理解", "觀點記錄", "同理回應", "摘要歸納"], "在聆聽時區分說話者的事實、感受、需求與觀點，以關鍵詞和結構筆記保留脈絡，再用自己的話摘要並回應。", "把自己的意見寫進摘要會扭曲原話；需區分轉述、推論與回應，並保留語氣和重要條件。"),
    ("lesson-chinese-performance-1-iv-2", "1-Ⅳ-2：依情境辨識聲情與表達技巧並回應", ["聲情辨識", "語速重音", "情境判讀", "適切回應"], "比較語速、重音、停頓、音量與語氣如何配合說話情境和目的，判斷聲音線索與文字內容是否一致，再提出適切回應。", "只聽出情緒標籤不夠；需說明聲音證據、情境、說話者關係與回應是否尊重對方目的。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred twenty-nine unit samples", "Seven hundred thirty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
