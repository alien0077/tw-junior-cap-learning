#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bi-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列美洲自然環境、文化多樣性、經濟發展與臺灣互動。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列美洲環境、文化、區域經濟與全球連結。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bi-IV-1～4，採地圖、圖表、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bi-iv-1", "地 Bi-Ⅳ-1：自然環境", ["美洲自然環境", "地形與氣候", "河川與海岸", "環境適應"], "以地形、氣候、河川與生態帶資料，比較美洲不同區域的生活、聚落與產業條件。", "不能以北美或南美單一區域代表整個美洲，且需區分自然條件與人為開發。"),
    ("bi-iv-2", "地 Bi-Ⅳ-2：多元文化", ["文化多樣性", "移民與原住民族", "文化景觀", "空間認同"], "從移民、原住民族與文化景觀資料，分析人口流動如何形成多層次的文化空間與認同。", "避免把族群、國籍、語言與文化簡化為同一分類，也要辨識資料中的觀點位置。"),
    ("bi-iv-3", "地 Bi-Ⅳ-3：經濟發展與區域結盟", ["經濟發展", "區域結盟", "跨國分工", "貿易網絡"], "以貿易、產業鏈與區域組織資料，判讀美洲國家在合作、競爭與分工中的利益差異。", "要區分結盟承諾、實際流量與分配效果，不以協定名稱直接推論全民受益。"),
    ("bi-iv-4", "地 Bi-Ⅳ-4：臺灣與美洲互動", ["臺灣與美洲", "貿易與投資", "科技與教育", "跨區域互動"], "追蹤臺灣與美洲在貿易、科技、教育與文化上的互動節點，解釋全球網絡中的依賴與影響。", "結論須標示時間、對象與資料尺度，避免把美洲或臺灣當作單一行動者。"),
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
            blocker["reason"] = blocker["reason"].replace("Five hundred seventy-seven unit samples", "Five hundred eighty-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
