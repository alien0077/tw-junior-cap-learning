#!/usr/bin/env python3
"""Record public-school publisher evidence for social history F, Fa and Fb."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的戰後臺灣、政治外交與經濟社會變遷定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的戰後臺灣、民主化、外交與產業社會變化定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 F、Fa、Fb 的戰後政治、國際關係、經濟與社會，採史料、統計、討論及紙筆評量。"),
]
UNITS = [
    ("f", "F：當代臺灣", ["戰後臺灣", "制度變遷", "社會轉型", "國際脈絡"], "沿著戰後政權、經濟、社會與文化的時間線，對照制度轉折與人民生活資料，理解當代臺灣在國際環境與內部選擇中形成。", "不能把戰後發展寫成單一進步故事；要同時辨識制度限制、社會差異、受益與代價，以及資料中的不同聲音。"),
    ("fa", "Fa：政治外交的變遷", ["政治制度", "民主化", "外交關係", "國際位置"], "用憲政制度、選舉、外交文件與國際事件資料，分析臺灣政治制度與外交位置的變化，並區分國內改革和外部壓力的交互作用。", "選舉結果或外交事件本身不是完整因果；需交代制度背景、參與者、國際條件與不同群體的政治經驗。"),
    ("fb", "Fb：經濟社會的變遷", ["產業轉型", "都市化", "勞動與階級", "社會運動"], "比較農業、工業、服務業、人口移動與社會運動資料，追蹤經濟轉型如何改變家庭、勞動和城鄉關係，並評估成長與分配的落差。", "GDP、產值或都市建設不能單獨代表生活改善；要把所得、勞動條件、性別、地區與環境成本一起檢視。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred sixty-four unit samples", "Six hundred sixty-seven unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
