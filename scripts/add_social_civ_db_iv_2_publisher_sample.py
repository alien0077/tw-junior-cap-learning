#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Db-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/673544799.pdf", "國立卓蘭高中附設國中部公民課程計畫；使用南一版教科書，列公 Db-IV-2 國家促成個人基本生活保障的責任，安排社會福利、社會救助與公共責任的討論及學習歷程評量。"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course113/file_school/15683227287080309.pdf", "嘉義縣阿里山國民中小學 113 學年度七年級社會公民教學計畫；教材版本明載康軒版，列公 Db-Ⅳ-2，從社會救助、社會保險、社會津貼與福利服務說明國家責任及不同群體需求，採教師觀察、自評與紙筆測驗。"),
    "hanlin": ("https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO", "新北市立溪崑國民中學 114 學年度七年級第二學期部定課程計畫；教材資源標示翰林版教科書，列公 Db-IV-2，從社會安全制度與慈善、工業化社會問題的歷史脈絡，分析國家以制度保障基本生活與人性尊嚴，採口頭問答、觀察及討論評量。"),
}
CONCEPTS = ["說明國家為何須以公共制度促成基本生活保障，將人性尊嚴、風險分擔與社會參與連結起來", "比較社會救助、社會保險、社會津貼與福利服務的保障對象、風險處理方式與制度限制", "以不同家庭與生活風險案例評估公共責任、個人責任、民間互助與資源公平之間的分工"]
REPRESENTATIONS = ["生活風險—基本需求—制度工具—保障結果流程圖", "社會救助、保險、津貼與福利服務比較矩陣", "個人、家庭、民間團體與國家責任的多層次分工圖"]
ASSESSMENT = ["社會福利案例閱讀", "制度工具比較", "不同需求觀點討論", "口頭問答與課堂觀察", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-db-iv-2", "title": "公 Db-Ⅳ-2：國家保障基本生活的責任", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以社會福利與資源分配的公共責任作為入口，需融合國家介入的公平與責任界線。", "康軒明確拆分社會救助、社會保險、社會津貼與福利服務，適合建立制度工具比較，但需核對其概念順序。", "翰林從慈善到現代社會安全制度的歷史演變切入，需避免將慈善替代制度責任。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-one unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
