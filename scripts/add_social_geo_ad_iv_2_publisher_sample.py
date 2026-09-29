#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ad-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://course.cyc.edu.tw/upfile/course109/sub1/14535426760482702.pdf", "嘉義縣梅山國民中學 109 學年度七年級第二學期社會領域地理科；教材版本明載南一版第二冊，列地 Ad-Ⅳ-2 臺灣的人口組成。"),
    "kanghsuan": ("https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/113%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/%E9%AB%98%E9%9B%84%E5%B8%82%E7%AB%8B%E9%BC%93%E5%B1%B1%E9%AB%98%E7%B4%9A%E4%B8%AD%E5%AD%B8%28%E5%9C%8B%E4%B8%AD%E9%83%A8%29113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%AE%8A%E6%95%99_%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%29%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "高雄市立鼓山高級中學國中部 113 學年度集中式特教班社會課程進度；列地 Ad-Ⅳ-2 臺灣的人口組成，教材編輯欄明載康軒版第二冊。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490258175.pdf", "嘉義縣新港國民中學 114 學年度七年級第二學期社會領域地理科；第一篇臺灣的環境（下）第二章人口組成與族群文化，教材版本明載翰林版第二冊，列地 Ad-Ⅳ-2。"),
}
CONCEPTS = ["以年齡、性別與扶養關係描述人口組成", "運用人口金字塔、性別比與扶養比判讀人口結構", "由人口組成資料推論少子化、高齡化與社會支持需求"]
REPRESENTATIONS = ["人口金字塔", "性別比與扶養比計算表", "人口結構變化折線圖"]
ASSESSMENT = ["人口圖表判讀", "數據計算", "情境解釋", "紙筆測驗", "口頭問答"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-geo-ad-iv-2", "title": "地 Ad-Ⅳ-2：臺灣的人口組成", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人口成長與分布脈絡帶入人口組成和人口問題。", "康軒以人口組成連接多元族群、社會支持與人文環境。", "翰林明列人口金字塔、扶養比、性別比的圖表與計算判讀。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-two unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
