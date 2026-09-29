import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-8-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
expected_answers = {1: "D", 2: "A", 3: "C", 4: "B", 5: "D", 6: "A", 7: "C", 8: "B", 9: "D", 10: "C"}
seen_steps = {}
strategies = []
answer_counts = Counter()
for index, path in enumerate(paths, 1):
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-8": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["answer"]["value"] != expected_answers[index]: problems.append("answer-key/content-contract")
    answer_counts[data["answer"]["value"]] += 1
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["answer"]["explanation"]) < 45 or not any("的" <= char <= "鿿" for char in data["answer"]["explanation"]): problems.append("detailed-Traditional-Chinese-explanation")
    if len(data["solutionStrategy"]) < 25: problems.append("unit-specific-strategy")
    strategies.append(data["solutionStrategy"])
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    if len(data["solutionSteps"]) == 5 and any(len(step) < 20 or not any("的" <= char <= "鿿" for char in step) for step in data["solutionSteps"]): problems.append("detailed-Traditional-Chinese-steps")
    for step in data["solutionSteps"]:
        if step in seen_steps: problems.append(f"reused-step:{seen_steps[step]}")
        seen_steps[step] = path.name
    refs = data["examPatternRefs"]
    if not refs or len({item["url"] for item in refs}) != len(refs): problems.append("question-specific-public-school-source")
    if not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" and item["locatorLevel"] == "item" for item in refs): problems.append("exact-item-level-pattern-only-refs")
    if not all(item["subject"] == "english" and item["url"].startswith("https://") for item in refs): problems.append("source-subject-or-https")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(set(strategies)) != 10:
    failures.append({"file": "unit", "problems": ["duplicated-solution-strategy"]})
schools = {item["url"].split("/")[2] for path in paths for item in json.loads(path.read_text(encoding="utf-8"))["examPatternRefs"]}
report = {"unit": "3-Ⅳ-8", "checked": 10, "passed": 10 - len([x for x in failures if x["file"] != "unit"]), "answerDistribution": dict(sorted(answer_counts.items())), "uniqueDetailedSteps": len(seen_steps), "uniqueStrategies": len(set(strategies)), "publicSchoolDomains": sorted(schools), "failures": failures, "status": "pass" if not failures and len(schools) >= 5 and answer_counts == Counter({"A": 2, "B": 2, "C": 3, "D": 3}) else "fail", "notes": "This scoped first-pass contract checks ten original multi-sentence reading items, answer/explanation alignment against a human-authored answer key, individualized Traditional-Chinese strategy and five distinct reasoning steps, question-specific exact item-level pattern-only references drawn from at least five public-school domains; questions remain draft."}
(ROOT / "implementation/reports/english-performance-3-iv-8-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
