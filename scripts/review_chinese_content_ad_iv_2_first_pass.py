import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; paths=sorted((ROOT/"questions/chinese").glob("question-chinese-content-ad-iv-2-*.json")); assert len(paths)==10
for p in paths:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]=="lesson-chinese-content-ad-iv-2" and d["reviewStatus"]=="draft"; assert len(d["options"])==4 and d["answer"]["value"] in {x["id"] for x in d["options"]}; assert len(d["solutionSteps"])==5 and len(d["examPatternRefs"])==3; assert all(x["reuseDecision"]=="pattern-only" and x["status"]=="recorded" for x in d["examPatternRefs"]); assert d["provenance"]["origin"]=="original"
report={"unit":"Ad-Ⅳ-2","checked":len(paths),"passed":len(paths),"failures":[],"status":"pass","notes":"每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。"}; (ROOT/"implementation/reports/chinese-content-ad-iv-2-first-pass-review.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps({"status":"pass","unit":"Ad-Ⅳ-2：新詩現代散文現代小說劇本","questions":len(paths),"reviewStatus":"draft"},ensure_ascii=False))
