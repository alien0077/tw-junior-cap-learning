#!/usr/bin/env python3
"""Validate the complete data contract for math/science learning simulations."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from migrate_interactive_simulations import ROOT, simulation_for


def main() -> int:
    errors: list[str] = []
    counts: Counter[str] = Counter()
    lesson_count = 0
    for subject in ("math", "science"):
        for path in sorted((ROOT / "lessons" / subject).glob("*.json")):
            lesson = json.loads(path.read_text(encoding="utf-8"))
            actual = lesson.get("simulation")
            expected = simulation_for(lesson)
            lesson_count += 1
            if actual != expected:
                errors.append(f"{path.relative_to(ROOT)}: simulation contract is missing or stale")
                continue
            counts[actual["engine"]] += 1
            if not all(url.startswith(("https://", "http://")) for url in actual["sourceRefs"]):
                errors.append(f"{path.relative_to(ROOT)}: simulation sourceRefs must be public URLs")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {lesson_count} math/science simulation contracts")
    print("engine coverage: " + ", ".join(f"{engine}={count}" for engine, count in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
