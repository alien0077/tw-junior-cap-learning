#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Bc-IV-3."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://course.cyc.edu.tw/upfile/course110/sub1/14811443628817597.pdf",
        "嘉義縣國民中學公立校方 110 學年度社會領域課程計畫，教材版本標示南一版第二冊；定位公 Bc-Ⅳ-3，涵蓋社會規範隨時間與空間變動、族群／性別／性傾向／身心障礙相關規範，以及性別平等案例與政府措施。",
    ),
    "kanghsuan": (
        "https://www.csjh.kh.edu.tw/fxmteach/110/110%E7%89%B9%E6%AE%8A%E7%8F%AD%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/110%E7%89%B9%E6%95%99%E7%8F%AD/110%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E7%89%B9%E6%95%99%E6%B7%B7%E9%BD%A1%E4%B8%80%E7%8F%AD%E8%AA%B2%E7%A8%8B%E9%80%B2%E5%BA%A6%E8%A8%88%E7%95%AB%E8%A1%A8.pdf",
        "高雄市立中山國民中學公立特教課程計畫，教材版本列康軒版第一、二冊；定位公 Bc-Ⅳ-3，將社會規範變動與族群、性別、性傾向及身心障礙議題轉化為生活化、分段與討論式學習。",
    ),
    "hanlin": (
        "https://www.ckjhs.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9MelU0TDNCMFlWODJNakU1WHpZNU1USXlNREJmTkRJMU1qTXVjR1Jt&fname=WSGGXSQKRKDCOOYXLOLKWWXTZSPKWTRL14JCB114A1A1GCFCYSA4FCB4FGOOJG50VWPOXT154404MOWS1430ICNPOP34XSGC01YTNOB5WSB001PODGGGQKUSTWPOXXKKVSNOXWXTMKJCUSIC14JCSW20HDNPMLRKLKUSOPTWQOA4TS50DGQO210024LKNOWTVW30LKKKWSNORKMP21XTLKB5POMKOPB400SSPKROKK04POPO",
        "新北市立溪崑國民中學 114 學年度公立校方課程計畫，教材版本明載翰林版；定位公 Bc-Ⅳ-3，從正式／非正式規範、法律發展與同性婚姻合法化比較報告，安排規範變動的資料閱讀、觀點討論與口頭／觀察評量。",
    ),
}
CONCEPTS = [
    "理解社會規範不是固定不變的命令，而會隨時代、空間、文化、權力關係與公共討論改變",
    "比較族群、性別、性傾向與身心障礙相關規範的變動，辨識制度修正如何回應不平等與權利需求",
    "以時間線、前後規範對照和不同群體觀點分析規範改變的原因、影響與仍待解決的問題",
]
REPRESENTATIONS = [
    "社會規範變動時間線與前後條文／做法對照表",
    "規範改變原因—行動者—制度回應—群體影響因果圖",
    "同一事件的族群、性別、性傾向與身心障礙觀點比較矩陣",
]
ASSESSMENT = [
    "規範變動案例與資料閱讀",
    "正式／非正式規範與制度變遷分類",
    "不同群體觀點的證據式討論",
    "時間線與前後對照學習單",
    "口頭問答、課堂觀察或紙筆評量",
]


def main() -> None:
    records = []
    for publisher, (url, locator) in SOURCES.items():
        records.append({
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator} 核讀 2026-09-20。",
            "accessedAt": "2026-09-20",
            "observedConcepts": CONCEPTS,
            "observedRepresentations": REPRESENTATIONS,
            "observedAssessment": ASSESSMENT,
            "licenseBoundary": "只記錄公立學校課程計畫的章節、學習重點與評量方向，不複製教材、影片、圖表、題目或答案。",
        })
    record = {
        "lessonId": "lesson-social-content-civ-bc-iv-3",
        "title": "公 Bc-Ⅳ-3：社會規範隨時間與空間變動",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": records,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以規範變動與性別平等案例、政府措施相連，需在融合時補足其他身分群體的比較證據。",
                "康軒以特教課程的生活化、分段與討論方式呈現，需保留概念完整性，不把教學調整誤當成版本內容差異。",
                "翰林以正式／非正式規範、法律發展與同性婚姻資料閱讀呈現，需與族群及身心障礙規範變化並列核對。",
            ],
            "originalSynthesisBoundary": "本樣本只記錄三筆公立學校章節級證據；lesson 正文、圖表、互動與題目仍須逐單元融合、內容／版權審查與 Terra 複核，維持 draft，不升級 publisher status。",
        },
    }
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"] for item in data["units"]}
    added = []
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
            blocker["reason"] = re.sub(r"Three hundred [a-z-]+ unit samples", "Three hundred ninety-three unit samples", reason)
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
