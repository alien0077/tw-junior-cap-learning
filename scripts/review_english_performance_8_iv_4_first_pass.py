import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-8-iv-4-first-pass-review.json"
failures = []
for i in range(1, 11):
    path = OUT / f"question-english-performance-8-iv-4-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    checks = [
        (data.get("lessonId") == "lesson-english-performance-8-iv-4", "lessonId"),
        (data.get("reviewStatus") == "draft", "reviewStatus"),
        (len(data.get("options", [])) == 4 and len({o.get("id") for o in data.get("options", [])}) == 4, "options"),
        (data.get("answer", {}).get("value") in {o.get("id") for o in data.get("options", [])}, "answer"),
        (data.get("provenance", {}).get("origin") == "original", "origin"),
        (len(data.get("solutionSteps", [])) == 5, "solutionSteps"),
        (len(data.get("examPatternRefs", [])) == 3, "examPatternRefs-count"),
        (all(r.get("reuseDecision") == "pattern-only" and r.get("status") == "recorded" for r in data.get("examPatternRefs", [])), "examPatternRefs-status"),
    ]
    for ok, label in checks:
        if not ok:
            failures.append({"index": i, "error": label})
report = {"unit": "8-Ⅳ-4", "checked": 10, "passed": 0 if failures else 10, "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item includes an original cultural-respect and appreciation scenario, answer, explanation, strategy, five detailed steps, and three public-school English assessment pattern-only references; content remains draft."}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
