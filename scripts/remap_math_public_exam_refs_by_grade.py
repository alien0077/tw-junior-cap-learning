#!/usr/bin/env python3
"""Move explicit grade-7/8 math pattern refs to grade-matched public exam PDFs."""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
TARGETS = {
    "7": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/66b1c8536c734e12643924e2",
        "title": "臺中市立至善國民中學 112 學年度第二學期第一次定期評量七年級數學科",
        "year": "112",
        "observedPattern": "年級相符的數與量、代數、幾何與資料題；只吸收題型、資料型態與作答結構。",
    },
    "8": {
        "url": "https://school.tc.edu.tw/open-message/193521/get-file/697b23af02d6b7546a022da8.pdf",
        "title": "臺中市立至善國民中學 114 學年度第一學期第二次定期評量八年級數學科",
        "year": "114",
        "observedPattern": "年級相符的根式、因式分解、畢氏定理與幾何資料題；只吸收題型、資料型態與作答結構。",
    },
}


def infer_grade(lesson_id: str) -> str:
    matches = re.findall(r"(?:^|-)((?:7|8|9))(?:-|$)", lesson_id)
    return matches[-1] if matches else "unclassified"


def ref_for(grade: str, data: dict) -> dict:
    target = TARGETS[grade]
    title = f"{target['title']}；本題為原創 pattern-only 改寫，非原題題號重製"
    return {
        "url": target["url"],
        "title": title,
        "year": target["year"],
        "subject": "math",
        "locator": f"{target['title']}；公開試卷頁面與年級已核對；本題使用全新題幹、數值、選項與解析，不宣稱一對一題號對應",
        "observedPattern": target["observedPattern"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "paper",
    }


def main() -> None:
    counts = collections.Counter()
    changed = []
    for path in sorted((ROOT / "questions" / "math").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not any(ref.get("url") == OLD for ref in data.get("examPatternRefs", [])):
            continue
        grade = infer_grade(str(data.get("lessonId", "")))
        if grade not in TARGETS:
            continue
        refs = [ref for ref in data.get("examPatternRefs", []) if ref.get("url") != OLD]
        target_url = TARGETS[grade]["url"]
        if not any(ref.get("url") == target_url for ref in refs):
            refs.append(ref_for(grade, data))
        data["examPatternRefs"] = refs
        provenance = data.get("provenance", {})
        if provenance.get("sourceUrl") == OLD:
            target = TARGETS[grade]
            provenance["sourceUrl"] = target["url"]
            provenance["sourceLocator"] = f"{target['title']}；公開頁面年級／科目已核對；原創 pattern-only 改寫，待逐題內容 QA。"
            data["provenance"] = provenance
        data["reviewStatus"] = "draft"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        counts[grade] += 1
        changed.append({"path": str(path.relative_to(ROOT)), "grade": grade, "newSourceUrl": TARGETS[grade]["url"]})
    report = {
        "status": "pass",
        "changed": len(changed),
        "countsByGrade": dict(counts),
        "oldSourceUrl": OLD,
        "newSources": {grade: target["url"] for grade, target in TARGETS.items()},
        "referenceMode": "pattern-only",
        "boundary": "只修正顯式年級的來源適配 metadata；未分類與九年級 refs 保留待審，不改成錯誤完成。",
        "items": changed,
    }
    out = ROOT / "implementation/reports/math-public-exam-ref-remap-20260908.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "changed", "countsByGrade", "referenceMode")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
