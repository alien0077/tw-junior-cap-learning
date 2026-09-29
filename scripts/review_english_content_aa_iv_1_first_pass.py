#!/usr/bin/env python3
"""First-pass contract review for English Aa-IV-1 rewritten questions."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/english").glob("question-english-content-aa-iv-1-*.json"))
assert len(paths) == 10, len(paths)
prompts, step_sigs, answers = set(), set(), Counter()
for p in paths:
    d = json.loads(p.read_text(encoding="utf-8"))
    assert d["reviewStatus"] == "draft"
    assert d["lessonId"] == "lesson-english-content-aa-iv-1"
    assert d["knowledgeIds"] == ["kg-english-content-aa-iv-1"]
    assert len(d["options"]) == 4
    assert d["answer"]["value"] in {x["id"] for x in d["options"]}
    assert d["answer"]["explanation"] and d["solutionStrategy"]
    assert len(d["solutionSteps"]) == 5
    assert len(d["examPatternRefs"]) == 3
    assert all(x["reuseDecision"] == "pattern-only" for x in d["examPatternRefs"])
    assert d["prompt"] not in prompts
    prompts.add(d["prompt"])
    sig = tuple(d["solutionSteps"])
    assert sig not in step_sigs
    step_sigs.add(sig)
    answers[d["answer"]["value"]] += 1
print(f"first-pass reviewed {len(paths)}/10; answer distribution={dict(sorted(answers.items()))}; refs=3; steps=5; status=draft")
