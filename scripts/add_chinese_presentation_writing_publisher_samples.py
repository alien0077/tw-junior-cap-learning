#!/usr/bin/env python3
"""Record public-school publisher evidence for presentation and writing units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版報告、演說、論辯與寫作表達定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版口語發表、科技表達與寫作歷程定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 2-Ⅳ-5、6-Ⅳ-1、6-Ⅳ-2，採報告演說、標點與寫作歷程評量。"),
]
UNITS = [
    ("lesson-chinese-performance-2-iv-5", "2-Ⅳ-5：報告評論演說與論辯", ["報告", "評論", "演說", "論辯"], "把主題、受眾、證據和時間限制轉成可講述的結構，透過開場定位、段落轉承、圖表說明與結尾回扣完成報告或演說；評論時同時指出內容與表達的依據。", "只評口才會忽略證據；需分開檢查主張是否成立、組織是否清楚、語音是否可懂，以及回應提問是否準確。"),
    ("lesson-chinese-performance-6-iv-1", "6-Ⅳ-1：善用標點增進情感與說服", ["標點", "語氣", "節奏", "說服"], "把標點視為讀者理解的路標：依句間關係、停頓長短與語氣轉折安排標點，再朗讀檢查情感是否被放大或論旨是否被誤讀。", "標點不是裝飾或越多越好；需比較替換前後的句意、語氣與邏輯，確認每個符號都有可說明的功能。"),
    ("lesson-chinese-performance-6-iv-2", "6-Ⅳ-2：審題立意取材組織遣詞修訂成文", ["審題", "立意", "取材", "修訂"], "先圈出題目的限制與任務，再形成可回答的中心觀點，選擇能支撐觀點的材料，以段落功能安排順序，最後從內容、結構、語句和格式多輪修訂。", "寫得很多不等於切題；需把每段回扣題目要求，刪除沒有功能的細節，並用具體修改說明文章如何變得更清楚。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id,
            "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred thirty-eight unit samples", "Seven hundred forty-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
