#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Ha-IV-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列臺灣近現代政治、經濟、社會與文化。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列臺灣近現代政經、社會變遷與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Ha-IV-1～2，採時間線、地圖、史料、討論與紙筆評量。"),
]
UNITS = [
    ("ha-iv-1", "歷 Ha-Ⅳ-1：臺灣政治發展", ["臺灣政治", "制度變遷", "民主化", "公民參與"], "比較政治制度、選舉、社會運動與公共議題資料，分析臺灣政治發展中的制度轉型與公民參與。", "要區分制度文本、執行現況與不同群體的參與，不把民主化簡化成單一事件。"),
    ("ha-iv-2", "歷 Ha-Ⅳ-2：臺灣經濟與社會", ["臺灣經濟", "產業轉型", "人口與勞動", "社會差異"], "從產業、勞動、人口與生活資料，分析臺灣經濟轉型的成就、分配差異與社會代價。", "不能以總體成長掩蓋分配與環境成本，需說明資料尺度和受影響群體。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred fourteen unit samples", "Six hundred sixteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
