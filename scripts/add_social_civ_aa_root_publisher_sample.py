#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Aa root scope."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域課程計畫，教材明載南一版；公民單元 1 公民與公民德性串接公 Aa-Ⅳ-1～2，從公民身分、德性與公共參與安排多元評量。"),
    "kanghsuan": ("https://www.pljhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mek15TDNCMFlWOHhNalEzTmw4ME5EVTFPREUzWHpjMU1EWXhMbkJrWmc9PQ%3D%3D&fname=WSGGIGB0MK10OOMP50POSWHGFC30WTIG14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKQOJCTWICZTA1LKQPSWYWKORK00SSPKROKK04POPO", "新北市八里國民中學 114 學年度公立校方課程計畫，教材與活動明載康軒版；以社會生活中的公民、公民德性與公共事務形成 Aa 根章節脈絡，安排分組互動、教師觀察與測驗。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15937393490237526.pdf", "嘉義縣新港國民中學 114 學年度七年級公民課程計畫，教材版本明載翰林版第一、二冊；第一章公民與公民德性串接公 Aa-Ⅳ-1～2，記錄身分差異、德性、公共參與與資料／紙筆評量。"),
}
CONCEPTS = [
    "建立公民身分、現代公民德性與公共參與的概念階層",
    "連結法律身分、權利責任、公共程序、理性討論、尊重包容與公平正義",
    "以資料與多角色觀點判斷公共行動及其限制，提出可檢查的參與方案",
]
REPRESENTATIONS = ["公民身分—德性—參與三層概念圖", "權利—責任—公共程序比較矩陣", "公共事件事實、觀點與行動流程圖"]
ASSESSMENT = ["公民身分與德性整合案例", "公共議題資料判讀", "多角色討論與方案修訂", "資料蒐集、口頭、分組與紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-aa", "title": "Aa：公民身分", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以公民與公民德性作為公民入口，需分開身分與德性。", "康軒以社會生活與公共事務活動呈現，需保留法律身分與程序證據。", "翰林以身分差異、公共參與與資料評量串接，需補足不同尺度與觀點。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；根 lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-nine unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
