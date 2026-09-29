#!/usr/bin/env python3
"""Record public-school publisher evidence for social history G, H and Ha."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史考察、古典至傳統時代與政治社會文化互動定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史探究、古代文明與政治社會文化變遷定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 G、H、Ha 的史料探究、古典傳統與制度文化差異，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("g", "G：歷史考察（二）", ["資料蒐集", "比較史料", "空間脈絡", "歷史論證"], "把一個跨時空問題拆成資料可回答的子問題，利用時間軸、地圖與不同類型史料比較證據，再形成可被檢驗的論證。", "不能只挑支持預設結論的材料；需記錄反例、資料缺口、來源立場與比較尺度。"),
    ("h", "H：從古典到傳統時代", ["古代文明", "政權與社會", "思想與制度", "傳統秩序"], "比較古典文明到傳統時代的政權、社會階層、思想與制度如何相互支撐，並以不同地區案例辨識延續與變化。", "不能把文明演變排列成單一路線或高低階序；需說明不同環境、交流與權力關係造成的差異。"),
    ("ha", "Ha：政治社會文化變遷差異互動", ["政治制度", "社會階層", "文化傳播", "差異互動"], "將政治權力、社會組織與文化表現放在同一分析框架，從制度、日常生活與交流資料觀察差異如何被維持、協商或重組。", "文化相似不代表政治制度相同，制度移植也不代表社會結果一致；要分別指出互動的機制與限制。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred sixty-seven unit samples", "Six hundred seventy unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
