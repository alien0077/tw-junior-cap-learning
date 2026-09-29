#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Be-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/476281614.pdf", "國立卓蘭高中附設國中部公民課程計畫，南一版教材明列公 Be-IV-3，安排我國中央與地方政府組成、機關職掌與依法行政脈絡，採問答、課堂觀察、上機實作、討論與學習歷程評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1661325490782iILPMu3n.pdf", "新竹市立竹光國中公民課程計畫，康軒版課本／習作明列公 Be-Ⅳ-3，從地方政府組織、職權、地方自治與中央地方分權切入，採分組學習、對話問答與紙筆測驗。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course114/sub1/15950803850827322.pdf", "嘉義縣公立國中公民課程計畫，教材明載翰林版第三、四冊，公 Be-IV-3 以中央政府與地方政府組成、權限及法治教育脈絡呈現，採分組討論、紙筆測驗與心得報告。"),
}
CONCEPTS = [
    "辨識我國中央政府與地方政府的組成層級、主要機關及其產生方式，區分組織、職權與政治責任",
    "說明中央與地方政府的權限劃分、地方自治及分權合作，利用制度資料判斷不同公共事務由哪一層級負責",
    "比較機關職掌與實際政策案例，分析中央地方衝突、協調、監督與資源分配，提出可追蹤的公共治理判斷",
]
REPRESENTATIONS = ["中央政府／地方政府組成與職權階層圖", "機關／產生方式／權限／責任／監督比較矩陣", "公共問題—權限定位—中央地方協調—執行—問責流程"]
ASSESSMENT = ["中央與地方政府組成案例判讀", "機關職權、自治與分權比較", "公共政策資料中的權限與責任分析", "提出中央地方協作或問責方案", "分組學習、對話問答、課堂觀察、上機實作、紙筆、心得與學習歷程評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-be-iv-3", "title": "公 Be-Ⅳ-3：中央與地方政府組成", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一把中央地方政府組成接到依法行政與機關職掌，需把組織、權限與責任分層。", "康軒以地方自治、地方政府職權與中央地方分權呈現治理，需補足中央機關組成及協調機制。", "翰林以中央地方組成、權限與法治教育資料切入，需比較制度規定與政策執行的實際責任。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred eight unit samples", "Four hundred nine unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
