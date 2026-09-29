#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Be-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列東亞／南亞自然環境、多元文化、區域結盟與新興市場。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列自然環境、多元文化、經濟結盟及臺灣產業關聯。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Be-IV-1～4，採圖表判讀、討論、紙筆與問答評量。"),
]
UNITS = [
    ("be-iv-1", "地 Be-Ⅳ-1：自然環境", ["東亞與南亞", "季風與地形", "自然區域", "環境差異"], "以季風、地形、水文與人口分布圖比較東亞／南亞自然區域，說明環境差異對生活的影響。", "要求以圖表證據區分區域，不能用單一氣候類型概括兩大區域。"),
    ("be-iv-2", "地 Be-Ⅳ-2：多元文化", ["文化多樣性", "宗教與語言", "歷史交流", "文化景觀"], "以宗教、語言、飲食、城市與歷史交流案例，分析多元文化形成及其空間分布。", "學生需區分文化分布與刻板印象，並說明資料的時間與空間範圍。"),
    ("be-iv-3", "地 Be-Ⅳ-3：經濟發展與區域結盟", ["經濟發展", "區域結盟", "分工", "合作與競爭"], "以區域組織、貿易流向與產業分工資料，分析結盟如何改變市場、投資與區域發展。", "要求同時比較成員利益與非成員影響，不能將結盟直接等同所有地區都受益。"),
    ("be-iv-4", "地 Be-Ⅳ-4：新興市場與臺灣產業關聯", ["新興市場", "臺灣產業", "供應鏈", "機會與風險"], "以產業鏈、投資與貿易資料，探究南亞／東南亞新興市場與臺灣產業布局的關聯。", "學生需指出資料來源、供應鏈節點與環境／勞動風險，不能只把市場成長率當成產業機會。"),
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
            b["reason"] = b["reason"].replace("Five hundred sixty-one unit samples", "Five hundred sixty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
