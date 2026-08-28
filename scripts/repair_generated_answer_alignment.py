#!/usr/bin/env python3
"""Repair option ordering produced by the earlier substantive-rewrite batches.

The historical batch helpers rotated option text but left the answer letter in
the original order.  This script targets only those explicitly marked draft
questions and restores their original option order, preserving stable IDs and
the authored answer letter.
"""

import json
import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUESTION_ROOT = ROOT / "questions"
TARGET_NOTE = "no reproduction of public-exam wording, figures, or answer key."
REPAIR_MARKER = "answer alignment repaired 2026-08-28"


def is_target(data):
    provenance = data.get("provenance", {})
    return (
        data.get("updatedAt") == "2026-08-28"
        and data.get("reviewStatus") == "draft"
        and provenance.get("origin") == "original"
        and TARGET_NOTE in provenance.get("authoringNote", "")
        and REPAIR_MARKER not in provenance.get("authoringNote", "")
        and len(data.get("options", [])) == 4
        and data.get("answer", {}).get("value") in {"A", "B", "C", "D"}
    )


def restore_original_order(options, answer_value):
    answer_index = ord(answer_value) - ord("A")
    shift = (4 - answer_index) % 4
    if not shift:
        restored = options
    else:
        restored = options[-shift:] + options[:-shift]
    return [
        {"id": chr(ord("A") + index), "text": option["text"]}
        for index, option in enumerate(restored)
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mark-existing",
        action="store_true",
        help="只為已修復的選項順序補上冪等標記，不再次旋轉選項",
    )
    args = parser.parse_args()
    targets = []
    for path in sorted(QUESTION_ROOT.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if is_target(data):
            targets.append(path)

    for path in targets:
        data = json.loads(path.read_text(encoding="utf-8"))
        answer_value = data["answer"]["value"]
        if not args.mark_existing:
            data["options"] = restore_original_order(data["options"], answer_value)
        note = data["provenance"]["authoringNote"]
        data["provenance"]["authoringNote"] = f"{note} {REPAIR_MARKER}."
        answer_option = next(
            option for option in data["options"] if option["id"] == answer_value
        )
        if not answer_option["text"]:
            raise ValueError(f"empty answer option: {path}")
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(f"repaired {len(targets)} generated question files")


if __name__ == "__main__":
    main()
