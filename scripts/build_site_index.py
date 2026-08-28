#!/usr/bin/env python3
"""Build the compact data index consumed by the static M5 site.

The website must not enumerate every source JSON at page load or depend on a
moving branch.  This index is generated from the checked-out repository during
deployment and points detail requests at that exact revision.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ("chinese", "english", "math", "science", "social")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def build_index(revision: str) -> dict:
    project = read_json(ROOT / "project-state.json")
    question_paths: dict[str, list[str]] = defaultdict(list)
    question_records = []
    active_questions = 0
    for subject in SUBJECTS:
        for path in sorted((ROOT / "questions" / subject).glob("*.json")):
            question = read_json(path)
            if question.get("reviewStatus") == "deprecated":
                continue
            question_paths[question["lessonId"]].append(relative(path))
            question_records.append(
                {
                    key: question[key]
                    for key in (
                        "id", "subject", "type", "prompt", "options", "knowledgeIds",
                        "difficulty", "answer", "reviewStatus", "updatedAt", "lessonId",
                    )
                    if key in question
                }
            )
            active_questions += 1

    lessons = []
    for subject in SUBJECTS:
        for path in sorted((ROOT / "lessons" / subject).glob("*.json")):
            lesson = read_json(path)
            if lesson.get("reviewStatus") == "deprecated":
                continue
            lessons.append(
                {
                    **lesson,
                    "summary": lesson["content"]["summary"],
                    "path": relative(path),
                    "questionPaths": sorted(question_paths[lesson["id"]]),
                }
            )

    mappings = []
    for path in sorted((ROOT / "textbook-mapping").glob("*/*.json")):
        mapping = read_json(path)
        if not str(mapping.get("id", "")).startswith("mapset-"):
            continue
        volumes = mapping.get("volumes", [])
        mappings.append(
            {
                "id": mapping["id"],
                "subject": mapping["subject"],
                "publisher": mapping["publisher"],
                "academicYear": mapping["academicYear"],
                "status": mapping["status"],
                "path": relative(path),
                "volumeCount": len(volumes),
                "entryCount": sum(len(volume.get("entries", [])) for volume in volumes),
                "source": {
                    key: mapping["source"].get(key)
                    for key in ("type", "url", "locator", "verifiedAt", "confidence")
                },
            }
        )

    active_lessons = len(lessons)
    missing_questions = [lesson["id"] for lesson in lessons if len(lesson["questionPaths"]) < 10]
    if missing_questions:
        raise ValueError(f"active lessons without 10 questions: {', '.join(missing_questions[:10])}")

    source_base = "../" if revision == "local" else f"https://raw.githubusercontent.com/alien0077/tw-junior-cap-learning/{revision}/"
    return {
        "version": 2,
        "generatedAt": date.today().isoformat(),
        "sourceRevision": revision,
        "sourceBase": source_base,
        "project": {
            "updatedAt": project.get("updatedAt"),
            "dataCounts": project.get("dataCounts", {}),
            "activeLessons": active_lessons,
            "activeQuestions": active_questions,
        },
        "lessons": lessons,
        "questions": sorted(question_records, key=lambda question: question["id"]),
        "mappings": mappings,
        "validation": {
            "subjects": dict(Counter(lesson["subject"] for lesson in lessons)),
            "lessonCount": active_lessons,
            "questionCount": active_questions,
            "mappingSetCount": len(mappings),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--revision", required=True, help="immutable Git revision used for detail requests")
    parser.add_argument("--output", type=Path, default=ROOT / "site" / "data-index.json")
    parser.add_argument("--check", action="store_true", help="validate an existing index instead of writing it")
    args = parser.parse_args()
    index = build_index(args.revision)
    rendered = json.dumps(index, ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("site data index is stale or missing")
        print(f"site index verified: {index['validation']}")
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    print(f"site index written: {args.output} {index['validation']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
