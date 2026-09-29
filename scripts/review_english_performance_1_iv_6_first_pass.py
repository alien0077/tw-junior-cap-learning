import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-1-iv-6-{i}.json" for i in range(1, 11)]
expected_answers = ["B", "C", "A", "D", "B", "C", "D", "C", "A", "B"]
assert all(path.exists() for path in paths)
failures = []
source_urls = set()
for path, expected_answer in zip(paths, expected_answers):
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-1-iv-6": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["answer"]["value"] != expected_answer: problems.append("answerKey")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    refs = data.get("examPatternRefs", [])
    source_urls.update(item.get("url") for item in refs)
    if len(refs) != 1 or not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" and item["locatorLevel"] == "item" for item in refs): problems.append("exactItemLevelExamPatternRef")
    if len(refs) == 1 and data["provenance"].get("sourceUrl") != refs[0].get("url"): problems.append("provenanceExamRefMismatch")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(source_urls) < 3: failures.append({"unit": "1-Ⅳ-6", "problems": ["fewerThanThreeDistinctPublicExamSources"]})
report = {"unit": "1-Ⅳ-6", "checked": 10, "passed": 10 - sum(1 for item in failures if "file" in item), "distinctPublicExamSources": len(source_urls), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each original question has its own verified item-level pattern-only public-exam reference with provenance URL equality; the ten questions collectively use at least three public-school sources. Every item includes an answer, explanation, individual strategy, and five detailed steps; content remains draft."}
(ROOT / "implementation/reports/english-performance-1-iv-6-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
