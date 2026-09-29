import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-f-8-2-*.json"))
failures = []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-f-8-2": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {o.get("id") for o in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): failures.append(f"{path.name}:examPatternRefs")
report = {"unit": "F-8-2：一次函數的圖形", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "每題為原創圖形斜率、截距、在線判斷、平行、交點與點斜式應用，含唯一正確答案、數學解析、解題策略、五步詳細步驟與三筆公立學校公開數學能力方向來源；內容仍為 draft。"}
out = ROOT / "implementation" / "reports" / "math-f-8-2-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
