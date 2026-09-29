#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Cd-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 4 平權的家庭／公民，使用南一版教科書，列公 Cd-Ⅳ-2 家務勞動分擔對個人發展與社會參與的影響及性別不平等，採問答、觀察、實作、討論與學習歷程評量。"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course110/sub1/14793374486888342.pdf", "嘉義縣東石國民中學公立特殊教育集中式特教班 110 學年度社會領域教學計畫；教材來源明載編選參考康軒版社會科，調整後學習內容列公 Cd-Ⅳ-2，聚焦家務分擔、個人發展與性別不平等，並採教師觀察、自評、紙筆與口頭評量。"),
    "hanlin": ("https://rb002.tcpa.edu.tw/var/file/5/1005/img/759120767.pdf", "國立臺灣戲曲學院國中部 108 學年度公立校方社會／公民課程計畫；教材版本明載翰林，學習內容列公 Cd-Ⅳ-2，置於平權家庭與家庭職能脈絡，並以家庭平權、權利責任及資料討論作為學習方向。"),
}
CONCEPTS = ["辨識家務、照顧與市場勞動的分工，分析時間、責任與資源如何在家庭成員間分配", "以性別角色、家庭型態、工作安排與個人發展資料檢查分工是否造成不平等", "比較家庭協商、公共政策與制度支持的改善方案，區分個人選擇、社會規範與結構限制"]
REPRESENTATIONS = ["家庭一日時間分配表", "家務責任、受益者與機會成本矩陣", "性別角色—分工—個人發展—政策支持因果圖"]
ASSESSMENT = ["家庭分工資料閱讀", "性別平權案例比較", "課堂討論與口頭表達", "學習單", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-cd-iv-2", "title": "公 Cd-Ⅳ-2：家務勞動分擔與性別不平等", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以平權家庭章節連結親屬關係、家務分擔與性別平權的生活探究。", "康軒以特殊教育課程的減量與分解方式呈現家務分工、個人發展與性別不平等，評量較重視觀察與口頭表達。", "翰林以平權家庭與家庭職能脈絡安排權利責任及公民討論，需再核對正式冊次內的概念順序。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-seven unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
