#!/usr/bin/env python3
"""First-pass structural and unit-specific review for Be-IV-2 questions."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/chinese").glob("question-chinese-content-be-iv-2-*.json"))
assert len(paths) == 10, f"expected 10 questions, got {len(paths)}"
items = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
assert len({x["id"] for x in items}) == 10
assert all(x["lessonId"] == "lesson-chinese-content-be-iv-2" for x in items)
assert all(x["knowledgeIds"] == ["kg-chinese-content-be-iv-2"] for x in items)
assert all(x["reviewStatus"] == "draft" for x in items)
assert all(x["answer"]["value"] in {o["id"] for o in x["options"]} for x in items)
assert all(len(x["solutionSteps"]) == 5 for x in items)
assert all(len(x["examPatternRefs"]) == 3 for x in items)
assert len({x["prompt"] for x in items}) == 10
assert len({tuple(x["solutionSteps"]) for x in items}) == 10
answers = {letter: sum(x["answer"]["value"] == letter for x in items) for letter in "ABCD"}
print(json.dumps({"status": "pass", "unit": "Be-Ⅳ-2：書信便條對聯等人際溝通", "questions": 10, "answers": answers, "reviewStatus": "draft"}, ensure_ascii=False))
