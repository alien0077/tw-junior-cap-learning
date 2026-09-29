#!/usr/bin/env python3
"""First-pass answers, worked steps, and source locators for English 5-IV-12."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("A", "Coach Lee"), 2: ("B", "To share news about a move"),
    3: ("C", "Warm and cheerful"), 4: ("D", "Fruit"),
    5: ("A", "Say whether the writer can join and respond by Tuesday"),
    6: ("B", "Thank you for asking, but I cannot attend because I have a family appointment."),
    7: ("C", "Write a short message"),
    8: ("D", "The writer finds the jacket useful in cool weather"),
    9: ("B", "Of course. We can practice after lunch, and I can listen to your opening."),
    10: ("C", "Answer the date, meal, and hobby questions in order, then ask one related question."),
}


def main() -> None:
    keys: Counter[str] = Counter()
    prompts, strategies, steps = [], [], []
    for number, (key, correct) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-12-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft"
        assert item["answer"]["value"] == key and options[key] == correct
        assert item["answer"]["explanation"] == item["solutionSteps"][-1]
        assert len(item["solutionSteps"]) == 5
        refs = item["examPatternRefs"]
        assert len(refs) == 3 and len({ref["url"] for ref in refs}) == 3
        assert all(ref["status"] == "recorded" and ref["reuseDecision"] == "pattern-only" and ref["locatorLevel"] == "page" for ref in refs)
        assert all("第" in ref["locator"] and "題" in ref["locator"] for ref in refs)
        keys[key] += 1
        prompts.append(item["prompt"])
        strategies.append(item["solutionStrategy"])
        steps.extend(item["solutionSteps"])
    assert keys == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), keys
    assert len(set(prompts)) == len(set(strategies)) == 10
    assert len(set(steps)) == 50
    print(json.dumps({"status": "pass", "reviewed": 10, "answerDistribution": dict(sorted(keys.items())), "recordedPatternOnlyRefs": 30, "distinctStrategies": 10, "uniqueSteps": 50, "reviewStatus": "draft"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
