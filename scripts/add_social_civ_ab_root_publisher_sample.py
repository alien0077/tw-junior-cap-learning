#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ab root scope."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://course.cyc.edu.tw/upfile/course113/sub1/15651091365037354.pdf", "嘉義縣竹崎國民中學 113 學年度八年級公民課程計畫，教材明載南一版第三、四冊；人民與國家單元串接國家／政府、權力／權利與公 Ab-Ⅳ-1，安排觀察、紙筆與口頭評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1725516459151IF7DzrmY.pdf", "新竹市立竹光國民中學 113 學年度公民課程計畫，教材明載康軒版；政府與權力分立單元把公 Ab-Ⅳ-1 放在法治、政府職權與權力分立脈絡，採討論、問答、學習單與紙筆評量。"),
    "hanlin": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWOHhNakV5TVY4eU5ETXdNek0wWHpJMk5UZ3dMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCOK20QPRLPKQPROECUSQOWSTSRKB0DGTSPLJHEDXWPK10", "新北市立淡水國民中學 114 學年度八年級公民課程計畫，教材明載翰林版；民主政治運作單元串接法治、權力／權利、權力分立與憲政制度，採課堂參與、自我解釋與摘要策略。"),
}
CONCEPTS = [
    "建立權力、權利與責任的層次關係，理解權力可能實現也可能侵害權利",
    "連結國家、政府、法治、權力分立、憲政限制、監督與救濟",
    "以不同時間、尺度與利害關係人資料分析公共權力，提出兼顧權利與責任的監督或修正方案",
]
REPRESENTATIONS = ["權力—權利—責任三層概念圖", "國家／政府／制度／人民的關係矩陣", "授權—行使—影響—監督—救濟流程"]
ASSESSMENT = ["權力與權利整合案例", "政府措施與憲政限制資料閱讀", "不同觀點與尺度比較", "監督／申訴方案討論", "口頭、分組、紙筆與學習單評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-ab", "title": "Ab：權力、權利與責任", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人民與國家串接權力／權利，需保留國家與政府的區分。", "康軒以法治、政府職權與權力分立串接，需補足責任、監督與救濟。", "翰林以民主政治、法治與憲政制度連續呈現，需以資料檢查權力行使的實際影響。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；根 lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred unit samples", "Four hundred one unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
