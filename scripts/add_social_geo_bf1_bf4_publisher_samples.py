#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bf-IV-1..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列西亞北非自然資源、伊斯蘭文化、國際衝突與跨文化互動。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列自然資源、伊斯蘭文化、區域衝突及與西方互動。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bf-IV-1～4，採圖表判讀、討論、紙筆與問答評量。"),
]
UNITS = [
    ("bf-iv-1", "地 Bf-Ⅳ-1：自然資源", ["西亞北非", "石油與水資源", "資源分布", "資源政治經濟"], "以石油、天然氣與水資源分布圖，分析自然資源、人口聚落、產業與國際關係的空間連結。", "要求區分資源蘊藏、開採與收益分配，不能把資源豐富直接等同全民富裕。"),
    ("bf-iv-2", "地 Bf-Ⅳ-2：伊斯蘭文化", ["伊斯蘭文化", "宗教生活", "空間分布", "文化多樣性"], "以宗教分布、城市生活與歷史交流資料，理解伊斯蘭文化的核心與不同地區的多樣表現。", "學生需避免將宗教信仰、政治制度與所有個人行為混為一談。"),
    ("bf-iv-3", "地 Bf-Ⅳ-3：國際衝突", ["國際衝突", "資源與領土", "多方利害", "歷史脈絡"], "用時間線與利害關係人圖分析衝突的歷史、資源、領土與政治因素，區分事件事實和立場解釋。", "要求標示資料來源與多方觀點，避免將複雜衝突歸因於單一宗教或族群。"),
    ("bf-iv-4", "地 Bf-Ⅳ-4：伊斯蘭與西方互動", ["跨文化互動", "殖民與現代化", "全球媒體", "互動影響"], "以歷史、貿易、移民與媒體案例，追蹤伊斯蘭社會與西方互動中的交流、權力與相互影響。", "學生需區分交流與支配、個案與整體，並用證據避免文明二分法。"),
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
            b["reason"] = b["reason"].replace("Five hundred sixty-five unit samples", "Five hundred sixty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
