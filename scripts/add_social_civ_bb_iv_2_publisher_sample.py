#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bb-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://course.cyc.edu.tw/upfile/course114/sub1/15950803923674214.pdf", "嘉義縣公立國中公民課程計畫，教材明載南一版第一、二冊，將公 Bb-Ⅳ-2 放在志願結社與公共生活脈絡，要求分析團體特徵、公共影響與參與行動，採問答、觀察、討論、上機與學習歷程評量。"),
    "kanghsuan": ("https://www.bish.tp.edu.tw/get_file.php?file_dir=data10710%2F&file_name=0d301d84a39c7bbdf88a3f4567228072.pdf&rename=%E4%B8%83%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%28%E5%85%AC%E6%B0%91%E8%88%87%E7%A4%BE%E6%9C%83%29.pdf", "臺北市靜修中學國中部七年級公民課程計畫，選用康軒版，列出公 Bb-Ⅳ-2 志願結社的特徵與公共生活影響，並以教師觀察、自評、同儕互評、口頭詢問與紙筆測驗評量。"),
    "hanlin": ("https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO", "新北市溪崑國中七年級部定課程計畫，教材明載翰林版，公 Bb-IV-2 以志願結社對公共意見與環境政策的影響為例，使用新聞資料、ORID 討論、學習單與隨堂測驗。"),
}
CONCEPTS = [
    "辨識志願結社的自願加入、共同目標、非營利取向、自治與組織持續性等特徵，並和政府機關、營利企業及臨時群眾區分",
    "分析志願結社如何彙集需求、形成公共意見、代表特定群體、監督政策或提供公共服務",
    "評估志願結社的代表性、透明度、資源與權力差異，以及其對公共生活的正面影響與可能限制",
]
REPRESENTATIONS = ["志願結社特徵與其他組織比較矩陣", "需求—組織—公共意見—政策影響關係圖", "資料事實—團體行動—公共效果—代表性與責任檢核流程"]
ASSESSMENT = ["志願結社特徵案例辨識", "政府、企業、正式團體與志願結社比較", "新聞或政策資料中的公共影響判讀", "規劃透明、包容且可追蹤的團體參與行動", "口頭問答、教師觀察、分組討論、學習單、紙筆與學習歷程評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-bb-iv-2", "title": "公 Bb-Ⅳ-2：志願結社與公共生活", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一強調志願結社特徵與公共參與行動，需把組織結構和公共影響分別驗證。", "康軒把志願結社放在民主與人權公民素養中，需補足代表性、資源差異與透明責任。", "翰林用環境團體與新聞資料說明政策影響，需比較公共意見形成、監督與可能的偏誤或排除。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred five unit samples", "Four hundred six unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
