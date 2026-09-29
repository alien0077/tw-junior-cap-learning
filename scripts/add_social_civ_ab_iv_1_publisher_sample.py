#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ab-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://course.cyc.edu.tw/upfile/course113/sub1/15651091365037354.pdf", "嘉義縣竹崎國民中學 113 學年度八年級公民課程計畫，教材明載南一版第三、四冊；人民與國家單元列公 Ab-Ⅳ-1，安排政府權力與人民權利的差別、關聯及教師觀察、紙筆與口頭評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1725516459151IF7DzrmY.pdf", "新竹市立竹光國民中學 113 學年度公民課程計畫，教材明載康軒版；政府與權力分立單元列公 Ab-Ⅳ-1，明確安排權力與權利差別／關聯，採分組學習、對話問答與紙筆測驗。"),
    "hanlin": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWOHhNakV5TVY4eU5ETXdNek0wWHpJMk5UZ3dMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCOK20QPRLPKQPROECUSQOWSTSRKB0DGTSPLJHEDXWPK10", "新北市立淡水國民中學 114 學年度八年級公民課程計畫，教材明載翰林版；民主政治運作單元列公 Ab-Ⅳ-1，安排法治／人治、權利／權力差異與分權脈絡，採課堂參與與自我解釋／摘要策略。"),
}
CONCEPTS = [
    "區分能影響他人行動的權力與受制度保障、可主張並尋求救濟的權利",
    "以權力來源、作用對象、目的、法律與程序限制，對照權利主體、保障內容、限制條件與救濟途徑",
    "用時間線、規範文字、統計資料與多方觀點分析權力如何保護或侵害權利，以及權利如何要求權力受監督",
]
REPRESENTATIONS = ["權力來源—目的—對象—界線比較矩陣", "權利主體—保障內容—限制—救濟表", "公共措施的權力—權利因果鏈與時間線"]
ASSESSMENT = ["校園公共措施資料判讀", "權力與權利概念分類", "規範、程序與比例證據閱讀", "多方觀點申訴／監督方案", "口頭、分組、紙筆與學習單評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-ab-iv-1", "title": "公 Ab-Ⅳ-1：權力與權利的差別及關聯", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人民與國家脈絡呈現政府權力與人民權利，需保留國家／政府與授權關係。", "康軒明列權力與權利的差別及關聯，並採討論與問答，需補足法律、程序與比例證據。", "翰林把權利／權力放在法治與權力分立章節，需交叉核對監督、制衡與救濟的制度連結。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Four hundred unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
