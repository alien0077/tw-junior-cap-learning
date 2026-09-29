#!/usr/bin/env python3
"""Record public-school publisher evidence for social civics Bl-IV-1..3."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
BLOCKERS = ROOT / "implementation/reports/blockers.json"

SOURCES = {
    "nani": {
        "publisher": "南一",
        "url": "https://www.cksh.hc.edu.tw/uploads/1703731557126uLS1C2G5.pdf",
        "locator": "新竹市立建功高中國中部 110 學年度九年級社會領域公民課程計畫；文件標示教材版本為南一版，課程欄列公 Bl-IV-1、Bl-IV-2、Bl-IV-3。",
    },
    "kang": {
        "publisher": "康軒",
        "url": "https://course.cyc.edu.tw/upfile/course114/sub1/15939547496629384.pdf",
        "locator": "嘉義縣立布袋國民中學 114 學年度九年級社會領域課程計畫；文件標示教材版本為康軒版第五、六冊，課程欄列公 Bl-IV-1、Bl-IV-2、Bl-IV-3。",
    },
    "hanlin": {
        "publisher": "翰林",
        "url": "https://course.cyc.edu.tw/upfile/course114/file_school/15952869896665246.pdf",
        "locator": "嘉義縣阿里山國民中小學 114 學年度九年級社會領域課程計畫；文件標示教材版本為翰林版第五冊，課程欄列公 Bl-IV-1、Bl-IV-2、Bl-IV-3。",
    },
}

COMMON = {
    "sourceKind": "public-school-course-plan-identifying-publisher-material",
    "accessedAt": "2026-09-21",
    "originalSynthesisBoundary": "僅記錄公立學校課程計畫所標示的出版商版本、課綱概念代碼與單元定位；不複製教科書正文、例題、圖表或版權內容。正文與題目須另依官方課綱、Knowledge Graph 與可追溯公開試題重新原創撰寫。",
    "status": "chapter-level-recorded-pending-fusion-review",
}

UNITS = [
    {
        "unitId": "cur-social-content-civ-bl-iv-1",
        "lessonId": "lesson-social-content-civ-bl-iv-1",
        "title": "公 Bl-Ⅳ-1：個人與家庭的選擇",
        "focus": "從稀少資源與多元欲望出發，辨認個人或家庭面對的限制、可行方案與選擇依據。",
        "concepts": ["稀少性", "欲望與需求", "選擇限制", "個人與家庭的資源配置"],
        "representation": "用家庭時間、收入、空間與資訊的情境表格，比較可行方案與選擇條件；不把選擇簡化成單一標準答案。",
        "assessment": "題目要求學生先列出限制與方案，再說明選擇依據，避免把偏好判斷誤當成資源無限。",
    },
    {
        "unitId": "cur-social-content-civ-bl-iv-2",
        "lessonId": "lesson-social-content-civ-bl-iv-2",
        "title": "公 Bl-Ⅳ-2：機會成本的計算",
        "focus": "依序辨認可行方案、已選方案與未選方案，找出放棄方案中價值最高者，計算選擇的機會成本。",
        "concepts": ["機會成本", "最佳放棄方案", "顯性成本", "隱性成本"],
        "representation": "以時間或金錢限制的選擇表呈現各方案價值，明確區分支出的金額與最佳未選方案的價值，不把所有未選方案相加。",
        "assessment": "每題均要求寫出限制、已選方案、最佳放棄方案與成本判斷步驟，檢查是否誤選第二佳或把總支出當機會成本。",
    },
    {
        "unitId": "cur-social-content-civ-bl-iv-3",
        "lessonId": "lesson-social-content-civ-bl-iv-3",
        "title": "公 Bl-Ⅳ-3：以機會成本解釋選擇",
        "focus": "把機會成本用於解釋不同個人、不同限制或不同資訊下的選擇差異，並分辨描述行為與評價行為。",
        "concepts": ["選擇差異", "邊際比較", "限制條件", "行為解釋與價值評斷"],
        "representation": "以同一資源在不同人物或不同時間點的替代方案比較，推導機會成本改變後選擇可能如何改變。",
        "assessment": "題目要求以替代方案價值與限制條件提出解釋，不能只寫『比較喜歡』或把經濟分析誤寫成道德評語。",
    },
]


def main() -> None:
    data = json.loads(REPORT.read_text(encoding="utf-8"))
    existing = {item["lessonId"]: item for item in data["units"]}
    for unit in UNITS:
        record = {
            "lessonId": unit["lessonId"],
            "title": unit["title"],
            "evidenceStatus": COMMON["status"],
            "sources": [],
            "fusionReview": {
                "commonCore": [unit["focus"], *unit["concepts"]],
                "differencesToReview": [unit["representation"], unit["assessment"]],
                "originalSynthesisBoundary": COMMON["originalSynthesisBoundary"],
            },
        }
        for key in ("nani", "kang", "hanlin"):
            source = SOURCES[key]
            record["sources"].append({
                "publisher": key if key != "kang" else "kanghsuan",
                "sourceUrl": source["url"],
                "sourceKind": COMMON["sourceKind"],
                "locator": source["locator"],
                "accessedAt": COMMON["accessedAt"],
                "observedConcepts": [unit["focus"], *unit["concepts"]],
                "observedRepresentations": [unit["representation"]],
                "observedAssessment": [unit["assessment"]],
                "licenseBoundary": COMMON["originalSynthesisBoundary"],
            })
        existing[unit["lessonId"]] = record
    data["units"] = sorted(existing.values(), key=lambda item: item["lessonId"])
    data["unitCount"] = len(data["units"])
    REPORT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    blockers = json.loads(BLOCKERS.read_text(encoding="utf-8"))
    text = json.dumps(blockers, ensure_ascii=False)
    text = text.replace("Four hundred ninety-eight unit samples", "Five hundred one unit samples")
    BLOCKERS.write_text(json.dumps(json.loads(text), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("recorded", len(UNITS), "units; total samples", len(data["units"]))


if __name__ == "__main__":
    main()
