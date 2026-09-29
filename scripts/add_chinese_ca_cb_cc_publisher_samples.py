#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese Ca, Cb and Cc."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版物質、社群與精神文化內涵定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版物質生活、社群文化與精神價值定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 Ca、Cb、Cc 的物質文化、社群文化、精神文化與紙筆評量。"),
]
UNITS = [
    ("ca", "Ca：物質文化", ["器物與技術", "生活環境", "生產消費", "文化意義"], "從器物、建築、飲食、服飾與技術變化觀察人如何適應環境、組織生產並表達身分，並區分物質功能與後來賦予的象徵意義。", "不能只把物件當成古董或商品；需交代製作者、使用者、取得成本、保存脈絡與不同群體的意義。"),
    ("cb", "Cb：社群文化", ["社群認同", "規範與習俗", "地方記憶", "多元共存"], "比較家庭、社區、族群、校園與網路社群的語言、規範和記憶，分析共同體如何建立歸屬，也如何處理內部差異與外部互動。", "社群不是同質團體；要看誰能代表社群、誰被排除、規範如何改變以及不同成員的經驗。"),
    ("cc", "Cc：精神文化", ["信仰與價值", "思想傳承", "藝術表達", "意義詮釋"], "從信仰、哲學、文學、藝術與儀式資料分析人如何回答存在、倫理與共同生活問題，並追蹤精神文化在不同時代的傳承與轉化。", "不能把精神文化化約成固定教條；需區分文本、實踐、制度權威與個人詮釋的差異。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred seven unit samples", "Seven hundred ten unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
