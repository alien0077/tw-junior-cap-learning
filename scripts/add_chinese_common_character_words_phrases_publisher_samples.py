#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese character, word and phrase units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版常用字形音義、語詞認讀與正確使用定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版識字、語詞理解與語用辨析定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列常用字形音義、語詞認讀與語詞使用，採語境判讀及紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-common-character-form-sound-meaning", "常用字的形、音、義", ["字形辨識", "讀音", "字義", "部件與語境"], "把字形部件、讀音線索與句中意義互相驗證，處理形近、音近、多音多義字，並說明字義如何受語境限制。", "不能只靠部件猜義或只背一個讀音；需回到詞語和句子，檢查讀音、詞性與語意是否一致。"),
    ("lesson-chinese-common-words-recognition", "常用語詞的認讀與理解", ["語詞認讀", "詞義", "搭配", "語境理解"], "從詞語結構、上下文與搭配判斷讀音和意思，辨識同音異義、形近詞與語境轉義，再以完整句意驗證。", "認得字不等於理解詞；需辨認詞語整體、語法位置、語氣和搭配，不能逐字相加。"),
    ("lesson-chinese-common-phrases-usage", "常用語詞的正確使用", ["語詞使用", "語體", "搭配限制", "情境溝通"], "比較語詞的語體、感情色彩、搭配對象與使用情境，選擇符合對象、目的和句意的表達，而不是只看字面相近。", "近義詞不一定能互換；要檢查正式程度、褒貶、主客體搭配、時間範圍與語境禮貌。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred sixteen unit samples", "Seven hundred nineteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
