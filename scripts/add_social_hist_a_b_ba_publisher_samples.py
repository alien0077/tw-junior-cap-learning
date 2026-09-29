#!/usr/bin/env python3
"""Record public-school publisher evidence for social history A, B and Ba."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的時序、史料判讀與臺灣早期社會定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的歷史方法、早期臺灣與原住民族主題定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 A、B、Ba 的時間概念、證據閱讀、史前文化與原住民族，採圖表、史料、討論及紙筆評量。"),
]
UNITS = [
    ("a", "A：歷史的基礎觀念", ["時間與時序", "歷史證據", "因果與解釋", "多元觀點"], "用年代、遺物、文字記錄與口述材料比較同一事件的不同證據，練習把觀察、推論與仍待查證的部分分開。", "不能把年代先後直接當成因果，也不能把單一記錄者的說法當成唯一真相；要標示證據範圍與立場。"),
    ("b", "B：早期臺灣", ["臺灣早期歷史", "移動與交流", "族群互動", "環境條件"], "沿著海上交通、聚落與政權變化的線索，對照不同群體在臺灣活動的時間與空間，理解早期歷史不是單一政權的直線故事。", "需區分來臺、居住、治理與文化交流等不同關係，不能把後來的國家邊界倒套到早期社會。"),
    ("ba", "Ba：史前文化與臺灣原住民族", ["考古證據", "史前文化", "原住民族", "文化延續與變遷"], "從遺址分布、器物用途、環境適應與族群口述傳統交叉理解史前生活，並辨識考古分類與當代原住民族身分之間不能直接畫等號。", "考古遺物能支持生活方式的部分推論，但不必然能單獨證明族名、語言或完整信仰；結論要保留證據界線。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred fifty-five unit samples", "Six hundred fifty-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
