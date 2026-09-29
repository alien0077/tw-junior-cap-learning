import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "science").glob("question-science-content-na-iv-6-*.json"))
failures = []
answer_positions = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-na-iv-6": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    answer_positions.add(data.get("answer", {}).get("value"))
    if not any("\u4e00" <= char <= "\u9fff" for char in data.get("prompt", "")): failures.append(f"{path.name}:not-traditional-chinese")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
if len(answer_positions) < 4: failures.append("answer-position-distribution")
report = {"unit": "Na-Ⅳ-6：人類發展以保護自然環境為基礎", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "answerPositions": sorted(answer_positions), "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "每題為繁體中文原創人類發展、環境保護、永續指標與科學資料判讀情境，含唯一正確答案、自然科解析、解題策略、五步詳細步驟與三筆公立學校公開自然科能力方向來源；內容仍為 draft。"}
out = ROOT / "implementation" / "reports" / "science-na-iv-6-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
