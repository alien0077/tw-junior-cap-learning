#!/usr/bin/env python3
"""Find question prompts that remain identical after removing generator labels.

This is a content-quality gate, not a schema gate.  A repeated prompt is only
safe when the complete item is independently authored; therefore this report
also compares normalized option text and records every affected file.
"""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(value: object) -> str:
    text = str(value or "").lower()
    text = re.sub(r"\b(?:question|item|題目|第)\s*[-#]?\s*\d+\b", "question", text)
    text = re.sub(r"\b(?:kg|lesson|unit|單元)[-_：: ]*[a-z0-9ⅰ-ⅹ-]+\b", "unit", text)
    text = re.sub(r"\b(?:practice|exercise)\s*[-#]?\s*\d+\b", "practice", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def item_key(data: dict) -> tuple[str, str]:
    prompt = normalize(data.get("prompt"))
    options = "\n".join(
        f"{normalize(option.get('id'))}:{normalize(option.get('text'))}"
        for option in data.get("options", [])
    )
    return prompt, options


def main() -> int:
    groups: defaultdict[tuple[str, str], list[dict]] = defaultdict(list)
    for path in sorted((ROOT / "questions").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        groups[item_key(data)].append(
            {
                "path": str(path.relative_to(ROOT)),
                "id": data.get("id"),
                "subject": data.get("subject"),
                "lessonId": data.get("lessonId"),
                "knowledgeIds": data.get("knowledgeIds", []),
                "reviewStatus": data.get("reviewStatus"),
            }
        )

    duplicate_groups = [
        {
            "normalizedPrompt": key[0],
            "normalizedOptions": key[1],
            "copies": len(items),
            "subjects": dict(Counter(item["subject"] for item in items)),
            "items": items,
        }
        for key, items in groups.items()
        if len(items) > 1
    ]
    duplicate_groups.sort(key=lambda row: (-row["copies"], row["normalizedPrompt"]))
    affected = [item for row in duplicate_groups for item in row["items"]]
    summary = {
        "status": "blocked" if duplicate_groups else "pass",
        "totalQuestions": sum(len(items) for items in groups.values()),
        "duplicateGroups": len(duplicate_groups),
        "affectedQuestions": len(affected),
        "duplicateCopiesBeyondFirst": sum(row["copies"] - 1 for row in duplicate_groups),
        "subjects": dict(Counter(item["subject"] for item in affected)),
        "note": "Repeated normalized prompt and options are treated as template reuse until each item receives independent subject-specific authoring and answer QA.",
    }
    out = ROOT / "implementation/reports/question-template-reuse.json"
    out.write_text(
        json.dumps({"summary": summary, "groups": duplicate_groups}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if not duplicate_groups else 1


if __name__ == "__main__":
    raise SystemExit(main())
