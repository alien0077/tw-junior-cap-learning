import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = [p for p in (ROOT / "questions/science").glob("question-science-content-ing-iv-3-*.json") if re.fullmatch(r"question-science-content-ing-iv-3-\d+\.json", p.name)]
files.sort(key=lambda p: int(re.search(r"-(\d+)\.json$", p.name).group(1)))
expected = "ABCDBCDACB"
failures = []
for i, path in enumerate(files, 1):
    q = json.loads(path.read_text())
    if q.get("answer", {}).get("value") != expected[i - 1] or len(q.get("solutionSteps", [])) != 5:
        failures.append(path.name)
report = {"unit": "INg-Ⅳ-3", "checked": len(files), "passed": len(files) - len(failures), "failures": failures, "status": "pass" if len(files) == 10 and not failures else "fail"}
(ROOT / "implementation/reports/science-ing-iv-3-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
