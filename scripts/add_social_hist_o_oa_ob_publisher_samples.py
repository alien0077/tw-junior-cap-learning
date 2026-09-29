#!/usr/bin/env python3
"""Record public-school publisher evidence for social history O, Oa and Ob."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版歷史課程的近代世界變革、歐洲興起與多元世界互動定位。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版歷史課程的近代變革、歐洲政治社會與跨區域互動定位。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版歷史課程列 O、Oa、Ob 的近代世界變革、歐洲興起與多元互動，採史料、地圖、討論及紙筆評量。"),
]
UNITS = [
    ("o", "O：近代世界的變革", ["近代轉型", "科技與社會", "政治革命", "全球連結"], "比較政治革命、工業化、科學技術與全球貿易的資料，分析近代世界秩序如何改變，並追問變革由誰推動、誰受益及誰承擔成本。", "不能把科技或革命視為自動帶來進步；需區分制度變化、物質條件、勞動經驗與殖民擴張。"),
    ("oa", "Oa：近代歐洲興起", ["歐洲國家", "宗教與思想", "工業化", "帝國擴張"], "以國家制度、宗教思想、工業生產與海外擴張資料，追蹤近代歐洲力量上升的多重條件，並檢視其與其他地區的互動。", "歐洲興起不是單一文化優越的結果；要同時分析資源、制度、競爭、殖民暴力與跨區域借用。"),
    ("ob", "Ob：多元世界互動", ["跨區域交流", "帝國與殖民", "人口移動", "文化混融"], "從航線、商品、人口、疾病、法律與文化資料，分析近代多元世界的連結與不平等，辨識交流、強制移動與文化混融的不同機制。", "全球互動不等於平等互惠；需指出權力、暴力、資源分配與被移動者的觀點。"),
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
            blocker["reason"] = blocker["reason"].replace("Six hundred eighty-two unit samples", "Six hundred eighty-five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": len(UNITS)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
