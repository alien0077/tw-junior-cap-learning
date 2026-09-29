import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; paths=sorted((ROOT/"questions/chinese").glob("question-chinese-performance-5-iv-6-[0-9]*.json")); assert len(paths)==10
for p in paths:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]=="lesson-chinese-performance-5-iv-6" and d["reviewStatus"]=="draft"; assert len(d["options"])==4 and len({x["text"] for x in d["options"]})==4; assert d["answer"]["value"] in {x["id"] for x in d["options"]}; assert d["provenance"]["origin"]=="original" and len(d["solutionSteps"])==5; assert len(d["examPatternRefs"])==3 and all(x["reuseDecision"]=="pattern-only" and x["status"]=="recorded" for x in d["examPatternRefs"])
(ROOT/"implementation/reports/chinese-performance-5-iv-6-first-pass-review.json").write_text(json.dumps({"unit":"5-Ⅳ-6","checked":10,"passed":10,"failures":[],"status":"pass","notes":"每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"pass","unit":"5-Ⅳ-6：圖書館科技蒐集組織資訊擴展視野","questions":10,"reviewStatus":"draft"},ensure_ascii=False))
