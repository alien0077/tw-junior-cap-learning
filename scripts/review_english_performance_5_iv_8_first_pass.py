import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-5-iv-8-first-pass-review.json"
EXPECTED_KEYS = ["B", "C", "D", "A", "B", "C", "D", "A", "B", "C"]
EXPECTED_CORRECT_TEXT = [
    "At a ferry pier before sunrise", "Mina, Leo, and their neighbor",
    "She followed the footprint to the greenhouse", "The cart breaks while he is bringing the boat in",
    "To bring back his grandfather's walking stick", "Relief",
    "Heavy rain made the creek rise", "The student's memory gives them a new place to check",
    "They solve the route problem and arrive together",
    "Seed packet blows away → classmates search → note points to art room → packet found",
]
ALLOWED_URLS = {
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/109-1-1%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/3-%E8%8B%B1%E6%96%87.pdf",
    "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
    "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
}
failures = []
strategies, all_steps, refs_seen = [], [], set()
key_counts = Counter()
for i in range(1, 11):
    path = OUT / f"question-english-performance-5-iv-8-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    key = data.get("answer", {}).get("value")
    key_counts[key] += 1
    checks = [
        (data.get("id") == f"question-english-performance-5-iv-8-{i}", "stable id"),
        (data.get("lessonId") == "lesson-english-performance-5-iv-8", "lessonId"),
        (data.get("reviewStatus") == "draft", "draft gate"),
        (data.get("provenance", {}).get("origin") == "original", "original origin"),
        (len(data.get("options", [])) == 4 and len({o.get("id") for o in data.get("options", [])}) == 4, "four unique options"),
        (key == EXPECTED_KEYS[i - 1], "answer key matches reviewed key"),
        (next((o.get("text") for o in data.get("options", []) if o.get("id") == key), None) == EXPECTED_CORRECT_TEXT[i - 1], "key maps to expected correct answer"),
        ("正確答案：" + key in data.get("answer", {}).get("explanation", ""), "explicit answer in explanation"),
        (len(data.get("solutionSteps", [])) == 5 and all(len(s) >= 18 for s in data.get("solutionSteps", [])), "five detailed steps"),
        (len(data.get("solutionSteps", [])) == 5 and any(f"選{key}" in s for s in data.get("solutionSteps", [])), "step-by-step answer key matches option key"),
        (len(data.get("examPatternRefs", [])) == 3, "three exact public-exam refs"),
        (all(r.get("url") in ALLOWED_URLS and r.get("reuseDecision") == "pattern-only" and r.get("status") == "recorded" and r.get("locatorLevel") == "item" and "PDF第" in r.get("locator", "") and "題" in r.get("locator", "") for r in data.get("examPatternRefs", [])), "traceable page/item refs"),
        (len({r.get("url") for r in data.get("examPatternRefs", [])}) == 3, "three different public-school sources"),
        (len(data.get("solutionStrategy", "")) >= 30, "unit-specific strategy"),
    ]
    for ok, label in checks:
        if not ok:
            failures.append({"index": i, "error": label})
    strategies.append(data.get("solutionStrategy", ""))
    all_steps.extend(data.get("solutionSteps", []))
    refs_seen.update(r.get("url") for r in data.get("examPatternRefs", []))

if len(set(strategies)) != 10:
    failures.append({"error": "strategies are not unique"})
if len(all_steps) != 50 or len(set(all_steps)) != 50:
    failures.append({"error": "all 50 solution steps must be distinct"})
if key_counts != Counter({"A": 2, "B": 3, "C": 3, "D": 2}):
    failures.append({"error": f"answer distribution: {dict(key_counts)}"})

report = {
    "unit": "5-Ⅳ-8", "checked": 10, "passed": 0 if failures else 10,
    "answerDistribution": dict(sorted(key_counts.items())),
    "uniqueStrategies": len(set(strategies)), "uniqueDetailedSteps": len(set(all_steps)),
    "publicSchoolSources": len(refs_seen), "failures": failures,
    "status": "pass" if not failures else "fail",
    "notes": "Ten original simple-story note-comprehension questions; verified key-to-option mapping, explicit answers, distinct Chinese strategies and five-step explanations, three page/item-located pattern-only public-school exam refs per item. Questions remain draft pending full unit and release gates.",
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
