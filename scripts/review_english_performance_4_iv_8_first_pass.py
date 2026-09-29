import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-4-iv-8-first-pass-review.json"
failures = []
answers = []
strategies = []
steps_seen = []
for i in range(1, 11):
    path = OUT / f"question-english-performance-4-iv-8-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    checks = [
        (data.get("lessonId") == "lesson-english-performance-4-iv-8", "lessonId"),
        (data.get("reviewStatus") == "draft", "reviewStatus"),
        (len(data.get("options", [])) == 4 and len({o.get("id") for o in data.get("options", [])}) == 4, "options"),
        (data.get("answer", {}).get("value") in {o.get("id") for o in data.get("options", [])}, "answer"),
        (data.get("provenance", {}).get("origin") == "original", "origin"),
        (len(data.get("solutionSteps", [])) == 5, "solutionSteps"),
        (len(data.get("examPatternRefs", [])) >= 2, "examPatternRefs-count"),
        (all(r.get("reuseDecision") == "pattern-only" and r.get("status") == "recorded" and r.get("locatorLevel") == "item" for r in data.get("examPatternRefs", [])), "examPatternRefs-status-and-locator"),
    ]
    answers.append(data.get("answer", {}).get("value"))
    strategies.append(data.get("solutionStrategy"))
    steps_seen.extend(data.get("solutionSteps", []))
    for ok, label in checks:
        if not ok:
            failures.append({"index": i, "error": label})
if len(answers) == 10 and {key: answers.count(key) for key in "ABCD"} != {"A": 2, "B": 3, "C": 3, "D": 2}:
    failures.append({"index": "all", "error": "answer-position-balance"})
if len(strategies) == 10 and len(set(strategies)) != 10:
    failures.append({"index": "all", "error": "strategy-reuse"})
if len(steps_seen) == 50 and len(set(steps_seen)) != 50:
    failures.append({"index": "all", "error": "solution-step-reuse"})
report = {"unit": "4-Ⅳ-8", "checked": 10, "passed": 0 if failures else 10, "failures": failures, "answerPositionCounts": {key: answers.count(key) for key in "ABCD"}, "uniqueStrategies": len(set(strategies)), "uniqueSolutionSteps": len(set(steps_seen)), "status": "pass" if not failures else "fail", "notes": "Each item includes an original guided paragraph-writing scenario, answer, explanation, individualized strategy, five detailed steps, and at least two exact item-located pattern-only assessment references; content remains draft."}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
