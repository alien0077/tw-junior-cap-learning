#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese domain and performance overviews."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版國語文領域、學習表現與聆聽架構定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版國語文領域、能力指標與聆聽課程定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文領域列領域總綱、學習表現與聆聽教學評量。"),
]
UNITS = [
    ("lesson-chinese-language-arts-domain", "語文領域－國語文", ["語文領域", "聆聽", "口語表達", "閱讀寫作"], "以聆聽、口語表達、識字寫字、閱讀和寫作互相支援為領域架構，將語文理解、表達、文化與思辨放進真實溝通任務，而不是把能力切成孤立題型。", "只列出五大項不代表完成領域融合；需觀察不同版本如何安排能力進階、文本任務、文化脈絡與評量證據。"),
    ("lesson-chinese-learning-performance", "學習表現", ["學習表現", "能力進階", "理解表達", "情境應用"], "以學習者能觀察到的理解、表達、溝通、思辨與創作行動描述目標，從聽讀輸入走向口說寫作輸出，再以情境任務檢查能否遷移。", "把學習表現改寫成知識名詞會失去可觀察性；需保留行動、對象、條件與品質判準，才能設計答案與回饋。"),
    ("lesson-chinese-performance-1", "聆聽", ["聆聽理解", "訊息辨識", "觀點判讀", "互動回應"], "聆聽包含擷取訊息、辨認語氣與觀點、整理邏輯、評估來源以及回應互動；教學需讓學生從聲音與語境證據說明理解，而非只選出情緒標籤。", "聽見關鍵字不等於理解；要檢查是否掌握目的、說話者關係、條件限制與未明說的推論，並能用自己的話回應。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {item["lessonId"]: item for item in data["units"]}
    for lesson_id, title, core, representation, assessment in UNITS:
        units[lesson_id] = {
            "lessonId": lesson_id, "title": title,
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"}
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred fifty unit samples", "Seven hundred fifty-three unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
