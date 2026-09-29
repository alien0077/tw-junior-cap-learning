#!/usr/bin/env python3
"""Independent first-pass checks for English 5-IV-1's ten original questions."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {
    1: ("report", "B"), 2: ("light", "C"), 3: ("plant", "D"),
    4: ("match", "A"), 5: ("notice", "B"), 6: ("field", "C"),
    7: ("walk", "D"), 8: ("patient", "A"), 9: ("raise", "C"),
    10: ("record", "B"),
}


def main() -> None:
    rows = []
    prompts = []
    strategies = []
    all_steps = []
    key_counts: Counter[str] = Counter()
    for number, (correct_word, expected_key) in TARGETS.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-1-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft", f"item {number}: must remain draft"
        assert item["answer"]["value"] == expected_key, f"item {number}: answer key changed"
        assert options[expected_key] == correct_word, f"item {number}: key points to wrong word"
        assert item["answer"]["explanation"], f"item {number}: missing answer reasoning"
        assert item["solutionStrategy"], f"item {number}: missing strategy"
        assert len(item["solutionSteps"]) == 5, f"item {number}: expected five steps"
        assert len(set(item["solutionSteps"])) == 5, f"item {number}: repeated steps"
        refs = item["examPatternRefs"]
        assert len(refs) == 3, f"item {number}: expected three public-school sources"
        assert len({ref["url"] for ref in refs}) == 3, f"item {number}: source schools must be distinct"
        assert all(ref["status"] == "recorded" and ref["reuseDecision"] == "pattern-only" for ref in refs), f"item {number}: unresolved or non-pattern source"
        assert all(ref["locatorLevel"] == "page" and "第" in ref["locator"] and "題" in ref["locator"] for ref in refs), f"item {number}: source locator lacks page/item"
        assert item["provenance"]["sourceUrl"] in {ref["url"] for ref in refs}
        assert item["lessonId"] == "lesson-english-performance-5-iv-1"
        rows.append({"id": item["id"], "key": expected_key, "word": correct_word, "sources": len(refs)})
        prompts.append(item["prompt"])
        strategies.append(item["solutionStrategy"])
        all_steps.extend(item["solutionSteps"])
        key_counts[expected_key] += 1

    assert len(set(prompts)) == 10, "duplicate prompt"
    assert len(set(strategies)) == 10, "reused strategy"
    assert len(set(all_steps)) == 50, "reused worked step"
    assert key_counts == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), key_counts
    print(json.dumps({"status": "pass", "reviewed": len(rows), "keys": dict(sorted(key_counts.items())), "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(all_steps)), "recordedPatternOnlyRefs": sum(row["sources"] for row in rows), "reviewStatus": "draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
