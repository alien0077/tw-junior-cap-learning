#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese Ab, Ac and Ad."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版國文課程的字詞語境、句段組織與篇章理解定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版國文課程的字詞、句段與篇章閱讀表達定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 Ab、Ac、Ad，採語境判讀、句段重組、篇章主旨與紙筆評量。"),
]
UNITS = [
    ("ab", "Ab：字詞——讓字在語境中發聲", ["字詞語境", "形音義", "詞語搭配", "語意判讀"], "從上下文、搭配關係與語氣判斷字詞意義，對照字形、讀音、詞性和古今義，避免只背單一字典釋義。", "不能脫離句子選最熟悉的意思；需檢查詞性、搭配、指涉與語氣是否和全文一致。"),
    ("ac", "Ac：句段——把想法寫成讀者看得懂的話", ["句子結構", "段落銜接", "指涉與省略", "語意邏輯"], "把句子的主幹、修飾與指涉拆開，再以轉折、因果、承接和主題句重建段落如何推進觀點。", "句子通順不代表意思正確；要檢查代詞指涉、連接詞方向、訊息焦點與前後邏輯。"),
    ("ad", "Ad：篇章——沿著文字路線找主旨與意味", ["篇章結構", "主旨證據", "敘述視角", "語氣與意涵"], "沿著段落功能、重複意象、轉折與結尾回看文章，建立主旨—證據—推論鏈，並分辨作者明說、暗示與讀者延伸。", "主旨不能只靠標題或最後一句猜；需回指多處文本證據，並標示推論超出原文的部分。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-chinese-content-" + suffix
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
            blocker["reason"] = blocker["reason"].replace("Six hundred ninety-eight unit samples", "Seven hundred one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
