#!/usr/bin/env python3
"""Record public-school publisher evidence for social history P, Q and Qa."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史考察、現代世界發展與現代國家建立定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史探究、現代世界與國家建立定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 P、Q、Qa 的歷史探究、現代世界與國家建立，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("p", "P：歷史考察（五）", ["現代史料", "研究設計", "公共記憶", "證據表達"], "以現代世界或國家建立為題，設計可追溯的史料研究，將新聞、統計、口述與制度文件互相核對，再以清楚的證據鏈表達結論。", "現代資料不等於客觀資料；需注意作者、發布機構、時間、選樣與未被記錄的群體。"),
    ("q", "Q：現代世界的發展", ["世界大戰", "國際秩序", "科技社會", "全球化"], "以戰爭、國際組織、科技、經濟與社會運動資料，分析現代世界秩序的形成與重組，並比較全球事件在不同地區的時間差與影響。", "不能用單一事件解釋整個現代世界；要區分長期結構、短期決策、地方回應與跨國連鎖效應。"),
    ("qa", "Qa：現代國家建立", ["國家建立", "民族認同", "制度治理", "公民權利"], "比較不同現代國家的建構路徑，從憲法、疆界、教育、軍事與公民權資料分析國家認同如何形成及其排除效果。", "國家統一、制度穩定與公民平等不是同一件事；需檢視少數、殖民地、女性與異議者的制度位置。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred eighty-five unit samples", "Six hundred eighty-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
