#!/usr/bin/env python3
"""Record public-school publisher evidence for English reading performance 3-Ⅳ-10..12."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；故事要素、圖像預測與閱讀策略定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；故事文本、標題圖片推測與閱讀技巧活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；故事理解、預測策略與閱讀方法評量定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-10", "3-Ⅳ-10：辨識故事要素", ["故事要素", "角色", "場景", "情節"], "從角色、場景、問題、事件順序和結果整理故事骨架，利用轉折詞確認因果，再以文本句子說明哪個要素支持主旨。", "只列角色和地點不等於理解故事；需連結目標、衝突、行動與結果。"),
    ("lesson-english-performance-3-iv-11", "3-Ⅳ-11：從圖片標題書名推測", ["預測", "圖片", "標題", "書名"], "閱讀正文前先從圖片、標題、書名和版面形成可驗證預測，閱讀後標記哪些被證實、修正或推翻，避免把第一印象當作結論。", "預測不是猜答案；需寫出線索、推測範圍與更新理由。"),
    ("lesson-english-performance-3-iv-12", "3-Ⅳ-12：熟悉閱讀技巧", ["閱讀技巧", "掃讀", "略讀", "查證"], "依閱讀目的選擇略讀抓主旨、掃讀找細節、上下文猜詞、標記指涉或回讀查證，並說明策略如何節省時間或提高理解可靠度。", "每篇都逐字翻譯不一定最好；需依問題、文本難度和證據需求調整策略。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教材正文、歌詞、題目、答案或版面。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Eight hundred four unit samples", "Eight hundred seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
