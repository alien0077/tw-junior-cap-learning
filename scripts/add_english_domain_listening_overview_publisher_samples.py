#!/usr/bin/env python3
"""Record public-school publisher evidence for English domain and listening overviews."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course113/sub1/15636172843290327.pdf", "南一版第1、2冊七年級公立課程計畫；英語文領域、學習表現與聽力課程定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course112/sub1/15342166894673419.pdf", "康軒版第1、2冊七年級公立課程計畫；聽說讀寫整合、學習表現與聽力活動定位。"),
    ("hanlin", "https://course.cyc.edu.tw/upfile/course114/sub1/15939623345151225.pdf", "翰林版第1、2冊七年級公立課程計畫；英語文領域、能力進階與聽力理解定位。"),
]
UNITS = [
    ("lesson-english-language-domain", "語文領域－英語文", ["英語文領域", "聽說讀寫", "溝通", "文化"], "以聽、說、讀、寫互相支援的溝通能力為領域架構，將語言形式放回生活、學習與文化情境，讓理解和表達能跨技能遷移。", "只列技能清單不代表完成領域融合；需比較版本如何安排語言知識、溝通任務、文化材料與多元評量。"),
    ("lesson-english-learning-performance", "學習表現", ["能力進階", "理解", "表達", "策略遷移"], "以可觀察的聽辨、口語互動、閱讀理解、書面表達和學習策略描述能力，從模仿與辨識逐步走向在新情境中自主完成任務。", "把能力寫成單字或文法名詞會失去表現證據；需保留行動、情境、對象與品質判準。"),
    ("lesson-english-performance-1", "語言能力（聽）", ["聽力理解", "主旨", "細節", "語音線索"], "聽力理解要整合語音、重音、語調、關鍵詞、上下文與說話目的，先抓主旨再確認細節和推論，最後以口語或行動回應訊息。", "聽到熟悉單字不等於理解整段；需檢查是否掌握說話者關係、情境限制、主要意圖與未明說的訊息。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred sixty-five unit samples", "Seven hundred sixty-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
