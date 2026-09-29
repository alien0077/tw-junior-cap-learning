import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=sorted((ROOT/"questions/social").glob("question-social-content-hist-kb-iv-2-*.json")); failures=[]
for p in files:
 d=json.loads(p.read_text(encoding="utf-8")); opts=d.get("options",[]); refs=d.get("examPatternRefs",[])
 if (len(opts)!=4 or d.get("answer",{}).get("value") not in {o.get("id") for o in opts} or not d.get("answer",{}).get("explanation") or not d.get("solutionStrategy") or len(d.get("solutionSteps",[]))!=5 or len(refs)<3 or any(r.get("status")!="recorded" or r.get("reuseDecision")!="pattern-only" for r in refs) or d.get("reviewStatus")!="draft" or d.get("lessonId")!="lesson-social-content-hist-kb-iv-2"): failures.append(p.name)
report={"unit":"歷 Kb-Ⅳ-2","checked":len(files),"passed":len(files)-len(failures),"failures":failures,"status":"pass" if len(files)==10 and not failures else "fail","sourceCountPerQuestion":3,"note":"第一輪逐題契約檢查；題目以公立學校公開試題的能力與資料型態 pattern-only 參照，重新設計擴張資源、殖民行政、身分分類、移民勞動、抵抗協商、戰爭日常、帝國外交、殖民教育、戰爭記憶與多重證據情境，未複製原題。"}
(ROOT/"implementation/reports/social-hist-kb-iv-2-first-pass-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(report,ensure_ascii=False)); raise SystemExit(0 if report["status"]=="pass" else 1)
