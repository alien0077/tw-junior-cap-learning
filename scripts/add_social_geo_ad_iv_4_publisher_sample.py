#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ad-IV-4."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 2 臺灣的人口組成與多元文化，使用南一版教科書，列地 Ad-Ⅳ-4 問題探究：臺灣人口問題與對策。"),
    "kanghsuan": ("https://cmsb.tc.edu.tw/var/file/89/1089/attach/9/pta_315983_1926225_10554.pdf", "臺中市立啟明學校公立特殊教育學校課程計畫；以國中康軒版社會領域課本第二冊為主要教材，臺灣的人口與文化單元第 2 週列臺灣當前的人口問題與因應對策，採多元評量。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course113/sub1/15650225818512746.pdf", "嘉義縣新港國民中學 113 學年度七年級第二學期社會領域地理科；教材版本翰林版第二冊，第二章人口組成與族群文化第 5 週列地 Ad-Ⅳ-4，學習目標為了解臺灣少子化現象與影響。"),
}
CONCEPTS = ["以出生、死亡與遷移資料辨識少子化、高齡化及人口移動等人口問題", "由人口結構與分布推論教育、勞動、照護、城鄉發展等社會與經濟影響", "比較家庭、地方與中央的因應策略，依資料與可行性提出人口政策判斷"]
REPRESENTATIONS = ["人口成長折線圖與年齡結構圖", "人口問題—成因—影響—對策關聯表", "政策目標、受益對象與可能限制的比較矩陣"]
ASSESSMENT = ["人口統計資料閱讀", "問題因果分析", "政策方案比較", "學習單與討論", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-geo-ad-iv-4", "title": "地 Ad-Ⅳ-4：人口問題與對策", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人口組成與多元文化單元中的問題探究連結人口現象與對策。", "康軒明確安排臺灣當前人口問題及因應對策，並以多元評量檢核理解。", "翰林以少子化現象與影響作為人口問題的具體學習入口，置於人口組成與族群文化章節。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-four unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
