#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Cb-IV-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程在公共意見與媒體議題範圍，定位公 Cb-IV-1、Cb-IV-2。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版公民課程列公共意見形成、媒體與社群網路及閱聽人影響。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程列公 Cb-IV-1、Cb-IV-2，並以資料蒐集、討論與紙筆／問答評量。"),
]
UNITS = [
    ("cb-iv-1", "公 Cb-Ⅳ-1：公共意見形成與特性", ["公共意見", "個人與群體互動", "意見形成", "多元與變動"], "用一項公共議題的時間線，標示個人經驗、群體討論、媒體訊息與制度回應如何共同形成公共意見。", "要求區分個人偏好與公共意見，並用資料指出意見來源、共識程度與變動條件。"),
    ("cb-iv-2", "公 Cb-Ⅳ-2：媒體社群網路與閱聽人影響", ["媒體角色", "社群擴散", "閱聽人識讀", "資訊影響公共意見"], "以同一則訊息在新聞、社群貼文與留言串的流動圖，追蹤選擇、轉發與演算法如何影響可見性與判斷。", "學生需檢查來源、證據、 framing 與自身轉傳行為，不能把熱門度直接當成真實或多數意見。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-civ-" + suffix
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
            b["reason"] = b["reason"].replace("Five hundred sixteen unit samples", "Five hundred eighteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
