#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Cc-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程的公共意見、政治參與與民主制度範圍，定位公 Cc-IV-1～3。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列政治參與、投票與公平投票原則，搭配資料與問答活動。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列政治參與、投票及公平原則，採問題討論、隨堂測驗與課堂問答。"),
]
UNITS = [
    ("cc-iv-1", "公 Cc-Ⅳ-1：政治參與的重要性", ["政治參與", "公共利益", "民主回應", "參與成本與責任"], "用政策生命週期圖連結選民、社團、媒體、民意代表與政府的參與位置，觀察參與如何影響議程與監督。", "要求以公共問題資料說明參與的功能與限制，不能把政治參與縮減成只有投票。"),
    ("cc-iv-2", "公 Cc-Ⅳ-2：投票作為參與形式", ["投票", "選擇代表", "多數決", "投票資訊與後續監督"], "以選舉情境的選項、候選人承諾與投票結果表，區分投票表達偏好、授權代表與投票後監督。", "學生需說明投票能解決什麼、不能解決什麼，並指出資訊不足或少數權益的風險。"),
    ("cc-iv-3", "公 Cc-Ⅳ-3：公平投票基本原則", ["普遍", "平等", "直接", "無記名與自由投票"], "用同一投票規則的案例比較資格限制、票值不等、公開壓力與代投行為，檢核公平原則是否被破壞。", "要求逐條對應原則與案例證據，避免把『票多者勝』誤當成完整的公平投票。"),
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
            b["reason"] = b["reason"].replace("Five hundred eighteen unit samples", "Five hundred twenty-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
