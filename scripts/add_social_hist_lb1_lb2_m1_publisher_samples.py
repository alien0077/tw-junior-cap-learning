#!/usr/bin/env python3
"""Record public-school publisher evidence for social history Lb-IV-1..2 and M-IV-1."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的當代東亞、國際互動與探究活動定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的冷戰東亞、東南亞區域互動與資料探究定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 Lb-Ⅳ-1、Lb-Ⅳ-2 與 M-Ⅳ-1，採史料、地圖、討論及探究評量。"),
]
UNITS = [
    ("lb-iv-1", "歷 Lb-Ⅳ-1：冷戰東亞競合", ["冷戰", "東亞", "陣營互動", "臺灣位置"], "以時間軸、地圖與不同陣營的政策資料，對照冷戰在東亞的軍事、政治與經濟競合，辨識地方經驗如何受全球格局牽動。", "要區分全球冷戰架構與各地自身的政治選擇，不能把東亞歷史簡化成美蘇兩方單線命令。"),
    ("lb-iv-2", "歷 Lb-Ⅳ-2：東南亞國際組織發展影響", ["東南亞", "區域組織", "國際合作", "發展差異"], "比較東南亞區域合作的成立背景、成員利益與政策限制，從地圖、條約與經濟社會指標判斷國際組織對區域發展的實際影響。", "需把組織成立宗旨、會員國利益與執行成效分開，不能只因有共同宣言就推定合作已經成功。"),
    ("m-iv-1", "歷 M-Ⅳ-1：從主題 K、L 選題深入探究或踏查展演", ["歷史探究", "選題", "史料查證", "踏查展演"], "把主題 K、L 的問題轉成可查證的探究題，設計史料蒐集、地方踏查或展演的證據鏈，再用成果回應原問題並說明限制。", "探究成果不能只靠漂亮展示；要交代問題、來源、判讀方法、反例與修正依據，讓觀眾能追溯結論如何形成。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-social-content-hist-" + suffix
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
            blocker["reason"] = blocker["reason"].replace("Six hundred fifty-two unit samples", "Six hundred fifty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
