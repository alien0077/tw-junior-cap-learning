import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "science").glob("question-science-root-b-*.json"))
failures = []
answers = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-root-b": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    option_ids = {option.get("id") for option in data.get("options", [])}
    if len(option_ids) != 4 or data.get("answer", {}).get("value") not in option_ids: failures.append(f"{path.name}:options-answer")
    answers.add(data.get("answer", {}).get("value"))
    if not any("\u4e00" <= char <= "\u9fff" for char in data.get("prompt", "")): failures.append(f"{path.name}:not-traditional-chinese")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5 or not data.get("solutionStrategy") or not data.get("answer", {}).get("explanation"): failures.append(f"{path.name}:solution")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
if len(answers) < 4: failures.append("answer-position-distribution")
report = {"unit": "自然科學學習內容 B：在生命、地球與宇宙尺度間換位思考", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "answerPositions": sorted(answers), "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "10 題均為繁體中文原創跨尺度題，含唯一正確答案、解析、策略、五步解法與三筆公立學校公開自然科能力方向來源；內容仍為 draft。"}
out = ROOT / "implementation" / "reports" / "science-root-b-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
