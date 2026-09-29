import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions/english").glob("question-english-performance-7-iv-2-*.json"))
expected = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]
answer_fragments = [
    "carry pollen between flowers",
    "strong wind and rain can make an outdoor event unsafe",
    "the red envelope is a customary way to share good wishes",
    "sun's position changes the angle of light and shadow length",
    "validate payment or entry for the ride",
    "yeast can produce gas while the dough rests, making it rise",
    "rain may discourage cycling, but the chart alone does not prove the cause",
    "revise the prediction toward gardening and keep reading for confirmation",
    "horse travel was slower and the route distance affected delivery time",
    "the examples support the prediction, so keep it provisionally",
]
source_urls = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
    "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
    "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
}
failures = []
keys, prompts, strategies, all_steps = Counter(), set(), set(), []
for path in files:
    number = int(path.stem.rsplit("-", 1)[1])
    item = json.loads(path.read_text(encoding="utf-8"))
    key = item.get("answer", {}).get("value")
    options = item.get("options", [])
    mapping = {option.get("id"): option.get("text", "") for option in options}
    steps = item.get("solutionSteps", [])
    refs = item.get("examPatternRefs", [])
    if key != expected[number - 1]: failures.append(f"{path.name}:answer-key")
    if len(mapping) != 4 or set(mapping) != set("ABCD"): failures.append(f"{path.name}:option-ids")
    if answer_fragments[number - 1].casefold() not in mapping.get(key, "").casefold(): failures.append(f"{path.name}:answer-text")
    if item.get("answer", {}).get("explanation") != (steps or [None])[-1]: failures.append(f"{path.name}:answer-explanation")
    if len(steps) != 5 or any(not str(step).strip() for step in steps): failures.append(f"{path.name}:five-steps")
    if steps and key not in steps[-1]: failures.append(f"{path.name}:final-answer-key")
    if len(steps) == 5 and set(re.findall(r"(?<![A-Za-z])[A-D](?![A-Za-z])", steps[-2])) != set("ABCD") - {key}:
        failures.append(f"{path.name}:distractor-exclusion")
    if item.get("reviewStatus") != "draft": failures.append(f"{path.name}:draft-state")
    if item.get("lessonId") != "lesson-english-performance-7-iv-2": failures.append(f"{path.name}:lesson-link")
    if len(refs) != 3 or {ref.get("url") for ref in refs} != source_urls: failures.append(f"{path.name}:source-set")
    for ref in refs:
        if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only": failures.append(f"{path.name}:source-status")
        if ref.get("locatorLevel") != "page" or not ref.get("locator"): failures.append(f"{path.name}:source-locator")
    if "Terra" in item.get("provenance", {}).get("authoringNote", ""): failures.append(f"{path.name}:terra-note")
    keys[key] += 1
    prompts.add(item.get("prompt"))
    strategies.add(item.get("solutionStrategy"))
    all_steps.extend(steps)

if len(files) != 10: failures.append(f"question-count:{len(files)}")
if len(prompts) != 10: failures.append("duplicate-prompts")
if len(strategies) != 10: failures.append("duplicate-strategies")
if len(all_steps) != 50 or len(set(all_steps)) != 50: failures.append("duplicate-solution-steps")
if keys != Counter({"A": 3, "B": 3, "C": 2, "D": 2}): failures.append(f"answer-distribution:{dict(keys)}")
report = {
    "unit": "7-Ⅳ-2：利用背景知識",
    "checked": len(files),
    "passed": len(files) - len(failures),
    "failures": failures,
    "answerDistribution": dict(keys),
    "distinctSourceUrls": len(source_urls),
    "distinctStrategies": len(strategies),
    "uniqueSolutionSteps": len(set(all_steps)),
    "status": "pass" if len(files) == 10 and not failures else "fail",
    "notes": "逐題檢查答案選項、排除步驟、答案解析、三份精確定位公校試題pattern-only來源與draft狀態。",
}
report_path = ROOT / "implementation/reports/english-performance-7-iv-2-first-pass-review.json"
report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
