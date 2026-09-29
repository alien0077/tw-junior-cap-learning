#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese writing techniques and genres."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版仿寫、改寫、實用文本與創作表達定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版寫作技巧、文本任務與作品發表定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 6-Ⅳ-3、6-Ⅳ-4、6-Ⅳ-5，採仿寫改寫、功能文本與創作發表評量。"),
]
UNITS = [
    ("lesson-chinese-performance-6-iv-3", "6-Ⅳ-3：仿寫改寫等技巧", ["仿寫", "改寫", "文體轉換", "語氣控制"], "先辨識原文的敘述視角、段落功能與語氣，再只改動指定變項；完成後對照原文與新稿，說明哪些效果被保留、哪些因改寫而改變。", "換掉幾個詞不算改寫；必須保留任務核心並交代改動規則，避免把原作句段直接搬用。"),
    ("lesson-chinese-performance-6-iv-4", "6-Ⅳ-4：依需求書寫各類文本", ["功能文本", "受眾", "格式", "資訊完整"], "先確認文本用途與讀者，再選擇書信、報告、公告、說明或評論的結構與語域；以必要資訊、可操作指示和格式線索檢查讀者能否完成任務。", "文體名稱不是格式本身；需檢查開頭、資訊順序、稱謂或標題、行動要求與結尾是否符合真實使用情境。"),
    ("lesson-chinese-performance-6-iv-5", "6-Ⅳ-5：主動創作自訂題目表述見解發布", ["自主創作", "自訂題目", "觀點表述", "發布"], "從生活觀察或問題形成可探究的題目，選定想對話的讀者與觀點，安排材料和語氣完成作品，再依發布媒介檢查引用、版權、個資與讀者回應方式。", "自由選題不等於沒有約束；題目、觀點、材料和發布對象必須互相支撐，並清楚區分事實、感受與主張。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred forty-one unit samples", "Seven hundred forty-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
