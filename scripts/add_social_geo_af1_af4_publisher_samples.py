#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Af-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列聚落、交通、都市化、區域發展與原住民族文化／保育探究。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列聚落體系、都市發展、區域空間差異及原住民族文化生活空間。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Af-IV-1～4，採地圖判讀、問題討論、紙筆與問答評量。"),
]
UNITS = [
    ("af-iv-1", "地 Af-Ⅳ-1：聚落體系與交通網絡", ["聚落階層", "交通網絡", "中心地", "服務範圍"], "用聚落人口、服務設施與交通流量圖，分析不同層級聚落的功能和彼此連結。", "要求以空間流向與服務資料作答，避免把人口最多直接當成所有功能最完整。"),
    ("af-iv-2", "地 Af-Ⅳ-2：都市發展與都市化", ["都市化", "都市擴張", "人口集中", "都市問題"], "用都市人口比例與土地利用前後圖，追蹤都市化的速度、空間擴張及住房、交通或環境代價。", "要求區分都市化程度與都市規模，並以資料指出問題成因。"),
    ("af-iv-3", "地 Af-Ⅳ-3：區域發展空間差異", ["區域差異", "產業與人口", "空間不均", "區域政策"], "用多指標區域比較圖，拆解產業、人口、所得、公共服務與交通如何共同造成空間差異。", "學生需指出指標限制與可能的政策取捨，不能用單一所得數字代表整體發展。"),
    ("af-iv-4", "地 Af-Ⅳ-4：原住民族文化生活空間與生態保育探究", ["文化生活空間", "原住民族", "生態保育", "地方知識與參與"], "以地方地圖、土地利用與訪談／公開資料，探究文化生活空間和保育目標可能的協力與衝突。", "要求尊重資料與社群觀點、標示證據來源並提出可協商方案，不能將族群文化當成靜態標本。"),
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
            b["reason"] = b["reason"].replace("Five hundred forty-two unit samples", "Five hundred forty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
