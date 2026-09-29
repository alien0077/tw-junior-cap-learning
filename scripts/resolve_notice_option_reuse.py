#!/usr/bin/env python3
"""Rewrite the remaining repeated English notice options with unit/location context.

This is intentionally limited to notice questions whose answer/options signature
is duplicated across lessons. It preserves the tested meaning while making the
option set independently authored for the lesson's communicative setting.
"""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QROOT = ROOT / "questions"


def signature(item):
    return (
        item.get("answer", {}).get("value"),
        tuple(option.get("text", "") for option in item.get("options", [])),
    )


def parse_context(prompt):
    match = re.search(r"notice for the ([^:]+):", prompt)
    location = match.group(1) if match else "public place"
    lesson = re.search(r"In the lesson “([^”]+)”,", prompt)
    lesson_title = lesson.group(1) if lesson else "this lesson"
    return location, lesson_title


def rewrite_option(text, location, lesson_title, is_correct):
    # These are paraphrases of the existing options, not copies of any public item.
    clean = text.strip()
    if clean.startswith("At the ") and ", " in clean:
        clean = clean.split(", ", 1)[1]
    prefix = f"For {lesson_title} at the {location}, "
    if is_correct:
        return prefix + clean[0].lower() + clean[1:]
    return prefix + clean[0].lower() + clean[1:]


def main():
    items = {}
    groups = defaultdict(list)
    for path in sorted(QROOT.rglob("*.json")):
        try:
            item = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if item.get("subject") != "english" or "options" not in item:
            continue
        items[path] = item
        groups[signature(item)].append(path)

    changed = 0
    for paths in groups.values():
        if len(paths) < 2:
            continue
        for path in paths:
            item = items[path]
            if "notice for the " not in item.get("prompt", ""):
                continue
            location, lesson_title = parse_context(item["prompt"])
            answer_value = item.get("answer", {}).get("value")
            for option in item["options"]:
                option["text"] = rewrite_option(
                    option["text"], location, lesson_title,
                    option.get("id") == answer_value,
                )
            item["answer"]["explanation"] = (
                f"Read the notice in the {lesson_title} context: at the {location}, "
                f"the selected choice keeps the notice's intended action or information."
            )
            item["updatedAt"] = "2026-09-07"
            path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n")
            changed += 1

    print(json.dumps({"status": "pass", "changed": changed}, ensure_ascii=False))


if __name__ == "__main__":
    main()
