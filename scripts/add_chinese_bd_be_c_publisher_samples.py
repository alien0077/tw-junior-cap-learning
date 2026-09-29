#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese Bd, Be and C."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版議論、應用文本與文化內涵閱讀表達定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版議論、應用文本與文化內容定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 Bd、Be、C 的論證、應用溝通、文化內涵與紙筆評量。"),
]
UNITS = [
    ("bd", "Bd：議論文本", ["主張與論據", "推理關係", "反方觀點", "論證評估"], "區分主張、理由、證據與假設，檢查論據是否真的支持結論，再比較反方觀點與作者如何處理限制。", "有例子不等於有證明；需檢查證據代表性、因果跳躍、概念定義與未處理的反例。"),
    ("be", "Be：應用文本", ["溝通目的", "受眾情境", "格式與語氣", "資訊行動"], "從公告、報告、申請、說明與媒體訊息判斷目的、受眾、格式和語氣，評估資訊是否足以讓讀者採取正確行動。", "格式正確不代表溝通有效；要檢查關鍵資訊、責任歸屬、時間條件、禮貌尺度與讀者需求。"),
    ("c", "C：文化內涵", ["文化脈絡", "價值觀念", "文本與生活", "多元觀點"], "把文學、歷史、語言、習俗與現代生活放回形成它們的社會脈絡，辨識文化延續、轉化及不同群體對同一符號的詮釋。", "不能把文化當成固定的民族性格；需區分文本表述、歷史情境、實際生活與後來的再詮釋。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred four unit samples", "Seven hundred seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
