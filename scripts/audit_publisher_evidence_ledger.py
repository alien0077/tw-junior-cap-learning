#!/usr/bin/env python3
"""Build an auditable, non-promoting ledger for publisher evidence."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLISHERS = ("nani", "kanghsuan", "hanlin")


def load_lessons() -> dict[str, dict]:
    lessons = {}
    for path in (ROOT / "lessons").glob("*/*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict) and isinstance(data.get("id"), str):
            lessons[data["id"]] = {"path": str(path.relative_to(ROOT)), "data": data}
    return lessons


def resolve_lesson(lessons: dict[str, dict], lesson_id: str):
    """Resolve stable curriculum IDs to their materialized lesson endpoint.

    Root lesson endpoints deliberately use ``content-root-a/b`` names, while
    the implementation specs retain the curriculum ``content-a/b`` IDs.  The
    science J endpoint is a legacy stable ID kept for compatibility.  These
    aliases are endpoint resolution only; they never promote publisher status.
    """
    candidates = []
    if lesson_id.startswith("cur-"):
        suffix = lesson_id[4:]
        candidates.append("lesson-" + suffix)
        if suffix.endswith("-a") or suffix.endswith("-b"):
            subject, rest = suffix.split("-", 1)
            candidates.append(f"lesson-{subject}-content-root-{rest[-1]}")
        if suffix == "science-content-j":
            candidates.append("lesson-science-j")
    else:
        candidates.append(lesson_id)
    for candidate in candidates:
        if candidate in lessons:
            return lessons[candidate]
    return None


def main() -> int:
    lessons = load_lessons()
    sample_report = json.loads((ROOT / "implementation/reports/publisher-chapter-evidence-samples.json").read_text(encoding="utf-8"))
    sample_records = {str(item.get("lessonId")): item for item in sample_report.get("units", []) if isinstance(item, dict)}
    units = []
    status_counts = Counter()
    complete_records = Counter()
    chapter_sample_records = Counter()
    chapter_sample_units = set()
    blocked_units = Counter()
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        lesson_id = spec["lessonId"]
        lesson = resolve_lesson(lessons, lesson_id)
        lesson_data = lesson["data"] if lesson else {}
        sample = sample_records.get(lesson["data"]["id"]) if lesson else None
        if sample is None and lesson_id.startswith("cur-"):
            sample = sample_records.get("lesson-" + lesson_id[4:])
        if sample is None and lesson_id in {"cur-science-content-a", "cur-science-content-b"}:
            sample = sample_records.get("lesson-science-content-" + lesson_id[-1])
        records = {
            str(item.get("publisher", "")).lower(): item
            for item in lesson_data.get("publisherResearch", [])
            if isinstance(item, dict)
        }
        publishers = {}
        reasons = []
        has_all_chapter_samples = True
        for publisher in PUBLISHERS:
            evidence = spec.get("fusedScope", {}).get("publisherEvidence", {}).get(publisher, {})
            status = evidence.get("status", "missing")
            record = records.get(publisher, {})
            source_url = record.get("sourceUrl")
            locator = record.get("chapterLocator")
            publishers[publisher] = {
                "specStatus": status,
                "researchRecord": bool(record),
                "sourceUrlPresent": bool(str(source_url or "").strip()),
                "chapterLocatorPresent": bool(str(locator or "").strip()),
                "access": record.get("access"),
                "reviewedAt": record.get("reviewedAt"),
            }
            status_counts[status] += 1
            if record and source_url and locator:
                complete_records[publisher] += 1
            sample_source = next((item for item in (sample or {}).get("sources", []) if str(item.get("publisher", "")).lower() == publisher), {})
            sample_url = sample_source.get("sourceUrl")
            sample_locator = sample_source.get("locator")
            if sample_url and sample_locator:
                chapter_sample_records[publisher] += 1
            else:
                has_all_chapter_samples = False
            if status != "verified":
                reasons.append(f"{publisher}:spec-status={status}")
            if not record:
                reasons.append(f"{publisher}:missing-publisherResearch-record")
            elif not source_url or not locator:
                reasons.append(f"{publisher}:missing-sourceUrl-or-chapterLocator")
        if has_all_chapter_samples:
            chapter_sample_units.add(lesson_id)
        if not lesson:
            reasons.append("missing-lesson-endpoint")
        if reasons:
            blocked_units["publisher-evidence-pending"] += 1
        units.append({
            "lessonId": lesson_id,
            "specPath": str(path.relative_to(ROOT)),
            "lessonPath": lesson["path"] if lesson else None,
            "publishers": publishers,
            "chapterSampleRecord": bool(has_all_chapter_samples),
            "blockingReasons": reasons,
        })

    report = {
        "ledgerVersion": "1.0",
        "sourceBoundary": "This ledger separates chapter-level sample evidence from publisher fusion status; chapter samples never promote book-level-only to verified.",
        "unitCount": len(units),
        "publisherCount": len(PUBLISHERS),
        "specStatusCounts": dict(sorted(status_counts.items())),
        "researchRecordWithUrlAndChapterLocator": dict(sorted(complete_records.items())),
        "chapterSampleRecordsWithUrlAndLocator": dict(sorted(chapter_sample_records.items())),
        "chapterSampleUnitCount": len(chapter_sample_units),
        "blockedUnitCounts": dict(sorted(blocked_units.items())),
        "units": units,
    }
    out = ROOT / "implementation/reports/publisher-evidence-ledger.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "unitCount": len(units),
        "specStatusCounts": dict(sorted(status_counts.items())),
        "researchRecordWithUrlAndChapterLocator": dict(sorted(complete_records.items())),
        "chapterSampleRecordsWithUrlAndLocator": dict(sorted(chapter_sample_records.items())),
        "chapterSampleUnitCount": len(chapter_sample_units),
        "blockedUnits": sum(blocked_units.values()),
        "report": str(out),
    }, ensure_ascii=False))
    return 0 if len(units) == 1027 else 1


if __name__ == "__main__":
    raise SystemExit(main())
