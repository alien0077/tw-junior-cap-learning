import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-1-iv-7-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
institutions = set()
expected_answers = {1: "C", 2: "A", 3: "D", 4: "B", 5: "C", 6: "D", 7: "A", 8: "B", 9: "C", 10: "D"}
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-1-iv-7": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    number = int(path.stem.rsplit("-", 1)[-1])
    if data["answer"]["value"] != expected_answers[number]: problems.append("answer-key-regression")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    refs = data["examPatternRefs"]
    if len(refs) != 1 or not all(item["reuseDecision"] == "pattern-only" and item["status"] == "recorded" and item.get("locatorLevel") == "item" and item.get("locator") and item.get("url") == data["provenance"].get("sourceUrl") for item in refs): problems.append("examPatternRefs")
    if len(data.get("solutionStrategy", "")) < 30 or not all(len(step) >= 16 for step in data.get("solutionSteps", [])): problems.append("strategyOrDetailedSteps")
    for ref in refs:
        if "ycjh.hlc.edu.tw" in ref["url"]: institutions.add("宜昌國中")
        elif "csjh.kl.edu.tw" in ref["url"]: institutions.add("中山高中國中部")
        elif "chhs.tp.edu.tw" in ref["url"]: institutions.add("景興國中")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(institutions) < 3: failures.append({"scope": "unit", "problems": ["fewer-than-three-distinct-public-schools"]})
report = {"unit": "1-Ⅳ-7", "checked": 10, "passed": 10 - sum("file" in x for x in failures), "distinctPublicSchools": sorted(institutions), "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item has one exact item-level pattern-only reference matching its provenance URL; the set spans at least three public schools. Every item has an original passage, answer, strategy, and five detailed steps; all remain draft."}
(ROOT / "implementation/reports/english-performance-1-iv-7-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
