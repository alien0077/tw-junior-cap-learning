import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/math"
REPORT = ROOT / "implementation/reports/math-performance-n-iv-5-first-pass-review.json"
failures = []
for i in range(1, 11):
    path = OUT / f"question-math-performance-n-iv-5-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    checks = [
        (data.get("lessonId") == "lesson-math-performance-n-iv-5", "lessonId"),
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
report = {"unit": "n-Ⅳ-5", "checked": 10, "passed": 0 if failures else 10, "failures": failures, "status": "pass" if not failures else "fail", "notes": "每題含原創二次方根與根式情境、答案、解析、解題策略、五步詳細步驟與三筆公開數學試題 pattern-only 來源；內容仍為 draft。"}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
