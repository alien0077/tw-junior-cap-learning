#!/usr/bin/env python3
"""Record public-school publisher evidence for social history A-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程以紀年、分期、時序與史料判讀建立歷史研究基礎。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列紀年換算、時序、分期與資料判讀活動。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 A-IV-1 紀年與分期，採時間線、史料、討論與紙筆評量。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    lesson_id = "lesson-social-content-hist-a-iv-1"
    title = "歷 A-Ⅳ-1：紀年與分期"
    core = ["紀年系統", "時間線", "時序判讀", "歷史分期"]
    units[lesson_id] = {
        "lessonId": lesson_id, "title": title,
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": [{
            "publisher": publisher, "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": locator, "accessedAt": "2026-09-21",
            "observedConcepts": [title, *core],
            "observedRepresentations": ["以年代表、不同紀年換算、事件先後與分期界線進行時序判讀。"],
            "observedAssessment": ["要求說明時間座標、分期依據與史料可支持的結論，不把年份大小直接當作因果。"],
            "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
        } for publisher, url, locator in SOURCES],
        "fusionReview": {
            "commonCore": core,
            "differencesToReview": ["南一偏重紀年基礎與時序，康軒強調換算與活動操作，翰林連結時間線、史料與分期判讀。"],
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
            blocker["reason"] = blocker["reason"].replace("Five hundred eighty-nine unit samples", "Five hundred ninety unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 1}, ensure_ascii=False))

if __name__ == "__main__":
    main()
