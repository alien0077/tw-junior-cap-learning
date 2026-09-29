#!/usr/bin/env python3
"""First-pass, unit-specific review for N-8-4; never promotes reviewStatus."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/math/lesson-math-content-n-8-4.json"
EXPECTED = {1:"B",2:"C",3:"A",4:"B",5:"C",6:"B",7:"B",8:"B",9:"C",10:"B"}
ANCHORS = ("公差", "等差", "首項", "通項", "項次", "遞推", "相鄰", "間隔", "負公差")

def main() -> int:
    lesson = json.loads(LESSON.read_text(encoding="utf-8"))
    failures = []
    checks = []
    if lesson.get("reviewStatus") != "draft":
        failures.append({"scope":"lesson", "reason":"reviewStatus must remain draft"})
    for path in sorted((ROOT / "questions/math").glob("question-math-content-n-8-4-*.json")):
        n = int(path.stem.rsplit("-", 1)[1])
        data = json.loads(path.read_text(encoding="utf-8"))
        answer = data.get("answer", {})
        text = " ".join([data.get("prompt", ""), data.get("solutionStrategy", ""), *data.get("solutionSteps", [])])
        row = {
            "question": n,
            "path": str(path.relative_to(ROOT)),
            "draftPreserved": data.get("reviewStatus") == "draft",
            "answerMatchesManualKey": answer.get("value") == EXPECTED[n],
            "expectedAnswer": EXPECTED[n],
            "explanationPresent": bool(str(answer.get("explanation", "")).strip()),
            "unitSpecificAnchors": sorted({x for x in ANCHORS if x in text}),
            "detailedSteps": len(data.get("solutionSteps", [])) >= 5 and all(str(x).strip() for x in data.get("solutionSteps", [])),
            "publicPatternRefs": bool(data.get("examPatternRefs")),
        }
        row["passed"] = all((row["draftPreserved"], row["answerMatchesManualKey"], row["explanationPresent"], len(row["unitSpecificAnchors"]) >= 1, row["detailedSteps"], row["publicPatternRefs"]))
        if not row["passed"]: failures.append(row)
        checks.append(row)
    summary = {"status":"pass" if not failures else "blocked", "unit":"N-8-4", "questions":len(checks), "passed":sum(x["passed"] for x in checks), "failed":len(failures), "reviewStatusChange":"none; lesson and questions remain draft", "limitation":"Does not replace three-publisher full-text evidence, distractor/copyright review, Terra second review, or release approval."}
    out = ROOT / "implementation/reports/math-n8-4-first-pass-review.json"
    out.write_text(json.dumps({"summary":summary,"failures":failures,"checks":checks},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1

if __name__ == "__main__": raise SystemExit(main())
