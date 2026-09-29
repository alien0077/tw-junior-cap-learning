#!/usr/bin/env python3
"""Review the independent first pass for Hist Ia root."""
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = [ROOT / "questions/social" / f"question-social-content-hist-ia-{i}.json" for i in range(1, 11)]
answers = Counter(); prompts = set()
for p in files:
    d = json.loads(p.read_text(encoding="utf-8")); assert d["lessonId"] == "lesson-social-content-hist-ia" and d["knowledgeIds"] == ["kg-social-content-hist-ia"]
    assert d["reviewStatus"] == "draft" and len(d["solutionSteps"]) == 5 and len(d["examPatternRefs"]) == 3
    assert all(x["status"] == "recorded" and x["locatorLevel"] == "paper" for x in d["examPatternRefs"])
    a = d["answer"]["value"]; assert d["options"][ord(a)-65]["text"] in d["answer"]["explanation"]
    assert d["prompt"] not in prompts; prompts.add(d["prompt"]); answers[a] += 1
assert answers == Counter({"A": 3, "B": 2, "C": 2, "D": 3}), answers
print(f"reviewed {len(files)}/{len(files)} independent questions; answerDistribution={dict(sorted(answers.items()))}")
