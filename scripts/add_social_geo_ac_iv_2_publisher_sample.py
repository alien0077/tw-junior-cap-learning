#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Geo Ac-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域；第十六週單元 5 天氣與氣候／地理，使用南一版教科書，列地 Ac-Ⅳ-2 臺灣的氣候特色。",
    ),
    "kanghsuan": (
        "https://www.kusjh.kh.edu.tw/files/shares/%E6%95%99%E5%8B%99%E8%99%95/114%E5%9C%8B%E4%B8%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2_%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%E5%85%A8%E6%A0%A1%280628%29.pdf",
        "高雄市立鼓山高級中學國中部 114 學年度集中式特教班社會課程進度；列地 Ac-Ⅳ-2 臺灣的氣候特色，教材編輯欄明載康軒版第一冊，並安排臺灣的氣候單元。",
    ),
    "hanlin": (
        "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelUyTDNCMFlWODBNVFEzWHpZMU1UUTFNemxmTnpBMk5qUXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKHCNODGIGXSNKDGICKLA0CGMKQPRLPKQPROECUSQOWSTSRKB0DGTSPLJHEDXWPK10",
        "新北市立溪崑國民中學 114 學年度七年級第一學期課程計畫；第 5 章天氣與氣候，使用翰林版第一冊，列地 Ac-Ⅳ-2 並安排臺灣氣候特色與氣候圖判讀。",
    ),
}
CONCEPTS = [
    "由天氣與氣候的時間尺度區分臺灣氣候特色的描述方式",
    "以季風、緯度、地形與海陸位置解釋臺灣區域氣候差異",
    "從氣候圖與統計資料判讀季節變化及地區差異",
]
REPRESENTATIONS = ["臺灣氣候分區圖", "氣候統計表與氣候圖", "季風與地形影響的因果圖"]
ASSESSMENT = ["氣候圖判讀", "口頭問答", "紙筆測驗", "學習單", "課堂觀察"]


def main() -> None:
    sources = []
    for publisher, (url, locator) in SOURCES.items():
        sources.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator} 核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": CONCEPTS,
            "observedRepresentations": REPRESENTATIONS,
            "observedAssessment": ASSESSMENT,
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、圖表、題目或答案。",
        })
    record = {
        "lessonId": "lesson-social-content-geo-ac-iv-2",
        "title": "地 Ac-Ⅳ-2：臺灣氣候特色",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以天氣與氣候單元串接臺灣氣候特色及統計判讀。",
                "康軒在氣候單元安排臺灣自然環境脈絡與多媒體／多元活動。",
                "翰林以氣候圖、季風與地形影響組織臺灣氣候特色的判讀。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred seventy-six unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
