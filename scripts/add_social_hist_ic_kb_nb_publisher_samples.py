#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Ic, Kb and Nb."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版社會文化調適、現代國家挑戰與普世宗教發展定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版社會文化變遷、國家挑戰與宗教文化發展定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 Ic、Kb、Nb 的社會文化調適、國家挑戰與普世宗教，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("ic", "Ic：社會文化調適變遷", ["社會文化", "制度調適", "身分認同", "日常生活"], "比較家庭、教育、宗教、媒體與社會運動資料，分析社會文化如何在制度變遷與跨域交流中調適、延續或產生衝突。", "不能用少數精英文本代表所有社會；需納入日常生活、性別、階級、族群與地方差異。"),
    ("kb", "Kb：現代國家的挑戰", ["國家治理", "民主與權利", "經濟危機", "社會分歧"], "從戰爭、經濟危機、民主制度、社會運動與全球化資料，分析現代國家面對的治理挑戰與回應，並檢視權利與安全的取捨。", "國家提出的解決方案不一定代表所有公民利益；要區分政策目標、執行結果與被排除者的聲音。"),
    ("nb", "Nb：普世宗教起源發展", ["宗教起源", "信仰傳播", "制度化", "社會影響"], "比較普世宗教的起源情境、經典與組織發展，追蹤信仰如何經由商路、移民與政治權力傳播，並分析其社會整合與衝突作用。", "不能把宗教只當作抽象教義或單一文化標籤；需區分信仰實踐、制度權威、地方轉化與不同信徒經驗。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred ninety-one unit samples", "Six hundred ninety-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
