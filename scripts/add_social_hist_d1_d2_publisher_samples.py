#!/usr/bin/env python3
"""Record public-school publisher evidence for social history D-IV-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程列近代世界變動、海洋交流、殖民與史料判讀。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程列近代國家、全球交流、殖民與資料探究。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列歷 D-IV-1～2，採時間線、地圖、史料、討論與紙筆評量。"),
]
UNITS = [
    ("d-iv-1", "歷 D-Ⅳ-1：近代世界變動", ["近代世界", "海洋交流", "國家競爭", "全球連結"], "用航線、貿易、軍事與人口流動資料，分析近代世界連結擴張及不同地區的受益與代價。", "不能把近代化描述成單一路徑，需同時檢查交流、暴力、制度與地方回應。"),
    ("d-iv-2", "歷 D-Ⅳ-2：殖民與帝國", ["殖民", "帝國擴張", "資源與勞動", "地方回應"], "比較統治者政策、資源流動、勞動與地方回應資料，判讀殖民關係中的權力與長期影響。", "要區分官方敘事、被統治者經驗與後來研究，不能只用建設成果合理化支配關係。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"} for publisher, url, locator in SOURCES],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str): blocker["reason"] = blocker["reason"].replace("Five hundred ninety-eight unit samples", "Six hundred unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
