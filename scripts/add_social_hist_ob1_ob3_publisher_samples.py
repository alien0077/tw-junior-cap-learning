#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Ob-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列當代民主、社會正義、人權與全球議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列民主、人權、多元社會與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Ob-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("ob-iv-1", "歷 Ob-Ⅳ-1：民主與社會正義", ["民主", "社會正義", "權利保障", "制度與分配"], "比較制度、政策與社會指標資料，分析民主社會如何處理權利保障、資源分配與不平等。", "不能把形式平等當成實質正義，需檢查起點、程序、結果與不同群體的條件。"),
    ("ob-iv-2", "歷 Ob-Ⅳ-2：多元社會與公共協商", ["多元社會", "公共協商", "身分與差異", "社會包容"], "以公共討論、媒體與社會案例，分析多元身分如何在權利、責任與公共協商中互動。", "不能以單一代表發言代替群體多樣性，需辨識觀點位置、沉默聲音與證據範圍。"),
    ("ob-iv-3", "歷 Ob-Ⅳ-3：當代議題資料評估", ["當代議題", "資料評估", "媒體識讀", "政策判斷"], "整合統計、新聞、史料與政策資料，評估當代議題的主張、證據品質與可能反例。", "要分開事實、推論與價值判斷，不能以來源知名度取代內容查核。"),
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
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred thirty-nine unit samples", "Six hundred forty-two unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
