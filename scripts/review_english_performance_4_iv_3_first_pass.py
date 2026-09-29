#!/usr/bin/env python3
"""Independent contract review for the authored English 4-IV-3 question set."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_ANSWERS = {1: "C", 2: "B", 3: "B", 4: "A", 5: "D", 6: "C", 7: "B", 8: "D", 9: "C", 10: "A"}
paths = sorted((ROOT / "questions/english").glob("question-english-performance-4-iv-3-*.json"))
failures = []
answers, strategies, step_sets = [], [], []
institutions, urls = set(), set()
for path in paths:
    item = json.loads(path.read_text(encoding="utf-8"))
    number = int(path.stem.rsplit("-", 1)[1])
    labels = [option.get("id") for option in item.get("options", [])]
    texts = [option.get("text", "") for option in item.get("options", [])]
    answer = item.get("answer", {}).get("value")
    if item.get("lessonId") != "lesson-english-performance-4-iv-3": failures.append(f"{path.name}: lessonId")
    if item.get("reviewStatus") != "draft": failures.append(f"{path.name}: status must remain draft")
    if answer != EXPECTED_ANSWERS.get(number): failures.append(f"{path.name}: answer differs from independently checked key")
    if len(labels) != 4 or set(labels) != set("ABCD") or answer not in labels: failures.append(f"{path.name}: answer/choice structure")
    if len(set(texts)) != 4: failures.append(f"{path.name}: duplicate choices")
    if len(item.get("answer", {}).get("explanation", "")) < 75: failures.append(f"{path.name}: insufficient explanation")
    if len(item.get("solutionSteps", [])) != 5 or any(len(step) < 18 for step in item.get("solutionSteps", [])): failures.append(f"{path.name}: needs five detailed steps")
    if len(item.get("examPatternRefs", [])) != 3: failures.append(f"{path.name}: needs three public-exam references")
    for ref in item.get("examPatternRefs", []):
        if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only": failures.append(f"{path.name}: reference not recorded/pattern-only")
        if ref.get("locatorLevel") != "item" or "PDF第" not in ref.get("locator", "") or "題" not in ref.get("locator", ""): failures.append(f"{path.name}: source locator is not item-specific")
        if not ref.get("observedPattern"): failures.append(f"{path.name}: missing observed pattern")
        institutions.add(ref.get("title", ""))
        urls.add(ref.get("url", ""))
    answers.append(answer)
    strategies.append(item.get("solutionStrategy"))
    step_sets.append(tuple(item.get("solutionSteps", [])))

if len(paths) != 10: failures.append(f"expected ten questions, found {len(paths)}")
if len(set(strategies)) != 10: failures.append("strategies are not independently authored")
if len(set(step_sets)) != 10: failures.append("solution steps are not independently authored")
answer_counts = Counter(answers)
if len(answer_counts) != 4 or min(answer_counts.values(), default=0) < 2: failures.append(f"answer positions are not adequately distributed: {dict(answer_counts)}")
if len(urls) < 5 or len(institutions) < 5: failures.append("source set does not represent at least five public schools/exam URLs")

report = {
    "unit": "4-Ⅳ-3：正確書寫格式",
    "checked": len(paths),
    "passed": len(paths) if not failures else max(0, len(paths) - len(failures)),
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "failures": failures,
    "answerPositionCounts": dict(sorted(answer_counts.items())),
    "publicExamUrls": len(urls),
    "sourceTitles": sorted(institutions),
    "criteria": ["original prompts/options", "one keyed answer", "explanation distinguishes distractors", "unique strategy and five worked steps", "three recorded item-level public-school exam references", "draft status preserved"],
    "scopeNote": "AI first-pass question/content review only; not teacher review, textbook-version fusion, copyright clearance, Terra review or publication approval.",
}
out = ROOT / "implementation/reports/english-performance-4-iv-3-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
