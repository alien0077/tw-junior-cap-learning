#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Ba-IV-1..3 and Bb-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列自然地區、傳統維生、人口遷移文化擴散與產業轉型。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列自然環境差異、人口與文化、遷移及產業轉型內容。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Ba-IV-1～3、Bb-IV-1，採圖表判讀、討論、紙筆與問答評量。"),
]
UNITS = [
    ("ba-iv-1", "地 Ba-Ⅳ-1：自然地區差異", ["自然環境", "地形氣候", "區域差異", "人地關係"], "用地形、氣候與水文圖比較自然地區，說明自然條件如何提供機會也形成生活限制。", "要求以多種自然資料互證，不能以單一氣候數值概括整個地區。"),
    ("ba-iv-2", "地 Ba-Ⅳ-2：傳統維生方式與人口分布", ["傳統維生", "資源利用", "人口分布", "適應環境"], "將游牧、農牧、漁撈或山地利用案例放入資源與人口分布圖，分析生活方式和環境條件的互動。", "學生需說明文化與資源條件的連結，避免把傳統維生方式寫成固定不變或落後。"),
    ("ba-iv-3", "地 Ba-Ⅳ-3：人口成長遷移與文化擴散", ["人口成長", "人口遷移", "推力拉力", "文化擴散"], "用人口金字塔、遷移流向與文化傳播案例，區分人口數量變化、移動原因與文化擴散路徑。", "要求指出資料尺度與遷移原因，不能把人口增加、移入或文化交流混成同一件事。"),
    ("bb-iv-1", "地 Bb-Ⅳ-1：產業轉型", ["產業結構", "技術變遷", "勞動轉移", "區域調適"], "用產業結構與就業資料的時間序列，追蹤第一、二、三級產業轉換及其對地方人口與空間的影響。", "學生需連結技術、市場、政策與勞動資料，避免把產業轉型只理解成工廠搬遷。"),
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
            b["reason"] = b["reason"].replace("Five hundred forty-six unit samples", "Five hundred fifty unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
