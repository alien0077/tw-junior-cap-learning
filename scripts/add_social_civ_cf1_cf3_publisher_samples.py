#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Cf-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程市場競爭範圍，定位公 Cf-IV-1～3。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列競爭對消費者影響、競爭方式與市場進入。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列公 Cf-IV-1～3，採分組討論、紙筆測驗與課堂問答。"),
]
UNITS = [
    ("cf-iv-1", "公 Cf-Ⅳ-1：廠商競爭對消費者的影響", ["價格與品質", "選擇增加", "創新", "消費者剩餘與限制"], "用同一商品在廠商數量改變前後的價格、品質、選擇與服務資料，分辨競爭帶來的利益與可能的資訊限制。", "要求由資料指出消費者受益的面向及未必改善的條件，不能把競爭直接等同所有結果都更好。"),
    ("cf-iv-2", "公 Cf-Ⅳ-2：廠商競爭方式", ["價格競爭", "品質與服務", "廣告與品牌", "差異化"], "把廠商策略放入競爭矩陣，比較降價、提升品質、促銷、品牌與服務如何改變消費者選擇與成本。", "學生需連結策略、目標與可觀察結果，避免將任何行銷活動都稱為價格競爭。"),
    ("cf-iv-3", "公 Cf-Ⅳ-3：市場進入與競爭程度", ["進入障礙", "市場集中", "潛在競爭", "競爭程度"], "用市場進入成本、廠商數量與市場占有率資料，推論新廠商容易或困難進入時對競爭程度的影響。", "要求分開市場占有率、進入障礙與實際競爭行為，避免只用廠商數量作單一結論。"),
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
            b["reason"] = b["reason"].replace("Five hundred twenty-one unit samples", "Five hundred twenty-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
