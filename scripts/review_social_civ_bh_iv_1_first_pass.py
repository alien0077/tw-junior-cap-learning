import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];files=sorted((ROOT/"questions/social").glob("question-social-content-civ-bh-iv-1-*.json"));failures=[]
for p in files:
 d=json.loads(p.read_text(encoding="utf-8"));ids={x.get("id") for x in d.get("options",[])};refs=d.get("examPatternRefs",[])
 checks=[len(d.get("options",[]))==4,d.get("answer",{}).get("value") in ids,bool(d.get("answer",{}).get("explanation")),bool(d.get("solutionStrategy")),len(d.get("solutionSteps",[]))==5,d.get("reviewStatus")=="draft",d.get("lessonId")=="lesson-social-content-civ-bh-iv-1",len(refs)==3,all(r.get("status")=="recorded" and r.get("reuseDecision")=="pattern-only" for r in refs)]
 if not all(checks):failures.append(p.name)
result={"unit":"公 Bh-Ⅳ-1","checked":len(files),"passed":len(files)-len(failures),"failures":failures,"status":"pass" if len(files)==10 and not failures else "fail","notes":"每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。"}
(ROOT/"implementation/reports/social-civ-bh-iv-1-first-pass-review.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,ensure_ascii=False))
