#!/usr/bin/env python3
"""Record public-school publisher evidence for social geography Bb-IV-2..4."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版地理課程列經濟區域差異、全球關連與環境衝擊問題探究。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版地理課程列經濟地區、全球產業連結與環境問題探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版地理課程列地 Bb-IV-2～4，採圖表判讀、問題討論、紙筆與問答評量。"),
]
UNITS = [
    ("bb-iv-2", "地 Bb-Ⅳ-2：經濟地區差異", ["經濟發展", "區域差異", "產業結構", "發展指標"], "用所得、產業結構、基礎建設與人口資料比較區域發展，區分平均數與群體內差異。", "要求指出指標的範圍與限制，不能用單一 GDP 或所得數字代表整個區域生活品質。"),
    ("bb-iv-3", "地 Bb-Ⅳ-3：經濟全球關連", ["全球分工", "跨國產業鏈", "貿易流動", "互賴風險"], "以產品供應鏈和貿易流向圖，追蹤生產、加工、消費與物流如何跨越國界連結。", "學生需說明不同節點的利益與風險，不能把全球連結只寫成出口增加。"),
    ("bb-iv-4", "地 Bb-Ⅳ-4：環境衝擊探究", ["環境衝擊", "產業活動", "空間尺度", "調適與治理"], "以產業活動的污染、資源消耗或災害風險資料，建立原因—空間分布—受影響者—調適方案的探究鏈。", "要求以資料和尺度提出方案，並說明治理成本與受益／受損群體，避免只提出口號。"),
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
            b["reason"] = b["reason"].replace("Five hundred fifty unit samples", "Five hundred fifty-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
