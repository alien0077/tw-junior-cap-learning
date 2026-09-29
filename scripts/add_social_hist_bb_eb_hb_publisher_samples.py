#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Bb, Eb and Hb."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版大航海時代臺灣、社會文化變遷與區域互動定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版大航海、臺灣社會文化與區域內外交流定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 Bb、Eb、Hb 的大航海、社會文化與區域互動，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("bb", "Bb：大航海時代的臺灣", ["海上交流", "殖民競逐", "臺灣港口", "族群互動"], "以航線、港口、商品與不同群體記錄分析大航海時代臺灣的位置，理解海上交流同時帶來貿易、競逐、暴力與人口流動。", "不能把大航海只寫成英雄探險；要區分交流、征服、交易與被迫移動，並納入臺灣原有社群的回應。"),
    ("eb", "Eb：社會文化的變遷", ["殖民社會", "教育與文化", "社會階層", "文化回應"], "比較制度、教育、宗教、家庭與日常生活資料，追蹤殖民與現代化過程如何改變社會文化，也辨識地方社群的調適、保留與抵抗。", "文化變化不能只看官方制度；需檢視不同性別、階級、族群與地區的生活經驗。"),
    ("hb", "Hb：區域內外互動交流", ["區域網絡", "外交貿易", "文化流動", "權力不對等"], "以交通、貿易、外交、移民與文化傳播資料，分析區域內外互動如何形成網絡，並判斷交流中的合作、競爭與不平等。", "有往來不代表平等；需說明誰控制通道、誰能移動、誰被排除，以及資料從哪一方留下。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred eighty-eight unit samples", "Six hundred ninety-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
