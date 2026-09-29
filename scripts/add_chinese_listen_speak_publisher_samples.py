#!/usr/bin/env python3
"""Record public-school publisher evidence for the next Chinese listening/speaking units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版聆聽邏輯、科技媒介與口語表達定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版聆聽策略、資訊運用與情境表達定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 1-Ⅳ-3、1-Ⅳ-4、2-Ⅳ-1，採聆聽理解、媒介互動與經驗分享評量。"),
]
UNITS = [
    (
        "lesson-chinese-performance-1-iv-3",
        "1-Ⅳ-3：分辨聆聽內容邏輯並找方法",
        ["聆聽邏輯", "因果條件", "問題解決", "方法判斷"],
        "把聽到的內容拆成主張、理由、條件和結果，辨認說話者如何由問題推到方法，再檢查方法是否真的回應限制與目標。",
        "只記住結論會漏掉推理鏈；需把轉折、因果和條件標出，並以原有資訊說明方法的適用範圍。",
    ),
    (
        "lesson-chinese-performance-1-iv-4",
        "1-Ⅳ-4：運用科技資訊增進聆聽與互動",
        ["科技聆聽", "資訊篩選", "即時互動", "來源核對"],
        "運用錄音、字幕、共享筆記或線上回應保留聆聽線索，再比較不同媒介的時間戳、文字轉錄與原始來源，讓互動回應可被追查。",
        "工具能放大訊息卻不能替代判讀；自動轉錄、剪輯片段和匿名貼文都要回到原聲、上下文與來源交叉確認。",
    ),
    (
        "lesson-chinese-performance-2-iv-1",
        "2-Ⅳ-1：情境表達與經驗分享",
        ["情境表達", "經驗敘述", "對象意識", "口語組織"],
        "分享經驗時先判斷對象、目的與時間，再以事件順序、關鍵細節和個人感受組織敘述；同一經驗面對同儕、師長或公眾需調整語氣與資訊密度。",
        "把想到的細節全部倒出來不等於清楚；需取捨與目的有關的資訊，避免把推測說成親身觀察，並留出對方理解與追問的空間。",
    ),
]


def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
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
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred thirty-two unit samples", "Seven hundred thirty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
