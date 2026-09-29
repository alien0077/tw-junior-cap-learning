#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese Ba, Bb and Bc."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版記敘、抒情與說明文本的閱讀寫作定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版記敘、抒情、說明文本與閱讀表達定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列 Ba、Bb、Bc 的敘事細節、抒情語氣、說明結構與紙筆評量。"),
]
UNITS = [
    ("ba", "Ba：記敘文本——安排事件與寫出可感的細節", ["事件順序", "敘事視角", "場景細節", "人物行動"], "沿著事件起因、轉折、高潮與結果閱讀，觀察視角、動作、感官與場景細節如何共同塑造人物選擇及情節意義。", "記敘不是事件清單；需區分作者安排的時間順序、敘述者觀點與讀者依文本證據做出的推論。"),
    ("bb", "Bb：抒情文本", ["情感經驗", "意象", "語氣節奏", "情景交融"], "從意象反覆、語氣轉折、節奏與敘寫場景辨認情感變化，說明文字如何把個人感受連到時間、記憶與讀者經驗。", "不能只用情緒標籤回答；需回指具體語句、意象關係與語氣變化，避免把作者和讀者感受混為一談。"),
    ("bc", "Bc：說明文本", ["說明目的", "分類比較", "因果關係", "圖表與文字"], "辨認說明對象、範圍與目的，利用定義、分類、比較、因果及圖表資料重建資訊關係，判斷哪些是文本明示、哪些是合理推論。", "資料多不等於說明清楚；要檢查分類標準、因果證據、圖表尺度與關鍵條件是否被省略。"),
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for suffix, title, core, representation, assessment in UNITS:
        lesson_id = "lesson-chinese-content-" + suffix
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred one unit samples", "Seven hundred four unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
