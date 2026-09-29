#!/usr/bin/env python3
"""Ensure every answer explanation explicitly identifies its own answer."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    changed = 0
    files = 0
    for path in sorted((ROOT / "questions").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        answer = data.get("answer", {})
        value = answer.get("value")
        options = data.get("options", [])
        selected = next((item.get("text", "") for item in options if item.get("id") == value), "")
        explanation = answer.get("explanation", "")
        if not isinstance(value, str) or not isinstance(selected, str) or not selected:
            continue
        if value in explanation and selected in explanation:
            continue
        answer["explanation"] = (
            f"{explanation.rstrip('。；; ')}。正確答案為選項 {value}：「{selected}」。"
            "最後把這個選項放回題幹，確認它同時符合題目條件與本單元判準。"
        )
        data["answer"] = answer
        data["reviewStatus"] = "draft"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1
    report = {
        "changedQuestionFiles": changed,
        "status": "pass",
        "note": "Every changed explanation now names its answer id and exact option text; answer values and options were preserved; all remain draft.",
    }
    out = ROOT / "implementation/reports/missing-answer-reference-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
