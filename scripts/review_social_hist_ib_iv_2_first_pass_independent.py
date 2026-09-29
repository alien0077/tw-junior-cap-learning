#!/usr/bin/env python3
"""Review the independent first pass for Hist Ib-IV-2."""
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; files=[ROOT/"questions/social"/f"question-social-content-hist-ib-iv-2-{i}.json" for i in range(1,11)]
c=Counter();seen=set()
for p in files:
 d=json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"]=="lesson-social-content-hist-ib-iv-2" and d["knowledgeIds"]==["kg-social-content-hist-ib-iv-2"]
 assert d["reviewStatus"]=="draft" and len(d["solutionSteps"])==5 and len(d["examPatternRefs"])==3; assert all(x["status"]=="recorded" and x["locatorLevel"]=="paper" for x in d["examPatternRefs"])
 a=d["answer"]["value"]; assert d["options"][ord(a)-65]["text"] in d["answer"]["explanation"]; assert d["prompt"] not in seen;seen.add(d["prompt"]);c[a]+=1
assert c==Counter({"A":2,"B":3,"C":3,"D":2}),c
print(f"reviewed {len(files)}/{len(files)} independent questions; answerDistribution={dict(sorted(c.items()))}")
