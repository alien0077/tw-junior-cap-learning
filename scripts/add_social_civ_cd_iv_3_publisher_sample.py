#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Cd-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；使用南一版教科書，單元 5 公平正義與勞動參與／公民，列公 Cd-Ⅳ-3 立法保障公平的市場勞動參與，採口頭問答、課堂觀察、上機實作、討論及學習歷程檔案。"),
    "kanghsuan": ("https://web2.mtjh.tp.edu.tw/wp-content/uploads/doc/mtjh212/113_%E4%B9%9D%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%28%E5%85%AC%E6%B0%91%E7%A7%91%29%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "臺北市民族實驗國民中學 113 學年度九年級社會領域公民科課程計畫；校方頁面標示社會公民為康軒版，PDF 之公民課程列公 Cd-Ⅳ-3 及勞動參與單元，並安排課堂討論與紙筆評量。"),
    "hanlin": ("https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_69_5115%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB_%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "桃園市立中壢國民中學公立校方社會領域課程計畫；教材編輯與資源明載翰林版國中社會 9 上，社會中的勞動參與章節列公 Cd-Ⅳ-3，學習目標包含雇主／受僱者資源差異、勞動權益與公平參與，並採討論、資料蒐集、活動與紙筆測驗。"),
}
CONCEPTS = ["從雇主與受僱者的權力、資訊與資源差異理解市場勞動的結構性不對等", "區分工作權、工資工時、職場安全、就業安全與反歧視等受保障的勞動權益", "以案例與法規目的判斷立法如何降低不公平參與，並保留執行成效與申訴資料的證據界線"]
REPRESENTATIONS = ["雇主／受僱者權力與資源對照表", "工作情境—受影響權益—法律工具流程圖", "招募、待遇、安全與申訴資料的案例矩陣"]
ASSESSMENT = ["勞動案例資料閱讀", "權利與制度比較", "分組討論", "資料蒐集與口頭表達", "紙筆測驗"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-cd-iv-3", "title": "公 Cd-Ⅳ-3：立法保障公平勞動參與", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以公平正義與勞動參與單元連結權力差異、勞動權益與多元學習歷程評量。", "康軒以公民課程中的勞動參與章節與公 Cd-Ⅳ-3 條目建立案例討論和紙筆檢核。", "翰林以社會中的勞動參與章節展開經濟社會影響、雇主／受僱者資源差異及勞動權益保障。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-five unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
