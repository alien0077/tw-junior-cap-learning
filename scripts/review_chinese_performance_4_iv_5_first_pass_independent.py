#!/usr/bin/env python3
"""First-pass contract review for Ab-IV-5 layout and calligraphy questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
KG = "kg-chinese-performance-4-iv-5"
LESSON = "lesson-chinese-performance-4-iv-5"
files = sorted(OUT.glob("question-chinese-performance-4-iv-5-*.json"))
assert len(files) == 10, len(files)
prompts, steps, distribution = [], [], {"A": 0, "B": 0, "C": 0, "D": 0}
for path in files:
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["reviewStatus"] == "draft"
    assert item["lessonId"] == LESSON and item["knowledgeIds"] == [KG]
    assert len(item["options"]) == 4
    assert item["answer"]["value"] in {x["id"] for x in item["options"]}
    assert item["answer"]["explanation"] and item["solutionStrategy"]
    assert len(item["solutionSteps"]) == 5 and len(set(item["solutionSteps"])) == 5
    assert len(item["examPatternRefs"]) == 3
    assert all(x["reuseDecision"] == "pattern-only" for x in item["examPatternRefs"])
    prompts.append(item["prompt"]); steps.append(tuple(item["solutionSteps"]))
    distribution[item["answer"]["value"]] += 1
assert len(set(prompts)) == 10 and len(set(steps)) == 10
print(f"reviewed {len(files)}/10 independent questions; answerDistribution={distribution}")
