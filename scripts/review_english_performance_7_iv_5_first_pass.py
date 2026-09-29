"""Strict first-pass checks for the independently authored 7-IV-5 item set."""
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-7-iv-5-first-pass-review.json"
EXPECTED = ["B", "A", "C", "D", "B", "C", "A", "C", "B", "D"]
SCHOOLS = {"國昌國民中學", "宜昌國民中學", "大灣國民中學"}
failures = []
steps = []
strategies = []
answers = Counter()
source_urls = set()
for number, answer_key in enumerate(EXPECTED, 1):
    path = OUT / f"question-english-performance-7-iv-5-{number}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append({"item": number, "check": "json", "detail": str(exc)})
        continue
    options = data.get("options", [])
    option_ids = [option.get("id") for option in options]
    answer = data.get("answer", {})
    if data.get("id") != f"question-english-performance-7-iv-5-{number}":
        failures.append({"item": number, "check": "id"})
    if data.get("lessonId") != "lesson-english-performance-7-iv-5":
        failures.append({"item": number, "check": "lessonId"})
    if data.get("reviewStatus") != "draft":
        failures.append({"item": number, "check": "draft-gate"})
    if len(options) != 4 or set(option_ids) != set("ABCD") or len({o.get("text") for o in options}) != 4:
        failures.append({"item": number, "check": "four-distinct-options"})
    if answer.get("value") != answer_key:
        failures.append({"item": number, "check": "answer-key", "expected": answer_key, "actual": answer.get("value")})
    answers[answer.get("value")] += 1
    if len(re.findall(r"[\u4e00-\u9fff]", answer.get("explanation", ""))) < 18:
        failures.append({"item": number, "check": "substantive-traditional-chinese-explanation"})
    if len(re.findall(r"[\u4e00-\u9fff]", data.get("solutionStrategy", ""))) < 12:
        failures.append({"item": number, "check": "unit-specific-chinese-strategy"})
    strategies.append(data.get("solutionStrategy", ""))
    if len(data.get("solutionSteps", [])) != 5 or any(len(re.findall(r"[\u4e00-\u9fff]", s)) < 12 for s in data.get("solutionSteps", [])):
        failures.append({"item": number, "check": "five-detailed-chinese-steps"})
    steps.extend(data.get("solutionSteps", []))
    if not data.get("prompt") or len({o.get("text", "") for o in options}) != 4:
        failures.append({"item": number, "check": "original-item-content"})
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3:
        failures.append({"item": number, "check": "three-public-school-exam-refs"})
    found_schools = set()
    for ref in refs:
        title = ref.get("title", "")
        found_schools.update(school for school in SCHOOLS if school in title)
        source_urls.add(ref.get("url"))
        if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only":
            failures.append({"item": number, "check": "recorded-pattern-only-ref"})
        if ref.get("locatorLevel") != "item" or not re.search(r"第\s*\d+\s*頁.*第\s*\d+(?:至\s*\d+)?\s*題", ref.get("locator", "")):
            failures.append({"item": number, "check": "page-and-item-locator", "locator": ref.get("locator")})
        if ref.get("subject") != "english" or not ref.get("observedPattern"):
            failures.append({"item": number, "check": "source-subject-and-observed-pattern"})
    if found_schools != SCHOOLS:
        failures.append({"item": number, "check": "three-distinct-public-schools", "schools": sorted(found_schools)})

if answers != Counter({"A": 2, "B": 3, "C": 3, "D": 2}):
    failures.append({"check": "balanced-answer-distribution", "actual": dict(answers)})
if len(strategies) != 10 or len(set(strategies)) != 10:
    failures.append({"check": "ten-distinct-strategies"})
if len(steps) != 50 or len(set(steps)) != 50:
    failures.append({"check": "fifty-distinct-detailed-steps", "count": len(steps), "unique": len(set(steps))})

registry = json.loads((ROOT / "data/public-exam-sources.json").read_text(encoding="utf-8"))
registered = {source.get("questionUrl") for source in registry.get("sources", [])}
catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
catalogued = {source.get("url") for source in catalog.get("sources", [])}
for url in source_urls:
    if url not in registered or url not in catalogued:
        failures.append({"check": "source-registered-and-catalogued", "url": url})

report = {
    "unit": "7-Ⅳ-5",
    "checked": 10,
    "passed": 0 if failures else 10,
    "answerKey": EXPECTED,
    "answerDistribution": dict(sorted(answers.items())),
    "uniqueStrategies": len(set(strategies)),
    "uniqueDetailedSteps": len(set(steps)),
    "distinctPublicSchoolsPerItem": 3,
    "sourceUrls": len(source_urls),
    "failures": failures,
    "status": "pass" if not failures else "fail",
    "reviewScope": "answer-key correspondence, Chinese explanations/strategies/steps, uniqueness, exact page+item public-school pattern references, registry/catalog presence, and draft status; not textbook fusion or release approval",
    "reviewedAt": date.today().isoformat(),
}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
if failures:
    raise SystemExit(1)
