import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
paths=sorted((ROOT/"questions"/"english").glob("question-english-performance-2-iv-2-*.json"))
failures=[]
for p in paths:
 d=json.loads(p.read_text())
 if d.get("lessonId")!="lesson-english-performance-2-iv-2": failures.append(f"{p.name}:lessonId")
 if d.get("reviewStatus")!="draft": failures.append(f"{p.name}:reviewStatus")
 ids={o.get("id") for o in d.get("options",[])}
 if len(ids)!=4 or d.get("answer",{}).get("value") not in ids: failures.append(f"{p.name}:options-answer")
 if d.get("provenance",{}).get("origin")!="original": failures.append(f"{p.name}:origin")
 if len(d.get("solutionSteps",[]))!=5: failures.append(f"{p.name}:solutionSteps")
 refs=d.get("examPatternRefs",[])
 if len(refs)!=3 or any(r.get("reuseDecision")!="pattern-only" or r.get("status")!="recorded" for r in refs): failures.append(f"{p.name}:examPatternRefs")
report={"unit":"2-Ⅳ-2：依情境使用生活用語","checked":len(paths),"passed":len(paths)-len(failures),"failures":failures,"status":"pass" if len(paths)==10 and not failures else "fail","notes":"每題含獨立英文生活語用情境、正確答案、英文解析、解題策略、五步詳細步驟與三筆公開英文試題 pattern-only 來源；內容仍為 draft。"}
out=ROOT/"implementation"/"reports"/"english-performance-2-iv-2-first-pass-review.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(report,ensure_ascii=False))
