#!/usr/bin/env python3
"""First-pass answer mapping and provenance checks for English 5-IV-2."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("D", "Go straight for two blocks, then turn left."),
    2: ("B", "Sure. I said the meeting starts at nine."),
    3: ("C", "Can I help you?"),
    4: ("A", "Yes, Thursday evening works for me."),
    5: ("D", "I see your point, but"),
    6: ("C", "That is okay. Please bring it tomorrow."),
    7: ("B", "Of course, but please keep the call short."),
    8: ("A", "Yes, and we should arrive by 7:00."),
    9: ("C", "Please walk carefully and tell the staff."),
    10: ("B", "You should go to bed earlier and drink enough water."),
}

def main() -> None:
    keys: Counter[str] = Counter()
    prompts, strategies, steps = [], [], []
    for number, (key, correct_text) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-2-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft"
        assert item["answer"]["value"] == key and options[key] == correct_text
        assert item["answer"]["explanation"] and item["solutionStrategy"]
        assert len(item["solutionSteps"]) == 5 and item["solutionSteps"][-1] == item["answer"]["explanation"]
        refs = item["examPatternRefs"]
        assert len(refs) == 3 and len({ref["url"] for ref in refs}) == 3
        assert all(ref["status"] == "recorded" and ref["reuseDecision"] == "pattern-only" and ref["locatorLevel"] == "page" for ref in refs)
        assert all("PDF第" in ref["locator"] and "第" in ref["locator"] and "題" in ref["locator"] for ref in refs)
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
