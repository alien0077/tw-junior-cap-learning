import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = [p for p in (ROOT / "questions/science").glob("question-science-content-mc-iv-1-*.json") if re.fullmatch(r"question-science-content-mc-iv-1-\d+\.json", p.name)]
bad = []
for path in files:
    item = json.loads(path.read_text())
    if len(item.get("options", [])) != 4 or item.get("answer", {}).get("value") not in "ABCD" or len(item.get("solutionSteps", [])) != 5 or len(item.get("examPatternRefs", [])) < 3 or item.get("reviewStatus") != "draft": bad.append(path.name)
report = {"unit": "Mc-Ⅳ-1", "checked": len(files), "passed": len(files) if len(files) == 10 and not bad else 0, "failures": bad, "status": "pass" if len(files) == 10 and not bad else "fail"}
(ROOT / "implementation/reports/science-mc-iv-1-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
