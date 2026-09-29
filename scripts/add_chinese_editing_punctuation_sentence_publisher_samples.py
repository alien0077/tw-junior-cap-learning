#!/usr/bin/env python3
"""Record public-school publisher evidence for digital editing, punctuation and syntax."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版科技編輯、標點與句型表意定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版數位編輯、標點語氣與句式運用定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 6-Ⅳ-6、Ac-Ⅳ-1、Ac-Ⅳ-2，採數位作品、標點與句型辨識評量。"),
]
UNITS = [
    ("lesson-chinese-performance-6-iv-6", "6-Ⅳ-6：科技編輯作品及分享見解", ["數位編輯", "版本修訂", "媒體表達", "分享回饋"], "用數位工具編排文字、圖表與媒體，保留版本變更和引用紀錄；發布前檢查可讀性、個資、授權與連結，分享後依讀者回饋修訂觀點。", "把工具功能當成作品品質會忽略內容；需說明每個媒體如何支撐觀點，並保留可追溯的來源與修改痕跡。"),
    ("lesson-chinese-punctuation-effects", "標點符號的表意效果", ["標點", "句意", "停頓", "語氣"], "比較逗號、分號、冒號、引號、破折號與問號等符號在同一句中的替換效果，從停頓、層次和語氣解釋讀者如何重新理解關係。", "只背符號名稱不能解釋效果；需回到前後分句的邏輯與朗讀節奏，證明符號改變了什麼。"),
    ("lesson-chinese-sentence-patterns", "Ac-Ⅳ-2：用句型標明事件、判斷與立場", ["句型", "事件關係", "判斷", "立場"], "把句子拆成事件參與者、時間條件、因果或轉折關係，再觀察陳述、比較、讓步、推測與評價句型如何標示說話者的判斷強度與立場。", "句子變長不代表資訊完整；需檢查主語、關係詞和評價詞是否使責任、條件與立場變得可辨識。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred forty-four unit samples", "Seven hundred forty-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
