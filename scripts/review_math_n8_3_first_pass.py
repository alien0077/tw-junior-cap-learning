#!/usr/bin/env python3
"""First-pass, unit-specific review for N-8-3; never promotes reviewStatus."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-content-n-8-3.json"
QUESTION_DIR = ROOT / "questions/math"

EXPECTED = {
    1: ("B", 20), 2: ("D", 80), 3: ("B", 32), 4: ("C", 11),
    5: ("B", 17), 6: ("C", 22), 7: ("A", 36), 8: ("B", 32),
    9: ("C", 8), 10: ("C", "4、9、14、19"),
}

ANCHORS = ("項次", "項", "公差", "遞推", "通項", "相鄰差", "平方", "等差", "首項")


def main() -> int:
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    failures = []
    checks = []
    if lesson.get("reviewStatus") != "draft":
        failures.append({"scope": "lesson", "reason": "reviewStatus must remain draft"})
    for path in sorted(QUESTION_DIR.glob("question-math-content-n-8-3-*.json")):
        number = int(path.stem.rsplit("-", 1)[1])
        data = json.loads(path.read_text(encoding="utf-8"))
        expected_answer, expected_value = EXPECTED[number]
        answer = data.get("answer", {})
        text = " ".join([data.get("prompt", ""), data.get("solutionStrategy", ""), *data.get("solutionSteps", [])])
        item = {
            "question": number,
            "path": str(path.relative_to(ROOT)),
            "draftPreserved": data.get("reviewStatus") == "draft",
            "answerMatchesManualRecalculation": answer.get("value") == expected_answer,
            "expectedAnswer": expected_answer,
            "manualResult": expected_value,
            "explanationPresent": bool(str(answer.get("explanation", "")).strip()),
            "unitSpecificAnchors": sorted({anchor for anchor in ANCHORS if anchor in text}),
            "hasAtLeastThreeDetailedSteps": len(data.get("solutionSteps", [])) >= 3,
            "publicPatternRefs": len(data.get("examPatternRefs", [])) > 0,
        }
        item["passed"] = all((item["draftPreserved"], item["answerMatchesManualRecalculation"], item["explanationPresent"], len(item["unitSpecificAnchors"]) >= 1, item["hasAtLeastThreeDetailedSteps"], item["publicPatternRefs"]))
        if not item["passed"]:
            failures.append(item)
        checks.append(item)
    summary = {
        "status": "pass" if not failures else "blocked",
        "unit": "N-8-3",
        "scope": "first-pass answer, explanation, detailed-step, unit-specific and public-pattern-source review",
        "questions": len(checks),
        "passed": sum(1 for item in checks if item["passed"]),
        "failed": len(failures),
        "reviewStatusChange": "none; lesson and questions remain draft",
        "limitation": "This does not replace full three-publisher textbook evidence, Terra second review, copyright review, or release approval.",
    }
    out = ROOT / "implementation/reports/math-n8-3-first-pass-review.json"
    out.write_text(json.dumps({"summary": summary, "failures": failures, "checks": checks}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
