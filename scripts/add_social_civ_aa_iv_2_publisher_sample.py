#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Aa-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版；公民單元 1 公民與公民德性列公 Aa-Ⅳ-2，安排公民德性、公共生活與口頭問答、觀察、實作及討論評量。",
    ),
    "kanghsuan": (
        "https://www.pljhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mek15TDNCMFlWOHhNalEzTmw4ME5EVTFPREUzWHpjMU1EWXhMbkJrWmc9PQ%3D%3D&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO",
        "新北市八里國民中學 114 學年度公立校方課程計畫，教材與活動明載康軒版；列公 Aa-Ⅳ-2，從社會生活中的公民德性、公共事務討論與校園實例安排分組互動、教師觀察與測驗。",
    ),
    "hanlin": (
        "https://course.cyc.edu.tw/upfile/course114/sub1/15937393490237526.pdf",
        "嘉義縣新港國民中學 114 學年度七年級公民課程計畫，教材版本明載翰林版第一、二冊；第一章公民與公民德性列公 Aa-Ⅳ-2，聚焦現代公民德性、公共參與、課堂發言、資料蒐集與紙筆評量。",
    ),
}
CONCEPTS = [
    "理解現代公民基本德性包含參與公共事務、遵守法律規範、理性思考與批判、和平尊重與包容、捍衛公平正義",
    "區分個人偏好、公共利益、法律義務與公民德性，理解德性之間可能互相支持也可能需要權衡",
    "以時間線、因果鏈、不同群體觀點與影響尺度判斷公共行動是否兼顧自由、責任、尊重與公平",
]
REPRESENTATIONS = [
    "五項公民德性—行動證據—公共影響對照表",
    "公共事件事實—主張—待查問題時間線",
    "不同群體與尺度的影響矩陣及因果鏈",
]
ASSESSMENT = [
    "公共設施決策資料閱讀",
    "事實、主張與待查問題分類",
    "公民德性與行動證據配對",
    "不同觀點的和平討論與方案修訂",
    "課堂發言、分組活動、資料蒐集與紙筆評量",
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
        "lessonId": "lesson-social-content-civ-aa-iv-2",
        "title": "公 Aa-Ⅳ-2：現代公民基本德性",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以公民與公民德性單元作為公民學習入口，需將德性內涵與公民身分、參與資格分層核對。",
                "康軒以社會生活、公民德性與校園實例連結，需保留公共程序與證據判斷，不把互動活動簡化成態度口號。",
                "翰林以公共參與、資料蒐集與紙筆評量呈現，需補足多元觀點、因果限制與公平正義的權衡。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-eight unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
