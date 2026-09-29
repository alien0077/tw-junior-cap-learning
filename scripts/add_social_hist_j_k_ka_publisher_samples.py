#!/usr/bin/env python3
"""Record public-school publisher evidence for social history J, K and Ka."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史考察、現代國家興起與現代國家追求定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史探究、民族國家形成與制度建構定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 J、K、Ka 的史料探究、現代國家形成與國家追求，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("j", "J：歷史考察（三）", ["研究問題", "多重史料", "比較尺度", "歷史表達"], "以現代國家形成或制度變遷為題，整合法律、統計、地圖與個人記錄，檢查不同尺度的證據是否支持同一歷史解釋。", "不能因資料看似一致就忽略生成背景；要說明材料的時間、目的、讀者與不可回答的問題。"),
    ("k", "K：現代國家的興起", ["民族國家", "主權與疆界", "國家制度", "身份形成"], "比較主權、疆界、法律、教育與國民身分的形成，分析現代國家如何建立治理能力，也檢視國家分類對地方社群的影響。", "國家建立不只是一紙宣告；需區分制度設計、行政能力、地方接受與被排除者的經驗。"),
    ("ka", "Ka：現代國家的追求", ["國家建構", "改革方案", "公民身分", "權利與責任"], "從憲政、教育、軍事、經濟與公民權資料比較不同國家建構方案，判斷追求國家能力時如何調整權利、責任與社會整合。", "不能把國家強大等同人民自由或平等增加；要分開國家能力、權利分配與社會動員的效果。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred seventy-three unit samples", "Six hundred seventy-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
