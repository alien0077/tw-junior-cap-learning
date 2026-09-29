#!/usr/bin/env python3
"""Review the independent first pass for Hist Ia-IV-1."""
import json
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
files = [ROOT / "questions/social" / f"question-social-content-hist-ia-iv-1-{i}.json" for i in range(1, 11)]
answers = Counter()
prompts = set()
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["lessonId"] == "lesson-social-content-hist-ia-iv-1" and data["knowledgeIds"] == ["kg-social-content-hist-ia-iv-1"]
    assert data["reviewStatus"] == "draft" and len(data["solutionSteps"]) == 5 and len(data["examPatternRefs"]) == 3
    assert all(x["status"] == "recorded" and x["locatorLevel"] == "paper" for x in data["examPatternRefs"])
    answer = data["answer"]["value"]
    assert data["options"][ord(answer) - 65]["text"] in data["answer"]["explanation"]
    assert data["prompt"] not in prompts
    prompts.add(data["prompt"])
    answers[answer] += 1
assert answers == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), answers
print(f"reviewed {len(files)}/{len(files)} independent questions; answerDistribution={dict(sorted(answers.items()))}")
