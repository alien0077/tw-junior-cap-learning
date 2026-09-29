import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-5-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-5": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    refs = data["examPatternRefs"]
    if len(refs) < 2 or not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" and item["locatorLevel"] == "item" and item["locator"].strip() for item in refs): problems.append("examPatternRefs")
    if len({item["url"] for item in refs}) != len(refs): problems.append("duplicateExamSource")
    if not data["answer"]["explanation"].startswith("正確答案"): problems.append("answerExplanation")
    if not data["solutionStrategy"] or any(not step.strip() for step in data["solutionSteps"]): problems.append("solutionQuality")
    if any("待 Terra" in value or "Terra" in value for value in data["provenance"].values()): problems.append("prohibitedReview")
    if problems: failures.append({"file": path.name, "problems": problems})
report = {"unit": "3-Ⅳ-5", "checked": 10, "passed": 10 - len(failures), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item includes original context-sensitive response options, an answer, Traditional Chinese explanation, individual strategy, five steps, and at least two distinct public-school item-level pattern-only references; all remain draft. This is a structural/locator check, not expert content approval."}
(ROOT / "implementation/reports/english-performance-3-iv-5-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
