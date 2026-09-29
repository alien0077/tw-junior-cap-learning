#!/usr/bin/env python3
"""Record public-school publisher evidence for character formation, source reliability and punctuation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版造字原則、資訊判讀與標點語用定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版字形字義、資料可信度與標點安排定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列造字、閱讀判斷與 Ac-Ⅳ-1，採字詞辨識、來源評估與語意評量。"),
]
UNITS = [
    ("lesson-chinese-six-forms-character-making", "象形、指事、會意與形聲", ["造字原則", "象形", "指事", "會意", "形聲"], "以字形、構件和字義的關係比較象形、指事、會意與形聲，不把現代字形的相似誤當成造字證據；遇到不確定字源時查字典或字形資料。", "看到偏旁就直接猜讀音或意義容易誤判；需區分構形線索、現代使用和歷史字源，並說明證據強弱。"),
    ("lesson-chinese-source-reliability", "閱讀判斷：辨識可靠的資訊來源", ["來源可靠性", "作者資格", "證據", "交叉查證"], "從作者、發布機構、日期、引用資料、利益關係與可重現性檢查來源，再把同一主張與不同立場的原始資料交叉比對，避免只因版面專業或轉發量高就相信。", "有網址不等於可靠；需把主張拆成可查證的部分，分辨原始資料、二手報導、意見與未經證實的轉述。"),
    ("lesson-chinese-punctuation-effects-advanced", "Ac-Ⅳ-1：讓標點安排句意、聲音與關係", ["標點安排", "句意層次", "聲音節奏", "人際關係"], "在對話、敘事與論說中比較冒號、引號、刪節號、破折號、括號等符號如何同時安排資訊層次、朗讀聲音和說話者距離；改寫後以語境檢查是否產生歧義。", "同一標點在不同語境不一定有同一效果；需把符號與前後句、說話者態度、讀者預期一起判讀。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred forty-seven unit samples", "Seven hundred fifty unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
