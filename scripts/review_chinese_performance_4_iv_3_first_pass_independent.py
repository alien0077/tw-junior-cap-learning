#!/usr/bin/env python3
"""First-pass structural/content-contract review for Ab-IV-3 questions."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/chinese"
KG = "kg-chinese-performance-4-iv-3"
LESSON = "lesson-chinese-performance-4-iv-3"

files = sorted(OUT.glob("question-chinese-performance-4-iv-3-*.json"))
assert len(files) == 10, f"expected 10 questions, got {len(files)}"
prompts = []
step_sets = []
distribution = {"A": 0, "B": 0, "C": 0, "D": 0}
for path in files:
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["reviewStatus"] == "draft"
    assert item["lessonId"] == LESSON
    assert item["knowledgeIds"] == [KG]
    assert len(item["options"]) == 4
    assert item["answer"]["value"] in {option["id"] for option in item["options"]}
    assert item["answer"]["explanation"]
    assert item["solutionStrategy"]
    assert len(item["solutionSteps"]) == 5
    assert len(set(item["solutionSteps"])) == 5
    assert len(item["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" for ref in item["examPatternRefs"])
    prompts.append(item["prompt"])
    step_sets.append(tuple(item["solutionSteps"]))
    distribution[item["answer"]["value"]] += 1
assert len(set(prompts)) == 10
assert len(set(step_sets)) == 10
print(f"reviewed {len(files)}/10 independent questions; answerDistribution={distribution}")
