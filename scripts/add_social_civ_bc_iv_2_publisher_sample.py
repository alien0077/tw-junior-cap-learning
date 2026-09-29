#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bc-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版教科書；公民單元 4 社會中的文化同時列公 Bc-Ⅳ-2 日常生活規範與文化，安排文化脈絡、生活案例與口頭問答、觀察、實作及討論評量。",
    ),
    "kanghsuan": (
        "https://www.csjh.kh.edu.tw/fxmteach/113/113%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E8%BA%AB%E5%BF%83%E9%9A%9C%E7%A4%99%E9%A1%9E%E7%8F%AD%E7%B4%9A/113%E7%89%B9%E6%95%99%E7%8F%AD/113-2%E7%89%B9%E6%95%99%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%287-9%E5%B9%B4%E7%B4%9A%E6%B7%B7%E9%BD%A21%E7%8F%AD%E5%85%A8%29.pdf",
        "高雄市立中山國民中學 113 學年度公立特教課程計畫，教材編輯明載康軒版第一、二冊；列公 Bc-Ⅳ-2 日常生活規範與文化，採生活化的簡化、分解、直接教學與紙筆／口語評量。",
    ),
    "hanlin": (
        "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO",
        "新北市立溪崑國民中學 114 學年度公立校方課程計畫，教材明載翰林版教科書；第三篇公民與社會生活第二章社會規範將正式／非正式規範、法律發展與規範變動放入同一文化脈絡，並採 KWLQ、討論、學習單與自評互評。",
    ),
}
CONCEPTS = [
    "理解日常生活規範如何把群體價值與文化意義轉成可預期的行動方式",
    "比較不同群體在語言、飲食、服飾、信仰、節慶與公共空間中的規範差異，避免把自身習慣當成唯一標準",
    "以直接資料、不同角色觀點與規範目的判斷何時是文化差異、何時涉及不平等或需要協商的公共規則",
]
REPRESENTATIONS = [
    "行為—規範來源—文化意義—受影響者—可調整處五欄表",
    "同一行為在不同文化脈絡中的觀點比較矩陣",
    "規範目的、權利風險與協商修訂流程圖",
]
ASSESSMENT = [
    "校園與社區生活情境分類",
    "文化脈絡與規範目的資料閱讀",
    "不同群體觀點的證據式討論",
    "規範修訂方案學習單",
    "口頭問答、課堂觀察、紙筆或自評互評",
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
        "lessonId": "lesson-social-content-civ-bc-iv-2",
        "title": "公 Bc-Ⅳ-2：日常生活規範與文化",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以社會中的文化單元承接日常規範，需分開核對文化意義、規範功能與法律效力。",
                "康軒以特教課程的簡化、分解與生活化方式呈現，需保留不同群體文化觀點，不把調整教法誤當成出版社內容差異。",
                "翰林將正式／非正式規範、法律發展與規範變動放進公民生活脈絡，需補以日常文化資料的多元性與代表性限制。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-five unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
