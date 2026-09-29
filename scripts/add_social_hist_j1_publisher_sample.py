#!/usr/bin/env python3
"""Record public-school publisher evidence for social history J-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列全球化、國際組織、科技與當代社會議題。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列全球化、科技、國際參與與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 J-IV-1，採圖表、史料、討論與紙筆評量。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    lesson_id = "lesson-social-content-hist-j-iv-1"
    title = "歷 J-Ⅳ-1：全球化與當代社會"
    core = ["全球化", "國際組織", "科技變遷", "公共議題"]
    units[lesson_id] = {"lessonId": lesson_id, "title": title, "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": ["以全球流動、科技、國際組織與公共議題資料分析跨尺度互動。"], "observedAssessment": ["要求區分全球連結、權力差異、科技影響與政策回應，並以資料支持結論。"], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES], "fusionReview": {"commonCore": core, "differencesToReview": ["南一偏重全球化與國際組織，康軒連結科技與國際參與，翰林以圖表與史料探究當代議題。"], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"}}
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"]); data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Six hundred twenty-four unit samples", "Six hundred twenty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 1}, ensure_ascii=False))

if __name__ == "__main__": main()
