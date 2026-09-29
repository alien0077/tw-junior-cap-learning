#!/usr/bin/env python3
"""Record public-school publisher evidence for English listening performance 1-Ⅳ-4..6."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；日常對話、歌謠韻文與故事聽力定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；對話、歌曲與短劇音檔活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；生活對話、韻文與故事理解評量定位。"),
]
UNITS = [
    ("lesson-english-performance-1-iv-4", "1-Ⅳ-4：日常對話主要內容", ["日常對話", "主旨", "說話者", "互動目的"], "先辨認對話人物、場所與交談目的，再用關鍵詞和語氣抓住主要內容；遇到省略或口語縮略要以輪次與前後文補足意思。", "把每句翻成中文可能仍抓不到對話目的；需區分主旨、細節、態度與下一步行動。"),
    ("lesson-english-performance-1-iv-5", "1-Ⅳ-5：簡易歌謠韻文主要內容", ["歌謠韻文", "節奏", "關鍵詞", "整體意義"], "利用重讀、押韻、重複句與歌詞關鍵詞建立預測，再用整段情境確認歌謠或韻文的主要訊息；不把節奏練習誤當逐字翻譯。", "只聽出押韻不等於理解；需指出聲音重複如何協助記憶，並用內容線索說明整體意思。"),
    ("lesson-english-performance-1-iv-6", "1-Ⅳ-6：故事短劇主要內容", ["故事短劇", "角色", "事件順序", "情節主旨"], "依角色聲音、場景線索和事件轉折整理故事順序，辨認角色目標、問題與結果，再用簡短敘述或角色回應重建情節主旨。", "記住單一事件不等於掌握故事；需檢查因果、角色關係和結尾如何回應前面的問題。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred seventy-one unit samples", "Seven hundred seventy-four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
