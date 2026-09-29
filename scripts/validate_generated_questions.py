#!/usr/bin/env python3
"""Validate root-domain generated question files without promoting review status."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    args = parser.parse_args()
    files = args.files or sorted((ROOT / "questions/generated").glob("*.json"))
    schema = json.loads((ROOT / "schemas/question.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    errors = []
    seen = set()
    kg_counts = Counter()
    question_count = 0
    for path in files:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            items = data if isinstance(data, list) else [data]
        except Exception as exc:
            errors.append(f"{path}: JSON parse: {exc}")
            continue
        for item in items:
            question_count += 1
            for error in validator.iter_errors(item):
                errors.append(f"{path}: {error.message}")
            qid = item.get("id")
            if qid in seen:
                errors.append(f"duplicate question id: {qid}")
            seen.add(qid)
            if item.get("provenance", {}).get("origin") != "original":
                errors.append(f"{path}: origin is not original")
            if item.get("reviewStatus") != "draft":
                errors.append(f"{path}: generated question must remain draft")
            options = item.get("options", [])
            option_ids = [option.get("id") for option in options]
            answer = item.get("answer", {}).get("value")
            if len(option_ids) != len(set(option_ids)):
                errors.append(f"{path}: duplicate option ids")
            if answer not in option_ids:
                errors.append(f"{path}: answer is not one of the options")
            if not item.get("answer", {}).get("explanation", "").strip():
                errors.append(f"{path}: answer explanation is empty")
            provenance = item.get("provenance", {})
            if not provenance.get("sourceUrl", "").strip() or not provenance.get("sourceLocator", "").strip():
                errors.append(f"{path}: source URL/locator is empty")
            for kg in item.get("knowledgeIds", []):
                kg_counts[kg] += 1
    # An empty quarantine is valid after root questions have been promoted to
    # their canonical subject folders and validated by validate_data.py.
    report = {"files": len(files), "questions": question_count, "kgCounts": dict(sorted(kg_counts.items())), "errors": errors, "status": "passed" if not errors else "failed", "note": "quarantine is empty; root questions are canonical draft records"}
    out = ROOT / "implementation/reports/generated-question-validation.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"files": len(files), "questions": question_count, "errors": len(errors), "report": str(out)}, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
