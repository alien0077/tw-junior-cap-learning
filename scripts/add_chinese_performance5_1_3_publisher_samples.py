#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese performance 5-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版朗讀標點、句段理解與文本特色閱讀定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版閱讀流暢、句段概念與文本形式定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版 5-Ⅳ-1～5-Ⅳ-3 的朗讀、句段理解、文本形式與紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-performance-5-iv-1", "5-Ⅳ-1：標點效果與流暢有感朗讀", ["標點功能", "語氣節奏", "朗讀流暢", "情感理解"], "比較停頓、重音、語速與標點安排，從朗讀差異回看句意、語氣和情感，不把標點只當成形式規則。", "朗讀好聽不等於理解正確；需用句法、標點與上下文說明停頓和語氣選擇。"),
    ("lesson-chinese-performance-5-iv-2", "5-Ⅳ-2：理解句段主要概念及寫作目的觀點", ["句段概念", "寫作目的", "觀點判讀", "證據回指"], "先辨認句段主語、核心動作與限制條件，再連結段落位置和寫作目的，說明主要概念如何支撐作者觀點。", "主題詞不等於主要概念；需處理範圍、因果、轉折與作者意圖，並回指完整句段證據。"),
    ("lesson-chinese-performance-5-iv-3", "5-Ⅳ-3：理解文本內容形式與寫作特色", ["內容形式", "文體特徵", "表達手法", "文本效果"], "把文本說了什麼和怎麼說分開觀察，分析敘述、說明、議論或抒情手法如何造成資訊效果、情感效果與說服效果。", "列出修辭或文體名稱不代表完成分析；需說明形式如何改變讀者理解，並以文本細節支持。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred twenty-three unit samples", "Seven hundred twenty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
