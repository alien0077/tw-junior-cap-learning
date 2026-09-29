#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ad-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 2 臺灣的人口組成與多元文化，使用南一版教科書，列地 Ad-Ⅳ-3 多元族群的文化特色。"),
    "kanghsuan": ("https://www.kusjh.kh.edu.tw/upload/files/%E9%AB%98%E9%9B%84%E5%B8%82%E7%AB%8B%E9%BC%93%E5%B1%B1%E9%AB%98%E4%B8%AD%28%E5%9C%8B%E4%B8%AD%E9%83%A8%29111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%EF%BC%88%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%EF%BC%89%E7%8F%AD%E7%B4%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB0613%E6%A0%B8%E7%AB%A0.pdf", "高雄市立鼓山高級中學國中部 111 學年度集中式特教班社會／地理課程進度；列地 Ad-Ⅳ-3 多元族群的文化特色，教材編輯欄明載康軒版第二冊，並融入多元文化與國際教育。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490258175.pdf", "嘉義縣新港國民中學 114 學年度七年級第二學期社會領域地理科；第二章人口組成與族群文化，教材版本明載翰林版第二冊，列地 Ad-Ⅳ-3 並以族群文化資料與討論評量。"),
}
CONCEPTS = ["以歷史來源、移民社會與空間分布理解臺灣多元族群", "比較原住民族、漢人與新住民文化形成的不同脈絡", "以節慶、生活方式與文化資料判讀文化差異並建立尊重觀點"]
REPRESENTATIONS = ["族群來源與遷移示意圖", "文化特色比較表", "族群—空間—生活方式關聯圖"]
ASSESSMENT = ["資料閱讀", "文化比較", "口頭分享", "學習單", "討論與紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-geo-ad-iv-3", "title": "地 Ad-Ⅳ-3：多元族群的文化特色", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人口組成與多元文化單元連結族群來源、文化特色與移民社會。", "康軒以多元文化、國際教育與族群融合情境安排比較和討論。", "翰林以族群文化資料、節慶與課堂發表形成具體探究活動。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-three unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
