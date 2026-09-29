#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ab-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"

SOURCES = {
    "nani": {
        "url": "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "locator": "國立卓蘭高中附設國中部 113 學年度七年級社會領域；第十二週單元 4 臺灣的海岸與島嶼／地理，使用南一版教科書，列地 Ab-Ⅳ-3 臺灣的領海與經濟海域。",
    },
    "kanghsuan": {
        "url": "https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/114%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2_%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%85%A8%E6%A0%A1%280628%29.pdf",
        "locator": "高雄市立鼓山高級中學國中部 114 學年度集中式特教班社會課程進度；列地 Ab-Ⅳ-3 臺灣的領海與經濟海域，教材編輯欄明載康軒版第一冊，並以第 4 項臺灣的海域安排教學。",
    },
    "hanlin": {
        "url": "https://course.cyc.edu.tw/upfile/course111/sub1/15080292609222713.pdf",
        "locator": "嘉義縣忠和國民中學 111 學年度七年級第一、二學期社會領域地理科；第 149 頁標示翰林版第 1、2 冊，第 152–153 頁列地 Ab-Ⅳ-3，並安排領海、經濟海域差異與經濟海域重疊判讀。",
    },
}

CONCEPTS = [
    "分辨領海與經濟海域的權利範圍及概念差異",
    "以臺灣本島與離島位置解釋海域範圍和鄰國重疊的空間情境",
    "從地圖與海洋議題資料說明海域權利、主權與資源利用的關聯",
]
REPRESENTATIONS = [
    "臺灣本島與離島位置圖",
    "領海與經濟海域範圍示意圖",
    "海域重疊情境的地圖與資料表",
]
ASSESSMENT = ["地圖判讀", "口頭問答", "紙筆測驗", "小組討論", "學習單"]


def main() -> None:
    sources = []
    for publisher, source in SOURCES.items():
        sources.append(
            {
                "publisher": publisher,
                "sourceUrl": source["url"],
                "sourceKind": "public-school-course-plan-identifying-publisher-material",
                "locator": f"{source['locator']} 核讀 2026-09-20。",
                "accessedAt": "2026-09-20",
                "observedConcepts": CONCEPTS,
                "observedRepresentations": REPRESENTATIONS,
                "observedAssessment": ASSESSMENT,
                "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、地圖、題目或答案。",
            }
        )

    record = {
        "lessonId": "lesson-social-content-geo-ab-iv-3",
        "title": "地 Ab-Ⅳ-3：臺灣的領海與經濟海域",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一將海域概念放在臺灣海岸與島嶼單元，與離島和海岸情境連結。",
                "康軒以臺灣海域作為基本概念與海洋教育的教學活動。",
                "翰林明列領海、經濟海域差異及鄰國海域重疊的地圖判讀。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、地圖、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }

    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
    if record["lessonId"] not in existing:
        data["units"].append(record)
        added.append(record["lessonId"])
    data["unitCount"] = len(data["units"])
    data["updatedAt"] = "2026-09-20"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blockers_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(
                r"Three hundred [a-z-]+ unit samples",
                "Three hundred seventy-five unit samples",
                reason,
            )
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
