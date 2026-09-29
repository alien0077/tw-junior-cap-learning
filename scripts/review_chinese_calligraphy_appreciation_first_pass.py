#!/usr/bin/env python3
"""First-pass contract review for Chinese calligraphy appreciation."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/chinese" / f"question-chinese-calligraphy-appreciation-{i}.json" for i in range(1, 11)]
prompts, step_sigs, answers = set(), set(), Counter()
for path in paths:
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["reviewStatus"] == "draft" and item["lessonId"] == "lesson-chinese-calligraphy-appreciation"
    assert item["knowledgeIds"] == ["kg-chinese-content-ab-iv-8"] and len(item["options"]) == 4
    assert item["answer"]["value"] in {option["id"] for option in item["options"]}
    assert item["answer"]["explanation"] and item["solutionStrategy"] and len(item["solutionSteps"]) == 5
    assert len(item["examPatternRefs"]) == 3 and all(ref["reuseDecision"] == "pattern-only" for ref in item["examPatternRefs"])
    assert item["prompt"] not in prompts; prompts.add(item["prompt"])
    sig = tuple(item["solutionSteps"]); assert sig not in step_sigs; step_sigs.add(sig)
    answers[item["answer"]["value"]] += 1
print(f"first-pass reviewed {len(paths)}/10; answer distribution={dict(sorted(answers.items()))}; refs=3; steps=5; status=draft")
