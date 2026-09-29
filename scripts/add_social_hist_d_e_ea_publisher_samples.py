#!/usr/bin/env python3
"""Record public-school publisher evidence for social history D, E and Ea."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史考察、日本統治臺灣與政經變遷定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史探究、日治臺灣與制度及產業變化定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 D、E、Ea 的史料探究、殖民治理與政治經濟，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("d", "D：歷史考察（一）", ["問題形成", "史料查證", "地方觀察", "解釋與表達"], "從臺灣早期歷史提出可查證問題，選擇文字、地圖、遺址或口述資料，記錄證據限制後形成有理由的歷史解釋。", "考察不是把資料堆在一起；要區分原始材料與後設敘述，說明取樣、年代、立場及推論不確定性。"),
    ("e", "E：日本帝國時期的臺灣", ["殖民統治", "制度變化", "社會回應", "帝國與地方"], "以殖民行政、教育與警察制度、基礎建設及社會行動的資料，分析日本帝國如何治理臺灣，以及不同群體如何調適、合作或抵抗。", "不能只用現代化或壓迫其中一個單一標籤概括；需同時檢視制度受益、控制方式與地方經驗。"),
    ("ea", "Ea：政治經濟的變遷", ["殖民經濟", "產業與交通", "行政權力", "勞動與分配"], "比較土地、糖業、交通、貿易與勞動資料，追蹤殖民政策如何重組臺灣的生產與空間，並判斷成長數據背後的分配差異。", "產量或出口上升不等於普遍富裕；要把政策目標、資本控制、勞動條件與不同地區的成本分開分析。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred sixty-one unit samples", "Six hundred sixty-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
