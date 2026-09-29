import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/english").glob("question-english-performance-6-iv-6-*.json"))
expected = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
expected_answer_fragments = [
    "Today I will explain two safe cycling habits",
    "Article title, author or organization, URL, and access date",
    "Choose the main claim, two supporting details, and one conclusion",
    "Use a permitted image, credit its creator, and include the source",
    "Ask the classmate for permission and agree on what may be shared",
    "Favorite after-school activities: number of students (n=40)",
    "It came from the survey table on slide 3; I can show the source note",
    "Both claims, the evidence each uses, and a cautious conclusion",
    "Which feature was clearest, and what would you improve",
    "Check facts and links, credit images, remove private data, and test the page with a reader",
]
expected_urls = {
    "https://www2.csjh.kh.edu.tw/teach/exam/106%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83/%E9%81%B8%E4%BF%AE%E8%8B%B1%E6%96%87/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E9%81%B8%E4%BF%AE%E8%8B%B1%E6%96%87/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E9%81%B8%E8%8B%B1%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf",
}
failures = []
counts = Counter()
prompts, strategies, steps = set(), set(), []
for index, path in enumerate(paths):
    item = json.loads(path.read_text(encoding="utf-8"))
    question_number = int(path.stem.rsplit("-", 1)[1])
    key = item.get("answer", {}).get("value")
    options = item.get("options", [])
    option_map = {option.get("id"): option.get("text", "") for option in options}
    if key != expected[question_number - 1]: failures.append(f"{path.name}:answer-key")
    if len(options) != 4 or len(option_map) != 4 or not option_map.get(key): failures.append(f"{path.name}:options")
    if expected_answer_fragments[question_number - 1].casefold() not in option_map.get(key, "").casefold():
        failures.append(f"{path.name}:answer-text")
    if item.get("reviewStatus") != "draft": failures.append(f"{path.name}:must-remain-draft")
    if item.get("lessonId") != "lesson-english-performance-6-iv-6": failures.append(f"{path.name}:lesson-link")
    if item.get("answer", {}).get("explanation") != (item.get("solutionSteps") or [None])[-1]:
        failures.append(f"{path.name}:explanation-final-step")
    current_steps = item.get("solutionSteps", [])
    if len(current_steps) != 5 or any(not str(step).strip() for step in current_steps): failures.append(f"{path.name}:five-steps")
    if current_steps and key not in current_steps[-1]: failures.append(f"{path.name}:final-answer-key")
    if len(current_steps) == 5:
        elimination_keys = set(re.findall(r"\b[A-D]\b", current_steps[-2]))
        expected_distractors = set("ABCD") - {key}
        if elimination_keys != expected_distractors:
            failures.append(f"{path.name}:distractor-keys:{sorted(elimination_keys)}")
    refs = item.get("examPatternRefs", [])
    if len(refs) != 3 or {ref.get("url") for ref in refs} != expected_urls: failures.append(f"{path.name}:source-set")
    for ref in refs:
        if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only": failures.append(f"{path.name}:source-status")
        if not ref.get("locator") or ref.get("locatorLevel") not in {"page", "item"}: failures.append(f"{path.name}:source-locator")
    if any("bhjh.ntpc.edu.tw" in ref.get("url", "") for ref in refs): failures.append(f"{path.name}:unverified-index")
    counts[key] += 1
    prompts.add(item.get("prompt"))
    strategies.add(item.get("solutionStrategy"))
    steps.extend(current_steps)

if len(paths) != 10: failures.append(f"question-count:{len(paths)}")
if len(prompts) != 10: failures.append("duplicate-or-empty-prompts")
if len(strategies) != 10: failures.append("duplicate-or-empty-strategies")
if len(steps) != 50 or len(set(steps)) != 50: failures.append("duplicate-or-missing-solution-steps")
if counts != Counter({"A": 3, "B": 3, "C": 2, "D": 2}): failures.append(f"answer-distribution:{dict(counts)}")
report = {
    "unit": "6-Ⅳ-6：運用網路或課外資源分享",
    "checked": len(paths),
    "passed": len(paths) - len(failures),
    "failures": failures,
    "answerDistribution": dict(counts),
    "distinctSourceUrls": len(expected_urls),
    "distinctStrategies": len(strategies),
    "uniqueSolutionSteps": len(set(steps)),
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "notes": "核對選項與答案鍵、繁中五步詳解、三份有頁題定位的公校英文試題pattern-only來源及draft狀態；未複製原卷內容，不安排Terra審查。",
}
out = ROOT / "implementation/reports/english-performance-6-iv-6-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
