import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-7-iv-3-first-pass-review.json"
failures = []
strategies = []
step_sets = []
answers = Counter()
expected_urls = {
    "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf",
    "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
}
for i in range(1, 11):
    path = OUT / f"question-english-performance-7-iv-3-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    checks = [
        (data.get("lessonId") == "lesson-english-performance-7-iv-3", "lessonId"),
        (data.get("reviewStatus") == "draft", "reviewStatus"),
        (len(data.get("options", [])) == 4 and len({o.get("id") for o in data.get("options", [])}) == 4, "options"),
        (data.get("answer", {}).get("value") in {o.get("id") for o in data.get("options", [])}, "answer"),
        (data.get("provenance", {}).get("origin") == "original", "origin"),
        (len(data.get("solutionSteps", [])) == 5, "solutionSteps"),
        (len(data.get("examPatternRefs", [])) == 3, "examPatternRefs-count"),
        (all(r.get("reuseDecision") == "pattern-only" and r.get("status") == "recorded" and r.get("locatorLevel") in {"paper", "item"} for r in data.get("examPatternRefs", [])), "examPatternRefs-status"),
        ({r.get("url") for r in data.get("examPatternRefs", [])} == expected_urls, "examPatternRefs-sources"),
        (len(set(data.get("solutionSteps", []))) == 5, "solutionSteps-distinct"),
        (len(data.get("answer", {}).get("explanation", "")) >= 40 and "正確答案" in data.get("answer", {}).get("explanation", ""), "explanation-detailed"),
        (all(any("\u4e00" <= ch <= "\u9fff" for ch in step) for step in data.get("solutionSteps", [])), "solutionSteps-traditional-chinese"),
        (data.get("updatedAt") == "2026-09-27", "updatedAt"),
    ]
    strategies.append(data.get("solutionStrategy", ""))
    step_sets.extend(data.get("solutionSteps", []))
    answers[data.get("answer", {}).get("value")] += 1
    for ok, label in checks:
        if not ok:
            failures.append({"index": i, "error": label})
if len(set(strategies)) != 10:
    failures.append({"error": "strategies-not-unique"})
if len(set(step_sets)) != 50:
    failures.append({"error": "solution-steps-not-unique"})
if answers != Counter({"A": 2, "B": 3, "C": 3, "D": 2}):
    failures.append({"error": "answer-distribution", "actual": dict(answers)})
report = {"unit": "7-Ⅳ-3", "checked": 10, "passed": 0 if failures else 10, "answerDistribution": dict(answers), "uniqueStrategies": len(set(strategies)), "uniqueSolutionSteps": len(set(step_sets)), "publicSchoolSourceUrls": sorted(expected_urls), "failures": failures, "status": "pass" if not failures else "fail", "notes": "All 10 original questions have a keyed answer, detailed Traditional Chinese explanation, unique strategy and five distinct steps; each cites the same three verified public-school English assessment sources at paper level as pattern-only references. Questions remain draft; this structural/content pass does not replace full unit and copyright QA."}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
