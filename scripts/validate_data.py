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
        if rel_parts and rel_parts[0] == "textbook-mapping":
            volumes = data.get("volumes", [])
            for volume in volumes:
                for entry in volume.get("entries", []):
                    for item_id in entry.get("knowledgeIds", []):
                        if item_id not in kg_ids:
                            errors.append(f"{path}: missing mapping KG endpoint {item_id}")

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
