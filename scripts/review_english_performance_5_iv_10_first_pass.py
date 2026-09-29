#!/usr/bin/env python3
"""First-pass answer/source contract review for English 5-IV-10."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {1: ("A", "Patient practice can build skill and help someone else."), 2: ("B", "A student shares an umbrella with a classmate caught in the rain."), 3: ("C", "Find a suitable gift for her brother"), 4: ("D", "He stopped to help the neighbor"), 5: ("A", "From worried to confident"), 6: ("B", "Waiting for the First Leaf"), 7: ("C", "The child discovers an old map under a book."), 8: ("D", "Accepting useful help can make a hard task possible."), 9: ("B", "I think the child is honest because she returned the wallet instead of keeping the money."), 10: ("C", "Children and neighbors repair a sign together, making the park easier to find.")}


def main() -> None:
    key_counts: Counter[str] = Counter()
    prompts, strategies, steps = [], [], []
    for number, (expected_key, expected_text) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-10-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft"
        assert item["answer"]["value"] == expected_key
        assert options[expected_key] == expected_text
        assert item["answer"]["explanation"] and item["solutionStrategy"]
        assert item["answer"]["explanation"].endswith(f"Correct answer: {expected_key} — {expected_text.rstrip('.')}.")
        assert f"答案 {expected_key}" in " ".join(item["solutionSteps"])
        assert len(item["solutionSteps"]) == 5
        refs = item["examPatternRefs"]
        assert len(refs) == 3 and len({ref["url"] for ref in refs}) == 3
        assert all(ref["status"] == "recorded" and ref["reuseDecision"] == "pattern-only" and ref["locatorLevel"] == "page" for ref in refs)
        assert all("第" in ref["locator"] and "題" in ref["locator"] for ref in refs)
        key_counts[expected_key] += 1
        prompts.append(item["prompt"])
        strategies.append(item["solutionStrategy"])
        steps.extend(item["solutionSteps"])
    assert key_counts == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), key_counts
    assert len(set(prompts)) == 10
    assert len(set(strategies)) == 10
    assert len(set(steps)) == 50
    print(json.dumps({"status": "pass", "reviewed": 10, "answerDistribution": dict(sorted(key_counts.items())), "recordedPatternOnlyRefs": 30, "distinctStrategies": 10, "uniqueSteps": 50, "reviewStatus": "draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
