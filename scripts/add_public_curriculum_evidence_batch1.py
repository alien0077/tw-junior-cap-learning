#!/usr/bin/env python3
"""Record one directly read public-school curriculum-plan evidence item."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-science-content-id-iv-1"
SOURCE = "https://course.cyc.edu.tw/upfile/course114/sub1/15936406294964274.pdf"


def main() -> None:
    path = ROOT / "lessons/science/lesson-science-content-id-iv-1.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    refs = list(dict.fromkeys([*data.get("studyReferences", []), SOURCE]))
    data["studyReferences"] = refs
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {
        "updatedAt": "2026-09-07",
        "evidenceCount": 1,
        "evidence": [{
            "lessonId": LESSON_ID,
            "subject": "science",
            "sourceType": "public-school-curriculum-plan",
            "schoolJurisdiction": "嘉義縣公開課程計畫 PDF",
            "url": SOURCE,
            "locator": "PDF 第 24 頁；Id-Ⅳ-1 夏季白天較長、冬季黑夜較長；同頁列出以地球自轉／公轉模型解釋晝夜長短與四季的教學活動",
            "observedSignals": ["課綱概念與代碼", "模型／活動表徵", "晝夜長短與季節的概念順序"],
            "reuseDecision": "inspiration-only",
            "copyrightBoundary": "只保留可追溯定位與抽象教學訊號；不複製 PDF 文字、表格或題目。",
            "accessedAt": "2026-09-07"
        }],
        "note": "此為一個直接讀取的 public-school evidence sample，不推論為全庫出版社章節 evidence。"
    }
    out = ROOT / "implementation/reports/public-curriculum-evidence-batch1.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
