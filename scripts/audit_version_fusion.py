#!/usr/bin/env python3
"""Audit whether lessons have evidence for version-by-version LLM fusion.

This is intentionally an audit, not a content generator. It prevents the
existing full-lesson structure from being mistaken for version research.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_lessons() -> list[dict]:
    lessons: list[dict] = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if isinstance(data, dict) and data.get("id", "").startswith("lesson-"):
            data["_path"] = str(path.relative_to(ROOT))
            lessons.append(data)
    return lessons


def audit(lessons: list[dict], strict: bool) -> int:
    failures: list[tuple[str, str, str]] = []
    counts: dict[str, int] = {}
    interaction_signatures: dict[tuple[str, ...], list[str]] = {}
    for lesson in lessons:
        standard = lesson.get("authoringStandard", "legacy-outline")
        status = lesson.get("reviewStatus", "missing")
        counts[f"{standard}:{status}"] = counts.get(f"{standard}:{status}", 0) + 1
        if standard != "version-fused-v1":
            if strict and status in {"content-reviewed", "published"}:
                failures.append((lesson["id"], lesson["_path"], "reviewed lesson lacks version-fused-v1"))
            continue
        research = lesson.get("versionResearch")
        fusion = lesson.get("fusionRecord")
        if not isinstance(research, list) or not research:
            failures.append((lesson["id"], lesson["_path"], "missing versionResearch"))
        if not isinstance(fusion, dict):
            failures.append((lesson["id"], lesson["_path"], "missing fusionRecord"))
        if status in {"content-reviewed", "published"} and not lesson.get("terraReview"):
            failures.append((lesson["id"], lesson["_path"], "reviewed version-fused lesson lacks Terra review evidence"))
        if lesson.get("subject") in {"math", "science"}:
            design = lesson.get("simulation", {}).get("learningDesign")
            if not isinstance(design, dict):
                failures.append((lesson["id"], lesson["_path"], "math/science version-fused lesson lacks independent interaction design"))
            else:
                signature = tuple([str(design.get("type", "")), str(design.get("objective", "")), str(design.get("predictionPrompt", ""))]
                                  + [str(step.get("action", "")) + "|" + str(step.get("equation", "")) for step in design.get("steps", [])])
                interaction_signatures.setdefault(signature, []).append(lesson["id"])

    for signature, lesson_ids in interaction_signatures.items():
        if len(lesson_ids) > 1:
            for lesson_id in lesson_ids:
                failures.append((lesson_id, "", "interaction design is duplicated across units"))

    print(json.dumps({"lessonCount": len(lessons), "statusCounts": counts, "failureCount": len(failures)}, ensure_ascii=False, indent=2))
    for lesson_id, path, reason in failures:
        print(f"FAIL {lesson_id} {path}: {reason}")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail reviewed lessons not yet migrated")
    args = parser.parse_args()
    return audit(load_lessons(), args.strict)


if __name__ == "__main__":
    raise SystemExit(main())
