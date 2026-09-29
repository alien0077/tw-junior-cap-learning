#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Bn-IV-1..3."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"
SOURCES = [
    ("nani", "https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣永慶高中公立課程計畫；南一版公民課程進度中的日常交易單元，列公 Bn-IV-1、Bn-IV-2、Bn-IV-3。"),
    ("kanghsuan", "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf", "嘉義縣立布袋國民中學公立課程計畫；康軒版第五、六冊的公民課程欄，列日常生活交易、分工與自願交易相關的 Bn-IV-1～3。"),
    ("hanlin", "https://www.msjh.ntpc.edu.tw/uploads/1691978949408RP7cOuyZ.pdf", "臺北市立民生國民中學公立課程計畫；翰林版公民課程將 Bn-IV-1～3 排入日常生活的交易單元，採分組討論、課堂問答與作業評量。"),
]
UNITS = [
    {
        "lessonId": "lesson-social-content-civ-bn-iv-1",
        "title": "公 Bn-Ⅳ-1：個人與家庭滿足生活需求",
        "core": ["基本生活需求", "家庭資源", "生產與取得方式", "選擇與限制"],
        "representation": "以家庭一週的食衣住行需求表，分辨自製、購買、交換與公共服務等取得方式，並標出時間、金錢與技能限制。",
        "assessment": "學生需把需求、資源與取得方案連起來，說明為何同一家庭不會只靠單一方式滿足所有需求。",
    },
    {
        "lessonId": "lesson-social-content-civ-bn-iv-2",
        "title": "公 Bn-Ⅳ-2：從自給自足轉向交易",
        "core": ["分工", "專業化", "交易成本", "比較利益與互賴"],
        "representation": "用兩人或兩個家庭的時間與產出表，比較各自生產與分工交易後的可得數量，呈現互賴如何降低滿足需求的成本。",
        "assessment": "先辨認交易前的限制，再用產出或時間資料說明分工與交易的誘因，避免把交易只解釋成『比較方便』。",
    },
    {
        "lessonId": "lesson-social-content-civ-bn-iv-3",
        "title": "公 Bn-Ⅳ-3：自願交易對雙方的利益",
        "core": ["自願交易", "主觀價值", "互利交換", "資訊與公平交易條件"],
        "representation": "用交易前後雙方對物品價值與替代方案的比較表，說明在知情、自願且無強迫下，交易可同時提高雙方主觀利益。",
        "assessment": "要求指出雙方願意交換的理由與必要條件，並辨認欺瞞、強迫或資訊不對稱時不能直接推定雙方受益。",
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
                "licenseBoundary": "僅記錄公立學校課程計畫的出版商、單元定位與評量方向；不複製教科書正文、圖表、題目或答案。",
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
            b["reason"] = b["reason"].replace("Five hundred five unit samples", "Five hundred eight unit samples")
    BLOCKERS.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": 3}, ensure_ascii=False))

if __name__ == "__main__":
    main()
