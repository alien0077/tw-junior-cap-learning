#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Da-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-7-4.pdf", "國立卓蘭高中附設國中部 113 學年度七年級社會領域；單元 2 性別平權／公民，使用南一版教科書，明列公 Da-Ⅳ-2 日常生活中個人或群體可能面臨的不公平處境，並採口頭問答、觀察、上機實作、討論及學習歷程評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1725516459151IF7DzrmY.pdf", "新竹市立竹光國民中學 113 學年度社會領域課程計畫；公民單元列公 Da-Ⅳ-2，使用康軒版教科書，安排法律對兒童及少年保障與規範的案例學習，並以課堂參與、學習單與紙筆等方式評量。"),
    "hanlin": ("https://course.cyc.edu.tw/upfile/course111/sub1/15079736881394406.pdf", "嘉義縣太保市嘉新國民中學 111 學年度九年級社會領域課程計畫；教材版本明載翰林版第六冊，列公 Da-IV-2 日常生活中個人或群體可能面臨的不公平處境，並以單元問題、討論與紙筆測驗連結公平正義與社會安全。"),
}
CONCEPTS = ["從日常案例辨識個人或群體遭遇的不公平處境，並區分結果差異、資源限制與歧視性對待", "比較不同身分、需求與權力位置的經驗，使用事實資料而非單一印象判斷不公平的形成原因", "連結人權、平等與公平正義，評估法律保障、公共制度與社會行動如何回應不公平處境"]
REPRESENTATIONS = ["處境案例的身分—規則—資源—結果分析表", "不同群體的機會與障礙比較矩陣", "問題成因、權利保障與改善方案的因果圖"]
ASSESSMENT = ["生活案例資料閱讀", "不同觀點比較與理由說明", "課堂討論與口頭表達", "學習單或資料分析", "紙筆評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-da-iv-2", "title": "公 Da-Ⅳ-2：個人與群體的不公平處境", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以性別平權單元從生活經驗辨識不公平處境，需融合人權界線與規範變動的連結。", "康軒以兒童及少年法律保障與規範的案例作為制度回應入口，需核對法律案例與概念順序。", "翰林以公平正義與社會安全單元連結個人困境、國家保障與公共制度，需比較其問題探究及評量安排。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred eighty-eight unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
