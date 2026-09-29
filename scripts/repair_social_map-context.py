#!/usr/bin/env python3
"""Remove an objectively wrong geography-exhibition context from social questions.

This is deliberately narrow: it changes only the shared false context phrase in
questions already flagged by the conservative social-unit triage. Answers,
options, explanations, solution steps, sources and IDs are preserved.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"在(\d{4}年\d{1,2}月\d{1,2}日)區域地圖展的資料中，")


def main():
    changed = []
    for path in sorted((ROOT / "questions" / "social").glob("*.json")):
        data = json.loads(path.read_text())
        prompt = data.get("prompt", "")
        new_prompt = PATTERN.sub(r"在\1的社會議題資料中，", prompt)
        if new_prompt != prompt:
            data["prompt"] = new_prompt
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            changed.append(str(path.relative_to(ROOT)))
    print(json.dumps({"changed": len(changed), "paths": changed[:10]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
