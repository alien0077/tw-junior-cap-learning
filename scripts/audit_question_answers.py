#!/usr/bin/env python3
"""Audit answer correctness contracts for every question file."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    rows = []
    errors = []
    prompt_counts = Counter()
    for path in sorted((ROOT / "questions").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        options = data.get("options", [])
        option_ids = [str(o.get("id")) for o in options]
        option_texts = [str(o.get("text", "")).strip() for o in options]
        answer = str(data.get("answer", {}).get("value", ""))
        checks = {
            "answerPresent": bool(answer),
            "answerMapsToOption": data.get("type") != "single-choice" or answer in option_ids,
            "optionIdsUnique": len(option_ids) == len(set(option_ids)),
            "optionTextsNonEmpty": all(option_texts),
            "optionTextsUnique": len(option_texts) == len(set(option_texts)),
            "explanationPresent": bool(str(data.get("answer", {}).get("explanation", "")).strip()),
            "strategyPresent": bool(str(data.get("solutionStrategy", "")).strip()),
            "solutionStepsAtLeastThree": len(data.get("solutionSteps", [])) >= 3,
            "solutionStepsNonEmpty": all(str(step).strip() for step in data.get("solutionSteps", [])),
        }
        failed = [name for name, passed in checks.items() if not passed]
        if failed:
            errors.append({"path": str(path.relative_to(ROOT)), "id": data.get("id"), "failedChecks": failed})
        prompt_counts[data.get("prompt", "")] += 1
        rows.append({"path": str(path.relative_to(ROOT)), "id": data.get("id"), "passed": not failed, "checks": checks})
    duplicate_prompts = sum(count - 1 for count in prompt_counts.values() if count > 1)
    summary = {
        "status": "pass" if not errors else "blocked",
        "totalQuestions": len(rows),
        "passed": len(rows) - len(errors),
        "failed": len(errors),
        "duplicatePromptCopies": duplicate_prompts,
        "note": "Structural answer audit only; subject correctness, distractor quality and pedagogical review remain separate gates.",
    }
    out = ROOT / "implementation/reports/question-answer-audit.json"
    out.write_text(json.dumps({"summary": summary, "errors": errors, "questions": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
