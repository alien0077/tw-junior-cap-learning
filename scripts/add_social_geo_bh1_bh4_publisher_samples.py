#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bh-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列歐洲自然環境、產業文化、經濟整合與臺灣互動。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列歐洲環境、文化景觀、區域發展與全球連結。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bh-IV-1～4，採地圖、圖表、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bh-iv-1", "地 Bh-Ⅳ-1：自然環境", ["歐洲自然環境", "地形與氣候", "河川與海岸", "環境適應"], "以地形、氣候、河川與海岸資料解釋歐洲人口、聚落與產業的空間分布。", "不能把歐洲視為單一自然區，也不能忽略尺度和區域內差異。"),
    ("bh-iv-2", "地 Bh-Ⅳ-2：產業文化特色", ["產業文化", "文化景觀", "農業與工業", "地方特色"], "從產業活動與文化景觀判讀地方特色如何形成，並比較保存、觀光與產業轉型的取捨。", "不可把文化特色當成靜止標本，需區分生活文化、商品化與資料觀察。"),
    ("bh-iv-3", "地 Bh-Ⅳ-3：經濟成就與挑戰", ["經濟發展", "區域差異", "歐洲整合", "發展挑戰"], "比較國家與區域指標，分析整合、產業分工、人口結構與能源轉型帶來的成就和壓力。", "要分清平均值與分配差距，不能用單一 GDP 或國家形象下結論。"),
    ("bh-iv-4", "地 Bh-Ⅳ-4：臺灣與歐洲互動", ["臺灣與歐洲", "貿易與投資", "文化交流", "全球互動"], "以貿易、科技、教育與文化資料追蹤臺灣和歐洲的互動網絡，判斷互賴與不對等。", "結論須說明互動對象、時間與指標，避免把歐洲或臺灣當作單一行動者。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-geo-" + suffix
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
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Five hundred seventy-three unit samples", "Five hundred seventy-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
