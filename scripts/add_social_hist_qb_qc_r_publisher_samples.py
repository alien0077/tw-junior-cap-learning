#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Qb, Qc and R."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版帝國主義、戰爭與現代社會、歷史考察定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版帝國擴張、戰爭社會與歷史探究定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 Qb、Qc、R 的帝國主義、戰爭與現代社會、探究展演，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("qb", "Qb：帝國主義興起影響", ["帝國主義", "殖民擴張", "資源與勞動", "地方回應"], "比較帝國政策、貿易、軍事、人口與殖民地資料，分析帝國主義如何重組全球權力與資源，也納入被統治社會的回應與抵抗。", "不能只把帝國主義解釋為單一國家的野心；需同時分析資本、科技、制度、地方合作者與被剝削者。"),
    ("qc", "Qc：戰爭與現代社會", ["現代戰爭", "總體動員", "科技與暴力", "難民與記憶"], "從戰場、後勤、宣傳、平民生活、難民與戰後記憶資料，分析現代戰爭如何動員整個社會，並辨識科技、國家與個人責任。", "不能只以戰役勝負代表戰爭影響；要納入平民、殖民地、女性、兒童、難民與環境的經驗。"),
    ("r", "R：歷史考察（六）", ["綜合探究", "問題與證據", "公共溝通", "反思修正"], "從主題 Q 的現代世界議題提出研究問題，整合多重史料、統計、口述或地方踏查，經過同儕檢核後以展演或報告呈現並修正。", "成果不能只看形式與篇幅；必須能追溯問題、證據、推理、反例、版權界線與修正歷程。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id,
            "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {
                    "publisher": publisher,
                    "sourceUrl": url,
                    "sourceKind": "public-school-course-plan-identifying-publisher-material",
                    "locator": locator,
                    "accessedAt": "2026-09-21",
                    "observedConcepts": [title, *core],
                    "observedRepresentations": [representation],
                    "observedAssessment": [assessment],
                    "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
                }
                for publisher, url, locator in SOURCES
            ],
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
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Six hundred ninety-four unit samples", "Six hundred ninety-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
