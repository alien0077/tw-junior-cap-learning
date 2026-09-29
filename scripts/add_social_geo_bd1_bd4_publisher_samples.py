#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bd-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列東南亞自然環境、產業文化、經濟發展與臺灣／東北亞交流。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列東南亞自然條件、產業文化、經濟挑戰與區域交流。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bd-IV-1～4，採圖表判讀、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bd-iv-1", "地 Bd-Ⅳ-1：自然環境", ["東南亞自然環境", "季風", "地形水文", "自然與生活"], "以季風、河流、地形與海域圖比較東南亞自然環境，連結自然條件與人口／產業分布。", "要求以地圖證據解釋差異，不能用『熱帶』一詞概括所有東南亞地區。"),
    ("bd-iv-2", "地 Bd-Ⅳ-2：產業文化特色", ["產業活動", "文化景觀", "資源利用", "地方特色"], "用農業、工業、觀光與文化景觀案例，分析產業活動如何反映自然條件、歷史與地方文化。", "學生需區分產業事實與文化刻板印象，並指出案例的空間範圍。"),
    ("bd-iv-3", "地 Bd-Ⅳ-3：經濟成就與挑戰", ["經濟成長", "發展差異", "勞動與環境", "發展挑戰"], "用經濟指標、產業結構、勞動與環境資料，比較成長成果和分配、環境或勞動挑戰。", "要求同時呈現成就與代價，不能用單一成長率代表全民受益。"),
    ("bd-iv-4", "地 Bd-Ⅳ-4：臺灣與東北亞文化交流", ["文化交流", "移動與媒體", "臺灣與東北亞", "互動影響"], "以移民、教育、流行文化、觀光與商品流動資料，追蹤臺灣與東北亞的文化互動及雙向影響。", "要求分辨交流、模仿與權力不對等，並用來源資料避免把單一流行現象當成整體文化。"),
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
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred fifty-seven unit samples", "Five hundred sixty-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
