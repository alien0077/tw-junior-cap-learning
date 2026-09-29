#!/usr/bin/env python3
"""First-pass contract review for independent Ab-IV-3 questions."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; answers=Counter(); prompts=set(); step_sets=set()
for i in range(1,11):
 p=ROOT/"questions/chinese"/f"question-chinese-content-ab-iv-3-{i}.json"; d=json.loads(p.read_text(encoding="utf-8"))
 assert d["reviewStatus"]=="draft" and d["lessonId"]=="lesson-chinese-content-ab-iv-3" and d["knowledgeIds"]==["kg-chinese-content-ab-iv-3"]
 assert len(d["options"])==4 and d["answer"]["value"] in {x["id"] for x in d["options"]} and d["answer"]["explanation"]
 assert d["solutionStrategy"] and len(d["solutionSteps"])==5 and len(d["examPatternRefs"])==3 and all(x["reuseDecision"]=="pattern-only" for x in d["examPatternRefs"])
 assert d["prompt"] not in prompts and tuple(d["solutionSteps"]) not in step_sets; prompts.add(d["prompt"]); step_sets.add(tuple(d["solutionSteps"])); answers[d["answer"]["value"]]+=1
print(f"first-pass reviewed 10/10; answer distribution={dict(sorted(answers.items()))}; refs=3; steps=5; status=draft")
