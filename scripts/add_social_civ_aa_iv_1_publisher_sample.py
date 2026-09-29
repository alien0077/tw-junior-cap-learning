#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Aa-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf",
        "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版；公民單元 1 公民與公民德性定位公 Aa-Ⅳ-1，從國民／公民概念、公共參與與多元議題安排口頭問答、觀察、實作及討論評量。",
    ),
    "kanghsuan": (
        "https://www.pljhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mek15TDNCMFlWOHhNalEzTmw4ME5EVTFPREUzWHpjMU1EWXhMbkJrWmc9PQ%3D%3D&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO",
        "新北市八里國民中學 114 學年度公立校方課程計畫，教材與活動明載康軒版；列公 Aa-Ⅳ-1，從社會生活中的公民、公共事務與校園討論安排提問、分組互動、教師觀察與測驗。",
    ),
    "hanlin": (
        "https://course.cyc.edu.tw/upfile/course114/sub1/15937393490237526.pdf",
        "嘉義縣新港國民中學 114 學年度七年級公民課程計畫，教材版本明載翰林版第一、二冊；第一章公民與公民德性列公 Aa-Ⅳ-1，區分國民與公民、身分取得及資料蒐集／課堂發言／紙筆評量。",
    ),
}
CONCEPTS = [
    "區分公民、國民、居民與訪客等不同身分概念，理解公民身分與法律確認、權利、責任及參與資格的關聯",
    "從法規、名冊、人口資料與會議紀錄建立事件時間線，分辨直接資料、推論、因果主張與資料限制",
    "比較個人、社區、國家與跨國移動尺度下不同身分受到的影響，提出符合程序且尊重權利的公共參與方案",
]
REPRESENTATIONS = [
    "身分類型—法律依據—權利責任—參與資格比較表",
    "身分取得與公共事件的時間線",
    "不同角色與尺度的政策影響矩陣",
]
ASSESSMENT = [
    "公民與國民身分資料判讀",
    "身分取得法規與人口名冊閱讀",
    "公共會議紀錄的事實／推論辨識",
    "多角色參與方案討論",
    "口頭發言、分組活動、資料蒐集與紙筆評量",
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
        "lessonId": "lesson-social-content-civ-aa-iv-1",
        "title": "公 Aa-Ⅳ-1：公民概念",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以公民與公民德性單元作為七年級公民入口，需把公民身分與德性、參與概念分層處理。",
                "康軒以社會生活、公共事務與校園討論呈現，需保留程序、權利與身分法律依據，不把互動活動等同身分定義。",
                "翰林明確列出國民與公民差異及身分取得資料，需與其他版本的公共參與脈絡交叉核對，避免只背國籍法關鍵字。",
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-seven unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
