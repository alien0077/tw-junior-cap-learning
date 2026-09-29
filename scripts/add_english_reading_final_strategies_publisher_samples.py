#!/usr/bin/env python3
"""Record public-school publisher evidence for final English reading strategy units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；多元體裁閱讀、語境猜詞與事實意見辨識定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；文本體裁、上下文策略與資訊判讀活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；閱讀策略、不同文本與事實觀點評量定位。"),
]
UNITS = [
    ("lesson-english-performance-3-iv-16", "3-Ⅳ-16：閱讀不同體裁主題簡易文章", ["體裁", "主題", "說明文", "敘事文"], "比較公告、對話、說明、敘事或簡短訊息的目的、版面和組織方式，依文本類型選擇閱讀策略，再用證據回答主題與細節。", "不同體裁不能用同一種讀法；需先辨認任務和文本功能，避免把說明資料當故事或把意見當事實。"),
    ("lesson-english-context-clues", "Reading: Use Context Clues", ["上下文線索", "詞義推測", "句法", "驗證"], "利用同句定義、同義反義、例子、詞性與前後段落推測陌生字，再以替換測試、字典或後文交叉驗證，不把第一次猜測當答案。", "只靠中文直覺容易選錯；需記錄線索、候選詞義與驗證結果，並知道何時應停止推測改查來源。"),
    ("lesson-english-fact-opinion", "Reading: Fact or Opinion", ["事實", "意見", "證據", "語氣"], "檢查句子是否能由資料獨立驗證，辨認評價詞、推測語氣和立場，再比較同一主題中的事實、意見與帶有證據的主張。", "有數字不一定就是完整事實；需追問來源、範圍、時間和是否混入解釋或價值判斷。"),
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
            blocker["reason"] = blocker["reason"].replace("Eight hundred ten unit samples", "Eight hundred thirteen unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
