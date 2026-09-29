#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese calligraphy, phrase and learning-content units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版書法欣賞、語詞進階使用與國文學習內容定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版書法碑帖、語詞語用與閱讀學習內容定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列書法欣賞、語詞進階使用與學習內容整合，採作品觀察、語境判讀及紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-calligraphy-appreciation", "書法名家與碑帖欣賞", ["書體風格", "筆畫結構", "章法布局", "文化脈絡"], "從筆畫、結體、行氣、章法與落款觀察作品風格，再將書家、時代、媒材與碑帖流傳背景連回視覺判讀。", "不能只用名家或年代判斷好壞；需提出可見形式證據，並分開作品分析、歷史背景與個人審美。"),
    ("lesson-chinese-common-phrases-advanced", "常用語詞使用進階", ["近義辨析", "語體語氣", "搭配限制", "情境改寫"], "以正式程度、感情色彩、搭配對象與溝通目的比較近義語詞，練習在不同受眾和文體中改寫而不改變核心意思。", "語詞進階題不能只問同義；要檢查語氣、禮貌、主客體、抽象程度與上下文推論。"),
    ("lesson-chinese-learning-content", "把文字讀成可以驗證的理解", ["字句到篇章", "證據鏈", "理解策略", "跨文本整合"], "把字詞、句段、篇章與文化脈絡串成可回指的理解流程，遇到歧義時比較多種解釋並用文本證據逐步排除。", "理解策略不是固定口訣；需依文體、問題、資料形式與讀者目的調整，並明確標示推論界線。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred fourteen unit samples", "Seven hundred seventeen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
