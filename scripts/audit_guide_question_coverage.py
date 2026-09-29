#!/usr/bin/env python3
"""Audit the guide's three-original-question requirement by KG ID."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    bundle = json.loads((ROOT / "implementation/unit-specs.bundle.json").read_text(encoding="utf-8"))
    specs = [{"lessonId": spec["lessonId"], "knowledgeGraphIds": spec["knowledgeGraphIds"]} for spec in bundle["units"]]
    required = {kg for spec in specs for kg in spec["knowledgeGraphIds"]}
    validator = Draft202012Validator(
        json.loads((ROOT / "schemas/question.schema.json").read_text(encoding="utf-8")),
        format_checker=FormatChecker(),
    )
    original = Counter()
    reviewed = Counter()
    for path in (ROOT / "questions").rglob("*.json"):
        question = json.loads(path.read_text(encoding="utf-8"))
        for kg in question.get("knowledgeIds", []):
            if kg not in required:
                continue
            if question.get("provenance", {}).get("origin") == "original":
                original[kg] += 1
            if question.get("reviewStatus") == "content-reviewed":
                reviewed[kg] += 1
    generated_files = sorted((ROOT / "questions/generated").glob("*.json"))
    generated_ids = set()
    generated_errors = []
    generated_draft_count = 0
    for path in generated_files:
        question = json.loads(path.read_text(encoding="utf-8"))
        if question.get("id") in generated_ids:
            generated_errors.append(f"duplicate id: {question.get('id')}")
        generated_ids.add(question.get("id"))
        generated_errors.extend(f"{path.name}: {error.message}" for error in validator.iter_errors(question))
        generated_draft_count += question.get("reviewStatus") == "draft"
    missing = sorted(kg for kg in required if original[kg] < 3)
    report = {
        "requiredKnowledgeNodes": len(required),
        "nodesWithAtLeastThreeOriginal": len(required) - len(missing),
        "missingOrInsufficient": len(missing),
        "missingKnowledgeIds": missing,
        "originalQuestionCountMatched": sum(original.values()),
        "reviewedQuestionCountMatched": sum(reviewed.values()),
        "requiredPerNode": 3,
        "status": "pending-content-authoring" if missing else "passed",
        "generatedQuestionFiles": len(generated_files),
        "generatedQuestionIds": len(generated_ids),
        "generatedQuestionsDraft": generated_draft_count,
        "generatedQuestionSchemaErrors": generated_errors,
        "note": "Do not generate noun-swapped placeholders; each missing question requires unit-specific source-aware authoring and AI content QA.",
    }
    out = ROOT / "implementation/reports/question-coverage.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
