#!/usr/bin/env python3
"""Record two more directly read public-school curriculum-plan evidence items."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = [
    {
        "lessonId": "lesson-science-content-bc-iv-4",
        "url": "https://course.cyc.edu.tw/upfile/course110/sub1/14791698867465092.pdf",
        "locator": "PDF 第 84 頁；Bc-Ⅳ-3／Bc-Ⅳ-4；列出光合作用的概念、日光／二氧化碳／水分因素與以探究實驗證實的教學重點",
        "signals": ["課綱代碼與內容", "影響因素", "探究實驗與評量方向"],
    },
    {
        "lessonId": "lesson-science-content-fb-iv-1",
        "url": "https://course.cyc.edu.tw/upfile/course112/sub1/15365522954661690.pdf",
        "locator": "PDF 第 56 頁；Ed-Ⅳ-1／Ed-Ⅳ-2 與 Fb-Ⅳ-1～Fb-Ⅳ-4；列出銀河系、太陽系、行星公轉、月球與模型活動的概念順序",
        "signals": ["星系與太陽系層次", "行星公轉", "日月地模型活動"],
    },
]


def main() -> None:
    evidence = []
    for item in ITEMS:
        path = next(p for p in (ROOT / "lessons").glob("*/*.json") if json.loads(p.read_text(encoding="utf-8")).get("id") == item["lessonId"])
        data = json.loads(path.read_text(encoding="utf-8"))
        data["studyReferences"] = list(dict.fromkeys([*data.get("studyReferences", []), item["url"]]))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        evidence.append({
            "lessonId": item["lessonId"],
            "subject": "science",
            "sourceType": "public-school-curriculum-plan",
            "schoolJurisdiction": "嘉義縣公開課程計畫 PDF",
            "url": item["url"],
            "locator": item["locator"],
            "observedSignals": item["signals"],
            "reuseDecision": "inspiration-only",
            "copyrightBoundary": "只保留可追溯定位與抽象教學訊號；不複製 PDF 文字、表格或題目。",
            "accessedAt": "2026-09-07",
        })
    report = {"updatedAt": "2026-09-07", "evidenceCount": len(evidence), "evidence": evidence, "note": "直接讀取的 public-school evidence sample，不推論為全庫出版社章節 evidence。"}
    out = ROOT / "implementation/reports/public-curriculum-evidence-batch2.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
