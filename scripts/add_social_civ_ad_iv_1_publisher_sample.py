#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ad-IV-1."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www1.fsm.kh.edu.tw/plan/110/110-1%20%E5%85%AC%E6%B0%91.pdf", "高雄市立鳳山國中七年級公民課程計畫，南一版第三篇公民身分及社群第二章人性尊嚴與人權保障明列公 Ad-Ⅳ-1，安排課堂發言、紙筆測驗與資料蒐集。"),
    "kanghsuan": ("https://course.cyc.edu.tw/upfile/course109/sub1/14501846923277437.pdf", "嘉義縣忠和國中七年級公民課程計畫，康軒版第一冊人性尊嚴與人權保障單元明列公 Ad-Ⅳ-1，結合生活經驗、公共議題見解、課堂發言、紙筆測驗與資料蒐集。"),
    "hanlin": ("https://w3.qnm.kh.edu.tw/curriculum/5/5-1/%E7%A4%BE%E6%9C%83-%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-114-2-3%E5%B9%B4%E7%B4%9A.pdf", "高雄市立青年國中三年級公民課程計畫，翰林電子書／翰林行動大師教材脈絡明列公 Ad-IV-1，將人權、人性尊嚴與言論自由案例放入影片觀賞、課程討論與同理表達。"),
}
CONCEPTS = [
    "說明人權保障與人性尊嚴的關係，從人的不可被任意物化、羞辱或排除理解權利的最低保障",
    "用生活與公共案例辨識平等、自由、身體與人格尊嚴受侵害的情況，區分權利主張、偏好、限制與正當理由",
    "比較不同立場與資料，檢查限制人權是否有法律依據、正當目的、必要性與比例，提出尊重權利的回應",
]
REPRESENTATIONS = ["人性尊嚴—基本權利—國家義務概念鏈", "權利受影響者／限制理由／替代方案利害關係人矩陣", "案例事實—權利辨識—限制審查—證據結論流程"]
ASSESSMENT = ["人權與人性尊嚴案例判讀", "不同立場及資料比較", "言論與人格尊嚴衝突討論", "資料蒐集後提出權利保障方案", "課堂發言、影片／課程討論、紙筆與資料蒐集評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-ad-iv-1", "title": "公 Ad-Ⅳ-1：人權保障與人性尊嚴", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以人性尊嚴與人權保障的單元脈絡搭配資料蒐集，需把尊嚴受侵害的事實與權利判斷分開。", "康軒把生活經驗、公共議題與人權主張連接，需補足限制人權的正當性與比例檢查。", "翰林以言論自由等案例討論帶入同理表達，需補足受影響者、國家義務與替代方案比較。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred two unit samples", "Four hundred three unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
