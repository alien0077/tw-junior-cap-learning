#!/usr/bin/env python3
"""Validate the implementation-guide contract against repository data.

This validator distinguishes structural readiness from implementation/QA
completion. It never upgrades status and reports blocked/pending work.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def curriculum_index():
    result = {}
    for path in (ROOT / "curriculum").glob("*/*.json"):
        obj = load_json(path)
        if isinstance(obj, dict) and obj.get("id", "").startswith("cur-"):
            result[obj["id"]] = (path, obj)
    return result


def knowledge_ids():
    ids = set()
    for path in (ROOT / "knowledge").glob("*/*.json"):
        obj = load_json(path)
        for node in obj.get("nodes", []):
            if isinstance(node, dict) and isinstance(node.get("id"), str):
                ids.add(node["id"])
    return ids


def validate_spec(path: Path, schema, curricula, kg_ids, registry):
    errors = []
    try:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"YAML parse: {exc}"]
    try:
        jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(doc)
    except jsonschema.ValidationError as exc:
        errors.append(f"schema: {exc.message} at {'/'.join(map(str, exc.absolute_path))}")
    spec = doc.get("unitImplementationSpec", {}) if isinstance(doc, dict) else {}
    lesson_id = spec.get("lessonId")
    if lesson_id not in curricula:
        errors.append(f"lessonId not found in curriculum: {lesson_id}")
    if lesson_id and path.stem != lesson_id:
        errors.append(f"filename does not match lessonId: {path.name}")
    for kg_id in spec.get("knowledgeGraphIds", []):
        if kg_id not in kg_ids:
            errors.append(f"knowledgeGraphId not found: {kg_id}")
    for block in spec.get("interactiveBlocks", []):
        if block.get("component") not in registry:
            errors.append(f"component not registered: {block.get('component')}")
        if not block.get("studentActions"):
            errors.append("interactive block has no student action")
        if not block.get("misconceptionChecks"):
            errors.append("interactive block has no misconception check")
        if not all(
            isinstance(x, dict)
            and x.get("id")
            and x.get("trigger")
            and x.get("prompt")
            and x.get("expectedEvidence")
            for x in block.get("misconceptionChecks", [])
        ):
            errors.append("malformed misconception check")
        if not block.get("feedback", {}).get("incorrect"):
            errors.append("interactive block has no incorrect misconception feedback")
    def forbidden_value(value):
        if isinstance(value, str):
            normalized = value.strip().lower()
            return normalized in {"todo", "placeholder", "tbd"} or normalized.startswith("todo:")
        if isinstance(value, dict):
            return any(forbidden_value(v) for v in value.values())
        if isinstance(value, list):
            return any(forbidden_value(v) for v in value)
        return False
    if forbidden_value(spec):
        errors.append("contains a TODO/placeholder/TBD value")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec-dir", type=Path, default=ROOT / "implementation/unit-specs")
    parser.add_argument("--report", type=Path, default=ROOT / "implementation/reports/implementation-validation.json")
    args = parser.parse_args()
    schema = load_json(ROOT / "implementation/unit-implementation.schema.json")
    registry = load_json(ROOT / "implementation/component-registry.json")["components"]
    curricula = curriculum_index()
    kg = knowledge_ids()
    files = sorted(args.spec_dir.glob("*/*.yaml"))
    errors = {}
    statuses = Counter()
    evidence = Counter()
    components = Counter()
    for path in files:
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        spec = doc["unitImplementationSpec"]
        status = spec.get("status") or {}
        statuses[tuple(status.values())] += 1
        blocks = spec.get("interactiveBlocks") or []
        if blocks and isinstance(blocks[0], dict) and blocks[0].get("component"):
            components[blocks[0]["component"]] += 1
        publisher_evidence = ((spec.get("fusedScope") or {}).get("publisherEvidence") or {})
        for item in publisher_evidence.values():
            if isinstance(item, dict) and item.get("status"):
                evidence[item["status"]] += 1
        problem = validate_spec(path, schema, curricula, kg, registry)
        if problem:
            errors[str(path.relative_to(ROOT))] = problem

    ids = [yaml.safe_load(p.read_text(encoding="utf-8"))["unitImplementationSpec"]["lessonId"] for p in files]
    duplicate_ids = sorted({x for x in ids if ids.count(x) > 1})
    eligible_specs = 0
    for path in files:
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        state = spec.get("status") or {}
        if (
            state.get("designStatus") == "reviewed"
            and state.get("implementationStatus") == "implemented"
            and state.get("qaStatus") == "verified"
            and str(path.relative_to(ROOT)) not in errors
        ):
            eligible_specs += 1

    report = {
        "specVersion": "1.0",
        "counts": {"specFiles": len(files), "curriculumDocuments": len(curricula), "knowledgeIds": len(kg)},
        "statusCounts": {"|".join(k): v for k, v in sorted(statuses.items())},
        "publisherEvidenceCounts": dict(sorted(evidence.items())),
        "componentCounts": dict(sorted(components.items())),
        "duplicateLessonIds": duplicate_ids,
        "errors": errors,
        "completionGate": {"designStatus": "reviewed", "implementationStatus": "implemented", "qaStatus": "verified"},
        "completion": {"eligible": eligible_specs, "pending": len(files) - eligible_specs},
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"specFiles": len(files), "errors": len(errors), "eligible": eligible_specs, "pending": len(files) - eligible_specs, "report": str(args.report)}, ensure_ascii=False))
    return 1 if errors or len(files) != 1027 or len(curricula) < 1027 else 0


if __name__ == "__main__":
    raise SystemExit(main())
