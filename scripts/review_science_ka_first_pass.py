import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = [p for p in sorted(ROOT.joinpath("questions/science").glob("question-science-content-ka-*.json")) if re.fullmatch(r"question-science-content-ka-\d+\.json", p.name)]
failures = []
for p in files:
    d = json.loads(p.read_text())
    if len(d.get("options", [])) != 4 or d.get("answer", {}).get("value") not in {"A", "B", "C", "D"}: failures.append(p.name)
    if len(d.get("solutionSteps", [])) != 5 or not d.get("solutionStrategy"): failures.append(p.name + ":solution")
    if d.get("reviewStatus") != "draft" or d.get("knowledgeIds") != ["kg-science-content-ka"]: failures.append(p.name + ":metadata")
report = {"unit": "Ka", "checked": len(files), "passed": len(files) if not failures else 0, "failures": failures, "status": "pass" if not failures and len(files) == 10 else "fail"}
(ROOT / "implementation/reports/science-ka-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
