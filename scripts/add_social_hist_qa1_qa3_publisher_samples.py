#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Qa-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列全球化、民主、人權、環境與當代公共議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列全球議題、公共治理、多元社會與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Qa-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("qa-iv-1", "歷 Qa-Ⅳ-1：全球化與多元社會", ["全球化", "多元社會", "人口流動", "文化互動"], "以人口、媒體、貿易與文化資料，分析全球化如何形成多元社會及不同群體的互動。", "不能把全球化視為單向同質化，需檢查流動方向、權力與地方改造。"),
    ("qa-iv-2", "歷 Qa-Ⅳ-2：民主、人權與全球治理", ["民主", "人權", "全球治理", "制度責任"], "比較人權規範、民主制度與全球治理資料，評估制度承諾、實際保障與責任分配。", "需區分法律文本、執行成效與群體經驗，不能以單一制度名稱證明權利已被保障。"),
    ("qa-iv-3", "歷 Qa-Ⅳ-3：當代議題整合探究", ["當代議題", "資料整合", "政策評估", "多元觀點"], "整合統計、史料、新聞與政策資料，建立可追溯的當代議題解釋和行動評估。", "要分開證據、推論、價值與方案，並說明資料缺漏、反例與不確定性。"),
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
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred forty-three unit samples", "Six hundred forty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
