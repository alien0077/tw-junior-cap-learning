import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=sorted((ROOT/"questions/social").glob("question-social-content-hist-nb-iv-2-*.json")); failures=[]
for p in files:
 d=json.loads(p.read_text(encoding="utf-8")); opts=d.get("options",[]); refs=d.get("examPatternRefs",[])
 if (len(opts)!=4 or d.get("answer",{}).get("value") not in {o.get("id") for o in opts} or not d.get("answer",{}).get("explanation") or not d.get("solutionStrategy") or len(d.get("solutionSteps",[]))!=5 or len(refs)<3 or any(r.get("status")!="recorded" or r.get("reuseDecision")!="pattern-only" for r in refs) or d.get("reviewStatus")!="draft" or d.get("lessonId")!="lesson-social-content-hist-nb-iv-2"): failures.append(p.name)
report={"unit":"歷 Nb-Ⅳ-2","checked":len(files),"passed":len(files)-len(failures),"failures":failures,"status":"pass" if len(files)==10 and not failures else "fail","sourceCountPerQuestion":3,"note":"第一輪逐題契約檢查；題目以公立學校公開試題的能力與資料型態 pattern-only 參照，重新設計基督教時代、教會組織、羅馬與基督教、傳教翻譯、慈善社會、教會王權、十字軍交流、宗教改革、基督教文化與多重史料情境，未複製原題。"}
(ROOT/"implementation/reports/social-hist-nb-iv-2-first-pass-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(report,ensure_ascii=False)); raise SystemExit(0 if report["status"]=="pass" else 1)
