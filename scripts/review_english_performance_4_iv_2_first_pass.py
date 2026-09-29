import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
paths=sorted((ROOT/"questions"/"english").glob("question-english-performance-4-iv-2-*.json"))
failures=[]
strategies=[]
step_sequences=[]
answers=[]
institutions=set()
for p in paths:
 d=json.loads(p.read_text())
 if d.get("lessonId")!="lesson-english-performance-4-iv-2": failures.append(f"{p.name}:lessonId")
 if d.get("reviewStatus")!="draft": failures.append(f"{p.name}:reviewStatus")
 ids={o.get("id") for o in d.get("options",[])}
 if len(ids)!=4 or d.get("answer",{}).get("value") not in ids: failures.append(f"{p.name}:options-answer")
 if d.get("provenance",{}).get("origin")!="original": failures.append(f"{p.name}:origin")
 if len(d.get("solutionSteps",[]))!=5: failures.append(f"{p.name}:solutionSteps")
 if len(d.get("answer",{}).get("explanation",""))<75: failures.append(f"{p.name}:answer-explanation-too-short")
 if any(len(step)<18 for step in d.get("solutionSteps",[])): failures.append(f"{p.name}:step-too-short")
 strategies.append(d.get("solutionStrategy"))
 step_sequences.append(tuple(d.get("solutionSteps",[])))
 answers.append(d.get("answer",{}).get("value"))
 refs=d.get("examPatternRefs",[])
 if len(refs)!=3 or any(r.get("reuseDecision")!="pattern-only" or r.get("status")!="recorded" for r in refs): failures.append(f"{p.name}:examPatternRefs")
 for ref in refs:
  if not ref.get("locator") or not ref.get("observedPattern") or "PDF第" not in ref.get("locator","") or "題" not in ref.get("locator",""):
   failures.append(f"{p.name}:source-locator")
  institutions.add(ref.get("title", "").split("國中")[0])
if len(set(strategies))!=10: failures.append("strategies-not-individual")
if len(set(step_sequences))!=10: failures.append("steps-not-individual")
if len(set(answers))<4: failures.append("answer-position-distribution")
report={"unit":"4-Ⅳ-2：依圖示圖表寫句子","checked":len(paths),"passed":len(paths)-len(failures),"failures":failures,"status":"pass" if len(paths)==10 and not failures else "fail","sourceInstitutions":sorted(institutions),"notes":"逐題檢查唯一答案、充分解析、專屬策略、五步詳解、3筆含PDF頁碼／題號的公校試題pattern-only來源及draft狀態；不代表完整內容／版權審查已完成。"}
out=ROOT/"implementation"/"reports"/"english-performance-4-iv-2-first-pass-review.json"
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(report,ensure_ascii=False))
