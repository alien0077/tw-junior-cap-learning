#!/usr/bin/env python3
"""Strict first-pass review for original English 7-IV-1 dictionary questions."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("A", "The land beside a river"),
    2: ("B", "verb"),
    3: ("C", "An example sentence showing bright used for a person"),
    4: ("D", "The collocation 'make a decision'"),
    5: ("A", "A drama or performance"),
    6: ("B", "Rising sharply"),
    7: ("C", "The numbered sense and example about a seller asking a price"),
    8: ("D", "The word-family or related-words information"),
    9: ("B", "The pronunciation, part of speech, and example for each entry"),
    10: ("C", "Use context, identify the part of speech, compare senses and examples, then reread"),
}


def main() -> None:
    keys: Counter[str] = Counter()
    prompts, strategies, steps, urls = [], [], [], set()
    for number, (key, correct_text) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-7-iv-1-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in item["options"]}
        assert item["reviewStatus"] == "draft"
        assert item["answer"]["value"] == key and options[key] == correct_text
        assert item["answer"]["explanation"].endswith(f"Correct answer: {key} — {correct_text}.")
        assert len(item["solutionSteps"]) == 5
        assert item["solutionSteps"][-1].startswith(f"答案 {key}：") and correct_text in item["solutionSteps"][-1]
        assert item["answer"]["explanation"]
        refs = item["examPatternRefs"]
        assert len(refs) == 3 and len({ref["url"] for ref in refs}) == 3
        assert all(ref["status"] == "recorded" and ref["reuseDecision"] == "pattern-only" and ref["locatorLevel"] == "page" for ref in refs)
        assert all("第" in ref["locator"] and ("題" in ref["locator"] or "小題" in ref["locator"]) for ref in refs)
        assert all("bhjh.ntpc.edu.tw" not in ref["url"] for ref in refs)
        assert item["provenance"]["origin"] == "original"
        keys[key] += 1
        urls.update(ref["url"] for ref in refs)
        prompts.append(item["prompt"])
        strategies.append(item["solutionStrategy"])
        steps.extend(item["solutionSteps"])

    assert keys == Counter({"A": 2, "B": 3, "C": 3, "D": 2}), keys
    assert len(set(prompts)) == len(set(strategies)) == 10
    assert len(set(steps)) == 50
    print(json.dumps({
        "status": "pass", "reviewed": 10,
        "answerDistribution": dict(sorted(keys.items())),
        "recordedPatternOnlyRefs": 30, "distinctSourceUrls": len(urls),
        "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(steps)),
        "reviewStatus": "draft",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
