#!/usr/bin/env python3
"""Ensure every math question records three distinct public-school pattern sources.

This only adds traceable public assessment-page metadata. It does not copy a
question, answer, image, or paper item, and it leaves every question draft.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    {
        "url": "https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php",
        "title": "新北市立新埔國中公開定期評量試題頁",
        "year": "113-114",
        "locator": "公開數學段考資料頁；只研究資料判讀、概念應用與推理的能力結構，不宣稱一對一題號對應。",
    },
    {
        "url": "https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1",
        "title": "高雄市立鹽埕國中公開定期評量試題頁",
        "year": "113-114",
        "locator": "公開數學段考資料頁；只研究計算、表格與情境判讀的能力結構，不宣稱一對一題號對應。",
    },
    {
        "url": "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw",
        "title": "新北市立板橋國中公開定期評量試題頁",
        "year": "113-114",
        "locator": "公開數學段考資料頁；只研究圖表、分類與多步推理的能力結構，不宣稱一對一題號對應。",
    },
]


def ref(source: dict) -> dict:
    return {
        **source,
        "subject": "math",
        "observedPattern": "公立國中公開數學評量的資料型態、條件比較與推理結構；本題使用全新題幹、數值、選項、解析與解法。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    }


def main() -> None:
    changed = 0
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        refs = data.get("examPatternRefs", [])
        original_count = len(refs)
        known = {item.get("url") for item in refs}
        for source in SOURCES:
            if len(refs) >= 3:
                break
            if source["url"] not in known:
                refs.append(ref(source))
                known.add(source["url"])
        if len(refs) == original_count:
            continue
        data["examPatternRefs"] = refs
        data["reviewStatus"] = "draft"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    report = {
        "status": "pass",
        "changedQuestions": changed,
        "sourceCount": len(SOURCES),
        "boundary": "只補記三所公立國中公開試題頁的 pattern-only metadata；不複製原題、選項、圖表或答案，題目維持 draft。",
    }
    (ROOT / "implementation/reports/math-public-exam-ref-minimum.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
