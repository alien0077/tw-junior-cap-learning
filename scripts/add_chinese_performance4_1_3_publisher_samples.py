#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese performance 4-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版識字量、造字原則與字辭典查詢定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版識字寫字、構形理解與工具書使用定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版 4-Ⅳ-1～4-Ⅳ-3 的常用字、造字原則、多音多義與字辭典，採字詞辨析及紙筆評量。"),
]
UNITS = [
    ("lesson-chinese-performance-4-iv-1", "4-Ⅳ-1：認識至少4500字並使用3500字", ["識字量", "字形音義", "語境使用", "自主查證"], "在語境中擴充常用字庫，將字形、讀音、義項與詞語使用連結，並以閱讀與寫作反覆驗證是否真正能用。", "認得字表不等於能使用；需檢查在句中能否正確讀、寫、理解與轉用，不能只背缺乏語境的清單。"),
    ("lesson-chinese-performance-4-iv-2", "4-Ⅳ-2：造字原則輔助形音義理解", ["六書線索", "部件分析", "形音義聯繫", "字源限制"], "利用象形、指事、會意、形聲等造字線索幫助推測字義與讀音，再回到現代語境查證，避免把字源當成唯一現代解釋。", "造字分析是輔助線索不是萬能答案；需注意字形演變、借音、簡化與現代詞義的差距。"),
    ("lesson-chinese-performance-4-iv-3", "4-Ⅳ-3：字辭典處理一字多音多義", ["字辭典查詢", "多音多義", "義項選擇", "查證紀錄"], "先用句法和語境提出可能讀音與義項，再查紙本或數位字辭典比較例句、詞性和標記，記錄選擇理由與查證結果。", "不能把辭典第一個義項當正解；需核對本句詞性、搭配、時代、專門領域與讀音條件。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred seventeen unit samples", "Seven hundred twenty unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
