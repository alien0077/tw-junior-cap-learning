import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/english-performance-7-iv-4-first-pass-review.json"
expected = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E8%AA%9E.pdf",
    "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2790&name=112-2-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E8%81%BD%E5%8A%9B%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B1%E6%9B%89%E8%96%87.pdf&op=dlfile",
}
failures, strategies, steps = [], [], []
answers = Counter()
for i in range(1, 11):
    p = ROOT / f"questions/english/question-english-performance-7-iv-4-{i}.json"
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"item": i, "error": str(exc)})
        continue
    refs = d.get("examPatternRefs", [])
    key = d.get("answer", {}).get("value")
    checks = {
        "unit_and_draft": d.get("lessonId") == "lesson-english-performance-7-iv-4" and d.get("reviewStatus") == "draft",
        "four_unique_options": len(d.get("options", [])) == 4 and len({x.get("id") for x in d["options"]}) == 4 and len({x.get("text") for x in d["options"]}) == 4,
        "key_exists": key in {x.get("id") for x in d.get("options", [])},
        "original_provenance": d.get("provenance", {}).get("origin") == "original",
        "three_public_refs": len(refs) == 3 and {x.get("url") for x in refs} == expected,
        "refs_recorded_pattern_only": all(x.get("status") == "recorded" and x.get("reuseDecision") == "pattern-only" and x.get("locatorLevel") in {"paper", "item"} for x in refs),
        "five_detailed_steps": len(d.get("solutionSteps", [])) == 5 and len(set(d.get("solutionSteps", []))) == 5 and all(any("\u4e00" <= ch <= "\u9fff" for ch in s) for s in d.get("solutionSteps", [])),
        "explanation": len(d.get("answer", {}).get("explanation", "")) >= 40 and f"答案是 {key}" in d["answer"]["explanation"] or f"答案選 {key}" in d["answer"].get("explanation", "") or f"答案為 {key}" in d["answer"].get("explanation", "") or f"正確答案是 {key}" in d["answer"].get("explanation", ""),
        "strategy": len(d.get("solutionStrategy", "")) >= 20,
    }
    failures.extend({"item": i, "error": name} for name, passed in checks.items() if not passed)
    strategies.append(d.get("solutionStrategy", ""))
    steps.extend(d.get("solutionSteps", []))
    answers[key] += 1
if len(set(strategies)) != 10:
    failures.append({"error": "strategies-not-unique"})
if len(set(steps)) != 50:
    failures.append({"error": "solution-steps-not-unique", "unique": len(set(steps))})
expected_distribution = Counter({"A": 2, "B": 2, "C": 3, "D": 3})
if answers != expected_distribution:
    failures.append({"error": "answer-distribution", "actual": dict(answers)})
report = {
    "unit": "7-Ⅳ-4", "checked": 10, "passed": 0 if failures else 10,
    "answerDistribution": dict(answers), "uniqueStrategies": len(set(strategies)),
    "uniqueSolutionSteps": len(set(steps)), "sourceCountPerQuestion": 3,
    "publicSchoolSourceUrls": sorted(expected), "failures": failures,
    "status": "pass" if not failures else "fail",
    "notes": "Scoped review checks answer-key presence, unique options, detailed Traditional Chinese explanations/strategies/five-step solutions, recorded pattern-only public-school sources, and draft preservation. It does not replace full unit or copyright QA.",
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if not failures else 1)
