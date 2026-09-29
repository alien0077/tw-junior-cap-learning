#!/usr/bin/env python3
"""Remove authoring scaffolding from student-facing question text.

The transformation only removes generated labels such as ``question 3`` or
``practice``; it does not change the task, options, answer, or explanation of
the concept.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def clean_prompt(prompt: str) -> str:
    out = prompt
    out = re.sub(r"\s*[（(]「[^」]+」(?:practice|練習),\s*\d{1,2}:\d{2}[）)]", "", out, flags=re.I)
    out = re.sub(r"\s*[（(]question\s*\d+[）)]", "", out, flags=re.I)
    out = re.sub(r"For the「[^」]+」(?:practice|練習),\s*", "", out, flags=re.I)
    out = re.sub(r"For a「[^」]+」task,\s*", "", out, flags=re.I)
    out = re.sub(r"In the「[^」]+」lesson,\s*", "", out, flags=re.I)
    out = re.sub(r"Read the「[^」]+」text for day\s*\d+:\s*", "Read the short passage: ", out, flags=re.I)
    out = re.sub(r"「[^」]+」practice,\s*", "", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def clean_explanation(explanation: str) -> str:
    out = re.sub(r"\s*This item targets [^。.]*[。.]", "", explanation, flags=re.I)
    out = re.sub(r"\s*本題對應\s*KG[^。]*。", "", out, flags=re.I)
    out = re.sub(r"\s{2,}", " ", out).strip()
    return out


def main() -> int:
    changed = 0
    for path in sorted((ROOT / "questions").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        old_prompt = data.get("prompt", "")
        old_explanation = data.get("answer", {}).get("explanation", "")
        data["prompt"] = clean_prompt(old_prompt)
        data.setdefault("answer", {})["explanation"] = clean_explanation(old_explanation)
        if data["prompt"] != old_prompt or data["answer"]["explanation"] != old_explanation:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
    print(json.dumps({"changedFiles": changed, "status": "pass"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
