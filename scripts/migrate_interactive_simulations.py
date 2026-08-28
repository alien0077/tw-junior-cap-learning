#!/usr/bin/env python3
"""Attach a data-driven simulation contract to every math/science lesson.

The engine selection is intentionally based on the stable curriculum/KG code and
lesson scope, never on a title string.  It does not alter instructional prose,
questions, review status, or existing interactive steps.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MATH_ENGINES = {
    "n": "math-number-line",
    "a": "math-algebra-balance",
    "f": "math-function-graph",
    "g": "math-function-graph",
    "s": "math-geometry",
    "d": "math-data-lab",
}
SCIENCE_GROUPS = {
    "science-motion-lab": {"eb", "ec"},
    "science-energy-lab": {"ba", "bb"},
    "science-particle-lab": {"aa", "ab", "ca", "cb", "ja", "jb", "jc", "jd"},
    "science-life-system": {"bc", "bd", "da", "db", "dc", "ga", "gb", "gc"},
    "science-earth-space": {"ed", "fa", "fb", "hb", "ia", "ib", "ic", "id"},
}


def code_for(lesson: dict) -> str:
    prefix = f"kg-{lesson['subject']}-"
    return lesson["knowledgeIds"][0].removeprefix(prefix).replace("performance-", "").replace("content-", "")


def engine_for(lesson: dict, code: str) -> tuple[str, str, str]:
    # Some supplemental lessons have a thematic lessonScope while still pointing
    # at a teachable leaf KG code.  The code, not the display scope, decides
    # whether a concrete model is appropriate.
    if lesson["subject"] == "math" and not re.match(r"^[a-z]-[0-9]", code):
        return "concept-explorer", "explorer", "general"
    if lesson["subject"] == "science" and not re.match(r"^[a-z]{2,3}-iv-[0-9]", code):
        return "concept-explorer", "explorer", "general"
    if lesson["subject"] == "math":
        family = code.split("-", 1)[0]
        if family == "d" and code in {"d-9-2", "d-9-3"}:
            return "math-probability-lab", "model", "general"
        return MATH_ENGINES.get(family, "concept-explorer"), "model", "general"
    if lesson["id"] == "lesson-science-blood-circulation":
        return "science-life-system", "model", "circulation"
    family = code.split("-", 1)[0]
    for engine, families in SCIENCE_GROUPS.items():
        if family in families:
            return engine, "model", "general"
    return "concept-explorer", "explorer", "general"


def simulation_for(lesson: dict) -> dict:
    code = code_for(lesson)
    engine, mode, model = engine_for(lesson, code)
    refs = [ref for ref in lesson.get("studyReferences", []) if ref.startswith(("https://", "http://"))]
    if not refs:
        raise ValueError(f"{lesson['id']}: no public studyReferences for simulation")
    goal = lesson.get("interactive", {}).get("goal") or f"透過操作與觀察理解「{lesson['title']}」。"
    mission = lesson.get("interactive", {}).get("scenario") or "先提出預測，再只改變一項條件，記錄可觀察的改變並用證據解釋。"
    return {
        "id": f"sim-{lesson['subject']}-{code}",
        "engine": engine,
        "mode": mode,
        "model": model,
        "goal": goal,
        "mission": mission,
        "sourceRefs": refs,
    }


def main() -> int:
    changed = 0
    for subject in ("math", "science"):
        for path in sorted((ROOT / "lessons" / subject).glob("*.json")):
            lesson = json.loads(path.read_text(encoding="utf-8"))
            simulation = simulation_for(lesson)
            if lesson.get("simulation") != simulation:
                lesson["simulation"] = simulation
                path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                changed += 1
    print(f"simulation contracts updated: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
