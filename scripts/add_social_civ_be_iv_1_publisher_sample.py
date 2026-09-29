#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Be-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/476281614.pdf", "國立卓蘭高中附設國中部公民課程計畫，南一版教材明列公 Be-IV-1，將國家與政府、權力分立及政府體制放在人民與國家單元，安排問答、課堂觀察、上機實作、討論與學習歷程評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1661325490782iILPMu3n.pdf", "新竹市立竹光國中公民課程計畫，康軒版課本／習作明列公 Be-Ⅳ-1，從中央與地方政府、分權方式及地方自治切入，採分組學習、對話問答與紙筆測驗。"),
    "hanlin": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWOHhNakV5TVY4eU5ETXdNek0wWHpJMk5UZ3dMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCOK20QPRLPKQPROECUSQOWSTSRKB0DGTSPLJHEDXWPK10", "新北市淡水國中公民課程計畫，翰林版社會課本以政府體制、權力分立、三權／五權特色與中央政府互動為主題，安排自我解釋、摘要、課堂實作、課堂參與與紙筆測驗。"),
}
CONCEPTS = [
    "說明政府權力分立的目的，理解把立法、行政、司法等職能分開並相互制衡可降低權力集中與濫權風險",
    "比較三權分立與我國五權分立的機關職能、彼此互動及制度背景，不能只用機關名稱代替權力功能",
    "閱讀憲政制度與實際政治案例，辨識權力授予、監督、否決、彈劾、覆議或解散等制衡機制如何保障人民權利",
]
REPRESENTATIONS = ["政府權力分立與制衡關係圖", "立法／行政／司法／監察／考試職能比較矩陣", "權力授予—行使—監督—衝突—救濟流程"]
ASSESSMENT = ["政府體制與機關職能案例判讀", "三權與五權制度比較", "中央與地方分權資料閱讀", "以憲政原理分析權力衝突與制衡方案", "分組討論、對話問答、課堂實作、紙筆與學習歷程評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-be-iv-1", "title": "公 Be-Ⅳ-1：民主政府的權力分立", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人民與國家、政府體制的權力分立為入口，需將制度目的與具體制衡機制連結。", "康軒以中央地方分權與地方自治呈現分權實作，需補足中央政府內部的權力互動。", "翰林比較三權、五權與政府互動案例，需以制度資料檢查職權界線及人民權利保障。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred six unit samples", "Four hundred seven unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
