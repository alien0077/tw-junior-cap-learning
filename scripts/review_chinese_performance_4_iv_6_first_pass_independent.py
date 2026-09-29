#!/usr/bin/env python3
"""First-pass contract review for Ab-IV-6 handwriting questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/chinese"; KG="kg-chinese-performance-4-iv-6"; LESSON="lesson-chinese-performance-4-iv-6"
files=sorted(OUT.glob("question-chinese-performance-4-iv-6-*.json")); assert len(files)==10
prompts=[]; step_sets=[]; dist={"A":0,"B":0,"C":0,"D":0}
for p in files:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["reviewStatus"]=="draft" and d["lessonId"]==LESSON and d["knowledgeIds"]==[KG]; assert len(d["options"])==4; assert d["answer"]["value"] in {x["id"] for x in d["options"]}; assert d["answer"]["explanation"] and d["solutionStrategy"]; assert len(d["solutionSteps"])==5 and len(set(d["solutionSteps"]))==5; assert len(d["examPatternRefs"])==3 and all(x["reuseDecision"]=="pattern-only" for x in d["examPatternRefs"]); prompts.append(d["prompt"]); step_sets.append(tuple(d["solutionSteps"])); dist[d["answer"]["value"]]+=1
assert len(set(prompts))==10 and len(set(step_sets))==10
print(f"reviewed {len(files)}/10 independent questions; answerDistribution={dist}")
