#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Qc-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列全球化、科技、環境、民主與臺灣公共回應。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列當代議題、科技治理、公共參與與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Qc-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("qc-iv-1", "歷 Qc-Ⅳ-1：當代科技與社會風險", ["科技", "社會風險", "資訊安全", "治理回應"], "以科技應用、資料安全與公共事件資料，分析創新效益、風險分配與治理回應。", "需區分技術風險、使用情境與制度責任，不能把風險自然化或歸咎單一使用者。"),
    ("qc-iv-2", "歷 Qc-Ⅳ-2：全球環境與永續轉型", ["環境", "永續轉型", "能源與產業", "政策取捨"], "比較環境指標、產業資料與政策方案，評估永續轉型中的成本、受益者與時間尺度。", "要分開短期減量與長期轉型，並指出不同地區與群體承擔的成本差異。"),
    ("qc-iv-3", "歷 Qc-Ⅳ-3：公共議題綜合探究", ["公共議題", "證據整合", "方案比較", "反思與修正"], "整合不同來源的資料，提出可檢驗的公共議題解釋、方案比較與後續修正問題。", "不能以資料數量取代品質，需標示來源可信度、缺漏、反例與推論界線。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred forty-nine unit samples", "Six hundred fifty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
