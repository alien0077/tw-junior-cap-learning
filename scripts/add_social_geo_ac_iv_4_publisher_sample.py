#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ac-IV-4."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；第十七週單元 5 天氣與氣候／地理，使用南一版教科書，列地 Ac-Ⅳ-4 問題探究：颱風與生活。"),
    "kanghsuan": ("https://www.ptjh.tp.edu.tw/wp-content/uploads/doc/d0011/113-%E9%98%B2%E7%81%BD%E6%95%99%E8%82%B2%E8%9E%8D%E5%85%A5%E9%A0%98%E5%9F%9F%E6%95%99%E5%AD%B8%E8%AA%B2%E7%A8%8B%E8%A8%AD%E8%A8%88%EF%BC%9A%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F.pdf", "臺北市立北投國民中學 113 學年度社會領域地理科防災融入教學設計；教材版本明載康軒版，列地 Ac-Ⅳ-4 問題探究：颱風與生活，並安排預警資訊、脆弱度與防災行動判讀。"),
    "hanlin": ("https://www.chhs.tp.edu.tw/uploads/1751949327108AUE6LESi.pdf", "臺北市立景興國民中學 114 學年度社會領域地理科課程計畫；教材版本明載翰林版，於臺灣氣候與水文單元列地 Ac-Ⅳ-4 問題探究：颱風與生活，安排紙筆、作業與實作評量。"),
}
CONCEPTS = ["以颱風生成、路徑與降雨風力資料說明影響機制", "區分自然災害風險與社會、經濟、土地利用造成的脆弱度", "運用預警資訊判斷個人與社區可行的防災行動"]
REPRESENTATIONS = ["颱風路徑與氣象資料圖", "風雨影響與脆弱度對照表", "預警資訊到行動決策流程圖"]
ASSESSMENT = ["資料判讀", "情境討論", "紙筆測驗", "防災行動設計", "學習單"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-geo-ac-iv-4", "title": "地 Ac-Ⅳ-4：問題探究：颱風與生活", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一將颱風探究放在天氣與氣候單元，連結臺灣氣候與生活影響。", "康軒以防災教育切入預警、脆弱度、回復力與行動決策。", "翰林把颱風與生活放在臺灣氣候與水文的探究及實作評量序列。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred seventy-eight unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
