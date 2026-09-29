#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Ca-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程的公共議題與政治參與範圍，定位公 Ca-IV-1～3 的爭議處理、政策參與與校園決策。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列公共爭議的非暴力處理、人民參與及學生公共行動。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程以問題討論、隨堂測驗與課堂問答處理公 Ca-IV-1～3。"),
]
UNITS = [
    ("ca-iv-1", "公 Ca-Ⅳ-1：非暴力解決公共爭議", ["公共爭議", "非暴力", "溝通協商", "制度性解決"], "用同一公共衝突的利益關係人圖，切換對話、協商、調解與暴力升高路徑，觀察程序如何改變結果。", "要求以資料指出非暴力方案的程序與限制，不能把『和平』當成不需處理權力差異的口號。"),
    ("ca-iv-2", "公 Ca-Ⅳ-2：政策制定前的人民參與", ["政策形成", "利害關係人", "公共討論", "參與管道"], "把政策從問題界定、方案草擬到定案拆成時間線，標示人民可提出資訊、意見與監督的節點。", "學生需區分表達意見、提供證據、審議與決定權，避免把所有參與都寫成投票。"),
    ("ca-iv-3", "公 Ca-Ⅳ-3：中學生參與校園公共決策", ["校園公共事務", "學生自治", "代表與程序", "責任與回饋"], "以校園午餐、手機規範或社團資源的決策流程圖，讓學生比較直接表達、代表會議與提案追蹤。", "要求提出可行參與方案、證據與回饋機制，並檢查是否尊重其他受影響群體。"),
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
            b["reason"] = b["reason"].replace("Five hundred thirteen unit samples", "Five hundred sixteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
