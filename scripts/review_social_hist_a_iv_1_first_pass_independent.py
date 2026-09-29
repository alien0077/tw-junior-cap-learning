#!/usr/bin/env python3
"""First-pass review for the Hist A-IV-1 chronology and periodization bank."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions/social").glob("question-social-content-hist-a-iv-1-*.json"))
assert len(files) == 10, len(files)
prompts, step_sets, distribution = [], [], {"A": 0, "B": 0, "C": 0, "D": 0}
for path in files:
    item = json.loads(path.read_text(encoding="utf-8"))
    assert item["reviewStatus"] == "draft"
    assert item["lessonId"] == "lesson-social-content-hist-a-iv-1"
    assert item["knowledgeIds"] == ["kg-social-content-hist-a-iv-1"]
    assert len(item["options"]) == 4
    assert item["answer"]["value"] in {x["id"] for x in item["options"]}
    assert item["answer"]["explanation"] and item["solutionStrategy"]
    assert len(item["solutionSteps"]) == 5 and len(set(item["solutionSteps"])) == 5
    assert len(item["examPatternRefs"]) >= 3
    assert all(x["reuseDecision"] == "pattern-only" and x["status"] == "recorded" for x in item["examPatternRefs"])
    prompts.append(item["prompt"]); step_sets.append(tuple(item["solutionSteps"]))
    distribution[item["answer"]["value"]] += 1
assert len(set(prompts)) == 10 and len(set(step_sets)) == 10
print(f"reviewed {len(files)}/10 independent questions; answerDistribution={distribution}")
