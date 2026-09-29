#!/usr/bin/env python3
"""First-pass answer and public-source review for English 5-IV-11."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("A", "Name: Mia; Grade: 8; Activity: hiking"),
    2: ("B", "The science show"),
    3: ("C", "Class C"),
    4: ("D", "Snack"),
    5: ("A", "Jay's class"),
    6: ("B", "Bus 2"),
    7: ("C", "Select one workshop, add a phone number, and complete the emergency contact."),
    8: ("D", "Sort them"),
    9: ("B", "Apples are the most popular of the three."),
    10: ("C", "Choose the Saturday destination with the lowest listed price among the hat-required options."),
}


def main() -> None:
    keys: Counter[str] = Counter()
    prompts, strategies, steps = [], [], []
    for number, (key, correct_text) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-11-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft"
        assert item["answer"]["value"] == key and options[key] == correct_text
        assert item["answer"]["explanation"] and item["solutionStrategy"]
        assert len(item["solutionSteps"]) == 5 and item["solutionSteps"][-1] == item["answer"]["explanation"]
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
