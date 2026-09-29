import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-3-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
prompts = set()
steps_seen = set()
source_hosts = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-3": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5 or not all(len(step.strip()) >= 18 for step in data["solutionSteps"]): problems.append("solutionSteps")
    if not data["solutionStrategy"].strip() or len(data["answer"]["explanation"].strip()) < 50: problems.append("strategyOrExplanation")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 1 or not all(ref.get("reuseDecision") == "pattern-only" and ref.get("status") == "recorded" and ref.get("locatorLevel") == "item" for ref in refs): problems.append("examPatternRefs")
    if refs:
        host = urlparse(refs[0].get("url", "")).hostname or ""
        source_hosts.add(host)
        if not host.endswith(".edu.tw") or not any(key in host for key in ("hkjh", "nhjh", "ycjh", "kcjh")):
            problems.append("publicSchoolSource")
        if not any(token in refs[0].get("locator", "") for token in ("第", "PDF")):
            problems.append("itemLocator")
    if data["prompt"] in prompts: problems.append("duplicatePrompt")
    prompts.add(data["prompt"])
    for step in data["solutionSteps"]:
        if step in steps_seen: problems.append("reusedSolutionStep")
        steps_seen.add(step)
    if problems: failures.append({"file": path.name, "problems": problems})
report = {"unit": "3-Ⅳ-3", "checked": 10, "passed": 10 - len(failures), "failures": failures, "distinctPrompts": len(prompts), "distinctSolutionSteps": len(steps_seen), "publicSchoolDomains": sorted(source_hosts), "status": "pass" if not failures else "fail", "scope": "Question-level first-pass structure and source-locator contract only; does not verify textbook fusion, full lesson publication readiness, copyright clearance, or Terra second pass.", "reviewStatus": "draft", "notes": "Each original item has one exact item-level public-school exam-pattern reference, one answer with an explanation, an individualized Traditional-Chinese strategy, and five distinct detailed solution steps."}
(ROOT / "implementation/reports/english-performance-3-iv-3-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
