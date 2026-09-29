#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Be-IV-2."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": ("https://www.jlsh.mlc.edu.tw/var/file/12/1012/img/113-2-8-4.pdf", "國立卓蘭高中附設國中部八年級公民課程計畫，南一版教材將公 Be-Ⅳ-2 放在權力保障與權力分立脈絡，從政府職權與憲法規範連結權力限制，採問答、觀察、上機、討論與學習歷程評量。"),
    "kanghsuan": ("https://www.mtjh.tp.edu.tw/wp-content/uploads/doc/mtjh212/113_%E5%85%AB%E5%B9%B4%E7%B4%9A%E7%A4%BE%E6%9C%83%E9%A0%98%E5%9F%9F%28%E5%85%AC%E6%B0%91%E7%A7%91%29%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB.pdf", "臺北市民族實驗國中八年級公民課程計畫，選用康軒版，將公 Be-Ⅳ-2 放在政府與權力分立單元，以憲法規範、權力制衡、影片觀賞發表與紙筆測驗連結人權法治教育。"),
    "hanlin": ("https://www.tsjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWOHhNakV5TVY4eU5ETXdNek0wWHpJMk5UZ3dMbkJrWmc9PQ%3D%3D&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1DCB5WSJCPP5414HGJGA0VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCOK20QPRLPKQPROECUSQOWSTSRKB0DGTSPLJHEDXWPK10", "新北市淡水國中公民課程計畫，翰林版社會課本以政府職權的憲法界線、中央政府互動、課堂實作、課後閱讀與摘要／習題策略呈現公 Be-Ⅳ-2，並以課堂參與與紙筆測驗評量。"),
}
CONCEPTS = [
    "說明政府職權與行使必須受憲法規範，理解憲法同時配置政府權力並保障人民基本權利",
    "區分法律授權、行政裁量、權力分立與憲法界線，利用具體公權力案例檢查職權是否有依據、程序與合理限制",
    "分析政府權力與人民權利衝突時的監督、審查與救濟機制，提出符合權利保障、程序正義與責任政治的判斷",
]
REPRESENTATIONS = ["政府職權—憲法界線—人民權利三層關係圖", "機關權限／法律依據／程序／權利影響矩陣", "授權—行使—監督審查—救濟—責任追蹤流程"]
ASSESSMENT = ["政府職權與憲法限制案例判讀", "法律授權、行政裁量與越權比較", "中央政府互動及人權影響資料閱讀", "以憲法與程序提出監督或救濟方案", "影片觀賞發表、課堂實作、課後閱讀、摘要、紙筆與學習歷程評量"]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({"publisher": publisher, "sourceUrl": url, "sourceKind": "public-school-course-plan-identifying-publisher-material", "locator": f"{locator} 核讀 2026-09-20。", "accessedAt": "2026-09-20", "observedConcepts": CONCEPTS, "observedRepresentations": REPRESENTATIONS, "observedAssessment": ASSESSMENT, "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。"})
    record = {"lessonId": "lesson-social-content-civ-be-iv-2", "title": "公 Be-Ⅳ-2：政府職權與憲法規範", "evidenceStatus": "chapter-level-recorded-pending-fusion-review", "sources": records, "fusionReview": {"commonCore": CONCEPTS, "differencesToReview": ["南一以政府權力受限制與人民權利保障相連，需把憲法界線、程序與救濟具體化。", "康軒以權力分立、人權法治與影片討論切入，需補足法律授權、行政裁量與越權判準。", "翰林以政府互動及實作閱讀呈現，需比較中央機關職權、監督審查與責任追蹤。"], "originalSynthesisBoundary": "本樣本只記錄三筆可追溯的公開章節級證據；lesson 正文、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。"}}
    data = json.loads(REPORT.read_text(encoding="utf-8")); existing = {x["lessonId"] for x in data["units"]}; added = []
    if record["lessonId"] not in existing: data["units"].append(record); added.append(record["lessonId"])
    data["unitCount"] = len(data["units"]); data["updatedAt"] = "2026-09-20"; REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    bp = ROOT / "implementation/reports/blockers.json"; blockers = json.loads(bp.read_text(encoding="utf-8"))
    for b in blockers.get("blockers", []):
        if isinstance(b.get("reason"), str) and "unit samples" in b["reason"]: b["reason"] = re.sub(r"Four hundred seven unit samples", "Four hundred eight unit samples", b["reason"])
    bp.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"); print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
