#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese performance 4-IV-4..6."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版書體碑帖、書法布局與硬筆書寫定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版書體欣賞、行款布局與書寫表現定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版 4-Ⅳ-4～4-Ⅳ-6 的書體碑帖、行氣布局與硬筆字，採作品觀察、實作及紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-performance-4-iv-4", "4-Ⅳ-4：認識書體並欣賞碑帖", ["篆隸楷行草", "碑帖脈絡", "筆法結體", "作品鑑賞"], "比較篆、隸、楷、行、草的筆畫、結體與章法，將可見形式和時代、用途、書家及碑帖傳承背景連結。", "不能只靠書體名稱或作者判斷；需提出筆法、結體、章法等形式證據，並注意拓本與真跡的差異。"),
    ("lesson-chinese-performance-4-iv-5", "4-Ⅳ-5：欣賞書法行款布局行氣風格", ["行款", "布局", "行氣", "風格比較"], "從字距、行距、欄線、墨色、速度感與整體視線觀察作品行款布局，說明局部筆畫如何形成整體行氣和風格。", "布局不是單純整齊或漂亮；需把觀察、風格判斷與時代媒材條件分開，避免只用主觀形容詞。"),
    ("lesson-chinese-performance-4-iv-6", "4-Ⅳ-6：正確美觀硬筆字", ["硬筆結構", "筆畫比例", "間架安排", "書寫修正"], "以筆畫比例、部件位置、字距行距和書寫速度檢查硬筆字，透過局部重寫與整行比較修正可讀性及穩定性。", "美觀不能取代正確與可讀；需先檢查筆畫、結構、方向與標點，再談風格和個人特色。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred twenty unit samples", "Seven hundred twenty-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
