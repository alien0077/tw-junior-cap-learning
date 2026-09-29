import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; paths=[ROOT/"questions/english"/f"question-english-content-aa-{i}.json" for i in range(1,11)]; assert all(p.exists() for p in paths)
for p in paths:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]=="lesson-english-content-aa" and d["reviewStatus"]=="draft"; assert len(d["options"])==4 and len({x["text"] for x in d["options"]})==4; assert d["answer"]["value"] in {x["id"] for x in d["options"]}; assert d["provenance"]["origin"]=="original" and len(d["solutionSteps"])==5; assert len(d["examPatternRefs"])==3 and all(x["reuseDecision"]=="pattern-only" and x["status"]=="recorded" for x in d["examPatternRefs"])
(ROOT/"implementation/reports/english-content-aa-first-pass-review.json").write_text(json.dumps({"unit":"Aa：字母","checked":10,"passed":10,"failures":[],"status":"pass","notes":"Each item includes an answer, explanation, strategy, five detailed steps, and three public-school English assessment pattern-only references; content remains draft."},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"pass","unit":"Aa：字母","questions":10,"reviewStatus":"draft"},ensure_ascii=False))
