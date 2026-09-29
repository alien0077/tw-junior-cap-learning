#!/usr/bin/env python3
"""Focused review of two tr-IV-1 original questions mapped to Bihua item 33."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL = "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw"
EXPECTED = {
    1: {
        "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第5頁第33題",
        "step_terms": ["觀察", "摩擦", "條件", "選項", "推論"],
    },
    7: {
        "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第5頁第33題",
        "step_terms": ["替代", "正向力", "公平", "選項", "結論"],
    },
}


def main() -> int:
    errors: list[str] = []
    checked = []
    for number, expected in EXPECTED.items():
        path = ROOT / f"questions/science/question-science-performance-tr-iv-1-{number}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        refs = [r for r in q.get("examPatternRefs", []) if r.get("url") == URL]
        if q.get("reviewStatus") != "draft":
            errors.append(f"{q['id']}: must remain draft")
        if len(refs) != 1:
            errors.append(f"{q['id']}: expected exactly one Bihua reference")
        elif not (
            refs[0].get("status") == "recorded"
            and refs[0].get("locatorLevel") == "item"
            and refs[0].get("reuseDecision") == "pattern-only"
            and refs[0].get("locator") == expected["locator"]
            and refs[0].get("pattern") == refs[0].get("observedPattern")
        ):
            errors.append(f"{q['id']}: Bihua item-level evidence contract failed")
        if q.get("answer", {}).get("value") != "A":
            errors.append(f"{q['id']}: expected independently checked answer A")
        if len(q.get("answer", {}).get("explanation", "")) < 60:
            errors.append(f"{q['id']}: answer explanation is not sufficiently detailed")
        if len(q.get("solutionStrategy", "")) < 40:
            errors.append(f"{q['id']}: missing unit-question-specific strategy")
        steps = q.get("solutionSteps", [])
        if len(steps) != 5 or any(len(step) < 40 for step in steps):
            errors.append(f"{q['id']}: expected five substantive solution steps")
        else:
            for index, term in enumerate(expected["step_terms"]):
                if term not in steps[index]:
                    errors.append(f"{q['id']} step {index + 1}: missing topic-specific reasoning")
        checked.append(q["id"])

    report = {
        "status": "pass" if not errors else "fail",
        "checkedQuestions": checked,
        "sourceItem": "Bihua 114-2 grade 8 physics/chemistry, page 5 item 33",
        "checks": ["exact item locator", "pattern-only attribution", "answer and explanation", "question-specific strategy", "five detailed steps", "draft status retained"],
        "failures": errors,
        "reviewedAt": "2026-09-24",
    }
    output = ROOT / "implementation/reports/science-performance-tr-iv-1-bihua-review.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
