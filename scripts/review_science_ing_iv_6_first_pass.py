import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = [p for p in (ROOT / "questions/science").glob("question-science-content-ing-iv-6-*.json") if re.fullmatch(r"question-science-content-ing-iv-6-\d+\.json", p.name)]
files.sort(key=lambda p: int(re.search(r"-(\d+)\.json$", p.name).group(1)))
expected = "ABCDBCDACB"
bad = []
for i, path in enumerate(files):
    q = json.loads(path.read_text())
    if q.get("answer", {}).get("value") != expected[i] or len(q.get("solutionSteps", [])) != 5:
        bad.append(path.name)
report = {"unit": "INg-Ⅳ-6", "checked": len(files), "passed": len(files) - len(bad), "failures": bad, "status": "pass" if len(files) == 10 and not bad else "fail"}
(ROOT / "implementation/reports/science-ing-iv-6-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
