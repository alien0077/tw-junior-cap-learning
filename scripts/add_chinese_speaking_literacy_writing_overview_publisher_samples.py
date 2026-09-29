#!/usr/bin/env python3
"""Record public-school publisher evidence for Chinese speaking, literacy and writing overviews."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版口語表達、識字寫字與寫作課程定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版口語互動、文字能力與寫作歷程定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版國文課程列口語表達、識字寫字與寫作，採表達任務、字詞辨識與成文修訂評量。"),
]
UNITS = [
    ("lesson-chinese-performance-2", "口語表達", ["口語表達", "情境溝通", "組織語言", "互動回應"], "依對象、目的、關係和媒介組織口語，讓敘述、說明、提問、回饋與論辯各有可辨識的結構；表達後根據聽者反應調整，而不是只追求說得流利。", "聲音大或句子長不等於有效溝通；需檢查內容是否切題、證據是否足夠、語氣是否合宜，以及是否真正回應對方。"),
    ("lesson-chinese-performance-4", "識字與寫字", ["識字", "字形", "字音字義", "書寫"], "結合字形構件、音義線索、字典工具和書寫規範處理生字，並在真實語境中確認讀寫選擇；比較辨識正誤與書寫表現時，要指出可驗證的部件或筆畫依據。", "只靠偏旁猜字可能把形近字、同音字混在一起；需交叉使用字形、讀音、詞義和語境，不能只看單一線索。"),
    ("lesson-chinese-performance-6", "寫作", ["寫作", "構思", "組織", "修訂"], "把寫作視為從題目理解、觀點形成、材料選擇、段落組織到讀者回應的循環歷程；草稿、同儕回饋與多輪修訂都要回到寫作目的和證據。", "把一次完成的文章當成寫作能力會遮蔽歷程；需分辨內容、結構、語句、格式與發布情境的問題，再提出有理由的修改。"),
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
            blocker["reason"] = blocker["reason"].replace("Seven hundred fifty-three unit samples", "Seven hundred fifty-six unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__": main()
