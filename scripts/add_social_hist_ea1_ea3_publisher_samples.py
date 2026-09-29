#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Ea-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列近代東亞政權、殖民變動、臺灣與區域互動。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列近代東亞、殖民、民族國家與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 Ea-IV-1～3，採時間線、地圖、史料、討論與紙筆評量。"),
]
UNITS = [
    ("ea-iv-1", "歷 Ea-Ⅳ-1：近代東亞政權變動", ["近代東亞", "政權變動", "民族國家", "制度改革"], "比較近代東亞政權、改革與戰爭資料，分析制度轉型、國家競爭與社會變動的相互作用。", "不能把改革或戰爭只寫成領袖決定，需檢查制度、社會群體與國際環境。"),
    ("ea-iv-2", "歷 Ea-Ⅳ-2：殖民與地方社會", ["殖民統治", "地方社會", "資源與勞動", "文化治理"], "從行政、教育、資源與地方生活資料，判讀殖民治理如何改變社會並引發不同形式的回應。", "要區分統治政策、地方執行與人民經驗，不能以單一官方資料代表全部社會。"),
    ("ea-iv-3", "歷 Ea-Ⅳ-3：臺灣與東亞互動", ["臺灣史", "東亞互動", "人口與貿易", "文化交流"], "用人口、貿易、制度與文化資料追蹤臺灣與東亞互動，分析流動、權力與地方選擇。", "需標示時期與行動者，避免把臺灣或東亞視為固定且單一的主體。"),
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
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred unit samples", "Six hundred three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
