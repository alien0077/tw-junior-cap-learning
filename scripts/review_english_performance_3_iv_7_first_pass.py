import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-7-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
catalog_urls = {item["url"] for item in catalog["sources"]}
failures = []
answers = set()
strategies = set()
steps_seen = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-7": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    if not data["answer"]["explanation"].startswith("正確答案"): problems.append("Chinese answer explanation")
    if len(data["solutionStrategy"]) < 20: problems.append("solutionStrategy")
    refs = data["examPatternRefs"]
    if not refs or any(item.get("reuseDecision") != "pattern-only" or item.get("status") != "recorded" or item.get("locatorLevel") != "item" or not item.get("locator") or item.get("url") not in catalog_urls for item in refs): problems.append("examPatternRefs")
    if len({item["url"] for item in refs}) != len(refs): problems.append("duplicate exam source URL")
    answers.add(data["answer"]["value"]); strategies.add(data["solutionStrategy"]); steps_seen.update(data["solutionSteps"])
    if problems: failures.append({"file": path.name, "problems": problems})
if len(answers) < 3: failures.append({"file": "question-set", "problems": ["answer-key distribution"]})
if len(strategies) != 10: failures.append({"file": "question-set", "problems": ["strategies are not individually authored"]})
if len(steps_seen) < 45: failures.append({"file": "question-set", "problems": ["reasoning steps are insufficiently distinct"]})
report = {"unit": "3-Ⅳ-7", "checked": 10, "passed": 10 - sum(1 for item in failures if item["file"] != "question-set"), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Checks original draft status, answer/explanation, tailored five-step reasoning, unique strategies and item-level pattern-only refs present in the public source catalog; this is structural first-pass AI review, not teacher/expert approval."}
(ROOT / "implementation/reports/english-performance-3-iv-7-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
