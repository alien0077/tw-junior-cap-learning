#!/usr/bin/env python3
"""Repository data validation for CI."""
from __future__ import annotations
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "schemas"

def read_json(path: Path):
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)

def validate(path: Path, schema_path: Path, errors: list[str]):
    data = read_json(path)
    schema = read_json(schema_path)
    for error in Draft202012Validator(schema).iter_errors(data):
        location = ".".join(str(x) for x in error.absolute_path)
        errors.append(f"{path}: {location}: {error.message}")
    return data

def main() -> int:
    errors: list[str] = []
    json_files = [p for p in ROOT.rglob("*.json") if "site" not in p.parts]
    parsed = {}
    for path in json_files:
        try:
            parsed[path] = read_json(path)
        except Exception as exc:
            errors.append(f"{path}: invalid JSON: {exc}")

    for path, data in parsed.items():
        rel = path.relative_to(ROOT).as_posix()
        parts = rel.split("/")
        schema_path = None
        if rel.startswith("curriculum/"):
            schema_path = SCHEMA_DIR / "curriculum.schema.json"
        elif rel.startswith("knowledge/") and path.name != ".gitkeep":
            schema_path = SCHEMA_DIR / "knowledge.schema.json"
        elif rel.startswith("lessons/"):
            schema_path = SCHEMA_DIR / "lesson.schema.json"
        elif rel.startswith("questions/"):
            schema_path = SCHEMA_DIR / "question.schema.json"
        elif rel.startswith("textbook-mapping/"):
            schema_path = SCHEMA_DIR / (
                "textbook-mapping-set.schema.json"
                if str(data.get("id", "")).startswith("mapset-")
                else "textbook-mapping.schema.json"
            )
        elif rel.startswith("canonical-units/"):
            schema_path = SCHEMA_DIR / (
                "curriculum-unit-mapping.schema.json"
                if str(data.get("id", "")).startswith("unit-map-")
                else "canonical-unit.schema.json"
            )
        elif rel.startswith("migrations/") and path.name == "math-question-migration-pilot.json":
            schema_path = SCHEMA_DIR / "question-migration-manifest.schema.json"
        if schema_path and schema_path.exists():
            validate(path, schema_path, errors)

    ids: dict[str, Path] = {}
    kg_ids: set[str] = set()
    for path, data in parsed.items():
        parts = path.relative_to(ROOT).parts
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            item_id = data["id"]
            if item_id in ids:
                errors.append(f"duplicate id {item_id}: {ids[item_id]} and {path}")
            ids[item_id] = path
        if parts and parts[0] == "knowledge":
            for node in data.get("nodes", []):
                if isinstance(node, dict) and isinstance(node.get("id"), str):
                    kg_ids.add(node["id"])

    for path, data in parsed.items():
        rel_parts = path.relative_to(ROOT).parts
        if rel_parts and rel_parts[0] in {"lessons", "questions"}:
            if rel_parts[0] == "questions" and not data.get("lessonId"):
                errors.append(f"{path}: missing lessonId")
            for item_id in data.get("knowledgeIds", []):
                if item_id not in kg_ids:
                    errors.append(f"{path}: missing KG endpoint {item_id}")
            if data.get("provenance", {}).get("origin") != "original":
                errors.append(f"{path}: M4 content must use provenance.origin=original")
            if rel_parts[0] == "lessons" and data.get("subject") in {"math", "science"}:
                steps = data.get("interactive", {}).get("steps", [])
                if not isinstance(steps, list) or len(steps) < 3:
                    errors.append(f"{path}: math/science lesson requires at least 3 interactive steps")
        if rel_parts and rel_parts[0] == "textbook-mapping":
            volumes = data.get("volumes", [])
            for volume in volumes:
                for entry in volume.get("entries", []):
                    for item_id in entry.get("knowledgeIds", []):
                        if item_id not in kg_ids:
                            errors.append(f"{path}: missing mapping KG endpoint {item_id}")

    canonical_units = {
        data.get("id"): data
        for path, data in parsed.items()
        if path.relative_to(ROOT).parts[0] == "canonical-units"
        and str(data.get("id", "")).startswith("canonical-unit-")
    }
    curriculum_ids = {
        data.get("id")
        for path, data in parsed.items()
        if path.relative_to(ROOT).parts[0] == "curriculum"
    }
    for path, data in parsed.items():
        rel_parts = path.relative_to(ROOT).parts
        if rel_parts and rel_parts[0] == "canonical-units" and str(data.get("id", "")).startswith("canonical-unit-"):
            source = data.get("source", {})
            if not str(source.get("url", "")).startswith(("http://", "https://")):
                errors.append(f"{path}: canonical unit missing public source URL")
            if not str(source.get("locator", "")).strip():
                errors.append(f"{path}: canonical unit missing source locator")
            if data.get("teachable") is False and data.get("status") == "verified":
                errors.append(f"{path}: classification-only unit cannot be verified as teachable")
        if rel_parts and rel_parts[0] == "canonical-units" and str(data.get("id", "")).startswith("unit-map-"):
            if data.get("unitId") not in canonical_units:
                errors.append(f"{path}: missing canonical unit {data.get('unitId')}")
            elif canonical_units[data.get("unitId")].get("teachable") is False and data.get("relation") != "classifies":
                errors.append(f"{path}: non-teachable unit must use relation=classifies")
            for curriculum_id in data.get("curriculumIds", []):
                if curriculum_id not in curriculum_ids:
                    errors.append(f"{path}: missing curriculum endpoint {curriculum_id}")
    lesson_question_counts: dict[str, int] = {}
    for path, data in parsed.items():
        if path.relative_to(ROOT).parts[0] == "questions" and isinstance(data.get("lessonId"), str):
            lesson_question_counts[data["lessonId"]] = lesson_question_counts.get(data["lessonId"], 0) + 1
    lesson_ids = {item_id for item_id, path in ids.items() if path.relative_to(ROOT).parts[0] == "lessons"}
    lesson_by_id = {
        item_id: data
        for item_id, path in ids.items()
        if path.relative_to(ROOT).parts[0] == "lessons"
        for data in [parsed[path]]
    }
    for path, data in parsed.items():
        rel_parts = path.relative_to(ROOT).parts
        if rel_parts and rel_parts[0] == "migrations":
            for item in data.get("items", []):
                question_id = item.get("questionId")
                lesson_id = item.get("sourceLessonId")
                if question_id not in ids:
                    errors.append(f"{path}: missing question {item.get('questionId')}")
                if lesson_id not in lesson_by_id:
                    errors.append(f"{path}: missing lesson {lesson_id}")
                if question_id in ids and parsed[ids[question_id]].get("subject") != data.get("subject"):
                    errors.append(f"{path}: question subject mismatch {question_id}")
                if lesson_id in lesson_by_id and lesson_by_id[lesson_id].get("subject") != data.get("subject"):
                    errors.append(f"{path}: lesson subject mismatch {lesson_id}")
                target = item.get("targetUnitId")
                if target is not None and target not in canonical_units:
                    errors.append(f"{path}: missing target canonical unit {target}")
                if target is not None and target in canonical_units and canonical_units[target].get("subject") != data.get("subject"):
                    errors.append(f"{path}: target unit subject mismatch {target}")
                if target is not None and target in canonical_units and canonical_units[target].get("teachable") is False:
                    errors.append(f"{path}: migration target must be teachable or null {target}")
    for lesson_id in lesson_ids:
        if lesson_question_counts.get(lesson_id, 0) < 10:
            errors.append(f"{lesson_id}: only {lesson_question_counts.get(lesson_id, 0)} questions; minimum is 10")

    # A visible draft marker must never be paired with content-reviewed status.
    for lesson_id, lesson in lesson_by_id.items():
        if str(lesson.get("title", "")).startswith("草稿") and lesson.get("reviewStatus") != "draft":
            errors.append(f"{lesson_id}: draft title requires reviewStatus=draft")

    matrix_path = ROOT / "data/m4-coverage-matrix.json"
    if matrix_path in parsed and isinstance(parsed[matrix_path], dict):
        for row in parsed[matrix_path].get("rows", []):
            lesson_id = row.get("lessonId")
            if lesson_id in lesson_by_id:
                lesson_status = lesson_by_id[lesson_id].get("reviewStatus")
                if row.get("reviewStatus") != lesson_status or row.get("contentStatus") != lesson_status:
                    errors.append(f"coverage {lesson_id}: status must match lesson ({lesson_status})")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(parsed)} JSON files, {len(ids)} IDs, {len(kg_ids)} KG nodes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
