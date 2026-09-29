#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bg-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列撒哈拉以南非洲自然環境、資源、經濟發展與區域互動。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列非洲自然環境、資源利用、發展差異與區域問題。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bg-IV-1～4，採地圖、圖表、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bg-iv-1", "地 Bg-Ⅳ-1：自然環境", ["撒哈拉以南非洲", "地形與氣候", "水資源", "自然環境與生活"], "以氣候帶、河川、地形與植被分布圖，說明環境條件如何影響人口、聚落與產業選擇。", "不能把單一氣候帶推論成整個非洲，也不能把自然條件直接當成發展程度的唯一原因。"),
    ("bg-iv-2", "地 Bg-Ⅳ-2：產業與資源", ["資源分布", "農業與礦業", "產業鏈", "資源利用"], "從資源位置、開採方式、加工能力與出口路線追蹤產業鏈，分辨資源豐富和收益分配的差異。", "學生需區分產量、出口值、就業與居民所得，避免用單一指標判斷發展。"),
    ("bg-iv-3", "地 Bg-Ⅳ-3：經濟發展差異", ["經濟發展", "城鄉差異", "全球分工", "發展指標"], "比較區域資料與生活指標，分析歷史、制度、基礎建設與全球分工如何共同造成發展差異。", "不可把貧窮歸因於文化或族群特質；每個結論都要對應空間尺度與資料指標。"),
    ("bg-iv-4", "地 Bg-Ⅳ-4：區域問題與永續", ["人口與環境", "糧食安全", "都市化", "永續發展"], "以糧食、城市、土地與環境資料，評估發展政策的利害關係人、時間尺度與永續取捨。", "要分開短期成效與長期代價，並標示政策受益者、承擔成本者及證據限制。"),
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
            blocker["reason"] = blocker["reason"].replace("Five hundred sixty-nine unit samples", "Five hundred seventy-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
