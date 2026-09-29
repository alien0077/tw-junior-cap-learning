#!/usr/bin/env python3
"""Record public-school publisher evidence for social history C, Ca and Cb."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的清帝國治理、臺灣社會與政治經濟變化定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的清代臺灣、移墾社會、治理與文化互動定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 C、Ca、Cb 的政經制度、社會文化與資料判讀，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("c", "C：清帝國時期的臺灣", ["清帝國治理", "移墾社會", "邊疆與秩序", "族群互動"], "把行政制度、移民開墾、地方社會與對外關係放在同一時間軸，分析清帝國如何逐步調整臺灣治理，以及地方社會如何回應。", "不能把清帝國初期到後期的治理範圍視為一成不變，也不能用現代民族國家概念直接套用到當時的身分與秩序。"),
    ("ca", "Ca：政治經濟的變遷", ["行政制度", "港口與貿易", "土地開發", "區域連結"], "從行政區劃、港口貿易、土地利用與產業資料交叉判讀政治權力和經濟網絡的變化，說明制度調整如何影響不同地區與群體。", "要分開政策規定、實際執行與地方利益；貿易量增加不必然表示所有居民都同等受益。"),
    ("cb", "Cb：社會文化的變遷", ["社會組織", "信仰與教育", "族群互動", "文化調適"], "用地方文書、廟宇與信仰、教育傳播及族群生活資料，追蹤社會組織如何形成、衝突與協商，並辨識文化變遷中的延續與重組。", "不能把文化交流簡化成單向同化，也不能只從精英文字記錄推論所有人的生活；需交代資料代表性與沉默者。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred fifty-eight unit samples", "Six hundred sixty-one unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
