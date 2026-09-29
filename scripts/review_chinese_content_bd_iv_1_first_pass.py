#!/usr/bin/env python3
"""First-pass structural and unit-specific review for Bd-IV-1 questions."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/chinese").glob("question-chinese-content-bd-iv-1-*.json"))
assert len(paths) == 10, f"expected 10 questions, got {len(paths)}"
items = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
assert len({x["id"] for x in items}) == 10
assert all(x["lessonId"] == "lesson-chinese-content-bd-iv-1" for x in items)
assert all(x["knowledgeIds"] == ["kg-chinese-content-bd-iv-1"] for x in items)
assert all(x["reviewStatus"] == "draft" for x in items)
assert all(x["answer"]["value"] in {o["id"] for o in x["options"]} for x in items)
assert all(len(x["solutionSteps"]) == 5 for x in items)
assert all(len(x["examPatternRefs"]) == 3 for x in items)
assert len({x["prompt"] for x in items}) == 10
assert len({tuple(x["solutionSteps"]) for x in items}) == 10
answers = {letter: sum(x["answer"]["value"] == letter for x in items) for letter in "ABCD"}
print(json.dumps({"status": "pass", "unit": "Bd-Ⅳ-1：事實理論為論據達說服建構批判", "questions": 10, "answers": answers, "reviewStatus": "draft"}, ensure_ascii=False))
