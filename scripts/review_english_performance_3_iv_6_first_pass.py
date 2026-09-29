import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-6-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
all_answers = []
all_strategies = []
catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
catalog_urls = {item["url"] for item in catalog["sources"]}
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-6": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    refs = data["examPatternRefs"]
    if not refs or not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" and item["locatorLevel"] == "item" and item["locator"].strip() and item["url"] in catalog_urls for item in refs): problems.append("examPatternRefs")
    if len({item["url"] for item in refs}) != len(refs): problems.append("duplicateExamRef")
    if not data["answer"]["explanation"].startswith("正確答案"): problems.append("answerExplanation")
    if not data["solutionStrategy"] or any(not step.strip() for step in data["solutionSteps"]): problems.append("solutionQuality")
    all_answers.append(data["answer"]["value"])
    all_strategies.append(data["solutionStrategy"])
    if problems: failures.append({"file": path.name, "problems": problems})
if len(set(all_answers)) < 3: failures.append({"file": "unit", "problems": ["answerKeyLacksDistribution"]})
if len(set(all_strategies)) != 10: failures.append({"file": "unit", "problems": ["reusedStrategies"]})
report = {"unit": "3-Ⅳ-6", "checked": 10, "passed": 10 - sum(item["file"] != "unit" for item in failures), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item includes an original context-specific sentence pattern, keyed answer, Traditional Chinese explanation, distinct strategy, five steps, and verified item-level public-school exam pattern-only locator(s). This first pass checks structure and source traceability, not full subject or copyright approval; all remain draft."}
(ROOT / "implementation/reports/english-performance-3-iv-6-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
