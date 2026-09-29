#!/usr/bin/env python3
"""First-pass review for Hist D-IV-2 inquiry/exhibition questions."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=sorted((ROOT/"questions/social").glob("question-social-content-hist-d-iv-2-*.json")); assert len(files)==10
prompts=[]; step_sets=[]; dist={"A":0,"B":0,"C":0,"D":0}
for p in files:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["reviewStatus"]=="draft" and d["lessonId"]=="lesson-social-content-hist-d-iv-2" and d["knowledgeIds"]==["kg-social-content-hist-d-iv-2"]; assert len(d["options"])==4; assert d["answer"]["value"] in {x["id"] for x in d["options"]}; assert d["answer"]["explanation"] and d["solutionStrategy"]; assert len(d["solutionSteps"])==5 and len(set(d["solutionSteps"]))==5; assert len(d["examPatternRefs"])>=3 and all(x["status"]=="recorded" and x["reuseDecision"]=="pattern-only" for x in d["examPatternRefs"]); prompts.append(d["prompt"]); step_sets.append(tuple(d["solutionSteps"])); dist[d["answer"]["value"]]+=1
assert len(set(prompts))==10 and len(set(step_sets))==10
print(f"reviewed {len(files)}/10 independent questions; answerDistribution={dist}")
