#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ab-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "苗栗縣立建國國中公民課程計畫，南一版單元 5 校園生活與公共事務參與明列公 Ab-Ⅳ-2，安排口頭問答、觀察、電腦實作、討論與學習歷程評量。"),
    "kanghsuan": ("https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2024/plan/1484_plan.pdf", "新北市立新泰國中公民課程計畫，康軒版章節校園生活中的公共參與明列公 Ab-Ⅳ-2，使用平板、大屏、自製學習單與 Nearpod，要求學生從校園議題提出公共參與方案。"),
    "hanlin": ("https://www.ptskids.tw/storage_link/photos/63116d0ea7cac.pdf", "公共教育教學資源明列翰林版《國民中學社會－公民與社會篇第一冊》公 Ab-IV-2，以旁觀者介入反霸凌活動呈現尊重、同理、責任與公民德性。"),
}
CONCEPTS = [
    "辨識學生在校園中的受教、安全、平等、表意參與、隱私與人格尊嚴等權利，並說明權利行使與責任、規範及他人權利的界線",
    "以校園公共議題理解聆聽、尊重、同理、和平解決衝突、反霸凌與依程序參與等公民德性",
    "區分權利主張、個人偏好、校規、責任與程序，利用不同利害關係人及資料提出公平、可行且可檢驗的校園政策修正方案",
]
REPRESENTATIONS = ["權利—責任—規範—程序—救濟矩陣", "校園公共議題利害關係人與影響矩陣", "發現問題—蒐集證據—表達意見—協商決策—申訴追蹤流程"]
ASSESSMENT = ["校園政策案例閱讀", "權利、偏好、規則與責任分類", "反霸凌與尊重情境討論", "根據證據提出校園方案與修正版條文", "口頭、分組、學習單、觀察與紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校或公開教育資源的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-ab-iv-2", "title": "公 Ab-Ⅳ-2：校園權利與公民德性", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一把校園生活與公共事務參與連在一起，需將學生權利、責任與參與程序具體化。", "康軒以校園公共參與與數位互動活動呈現，需檢查方案是否有證據、利害關係人與可追蹤程序。", "翰林以反霸凌旁觀者介入切入公民德性，需補足權利救濟、校規界線與多方協商。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred one unit samples", "Four hundred two unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
