#!/usr/bin/env python3
"""Attach the existing broad learning-content KG endpoint to generated root questions.

The root KG remains the primary curriculum anchor. The additional broad KG is
needed because the legacy repository lesson used by the question validator is
`lesson-<subject>-learning-content`.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    changed = 0
    for path in sorted((ROOT / "questions/generated").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        subject = data["subject"]
        broad = f"kg-{subject}-learning-content"
        if broad not in data["knowledgeIds"]:
            data["knowledgeIds"].append(broad)
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(json.dumps({"changed": changed, "files": len(list((ROOT / 'questions/generated').glob('*.json')))}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
