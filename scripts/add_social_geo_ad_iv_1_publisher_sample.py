#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ad-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 2 臺灣的人口組成與多元文化，使用南一版教科書，列地 Ad-Ⅳ-1 臺灣的人口成長與分布。"),
    "kanghsuan": ("https://www.kusjh.kh.edu.tw/upload/files/%E9%AB%98%E9%9B%84%E5%B8%82%E7%AB%8B%E9%BC%93%E5%B1%B1%E9%AB%98%E4%B8%AD%28%E5%9C%8B%E4%B8%AD%E9%83%A8%29111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%EF%BC%88%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%EF%BC%89%E7%8F%AD%E7%B4%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB0613%E6%A0%B8%E7%AB%A0.pdf", "高雄市立鼓山高級中學國中部 111 學年度集中式特教班社會／地理課程進度；列地 Ad-Ⅳ-1 臺灣的人口成長與分布，教材編輯欄明載康軒版第二冊。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490258175.pdf", "嘉義縣新港國民中學 114 學年度七年級第二學期社會領域地理科；第一篇臺灣的環境（下）第一章人口成長與分布，教材版本明載翰林版第二冊，列地 Ad-Ⅳ-1。"),
}
CONCEPTS = ["以出生、死亡、移入與移出解釋人口成長變動", "以人口密度與分布圖判讀臺灣人口空間差異", "從自然增加、社會增加與遷移資料建立人口分布的因果解釋"]
REPRESENTATIONS = ["人口自然／社會增加流程圖", "人口密度分布圖", "人口成長與遷移統計圖表"]
ASSESSMENT = ["人口圖表判讀", "計算與比較", "紙筆測驗", "口頭說明", "學習單"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-geo-ad-iv-1", "title": "地 Ad-Ⅳ-1：臺灣的人口成長與分布", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一把人口成長與分布放在臺灣人口組成與多元文化的整體脈絡。", "康軒以人口變動、遷移、分布和人口議題串接第二冊的人文環境。", "翰林明列自然增加率、社會增加率、人口密度與人口分布圖的判讀步驟。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
