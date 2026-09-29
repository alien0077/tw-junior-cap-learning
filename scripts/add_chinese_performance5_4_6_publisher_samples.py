#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese performance 5-IV-4..6."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版閱讀策略、跨域整合與多元文本議題定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版整合閱讀、跨域知識與生活社會議題定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版 5-Ⅳ-4～5-Ⅳ-6 的閱讀策略、跨域議題、多元文本與紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-performance-5-iv-4", "5-Ⅳ-4：閱讀策略整合跨域知識解題", ["閱讀策略", "跨域知識", "問題拆解", "證據整合"], "依題目目的選擇預測、提問、摘要、圖表判讀與來源查證等策略，把文本資訊和學科知識整合成可驗證的解題路徑。", "套用策略名稱不等於有效解題；需說明問題類型、資料關係、排除過程與答案證據。"),
    ("lesson-chinese-performance-5-iv-5", "5-Ⅳ-5：多元閱讀理解議題與生活社會關聯", ["多元文本", "生活議題", "社會脈絡", "觀點比較"], "比較新聞、圖表、廣告、文學與公共資料如何呈現同一生活議題，辨認文本立場、受眾、證據和沉默的聲音。", "把生活經驗帶進閱讀不能取代文本證據；需分開個人感受、文本主張、外部事實與價值判斷。"),
    ("lesson-chinese-performance-5-iv-6", "5-Ⅳ-6：運用圖表資料增進閱讀理解", ["圖表閱讀", "資料尺度", "文字圖表互證", "推論限制"], "先讀圖表標題、單位、時間與樣本，再與正文的主張互相核對，判斷趨勢、差異與可支持的結論。", "圖表有數字不代表結論充分；要注意座標截斷、樣本偏差、相關與因果混淆及資料缺漏。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred twenty-six unit samples", "Seven hundred twenty-nine unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
