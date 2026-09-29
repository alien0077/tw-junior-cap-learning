import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-5-iv-9-first-pass-review.json"
EXPECTED_KEYS = ["B", "C", "D", "A", "B", "C", "D", "A", "B", "C"]
EXPECTED_TEXTS = [
    "Announcing the show and inviting families", "Auditorium, 9:15",
    "Wait behind the line and let riders exit first", "The guided tour",
    "Rain after 3 p.m.", "Pine Road", "The indoor talk in Room 2 at 7:00",
    "To ask visitors to return the tablets before leaving",
    "Route 6, Stop B, 4:20; student passes only",
    "East entrance; 6:00 start; dance show in gym; bring a reusable cup",
]
ALLOWED_URLS = {
    "https://school.tc.edu.tw/open-message/064526/get-file/628aea9f04ad8678f4674dca",
    "https://cgjh.hcc.edu.tw/p/405-1032-440270,c5348.php",
    "https://sljh.hcc.edu.tw/p/406-1034-491334,r1565.php?Lang=zh-tw",
    "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=358&cfsn=2105&name=109-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E5%BE%90%E7%BE%8E%E9%9B%B2.pdf&op=dlfile",
}
failures = []
key_counts = Counter()
strategies, steps, source_urls = [], [], set()
for i in range(1, 11):
    path = OUT / f"question-english-performance-5-iv-9-{i}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"index": i, "error": str(exc)})
        continue
    key = data.get("answer", {}).get("value")
    key_counts[key] += 1
    refs = data.get("examPatternRefs", [])
    options = data.get("options", [])
    option_text = next((option.get("text") for option in options if option.get("id") == key), None)
    checks = [
        (data.get("id") == f"question-english-performance-5-iv-9-{i}", "stable question ID"),
        (data.get("lessonId") == "lesson-english-performance-5-iv-9", "lesson linkage"),
        (data.get("reviewStatus") == "draft", "draft release gate"),
        (data.get("provenance", {}).get("origin") == "original", "original authoring"),
        (len(options) == 4 and {option.get("id") for option in options} == {"A", "B", "C", "D"}, "four unique options"),
        (key == EXPECTED_KEYS[i - 1], "answer key checked against source authoring"),
        (option_text == EXPECTED_TEXTS[i - 1], "answer key maps to intended answer text"),
        (f"正確答案：{key}" in data.get("answer", {}).get("explanation", ""), "explicit answer in explanation"),
        (len(data.get("solutionSteps", [])) == 5 and all(len(step) >= 18 for step in data.get("solutionSteps", [])), "five detailed solution steps"),
        (any(f"選{key}" in step for step in data.get("solutionSteps", [])), "worked steps use the answer option key"),
        (len(refs) == 3, "three exact public-exam pattern refs"),
        (all(ref.get("url") in ALLOWED_URLS and ref.get("reuseDecision") == "pattern-only" and ref.get("status") == "recorded" and ref.get("locatorLevel") == "item" and "PDF第" in ref.get("locator", "") and "題" in ref.get("locator", "") for ref in refs), "item/page locators and provenance state"),
        (len({ref.get("url") for ref in refs}) == 3, "three distinct sources per question"),
    ]
    for passed, label in checks:
        if not passed:
            failures.append({"index": i, "error": label})
    strategies.append(data.get("solutionStrategy", ""))
    steps.extend(data.get("solutionSteps", []))
    source_urls.update(ref.get("url") for ref in refs)

if len(set(strategies)) != 10:
    failures.append({"error": "strategies must be unique"})
if len(steps) != 50 or len(set(steps)) != 50:
    failures.append({"error": "all 50 explanation steps must be distinct"})
if key_counts != Counter({"A": 2, "B": 3, "C": 3, "D": 2}):
    failures.append({"error": f"answer distribution is {dict(key_counts)}"})

report = {
    "unit": "5-Ⅳ-9", "checked": 10, "passed": 0 if failures else 10,
    "answerDistribution": dict(sorted(key_counts.items())),
    "uniqueStrategies": len(set(strategies)), "uniqueDetailedSteps": len(set(steps)),
    "publicSources": len(source_urls), "failures": failures,
    "status": "pass" if not failures else "fail",
    "notes": "Ten original announcement/broadcast note-comprehension items; exact key-to-text and key-in-solution checks, distinct Chinese strategies and 50 detailed steps, three item/page-located official public-exam pattern-only refs each. Items remain draft.",
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
