#!/usr/bin/env python3
"""Normalize V2 interactive options without changing their intended answer."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
changed_lessons = changed_steps = removed_options = skipped_steps = 0


def option_text(option: object) -> object:
    """Convert a V2 option object to the string expected by lesson.schema.json."""
    return option.get("text", str(option)) if isinstance(option, dict) else option


def answer_label(index: int) -> str:
    return chr(ord("A") + index)


for p in (ROOT / "lessons").glob("*/*.json"):
    d = json.loads(p.read_text())
    interactive = d.get("interactive")
    if not isinstance(interactive, dict):
        continue
    dirty = False
    for step in interactive.get("steps", []):
        options = step.get("options") if isinstance(step, dict) else None
        if not isinstance(options, list):
            continue
        normalized = [option_text(option) for option in options]
        if not all(isinstance(option, str) for option in normalized):
            # The schema error is not safely repairable without authored text.
            skipped_steps += 1
            continue
        retained: list[str] = []
        old_to_new: dict[int, int] = {}
        first_index: dict[str, int] = {}
        for old_index, option in enumerate(normalized):
            if option not in first_index:
                first_index[option] = len(retained)
                retained.append(option)
            old_to_new[old_index] = first_index[option]
        if len(retained) < 2:
            # Do not invent a second choice merely to satisfy the schema.
            skipped_steps += 1
            continue
        old_answer = step.get("answer")
        new_answer = old_answer
        if isinstance(old_answer, str) and len(old_answer) == 1 and "A" <= old_answer <= "Z":
            old_answer_index = ord(old_answer) - ord("A")
            if old_answer_index < len(normalized):
                new_answer = answer_label(old_to_new[old_answer_index])
        if options != retained or old_answer != new_answer:
            step["options"] = retained
            step["answer"] = new_answer
            dirty = True
            changed_steps += 1
            removed_options += len(options) - len(retained)
    if dirty:
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        changed_lessons += 1
print(
    "normalized "
    f"{changed_steps} interactive steps in {changed_lessons} lessons; "
    f"removed {removed_options} exact duplicate options; skipped {skipped_steps} unsafe steps"
)
