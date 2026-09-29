#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese speaking/interaction units."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版口語表達、提問回饋與資訊媒介定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版口語互動、論辯與科技表達定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 2-Ⅳ-2、2-Ⅳ-3、2-Ⅳ-4，採提問回饋、論辯與科技表達評量。"),
]
UNITS = [
    ("lesson-chinese-performance-2-iv-2", "2-Ⅳ-2：掌握聽聞邏輯提問回饋", ["聽聞邏輯", "追問", "回饋", "對話修正"], "先重述對方主張與理由，再以缺少的條件、證據或定義提出追問；回饋要指出可保留之處與可修正之處，讓對話能繼續推進。", "把不同意直接當成回饋會使對話失焦；需區分理解確認、澄清問題、評估意見與下一步建議。"),
    ("lesson-chinese-performance-2-iv-3", "2-Ⅳ-3：明確表達與有條理論辯", ["明確表達", "論點組織", "論辯", "證據回應"], "在論辯前界定主張與判準，依序提出理由、證據和限制，再正面回應反方最強的理由；讓聽者能分辨事實、推論與價值判斷。", "堆疊例子不等於論證；每項證據都要說明支持哪個理由，並承認資料不足時的推論邊界。"),
    ("lesson-chinese-performance-2-iv-4", "2-Ⅳ-4：運用科技資訊豐富表達", ["科技表達", "多模態", "資訊選擇", "媒介倫理"], "依受眾和目的選擇圖表、聲音、影像或超連結，讓媒介補充而不取代口語主線；標示資料來源並檢查圖像、剪輯與文字是否造成誤導。", "加入動畫和素材不一定更有說服力；需檢查每個媒介是否解決理解障礙，並避免未授權或脫離脈絡的內容。"),
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
                {"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": locator, "accessedAt": "2026-09-21", "observedConcepts": [title, *core], "observedRepresentations": [representation], "observedAssessment": [assessment], "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。"}
                for publisher, url, locator in SOURCES
            ],
            "fusionReview": {"commonCore": core, "differencesToReview": [representation, assessment], "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。"},
        }
    data["units"] = sorted(units.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        if isinstance(blocker.get("reason"), str):
            blocker["reason"] = blocker["reason"].replace("Seven hundred thirty-five unit samples", "Seven hundred thirty-eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
