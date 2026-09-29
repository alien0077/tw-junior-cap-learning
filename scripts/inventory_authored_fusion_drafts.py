#!/usr/bin/env python3
"""Inventory existing long-form fusion manuscripts without reviewing them."""
from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = ROOT / "implementation/unit-specs"
LESSON_ROOT = ROOT / "lessons"
OUTPUT = ROOT / "implementation/reports/authored-fusion-writing-inventory.json"


def main() -> int:
    all_spec_files = sorted(SPEC_ROOT.glob("*/*.yaml"))
    spec_files = [
        path for path in all_spec_files
        if yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"].get("curriculumLevel") in {"learning-content", "learning-performance"}
    ]
    authored_ids: list[str] = []
    long_form_ids: list[str] = []
    total_by_level: Counter[str] = Counter()
    authored_by_level: Counter[str] = Counter()
    missing: list[str] = []
    any_body: list[str] = []
    full_length: list[str] = []
    for path in spec_files:
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        level = spec["curriculumLevel"]
        total_by_level[level] += 1
        lesson_id = spec["lessonId"].replace("cur-", "lesson-", 1)
        lesson_path = next(iter(LESSON_ROOT.glob(f"*/{lesson_id}.json")), None)
        if lesson_path is None:
            missing.append(lesson_id)
            continue
        lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
        body = lesson.get("teaching", {}).get("body", [])
        if body:
            any_body.append(lesson_id)
        synthesis = (lesson.get("fusionRecord") or {}).get("llmSynthesisNote", "")
        if len(body) >= 6 and synthesis.strip():
            authored_ids.append(lesson_id)
            authored_by_level[level] += 1
            if all(len(section.get("body", "")) > 100 for section in body):
                long_form_ids.append(lesson_id)
    total = len(spec_files)
    report = {
        "asOf": date.today().isoformat(),
        "scope": "learning-content and learning-performance implementation specs; topic/theme parent specs are excluded",
        "purpose": "Record pre-existing fusion manuscripts so they are not rewritten; this is not a content review or source-quality decision.",
        "method": {
            "includedWhen": "A matching lesson has at least six teaching.body sections and a non-empty fusionRecord.llmSynthesisNote. A separate long-form marker requires every body section to exceed 100 characters.",
            "limitations": "Structural inventory only. It does not judge originality, correctness, unit fit, source reading, publisher comparison, learner visibility, or review status. A listed unit records an authored manuscript to preserve; lesson-content review is reserved for the user's ChatGPT review and is not a Codex completion gate.",
        },
        "counts": {
            "allImplementationSpecs": len(all_spec_files),
            "learningUnitSpecs": total,
            "lessonFilesMatched": total - len(missing),
            "matchedLessonsWithAnyTeachingBody": len(any_body),
            "authoredFusionDraftsRecorded": len(authored_ids),
            "authoredFusionDraftPercent": round(len(authored_ids) * 100 / total, 2) if total else 0,
            "longFormDraftMarkerCount": len(long_form_ids),
            "draftsByCurriculumLevel": {
                level: {"units": total_by_level[level], "withFusionDraftRecord": authored_by_level[level]}
                for level in sorted(total_by_level)
            },
            "unmatchedSpecDerivedLessonIds": missing,
        },
        "authoredFusionDraftIds": sorted(authored_ids),
        "longFormDraftMarkerIds": sorted(long_form_ids),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["counts"], ensure_ascii=False))
    return 0 if total == 791 and len(all_spec_files) == 1027 else 1


if __name__ == "__main__":
    raise SystemExit(main())
