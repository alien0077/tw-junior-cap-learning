#!/usr/bin/env python3
"""First-pass contract review for Chinese classical word meaning."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
paths=[ROOT/"questions/chinese"/f"question-chinese-classical-word-meaning-{i}.json" for i in range(1,11)]
prompts,steps,answers=set(),set(),Counter()
for p in paths:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["reviewStatus"]=="draft" and d["lessonId"]=="lesson-chinese-classical-word-meaning"; assert d["knowledgeIds"]==["kg-chinese-content-ab-iv-6"] and len(d["options"])==4; assert d["answer"]["value"] in {x["id"] for x in d["options"]}; assert d["answer"]["explanation"] and d["solutionStrategy"] and len(d["solutionSteps"])==5; assert len(d["examPatternRefs"])==3 and all(x["reuseDecision"]=="pattern-only" for x in d["examPatternRefs"]); assert d["prompt"] not in prompts; prompts.add(d["prompt"]); s=tuple(d["solutionSteps"]); assert s not in steps; steps.add(s); answers[d["answer"]["value"]]+=1
print(f"first-pass reviewed {len(paths)}/10; answer distribution={dict(sorted(answers.items()))}; refs=3; steps=5; status=draft")
