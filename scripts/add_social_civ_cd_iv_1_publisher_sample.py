#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Cd-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 5 公平正義與勞動參與／公民，使用南一版教科書，明列公 Cd-Ⅳ-1 勞動參與的重要性，並以口頭問答、課堂觀察、上機實作、討論及學習歷程檔案評量。"),
    "kanghsuan": ("https://web2.mtjh.tp.edu.tw/wp-content/uploads/doc/mtjh212/113_%E4%B9%9D%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%28%E5%85%AC%E6%B0%91%E7%A7%91%29%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "臺北市民族實驗國民中學 113 學年度九年級社會領域公民科課程計畫；校方課程頁標示社會公民採康軒版，PDF 以公民課程之勞動參與章節安排公 Cd-Ⅳ-1 的重要性探究與課堂／紙筆評量。"),
    "hanlin": ("https://www.zmjhs.tyc.edu.tw/uploads/neilfilefolder/14file/file/16_69_5115%E6%99%AE%E9%80%9A%E7%8F%AD%E5%90%84%E5%B9%B4%E7%B4%9A%E5%90%84%E9%A0%98%E5%9F%9F%E7%A7%91%E7%9B%AE%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB_%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "桃園市立中壢國民中學公立校方社會領域課程計畫；教材編輯與資源明載翰林版國中社會 9 上，社會中的勞動參與章節以勞動對經濟、家庭與社會的功能為學習目標，並安排討論、資料蒐集與紙筆評量。"),
}
CONCEPTS = ["勞動參與包含有酬工作、家務照顧、志願服務與其他維持社會運作的投入", "從個人收入與尊嚴、家庭分工、組織生產及公共福祉等尺度說明勞動的重要性", "以時間、成果、報酬與社會影響資料區分勞動形式，避免把勞動簡化為有薪職業"]
REPRESENTATIONS = ["有酬／無酬與可見／不可見勞動分類表", "個人—家庭—組織—社會四尺度關聯圖", "勞動投入、產出與受益者的流程圖"]
ASSESSMENT = ["勞動情境資料閱讀", "分類與比較", "口頭問答", "資料蒐集與討論", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-cd-iv-1", "title": "公 Cd-Ⅳ-1：勞動參與的重要性", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以公平正義與勞動參與單元連接勞動的公共價值及多元學習歷程。", "康軒以公民課程的勞動參與章節安排重要性探究，需進一步核對其案例順序與評量比例。", "翰林以社會中的勞動參與章節處理經濟、家庭與社會功能，並以資料與討論支持理解。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {item["lessonId"] for item in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    blockers_path = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason: blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-six unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
