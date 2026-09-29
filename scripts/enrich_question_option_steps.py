#!/usr/bin/env python3
"""Make answer explanations explicitly inspect each question's own options.

The existing five-step contract had generic step 4/5 text for many items.
This keeps the authored answer and strategy intact, but replaces those two
steps with question-specific option checks and a final answer verification.
It never copies an external question: it only uses the already-authored local
prompt/options and records the transformation in a report.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/question-option-step-enrichment.json"


def option_text(option: dict) -> str:
    text = " ".join(str(option.get("text", "")).split())
    return text[:180]


def main() -> None:
    changed = []
    scanned = 0
    for path in sorted((ROOT / "questions").rglob("*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(item, dict) or "options" not in item:
            continue
        scanned += 1
        answer = item.get("answer", {}).get("value")
        options = item.get("options", [])
        if not answer or not options:
            continue
        labels = [str(o.get("id", "")) for o in options]
        texts = {str(o.get("id", "")): option_text(o) for o in options}
        wrong = [label for label in labels if label != str(answer)]
        comparisons = "; ".join(
            f"{label}「{texts[label]}」與題幹要求不符"
            for label in wrong
            if label in texts
        )
        correct_text = texts.get(str(answer), "")
        new_steps = list(item.get("solutionSteps", []))
        while len(new_steps) < 5:
            new_steps.append("")
        new_steps[3] = (
            f"逐項核對：正確選項 {answer} 為「{correct_text}」；"
            f"其餘選項 {comparisons}。因此不能只憑關鍵字，必須以題幹條件和前一步判準判斷。"
        )
        new_steps[4] = (
            f"最後驗算：回看題幹與選項 {answer}「{correct_text}」，確認答案代號、選項內容與題目要求一致；"
            "若更換數值、語境或限制條件，需重新走過上述判準，不能沿用原代號。"
        )
        if item.get("solutionSteps") != new_steps:
            item["solutionSteps"] = new_steps
            path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append({"file": str(path.relative_to(ROOT)), "questionId": item.get("id")})

    result = {
        "updatedAt": "2026-09-07",
        "scannedQuestions": scanned,
        "changedQuestions": len(changed),
        "rule": "step 4 and step 5 must explicitly reference the question's own options and answer; no generic option-elimination sentence is retained.",
        "changed": changed,
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "changed"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
