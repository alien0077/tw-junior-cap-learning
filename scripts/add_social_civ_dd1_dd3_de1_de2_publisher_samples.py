#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Dd-IV-1..3 and De-IV-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程的全球化、國際參與與科技生活範圍，定位公 Dd-IV-1～3、De-IV-1～2。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列全球化影響、臺海兩岸與國際參與，以及科技、公共事務與資訊風險。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列公 Dd-IV-1～3、De-IV-1～2，採資料蒐集、討論、報告與問答評量。"),
]
UNITS = [
    ("dd-iv-1", "公 Dd-Ⅳ-1：全球化現象與議題", ["全球化", "跨國流動", "商品與資訊網絡", "全球互賴"], "用商品、人口、資金與資訊的跨境流動圖，辨認全球化現象及其連結的生活議題。", "要求由跨境流動資料提出全球化判斷，不能把所有國際接觸都當成同一種全球化。"),
    ("dd-iv-2", "公 Dd-Ⅳ-2：全球化影響與回應評價", ["全球化影響", "受益與受損群體", "在地回應", "政策評價"], "用不同群體的利益與成本矩陣，比較全球化對消費、勞動、文化與環境的影響，再評估回應方案。", "要求明確指出評價標準、受影響者與證據，不能只以支持或反對全球化作答。"),
    ("dd-iv-3", "公 Dd-Ⅳ-3：臺海兩岸關係與國際參與", ["臺海兩岸關係", "國際參與", "交流與安全", "多重立場"], "用時間線與利害關係人圖呈現兩岸交流、國際組織與安全議題的交互影響，區分事實、立場與政策選擇。", "學生需標示資料來源與觀點位置，避免把單一政治立場當成唯一事實。"),
    ("de-iv-1", "公 De-Ⅳ-1：科技改變日常生活", ["科技創新", "生活型態", "生產與學習", "科技機會與代價"], "以同一日常活動的前後流程，追蹤科技如何改變時間、勞動、資訊取得與人際互動。", "要求同時描述便利與新限制，並以生活資料說明改變，不把科技進步等同無條件改善。"),
    ("de-iv-2", "公 De-Ⅳ-2：科技對公共參與與風險的影響", ["數位參與", "資訊風險", "錯誤訊息", "公共討論"], "用公共議題訊息的產製、推薦、轉傳與查核流程圖，分析科技擴大參與也可能放大偏誤與風險。", "學生需提出來源查核、隱私保護與負責任參與步驟，不能把按讚或轉發直接視為有效參與。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-civ-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator, "accessedAt": "2026-09-21",
                "observedConcepts": [title, *core],
                "observedRepresentations": [representation],
                "observedAssessment": [assessment],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            } for publisher, url, locator in SOURCES],
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
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred twenty-eight unit samples", "Five hundred thirty-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
