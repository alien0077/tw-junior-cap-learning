#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bb-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://course.cyc.edu.tw/upfile/course109/sub1/14535426760482702.pdf", "嘉義縣公立國中公民課程計畫，南一版第一冊把公 Bb-Ⅳ-1 放在志願團體／公民單元，連結公民參與公共事務、團體生活與口頭問答、課堂觀察、討論及紙筆評量。"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf", "嘉義縣阿里山國民中小學公民課程計畫，教材明載康軒版，從公民價值、社會團體與公共參與安排 Bb-Ⅳ-1 的概念理解、生活解析、分組討論與課堂問答。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490237526.pdf", "嘉義縣新港國中公民課程計畫，教材明載翰林版第一、二冊，公 Bb-Ⅳ-1 置於公民與公民德性、團體參與與公共生活脈絡，採課堂發言、紙筆測驗與資料蒐集。"),
}
CONCEPTS = [
    "區分家庭外團體、正式組織、非正式團體與志願結社，從共同目標、成員關係、規範與資源理解團體如何運作",
    "說明個人參與團體的原因與可能角色，分析團體如何滿足需求、形成認同、整合意見並影響公共生活",
    "比較不同團體的參與門檻、權力分配、代表性與公共影響，提出兼顧自主、透明、包容與責任的參與方案",
]
REPRESENTATIONS = ["個人—團體—公共生活三層關係圖", "團體類型／目標／規範／成員權力矩陣", "需求形成—組織行動—意見表達—公共影響—責任檢核流程"]
ASSESSMENT = ["團體類型與志願結社案例判讀", "成員角色、規範與權力關係比較", "團體對公共生活影響的資料閱讀", "設計包容且可追蹤的參與方案", "口頭問答、課堂觀察、分組討論、紙筆測驗與資料蒐集"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-bb-iv-1", "title": "公 Bb-Ⅳ-1：家庭外團體參與", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以志願團體與現代公民參與為入口，需把團體類型、成員角色與公共影響拆開分析。", "康軒從公民價值與社會團體的生活脈絡切入，需補足參與門檻、代表性與權力分配。", "翰林把公民德性、團體參與與資料蒐集並列，需以證據檢查團體是否真正包容並負公共責任。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred four unit samples", "Four hundred five unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
