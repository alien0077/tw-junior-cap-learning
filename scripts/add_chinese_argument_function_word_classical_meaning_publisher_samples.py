#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese argument and classical language units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版議論證據與文言語詞理解定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版論證閱讀、文言虛字與詞義判讀定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列議論證據、文言虛字與古今詞義，採語境分析及紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-argument-evidence-basics", "議論文本：從主張到論據", ["主張", "論據", "推理", "證據可信度"], "把議論文本拆成主張、理由、證據、隱含前提與反例，沿著推理關係判斷證據究竟支持哪一個結論。", "引用名人或數據不必然構成有效論證；需檢查來源、代表性、因果跳躍與概念是否偷換。"),
    ("lesson-chinese-classical-function-words", "文言虛字與古今義變", ["文言虛字", "句法功能", "古今語意", "語境判讀"], "以句法位置、前後語意與語氣功能判斷文言虛字，再比較同字在古今語境中的功能變化，避免用現代常見義直接套讀。", "虛字不是沒有意義；需觀察連接、語氣、時間、指涉與句型，並以整句翻譯回頭驗證。"),
    ("lesson-chinese-classical-word-meaning", "文言詞義與語詞結構", ["詞義推論", "古今詞義", "詞類活用", "語詞結構"], "從構詞、對偶、句法位置與上下文推論文言詞義，辨認古今異義、詞類活用與一詞多義，再用句意檢查解釋是否成立。", "不能只查單字表；需分辨詞在本句的詞性、搭配、修辭與時代語義，避免把現代詞義倒灌。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred thirteen unit samples", "Seven hundred sixteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
