#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Db-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/673544799.pdf", "國立卓蘭高中附設國中部公民課程計畫；使用南一版教科書，列公 Db-IV-1 個人基本生活保障與人性尊嚴、選擇自由的關聯，並連結資源分配、社會福利、討論與學習歷程評量。"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course113/file_school/15683227287080309.pdf", "嘉義縣阿里山國民中小學 113 學年度七年級社會公民教學計畫；教材版本明載康軒版，列公 Db-Ⅳ-1，從人性尊嚴、基本生活與人權保障展開，採教師觀察、自評、同儕互評、紙筆、口頭及專案／活動報告。"),
    "hanlin": ("https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO", "新北市立溪崑國民中學 114 學年度七年級第二學期部定課程計畫；教材資源標示翰林版教科書，列公 Db-IV-1，從慈善觀念、工業化社會問題到現代社會安全制度，說明基本生活保障與人性尊嚴，採口頭問答、觀察及討論評量。"),
}
CONCEPTS = ["說明基本生活保障不是單純物質救濟，而是使人能維持尊嚴、作出選擇並參與社會的條件", "比較慈善、社會救助、社會福利與制度性社會安全的目的、對象與限制", "用生活案例判斷基本需求、自由選擇、尊嚴與公共責任之間的關聯，避免把個人責任與制度責任二分化"]
REPRESENTATIONS = ["基本需求—尊嚴—選擇自由—社會參與關聯圖", "慈善、救助、福利與社會安全制度比較表", "個人處境、權利需求與公共制度回應的因果鏈"]
ASSESSMENT = ["社會安全案例閱讀", "制度功能比較", "口頭問答與課堂討論", "學習歷程或專案表達", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-db-iv-1", "title": "公 Db-Ⅳ-1：基本生活、人性尊嚴與選擇自由", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一將 Db-Ⅳ-1 放在資源分配與社會福利的脈絡，需融合資源分配方法與保障基本生活的連結。", "康軒以人性尊嚴與人權保障作為七年級入口，評量形式最完整，包含同儕、專案與活動表達。", "翰林以慈善到現代社會安全制度的歷史演變說明制度化保障，需區分慈善動機與國家制度責任。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
