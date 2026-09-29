#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bk-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/476281614.pdf", "國立卓蘭高中附設國中部公民課程計畫；使用南一版教科書，列公 Bk-IV-1 兒童及少年保護法律知識、立法目的與重要保護措施，並以口頭問答、觀察、上機實作、討論及學習歷程評量。"),
    "kanghsuan": ("https://www.zgjh.hc.edu.tw/uploads/1661325490782iILPMu3n.pdf", "新竹市立竹光國民中學 111 學年度社會領域課程計畫；公民權利保障與規範單元使用康軒版課本／習作，列公 Bk-Ⅳ-1，安排兒少法律理念、目的、措施與生活案例，採對話問答、紙筆測驗、學習單及數位即時回饋。"),
    "hanlin": ("https://www.csjh.kh.edu.tw/fxmteach/111/111%E7%89%B9%E6%AE%8A%E6%95%99%E8%82%B2%E7%8F%AD%E7%B4%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/111%E9%9B%86%E4%B8%AD%E5%BC%8F%E7%89%B9%E6%95%99%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/111-2%E9%9B%86%E4%B8%AD%E5%BC%8F%E7%89%B9%E6%95%99%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB%28%E6%B7%B7%E9%BD%A12%E7%8F%AD%29.pdf", "高雄市立中山國民中學集中式特教班課程計畫；教材編輯明載翰林版第二、三冊，列公 Bk-IV-1，將兒少權益維護安排在公民法律單元，並以簡化、減量、直接教學及紙筆／口語評量呈現。"),
}
CONCEPTS = ["辨識兒童及少年作為權利主體的法律保障需求，理解年齡、身心發展與權力不對等造成的特殊風險", "掌握兒少保護法律的立法目的與主要措施，區分保護、支持、限制與責任之間的關係", "用生活或新聞案例判斷兒少權益受到影響時的法律保障、求助管道與安全行動，避免把保護簡化成單純禁止"]
REPRESENTATIONS = ["兒少處境—權利風險—法律目的—保護措施對照表", "保護、支持、限制與責任的概念關聯圖", "案例事件、求助管道與制度回應的決策流程"]
ASSESSMENT = ["兒少法律案例閱讀", "保護措施與立法目的配對", "生活情境口頭問答", "法治教育學習單", "紙筆或數位即時評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-bk-iv-1", "title": "公 Bk-Ⅳ-1：兒童及少年法律保障", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以兒少法律知識、立法目的與保護措施並列，並延伸保護與限制的辯證問題。", "康軒以公民權利保障與規範單元安排兒少法律，加入數位即時回饋與生活案例，需核對正式教材概念順序。", "翰林以特殊教育課程的簡化、減量與兒少權益維護活動呈現，需保留權利主體概念而不把調整教材當成完整法律清單。"], "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-two unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
