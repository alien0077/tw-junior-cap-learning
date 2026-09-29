#!/usr/bin/env python3
"""Record public-school publisher evidence for social history L, La and Lb."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的當代東亞、共產政權與不同陣營互動定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的東亞局勢、共產政權與國際陣營互動定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 L、La、Lb 的東亞局勢、政權發展與陣營互動，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("l", "L：當代東亞的局勢", ["東亞秩序", "冷戰背景", "國家發展", "區域互動"], "以戰後時間軸、地圖與外交及經濟資料，分析東亞局勢如何受全球對抗、國家選擇與區域互動共同塑造。", "不能把東亞變化簡化為外部大國的棋局；需辨識地方行動者、國內政治與跨境社會力量。"),
    ("la", "La：共產政權在中國", ["政權建立", "革命與治理", "社會政策", "歷史記憶"], "比較革命動員、政權建立、經濟與社會政策的資料，分析共產政權在中國的治理方式與社會後果，並區分官方敘事和其他記錄。", "不能以單一政策結果概括所有時期與地區；要交代政策目標、執行差異、受影響群體與證據限制。"),
    ("lb", "Lb：不同陣營互動", ["陣營競合", "外交與安全", "經濟援助", "跨國影響"], "透過條約、宣傳、援助、軍事與貿易資料，比較不同陣營如何競爭與合作，並分析國際政策如何在地方被重新解讀與執行。", "不能把陣營標籤當成完整解釋；需區分正式政策、地方實踐、利益衝突及一般人民承擔的後果。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred seventy-six unit samples", "Six hundred seventy-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
