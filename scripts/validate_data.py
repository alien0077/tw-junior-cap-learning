#!/usr/bin/env python3
"""Repository data validation for CI."""
from __future__ import annotations
import json
import argparse
import re
import unicodedata
from collections import Counter
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

def normalized_text(value: object) -> str:
    """Normalize presentation-only differences before duplicate detection."""
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", value)).strip()

def question_signature(data: dict) -> tuple:
    """Return a stable signature for an entire question, excluding its ID."""
    options = tuple(
        (option.get("id"), normalized_text(option.get("text")))
        for option in data.get("options", [])
    )
    answer = data.get("answer", {})
    return (
        normalized_text(data.get("prompt")),
        options,
        normalized_text(answer.get("value")),
        normalized_text(answer.get("explanation")),
    )

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository data and M4 review state.")
    parser.add_argument(
        "--require-no-drafts",
        action="store_true",
        help="fail when lessons or questions remain in draft reviewStatus",
    )
    args = parser.parse_args()
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
        area = path.relative_to(ROOT).parts[0]
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            item_id = data["id"]
            if item_id in ids:
                errors.append(f"duplicate id {item_id}: {ids[item_id]} and {path}")
            ids[item_id] = path
        if area == "knowledge":
            for node in data.get("nodes", []):
                if isinstance(node, dict) and isinstance(node.get("id"), str):
                    kg_ids.add(node["id"])

    for path, data in parsed.items():
        area = path.relative_to(ROOT).parts[0]
        if area in {"lessons", "questions"}:
            if area == "questions" and not data.get("lessonId"):
                errors.append(f"{path}: missing lessonId")
            for item_id in data.get("knowledgeIds", []):
                if item_id not in kg_ids:
                    errors.append(f"{path}: missing KG endpoint {item_id}")
            origin = data.get("provenance", {}).get("origin")
            if origin not in {"original", "official-open", "licensed"}:
                errors.append(f"{path}: unsupported question provenance.origin={origin!r}")
        if area == "textbook-mapping":
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
    question_signatures: dict[tuple[str, tuple], Path] = {}
    question_prompts: dict[tuple[str, str], Path] = {}
    question_bodies: dict[tuple, Path] = {}
    lessons_by_id = {
        item_id: data
        for path, data in parsed.items()
        if path.relative_to(ROOT).parts[0] == "lessons"
        for item_id in [data.get("id")]
        if isinstance(item_id, str)
    }
    review_counts: Counter[tuple[str, str]] = Counter()
    for path, data in parsed.items():
        area = path.relative_to(ROOT).parts[0]
        if area in {"lessons", "questions"}:
            review_counts[(area, data.get("reviewStatus", "missing"))] += 1
        if area == "questions" and isinstance(data.get("lessonId"), str):
            lesson_question_counts[data["lessonId"]] = lesson_question_counts.get(data["lessonId"], 0) + 1
            lesson_id = data["lessonId"]
            signature_key = (lesson_id, question_signature(data))
            previous = question_signatures.get(signature_key)
            if previous is not None:
                errors.append(f"{path}: duplicate question content in {lesson_id}; same as {previous}")
            else:
                question_signatures[signature_key] = path
            body_key = (
                tuple((option.get("id"), normalized_text(option.get("text"))) for option in data.get("options", [])),
                normalized_text(data.get("answer", {}).get("value")),
                normalized_text(data.get("answer", {}).get("explanation")),
            )
            previous_body = question_bodies.get(body_key)
            if previous_body is not None:
                previous_data = parsed[previous_body]
                if previous_data.get("lessonId") != lesson_id:
                    errors.append(f"{path}: cross-lesson question template reuse; same answer/options as {previous_body}")
            else:
                question_bodies[body_key] = path
            prompt_key = (lesson_id, normalized_text(data.get("prompt")))
            previous_prompt = question_prompts.get(prompt_key)
            if previous_prompt is not None:
                errors.append(f"{path}: duplicate question prompt in {lesson_id}; same as {previous_prompt}")
            else:
                question_prompts[prompt_key] = path
            lesson = lessons_by_id.get(data["lessonId"])
            if lesson is None:
                errors.append(f"{path}: lessonId does not exist: {data['lessonId']}")
            else:
                if data.get("subject") != lesson.get("subject"):
                    errors.append(f"{path}: subject differs from lesson {data['lessonId']}")
                if not set(data.get("knowledgeIds", [])) & set(lesson.get("knowledgeIds", [])):
                    errors.append(f"{path}: no shared KG endpoint with lesson {data['lessonId']}")
            if data.get("type") in {"single-choice", "multiple-choice"}:
                option_ids = {option.get("id") for option in data.get("options", [])}
                if data.get("answer", {}).get("value") not in option_ids:
                    errors.append(f"{path}: answer.value is not one of its option IDs")
            provenance = data.get("provenance", {})
            origin = provenance.get("origin")
            if origin in {"official-open", "licensed"}:
                if not provenance.get("sourceUrl") or not provenance.get("sourceLocator"):
                    errors.append(f"{path}: {origin} questions require provenance.sourceUrl and sourceLocator")
    lesson_ids = set(lessons_by_id)
    for lesson_id in lesson_ids:
        if lesson_question_counts.get(lesson_id, 0) < 10:
            errors.append(f"{lesson_id}: only {lesson_question_counts.get(lesson_id, 0)} questions; minimum is 10")

    draft_count = review_counts[("lessons", "draft")] + review_counts[("questions", "draft")]
    if args.require_no_drafts and draft_count:
        errors.append(f"M4 release gate: {draft_count} lesson/question records remain draft")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"validated {len(parsed)} JSON files, {len(ids)} IDs, {len(kg_ids)} KG nodes")
    print(
        "review status: "
        f"lessons content-reviewed={review_counts[('lessons', 'content-reviewed')]}, "
        f"draft={review_counts[('lessons', 'draft')]}; "
        f"questions content-reviewed={review_counts[('questions', 'content-reviewed')]}, "
        f"draft={review_counts[('questions', 'draft')]}"
    )
    if draft_count:
        print("note: draft records passed structural validation only; they are excluded from completed M4 coverage.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
