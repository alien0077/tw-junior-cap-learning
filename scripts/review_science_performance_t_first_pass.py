import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
paths = sorted((DATA / "questions" / "science").glob("question-science-performance-t-*.json"))
failures = []
for p in paths:
    d = json.loads(p.read_text())
    if d.get("lessonId") != "lesson-science-performance-t": failures.append(f"{p.name}:lessonId")
    if d.get("reviewStatus") != "draft": failures.append(f"{p.name}:reviewStatus")
    if len(d.get("options", [])) != 4 or len({o.get("id") for o in d.get("options", [])}) != 4: failures.append(f"{p.name}:options")
    if d.get("answer", {}).get("value") not in {o.get("id") for o in d.get("options", [])}: failures.append(f"{p.name}:answer")
    if d.get("provenance", {}).get("origin") != "original": failures.append(f"{p.name}:origin")
    if len(d.get("solutionSteps", [])) != 5: failures.append(f"{p.name}:solutionSteps")
    refs = d.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): failures.append(f"{p.name}:examPatternRefs")
report = {"unit": "探究能力－思考智能（t）", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "status": "pass" if not failures and len(paths) == 10 else "fail", "notes": "每題含獨立探究推理情境、正確答案、解析、策略、五步詳細步驟與三筆公立學校自然科試題 pattern-only 來源；內容仍為 draft。"}
out = DATA / "implementation" / "reports" / "science-performance-t-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
