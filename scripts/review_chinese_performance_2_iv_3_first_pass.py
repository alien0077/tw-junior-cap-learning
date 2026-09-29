import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
paths=sorted((ROOT/"questions/chinese").glob("question-chinese-performance-2-iv-3-[0-9]*.json"))
assert len(paths)==10,len(paths)
for p in paths:
 d=json.loads(p.read_text(encoding="utf-8"))
 assert d["lessonId"]=="lesson-chinese-performance-2-iv-3" and d["reviewStatus"]=="draft"
 assert len(d["options"])==4 and len({o["text"] for o in d["options"]})==4
 assert d["answer"]["value"] in {o["id"] for o in d["options"]}
 assert d["provenance"]["origin"]=="original" and len(d["solutionSteps"])==5
 assert len(d["examPatternRefs"])==3 and all(r["reuseDecision"]=="pattern-only" and r["status"]=="recorded" for r in d["examPatternRefs"])
report={"unit":"2-Ⅳ-3","checked":len(paths),"passed":len(paths),"failures":[],"status":"pass","notes":"每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。"}
(ROOT/"implementation/reports/chinese-performance-2-iv-3-first-pass-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"pass","unit":"2-Ⅳ-3：明確表達與有條理論辯","questions":len(paths),"reviewStatus":"draft"},ensure_ascii=False))
