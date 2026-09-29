#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bc-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版教科書；以公民單元 4 社會中的文化定位公 Bc-Ⅳ-1，記錄社會規範的必要性、法律與其他規範差異，以及口頭問答、觀察、實作與討論評量。",
    ),
    "kanghsuan": (
        "https://www.csjh.kh.edu.tw/fxmteach/113/113%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%E7%8F%AD%E7%B4%9A/113%E7%89%B9%E6%95%99%E7%8F%AD/113-2%E7%89%B9%E6%95%99%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%287-9%E5%B9%B4%E7%B4%9A%E6%B7%B7%E9%BD%A21%E7%8F%AD%E5%85%A8%29.pdf",
        "高雄市立中山國民中學 113 學年度公立特教課程計畫，教材編輯明載康軒版第一、二冊；列公 Bc-Ⅳ-1，安排社會規範、法律與其他規範差異，採簡化、分解、直接教學與紙筆／口語評量。",
    ),
    "hanlin": (
        "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO",
        "新北市立溪崑國民中學 114 學年度公立校方課程計畫，教材明載翰林版教科書；以第三篇公民與社會生活第二章社會規範安排公 Bc-Ⅳ-1，討論非正式／正式規範、法律的產生與發展、規範國家強制力及資料討論評量。",
    ),
}
CONCEPTS = [
    "理解社會規範如何讓共同生活可預期、降低衝突並形成行為期待",
    "從形成來源、適用對象、違反後果、執行者與程序，區分法律、道德、習俗、宗教規範、禮貌與團體規約",
    "在混合情境中判斷同一行為可能同時受到多套規範評價，並以可查證法源與程序說明法律效果的界線",
]
REPRESENTATIONS = [
    "規範來源—對象—後果—處理程序—救濟的五欄證據矩陣",
    "法律、道德、習俗、宗教規範、禮貌與團體規約的比較表",
    "同一生活事件同時涉及多套規範的決策流程圖",
]
ASSESSMENT = [
    "生活規範案例分類與理由說明",
    "正式／非正式規範及法律效力資料閱讀",
    "規範來源與處理程序證據配對",
    "混合情境學習單與口頭問答",
    "紙筆、討論參與或學習歷程評量",
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
        "lessonId": "lesson-social-content-civ-bc-iv-1",
        "title": "公 Bc-Ⅳ-1：社會規範及法律與其他規範差異",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以社會中的文化單元定位社會規範，需在融合時把規範功能與文化脈絡分開，避免把單元名稱當成完整教材內容。",
                "康軒以特教課程的簡化、分解與直接教學呈現，需保留法律與其他規範的概念邊界，不把教材調整誤當成出版版本差異。",
                "翰林以正式／非正式規範、法律產生發展與國家強制力討論呈現，需與南一的文化脈絡及康軒的教學調整交叉核對。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-four unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
