import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
files=[p for p in (ROOT/"questions/science").glob("question-science-content-md-iv-4-*.json") if re.fullmatch(r"question-science-content-md-iv-4-\d+\.json",p.name)]
failures=[]
for p in files:
    x=json.loads(p.read_text())
    if len(x.get("options",[]))!=4 or x.get("answer",{}).get("value") not in "ABCD" or len(x.get("solutionSteps",[]))!=5 or len(x.get("examPatternRefs",[]))<3: failures.append(p.name)
report={"unit":"Md-Ⅳ-4","checked":len(files),"passed":len(files) if len(files)==10 and not failures else 0,"failures":failures,"status":"pass" if len(files)==10 and not failures else "fail"}
(ROOT/"implementation/reports/science-md-iv-4-first-pass-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(report,ensure_ascii=False))
