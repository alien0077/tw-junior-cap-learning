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
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            item_id = data["id"]
            if item_id in ids:
                errors.append(f"duplicate id {item_id}: {ids[item_id]} and {path}")
            ids[item_id] = path
        if path.parts and path.parts[0] == "knowledge":
            for node in data.get("nodes", []):
                if isinstance(node, dict) and isinstance(node.get("id"), str):
                    kg_ids.add(node["id"])

    for path, data in parsed.items():
        if path.parts and path.parts[0] in {"lessons", "questions"}:
            for item_id in data.get("knowledgeIds", []):
                if item_id not in kg_ids:
                    errors.append(f"{path}: missing KG endpoint {item_id}")
            if data.get("provenance", {}).get("origin") != "original":
                errors.append(f"{path}: M4 content must use provenance.origin=original")
        if path.parts and path.parts[0] == "textbook-mapping":
            volumes = data.get("volumes", [])
            for volume in volumes:
                for entry in volume.get("entries", []):
                    for item_id in entry.get("knowledgeIds", []):
                        if item_id not in kg_ids:
                            errors.append(f"{path}: missing mapping KG endpoint {item_id}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(parsed)} JSON files, {len(ids)} IDs, {len(kg_ids)} KG nodes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
