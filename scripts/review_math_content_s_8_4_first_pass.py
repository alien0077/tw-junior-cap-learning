import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-s-8-4-*.json"))
failures = []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-s-8-4": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
report = {"unit": "S-8-4：全等圖形", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "每題為原創剛體移動、SSS／SAS／ASA、對應頂點與邊、全等／相似區分、SSA 與 AAA 限制，含唯一正確答案、解析、解題策略、五步詳細步驟與三筆公立學校公開數學試題能力方向來源；內容仍為 draft。"}
out = ROOT / "implementation" / "reports" / "math-s-8-4-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
