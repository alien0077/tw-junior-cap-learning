import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "english").glob("question-english-performance-4-iv-4-*.json"))
expected = {1: "B", 2: "C", 3: "D", 4: "A", 5: "B", 6: "C", 7: "D", 8: "D", 9: "B", 10: "C"}
failures = []
answers = Counter()
urls = set()
prompts = set()
strategies = set()

for p in paths:
    d = json.loads(p.read_text())
    number = int(p.stem.rsplit("-", 1)[1])
    prefix = p.name
    if d.get("lessonId") != "lesson-english-performance-4-iv-4": failures.append(f"{prefix}:lessonId")
    if d.get("reviewStatus") != "draft": failures.append(f"{prefix}:reviewStatus")
    options = d.get("options", [])
    ids = [o.get("id") for o in options]
    if len(ids) != 4 or len(set(ids)) != 4 or set(ids) != {"A", "B", "C", "D"}: failures.append(f"{prefix}:options")
    actual = d.get("answer", {}).get("value")
    if actual != expected.get(number): failures.append(f"{prefix}:answer:{actual}")
    answers[actual] += 1
    if len(d.get("answer", {}).get("explanation", "")) < 90: failures.append(f"{prefix}:explanation")
    if len(d.get("solutionStrategy", "")) < 24: failures.append(f"{prefix}:strategy")
    strategies.add(d.get("solutionStrategy", ""))
    steps = d.get("solutionSteps", [])
    if len(steps) != 5 or any(len(step) < 14 for step in steps): failures.append(f"{prefix}:five-detailed-steps")
    prompt = d.get("prompt", "")
    if len(prompt) < 80 or prompt in prompts: failures.append(f"{prefix}:prompt")
    prompts.add(prompt)
    refs = d.get("examPatternRefs", [])
    if len(refs) != 3: failures.append(f"{prefix}:reference-count")
    for ref in refs:
        urls.add(ref.get("url", ""))
        locator = ref.get("locator", "")
        if (
            ref.get("reuseDecision") != "pattern-only"
            or ref.get("status") != "recorded"
            or ref.get("locatorLevel") != "item"
            or "PDF第" not in locator
            or "第" not in locator.split("PDF第", 1)[-1]
            or not ref.get("url", "").startswith("https://")
        ):
            failures.append(f"{prefix}:item-level-public-exam-reference")
    if d.get("provenance", {}).get("origin") != "original": failures.append(f"{prefix}:origin")

report = {
    "unit": "4-Ⅳ-4：填簡單表格",
    "checked": len(paths),
    "passed": len(paths) - len(failures),
    "failures": failures,
    "status": "pass" if len(paths) == 10 and not failures and len(urls) >= 3 and len(strategies) == 10 else "fail",
    "answerPositionCounts": dict(sorted(answers.items())),
    "publicExamUrls": len(urls),
    "criteria": ["independently authored table/form prompts and options", "fixed answer-key verification", "field-specific explanation", "distinct strategy and five worked steps", "three exact page/item public exam pattern-only refs per question", "draft status preserved"],
    "scopeNote": "AI first-pass only; not teacher review, publisher-version fusion, copyright clearance, Terra review, or publication approval.",
}
out = ROOT / "implementation" / "reports" / "english-performance-4-iv-4-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
