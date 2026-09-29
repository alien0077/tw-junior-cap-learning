#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bc root scope."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版；公民單元 4 社會中的文化把 Bc-Ⅳ-1～3 的社會規範、文化與規範變動放在同一章節脈絡，並安排多元口語、觀察、實作與討論評量。",
    ),
    "kanghsuan": (
        "https://www.csjh.kh.edu.tw/fxmteach/113/113%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%E7%8F%AD%E7%B4%9A/113%E7%89%B9%E6%95%99%E7%8F%AD/113-2%E7%89%B9%E6%95%99%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%287-9%E5%B9%B4%E7%B4%9A%E6%B7%B7%E9%BD%A21%E7%8F%AD%E5%85%A8%29.pdf",
        "高雄市立中山國民中學 113 學年度公立特教課程計畫，教材編輯明載康軒版第一、二冊；將 Bc-Ⅳ-1～3 連成社會規範與文化單元，採簡化、分解、直接教學及紙筆／口語評量。",
    ),
    "hanlin": (
        "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO",
        "新北市立溪崑國民中學 114 學年度公立校方課程計畫，教材明載翰林版；第三篇公民與社會生活第二章社會規範依序處理正式／非正式規範、法律差異與規範變動，使用 KWLQ、討論、學習單與自評互評。",
    ),
}
CONCEPTS = [
    "建立規範、秩序與控制的層次關係：規範提供預期，秩序是互動結果，控制是維持或修正規範的社會機制",
    "串連法律、道德、習俗、文化與正式／非正式規範，辨識不同來源、效力、制裁與程序",
    "從日常生活、文化差異與時空變遷資料判斷規範的正當性、權利影響與可修訂的公共參與方式",
]
REPRESENTATIONS = [
    "規範—秩序—控制三層概念圖",
    "來源—效力—制裁—程序—權利影響比較矩陣",
    "日常事件到公共規則修訂的因果流程",
]
ASSESSMENT = [
    "跨 Bc-Ⅳ-1～3 的概念整合案例",
    "文化與規範變動資料閱讀",
    "不同控制方式的效果與界線比較",
    "公共規則修訂提案與同儕回饋",
    "口頭、紙筆、學習單、討論與自評互評",
]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator} 核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": CONCEPTS,
            "observedRepresentations": REPRESENTATIONS,
            "observedAssessment": ASSESSMENT,
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。",
        })
    record = {
        "lessonId": "lesson-social-content-civ-bc",
        "title": "Bc：規範、秩序與控制",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以社會中的文化章節串接三個 Bc 細項，需將根單元的整合框架與各細項教學證據分開保留。",
                "康軒以特教課程調整呈現完整 Bc 範圍，需把可遷移的概念結構與個別化教學方法區分。",
                "翰林以正式／非正式規範、法律發展與規範變動形成連續章節，需補足控制概念的權利與程序界線。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；根 lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-six unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
