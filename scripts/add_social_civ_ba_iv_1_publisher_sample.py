#!/usr/bin/env python3
"""Record three public-school publisher-linked records for Civ Ba-IV-1."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
SOURCES = {
    "nani": (
        "https://course.cyc.edu.tw/upfile/course109/sub1/14535426760482702.pdf",
        "嘉義縣公立國中南一版社會課程計畫；公 Ba-Ⅳ-1 與親屬關係、家庭型態及家庭職能並列，安排家庭功能、社會變遷與口頭／課堂／紙筆評量。",
    ),
    "kanghsuan": (
        "https://www.kusjh.kh.edu.tw/upload/files/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%89%B9%E6%95%99%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB-%E5%85%A8-%E6%A0%B8%E7%AB%A0.pdf",
        "高雄市公立國中康軒版課程計畫；明列教材為康軒版，公 Ba-Ⅳ-1 探問家庭為基本且重要社會組織，搭配紙筆、口語與指認評量。",
    ),
    "hanlin": (
        "https://data.yjm.kh.edu.tw/curriculum113/01.%E4%B8%80%E7%94%B2%E5%9C%8B%E4%B8%AD%E6%99%AE%E9%80%9A%E7%8F%AD113%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/5.%E9%A0%98%E5%9F%9F%E5%AD%B8%E7%BF%92%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/5-1.%E5%90%84%E9%A0%98%E5%9F%9F%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/05%E7%A4%BE%E6%9C%83/%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%AA%B2%E7%A8%8B%E8%A8%88%E7%95%AB/113%E4%B8%80%E4%B8%8A%E7%A4%BE%E6%9C%83%E5%88%86%E7%A7%91%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%28%E5%85%AC%E6%B0%91%29.pdf",
        "高雄市公立國中翰林課程計畫；公 Ba-Ⅳ-1 放在家庭生活單元，搭配生活經驗、社會變遷、文字／圖表表達及課堂發言評量。",
    ),
}
CONCEPTS = [
    "家庭兼具日常照顧、情感支持、社會化與資源分工等功能，是基本但會隨社會變遷調整的社會組織",
    "分析家庭重要性要區分家庭成員關係、家庭功能、制度支持與不同家庭型態，不能把單一家庭經驗當成普遍規則",
    "用家庭資料、時間變化、生活案例與多方觀點說明家庭與社會的互動，並辨識家庭功能改變帶來的需求與公共支持",
]
REPRESENTATIONS = [
    "家庭功能—成員需求—社會支持對照表",
    "不同時期家庭型態與職能變化時間線",
    "生活案例、圖表與制度支持的因果鏈",
]
ASSESSMENT = [
    "家庭生活案例判讀",
    "家庭功能與社會組織分類",
    "家庭型態變化圖表閱讀",
    "小組討論、口頭問答、學習單與紙筆評量",
]
LICENSE = "只記錄公立學校課程計畫的版本、章節重點與評量方向，不複製教材、圖表、題目或答案。"


def main() -> None:
    sources = [
        {
            "publisher": publisher,
            "sourceUrl": url,
            "sourceKind": "public-school-course-plan-identifying-publisher-material",
            "locator": f"{locator} 核讀 2026-09-21。",
            "accessedAt": "2026-09-21",
            "observedConcepts": CONCEPTS,
            "observedRepresentations": REPRESENTATIONS,
            "observedAssessment": ASSESSMENT,
            "licenseBoundary": LICENSE,
        }
        for publisher, (url, locator) in SOURCES.items()
    ]
    record = {
        "lessonId": "lesson-social-content-civ-ba-iv-1",
        "title": "公 Ba-Ⅳ-1：家庭作為基本社會組織",
        "evidenceStatus": "chapter-level-recorded-pending-fusion-review",
        "sources": sources,
        "fusionReview": {
            "commonCore": CONCEPTS,
            "differencesToReview": [
                "南一以家庭功能、親屬關係與社會變遷銜接生活經驗與概念理解。",
                "康軒直接以家庭為基本且重要社會組織提問，偏重問題導向與多元口語／紙筆檢核。",
                "翰林把家庭放入家庭生活單元，結合生活經驗、圖表表達與社會變遷觀察。",
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
    data["updatedAt"] = "2026-09-21"
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blockers_path = ROOT / "implementation/reports/blockers.json"
    blockers = json.loads(blockers_path.read_text(encoding="utf-8"))
    for blocker in blockers.get("blockers", []):
        reason = blocker.get("reason")
        if isinstance(reason, str) and "unit samples" in reason:
            blocker["reason"] = re.sub(
                r"Four hundred (?:forty-four|forty-seven|fifty|fifty-three|fifty-six|fifty-nine|sixty-two|sixty-five|sixty-eight|seventy-one|seventy-four|seventy-seven|seventy-nine) unit samples",
                "Four hundred eighty unit samples",
                reason,
            )
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": data["unitCount"], "added": added}, ensure_ascii=False))


if __name__ == "__main__":
    main()
