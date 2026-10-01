#!/usr/bin/env python3
"""Validate production data contracts for all math/science simulations."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from simulation_contracts import contract_errors

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []
    counts: Counter[str] = Counter()
    lesson_count = 0

    for subject in ("math", "science"):
        for path in sorted((ROOT / "lessons" / subject).glob("*.json")):
            lesson = json.loads(path.read_text(encoding="utf-8"))
            lesson_count += 1
            lesson_errors = contract_errors(lesson)
            if lesson_errors:
                rel = path.relative_to(ROOT)
                errors.extend(f"{rel}: {message}" for message in lesson_errors)
                continue
            counts[lesson["simulation"]["engine"]] += 1

    if errors:
        print("\n".join(errors))
        return 1

    print(f"validated {lesson_count} math/science simulation contracts")
    print("engine coverage: " + ", ".join(f"{engine}={count}" for engine, count in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
