#!/usr/bin/env python3
"""Move unclassified cross-grade math pattern refs to the official CAP math source."""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CAP = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"


def explicit_grade(lesson_id: str) -> bool:
    return bool(re.findall(r"(?:^|-)((?:7|8|9))(?:-|$)", lesson_id))


def cap_ref(data: dict) -> dict:
    return {
        "url": CAP,
        "title": "114 年國中教育會考數學科公開試題；跨年級能力與資料型態參照；本題為原創 pattern-only 改寫",
        "year": "114",
        "subject": "math",
        "locator": "114 年國中教育會考數學科公開試題；跨年級數與量、代數、資料與不確定性、函數或空間與形狀能力參照；不宣稱一對一題號對應",
        "observedPattern": "跨年級數學公開評量的資料判讀、計算、表示轉換與推理要求；只吸收能力、資料型態與解題步驟。",
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    }


def main() -> None:
    count = 0
    by_lesson = collections.Counter()
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if explicit_grade(str(data.get("lessonId", ""))):
            continue
        if not any(ref.get("url") == OLD for ref in data.get("examPatternRefs", [])):
            continue
        data["examPatternRefs"] = [cap_ref(data) if ref.get("url") == OLD else ref for ref in data.get("examPatternRefs", [])]
        provenance = data.get("provenance", {})
        if provenance.get("sourceUrl") == OLD:
            provenance["sourceUrl"] = CAP
            provenance["sourceLocator"] = "114 年國中教育會考數學科公開試題；跨年級能力／資料型態參照；原創 pattern-only 改寫，待逐題內容 QA。"
            data["provenance"] = provenance
        data["reviewStatus"] = "draft"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
        by_lesson[data.get("lessonId", "")] += 1
    report = {
        "status": "pass",
        "changed": count,
        "oldSourceUrl": OLD,
        "newSourceUrl": CAP,
        "referenceMode": "pattern-only",
        "lessonCount": len(by_lesson),
        "countsByLesson": dict(by_lesson),
        "boundary": "只處理無法由 lesson ID 推導年級的根／學習表現／跨年級節點；明確七、八、九年級 refs 不在本次範圍。官方會考來源不等於逐題題號對應或內容 QA。",
    }
    out = ROOT / "implementation/reports/math-unclassified-ref-remap-20260908.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "changed", "lessonCount", "referenceMode")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
