import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "english").glob("question-english-performance-5-iv-6-*.json"))
expected_answers = {
    1: ("B", "Mia said that she was tired."),
    2: ("C", "Ben said that he would call me the next day."),
    3: ("D", "Lena said that she had finished her project two days before."),
    4: ("A", "Tom asked me to close the door."),
    5: ("B", "Sara asked me if I was ready."),
    6: ("D", "Kai said that they were meeting at the station that night."),
    7: ("C", "The teacher told students not to run in the hall."),
    8: ("A", "Nora said that she could help with the boxes."),
    9: ("D", "David said that the book was his."),
    10: ("B", "Amy asked me where I had put her keys."),
}
dawan_exam = "https://www.dwm.kh.edu.tw/upload/344/104_64184/105-2-2%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf"
dawan_answer = "https://www.dwm.kh.edu.tw/upload/344/104_64186/111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A7%A3%E7%AD%94%28%E4%BD%B3%E9%9F%B3%29.pdf"
guochang = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_4.pdf"
dashe = "https://www.dam.kh.edu.tw/upload/68/101_28414/107-1-1%E4%BA%8C%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E8%A9%95%E9%87%8F%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf"
expected_pairs = {
    "indirect-question": {(dawan_exam, "第2頁第25題"), (dawan_exam, "第2頁第21題"), (dawan_answer, "第4頁第六大題第2、3題")},
    "request-command": {(guochang, "第3頁第20題"), (guochang, "第3頁第22題"), (dawan_exam, "第2頁第29題")},
    "reported-statement": {(dawan_exam, "第2頁第29題"), (dawan_answer, "第4頁第六大題第2、3題"), (guochang, "第3頁第20題")},
    "reported-possession": {(dawan_exam, "第2頁第29題"), (dashe, "第1頁第10題"), (guochang, "第3頁第20題")},
}
failures, keys, prompts, strategies, all_steps = [], Counter(), [], [], []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    number = int(path.stem.rsplit("-", 1)[1])
    if data.get("lessonId") != "lesson-english-performance-5-iv-6": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if "Terra" in data.get("provenance", {}).get("authoringNote", ""): failures.append(f"{path.name}:Terra-conflict")
    options = {option.get("id"): option.get("text") for option in data.get("options", [])}
    key, expected_text = expected_answers[number]
    if set(options) != {"A", "B", "C", "D"}: failures.append(f"{path.name}:four-options")
    if data.get("answer", {}).get("value") != key or options.get(key) != expected_text: failures.append(f"{path.name}:answer-mapping")
    if not data.get("answer", {}).get("explanation") or len(data.get("answer", {}).get("explanation", "")) < 45: failures.append(f"{path.name}:explanation")
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(len(step) < 12 for step in steps): failures.append(f"{path.name}:five-detailed-steps")
    if len(data.get("solutionStrategy", "")) < 15: failures.append(f"{path.name}:strategy")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3: failures.append(f"{path.name}:three-refs")
    if any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") != "item" for ref in refs): failures.append(f"{path.name}:source-status-or-locator")
    pairs = {(ref.get("url"), ref.get("locator")) for ref in refs}
    allowed = expected_pairs["indirect-question"] if number in {5, 10} else expected_pairs["request-command"] if number in {4, 7, 8} else expected_pairs["reported-possession"] if number == 9 else expected_pairs["reported-statement"]
    if len(pairs) != 3 or not pairs.issubset(allowed): failures.append(f"{path.name}:source-item-mapping")
    if any("原卷句子" not in ref.get("observedPattern", "") for ref in refs): failures.append(f"{path.name}:pattern-only-disclosure")
    keys[key] += 1
    prompts.append(data.get("prompt", ""))
    strategies.append(data.get("solutionStrategy", ""))
    all_steps.extend(steps)
if len(paths) != 10: failures.append("question-count")
if len(set(prompts)) != 10: failures.append("duplicate-prompts")
if len(set(strategies)) != 10: failures.append("duplicate-strategies")
if len(all_steps) != 50 or len(set(all_steps)) != 50: failures.append("duplicate-or-missing-steps")
if keys != Counter({"A": 2, "B": 3, "C": 2, "D": 3}): failures.append("answer-distribution")
report = {"unit": "5-Ⅳ-6：轉述簡短對話", "checked": len(paths), "passed": len(paths) if not failures else 0, "answerDistribution": dict(sorted(keys.items())), "sourceRefs": sum(len(json.loads(path.read_text(encoding="utf-8"))["examPatternRefs"]) for path in paths), "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(all_steps)), "failures": failures, "status": "pass" if not failures else "fail", "notes": "逐題核對答案鍵與正解字串、五步詳解、答案分布、三筆公校逐題定位及 pattern-only 說明；題目仍為 draft。"}
out = ROOT / "implementation" / "reports" / "english-performance-5-iv-6-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
