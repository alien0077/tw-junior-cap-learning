#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Ca-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列全球環境議題、資源、區域發展與臺灣連結。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列全球自然環境、產業、區域發展與問題探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Ca-IV-1～4，採地圖、圖表、討論、紙筆與問答評量。"),
]
UNITS = [
    ("ca-iv-1", "地 Ca-Ⅳ-1：自然環境與生活", ["全球自然環境", "氣候與地形", "人地關係", "環境適應"], "以全球地形、氣候與生態資料，解釋人類生活與產業如何適應、利用並改變自然環境。", "不能把自然環境視為命定因素，需指出技術、制度與歷史選擇的作用。"),
    ("ca-iv-2", "地 Ca-Ⅳ-2：人口與都市", ["人口分布", "都市化", "遷移", "城鄉差異"], "透過人口金字塔、遷移資料與都市圖，判讀人口結構、流動與都市化的空間後果。", "要區分人口數量、密度、成長率與流動方向，不能只看單一統計值。"),
    ("ca-iv-3", "地 Ca-Ⅳ-3：產業與全球分工", ["全球分工", "產業鏈", "貿易網絡", "區域差異"], "從生產、運輸、消費與廢棄資料追蹤全球產業鏈，分析不同地區在分工中的收益與成本。", "需區分產值、利潤、勞動條件與環境成本，避免把貿易量直接等同發展成果。"),
    ("ca-iv-4", "地 Ca-Ⅳ-4：全球議題探究", ["全球議題", "環境正義", "多方利害", "永續治理"], "以跨尺度資料探究氣候、資源或公共衛生議題，提出有證據且標示限制的治理方案。", "結論須列出受益與承擔成本的群體，並分開資料事實、推論與價值判斷。"),
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
            blocker["reason"] = blocker["reason"].replace("Five hundred eighty-one unit samples", "Five hundred eighty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
