#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Qb-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列全球化、科技、環境與當代社會議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列全球議題、科技治理、公共參與與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Qb-IV-1～3，採圖表、史料、討論與紙筆評量。"),
]
UNITS = [
    ("qb-iv-1", "歷 Qb-Ⅳ-1：全球化、科技與生活", ["全球化", "科技", "生活變遷", "勞動與消費"], "以科技、產業、媒體與生活資料，分析全球化如何改變勞動、消費、溝通與日常生活。", "不能以便利性代表所有人的生活改善，需辨識數位落差、勞動條件與環境成本。"),
    ("qb-iv-2", "歷 Qb-Ⅳ-2：全球環境與社會責任", ["全球環境", "社會責任", "資源分配", "永續治理"], "比較環境資料、政策與利害關係人觀點，評估全球環境責任的分配與治理選擇。", "要分開科學觀察、責任推論與價值主張，不能把責任平均分配給所有人。"),
    ("qb-iv-3", "歷 Qb-Ⅳ-3：當代社會行動探究", ["當代社會", "行動探究", "公共參與", "成效評估"], "從議題、行動方案、資料與結果評估當代社會行動，提出可檢驗且標示限制的結論。", "需區分行動目標、過程證據與長期成效，避免把倡議口號當成政策結果。"),
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
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred forty-six unit samples", "Six hundred forty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
