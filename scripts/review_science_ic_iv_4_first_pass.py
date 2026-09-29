import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = [p for p in (ROOT / "questions/science").glob("question-science-content-ic-iv-4-*.json") if re.fullmatch(r"question-science-content-ic-iv-4-\d+\.json", p.name)]
failures = []
for path in files:
    data = json.loads(path.read_text())
    if len(data.get("options", [])) != 4 or data.get("answer", {}).get("value") not in "ABCD" or len(data.get("solutionSteps", [])) != 5:
        failures.append(path.name)
report = {"unit": "Ic-Ⅳ-4", "checked": len(files), "passed": len(files) if len(files) == 10 and not failures else 0, "failures": failures, "status": "pass" if len(files) == 10 and not failures else "fail"}
(ROOT / "implementation/reports/science-ic-iv-4-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
