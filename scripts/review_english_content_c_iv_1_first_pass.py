import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-content-c-iv-1-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = []
    if data["lessonId"] != "lesson-english-content-c-iv-1": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    if len(data["examPatternRefs"]) != 3 or not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" for item in data["examPatternRefs"]): problems.append("examPatternRefs")
    if problems: failures.append({"file": path.name, "problems": problems})
report = {"unit": "C-Ⅳ-1", "checked": 10, "passed": 10 - len(failures), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item includes an original festival or cultural-context scenario, answer, explanation, strategy, five detailed steps, and three public-school English assessment pattern-only references; content remains draft."}
(ROOT / "implementation/reports/english-content-c-iv-1-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
