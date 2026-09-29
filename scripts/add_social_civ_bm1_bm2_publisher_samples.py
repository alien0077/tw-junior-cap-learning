#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Bm-IV-1..2."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫第 79 頁起；文件標示公民教材為南一版第一、二冊，學習進度列公 Bm-IV-1、Bm-IV-2 的誘因與行為概念。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；文件標示康軒版第五、六冊，公民學習內容涵蓋 Bm-IV-1、Bm-IV-2 的誘因、行為與資料／問答評量。"),
    ("hanlin", "https://www.msjh.tp.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫第 1～2 頁；文件標示翰林版，列公 Bm-Ⅳ-1 家庭與學校透過誘因影響行為、Bm-Ⅳ-2 不同人對同一誘因的反應，以及問題討論、隨堂測驗與課堂問答。"),
]
UNITS = [
    {
        "lessonId": "lesson-social-content-civ-bm-iv-1",
        "title": "公 Bm-Ⅳ-1：家庭學校誘因與行為",
        "core": ["誘因", "獎勵與成本", "家庭與學校制度", "行為改變的可觀察結果"],
        "representation": "用校園規則、獎勵與後果的前後情境表，連結誘因改變、預期成本／利益與行為選擇，不把誘因等同命令。",
        "assessment": "學生須從案例標出誘因、受影響行為與可能的副作用，再用證據說明行為改變，避免只寫『有獎就會做』。",
    },
    {
        "lessonId": "lesson-social-content-civ-bm-iv-2",
        "title": "公 Bm-Ⅳ-2：不同人對相同誘因的反應",
        "core": ["偏好差異", "資源與限制", "資訊與信念", "同一誘因的異質反應"],
        "representation": "固定同一獎勵或規則，改變不同人物的目標、成本、先備經驗與可行選項，觀察反應如何分化。",
        "assessment": "要求區分共同誘因與個人條件，提出至少兩項可由資料支持的差異原因；不得用人格標籤取代分析。",
    },
]

def main():
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    units = {x["lessonId"]: x for x in data["units"]}
    for u in UNITS:
        units[u["lessonId"]] = {
            "lessonId": u["lessonId"], "title": u["title"],
            "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
            "sources": [{
                "publisher": publisher, "sourceUrl": url,
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": locator, "accessedAt": "2026-09-21",
                "observedConcepts": [u["title"], *u["core"]],
                "observedRepresentations": [u["representation"]],
                "observedAssessment": [u["assessment"]],
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、章節定位與評量方向；不複製教科書正文、圖表、題目或答案。",
            } for publisher, url, locator in SOURCES],
            "fusionReview": {
                "commonCore": u["core"],
                "differencesToReview": [u["representation"], u["assessment"]],
                "originalSynthesisBoundary": "三版本融合、內容／版權審查與 Terra 複核完成前維持 draft，不升級 publisher status。",
            },
        }
    data["units"] = sorted(units.values(), key=lambda x: x["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str):
            b["reason"] = b["reason"].replace("Five hundred three unit samples", "Five hundred five unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 2}, ensure_ascii=False))

if __name__ == "__main__":
    main()
