#!/usr/bin/env python3
"""Record public-school publisher evidence for social history I, Ia and Ib."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的傳統至現代、東亞世界與政治挑戰定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的近代轉型、東亞互動與政治回應定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 I、Ia、Ib 的傳統現代轉型、東亞交流與政治挑戰，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("i", "I：從傳統到現代", ["傳統秩序", "近代轉型", "全球交流", "制度與社會"], "以政治權力、經濟網絡、科技交通與社會身分的資料，追蹤傳統秩序如何面對近代轉型，並比較不同地區的時間差與回應。", "現代化不是單一路徑；需區分制度移植、地方調整與社會代價，不能把西方經驗當成所有地區的唯一標準。"),
    ("ia", "Ia：東亞世界延續變遷", ["東亞秩序", "區域交流", "國家形成", "文化轉換"], "從外交、貿易、思想與人口流動資料分析東亞世界的延續與變動，理解區域秩序如何因外來衝擊與內部改革重新排列。", "不能把東亞寫成被動接受外來影響；需同時辨識地方主動選擇、跨域交流與權力不對等。"),
    ("ib", "Ib：政治挑戰與回應", ["政治危機", "改革與革命", "國家治理", "社會動員"], "比較改革、革命、殖民治理與社會動員的史料，分析不同政治挑戰如何促成制度回應，並檢視回應是否改變權力分配。", "事件先後不等於政策因果；要指出行動者、資源、制度限制與未被納入的群體。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred seventy unit samples", "Six hundred seventy-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
