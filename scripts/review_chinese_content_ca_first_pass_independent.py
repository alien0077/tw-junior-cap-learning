#!/usr/bin/env python3
"""First-pass contract review for independent Chinese CA questions."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
answers = Counter()
prompts = set()
step_sets = set()

for i in range(1, 11):
    path = ROOT / "questions/chinese" / f"question-chinese-content-ca-{i}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["reviewStatus"] == "draft"
    assert data["lessonId"] == "lesson-chinese-content-ca"
    assert data["knowledgeIds"] == ["kg-chinese-content-ca"]
    assert len(data["options"]) == 4
    assert data["answer"]["value"] in {option["id"] for option in data["options"]}
    assert data["answer"]["explanation"]
    assert data["solutionStrategy"] and len(data["solutionSteps"]) == 5
    assert len(data["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" for ref in data["examPatternRefs"])
    assert data["prompt"] not in prompts
    assert tuple(data["solutionSteps"]) not in step_sets
    prompts.add(data["prompt"])
    step_sets.add(tuple(data["solutionSteps"]))
    answers[data["answer"]["value"]] += 1

print(
    "first-pass reviewed 10/10; "
    f"answer distribution={dict(sorted(answers.items()))}; refs=3; steps=5; status=draft"
)
