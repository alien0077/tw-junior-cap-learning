#!/usr/bin/env python3
"""First-pass contract review for the Hist Hb root question bank."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = [ROOT / "questions/social" / f"question-social-content-hist-hb-{i}.json" for i in range(1, 11)]
answers = Counter()
seen = set()
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["lessonId"] == "lesson-social-content-hist-hb"
    assert data["knowledgeIds"] == ["kg-social-content-hist-hb"]
    assert len(data["prompt"]) >= 30 and len(data["solutionSteps"]) == 5
    assert data["reviewStatus"] == "draft"
    assert len(data["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" and ref["status"] == "recorded" for ref in data["examPatternRefs"])
    answer = data["answer"]["value"]
    assert answer in "ABCD" and data["options"][ord(answer) - 65]["text"] in data["answer"]["explanation"]
    assert data["prompt"] not in seen
    seen.add(data["prompt"])
    answers[answer] += 1
assert answers == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), answers
print(f"reviewed {len(files)}/{len(files)} independent questions; answerDistribution={dict(sorted(answers.items()))}")
