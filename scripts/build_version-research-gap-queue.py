#!/usr/bin/env python3
"""Build an auditable queue for publisher-research gaps.

This report deliberately does not promote any lesson.  It separates missing
source locators from missing research fields so later work can add evidence
without confusing chapter metadata with actual version research.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READINESS = ROOT / "implementation/reports/version-research-readiness.json"
OUT = ROOT / "implementation/reports/version-research-gap-queue.json"


def main() -> None:
    data = json.loads(READINESS.read_text(encoding="utf-8"))
    queue = []
    by_subject = Counter()
    by_publisher = Counter()
    by_missing_field = Counter()
    by_kind = Counter()

    for unit in data["units"]:
        if unit.get("scope", "content") != "content":
            continue
        if unit.get("allThreeStructuredRecordsReady"):
            continue
        publishers = {}
        for publisher, details in unit.get("publisherDetails", {}).items():
            checks = details.get("checks", {})
            missing = sorted(key for key, value in checks.items() if not value)
            if not missing:
                continue
            locator = str(details.get("sourceLocator", ""))
            kind = "missing-source-url" if "url" in missing else "missing-research-field"
            if "url" in missing and len(missing) > 1:
                kind = "missing-url-and-research-field"
            publishers[publisher] = {
                "missing": missing,
                "sourceLocator": locator,
                "sourceStatus": unit.get("sourceStatus", "research-record-incomplete"),
                "nextAction": (
                    "Locate a legally readable publisher chapter/page or official chapter-level index; "
                    "then record URL, locator, review date, and original research notes."
                    if "url" in missing
                    else "Re-read the located source and fill every missing research field; do not copy textbook prose."
                ),
            }
            by_publisher[publisher] += 1
            by_kind[kind] += 1
            for field in missing:
                by_missing_field[f"{publisher}.{field}"] += 1
        if publishers:
            subject = unit.get("subject", "unknown")
            by_subject[subject] += 1
            queue.append(
                {
                    "lessonId": unit["lessonId"],
                    "subject": subject,
                    "title": unit.get("title", ""),
                    "sourceStatus": unit.get("sourceStatus", "research-record-incomplete"),
                    "publisherGaps": publishers,
                    "releaseDecision": "keep-draft-until-all-three-publishers-have-source-and-research-QA",
                }
            )

    result = {
        "updatedAt": "2026-09-07",
        "purpose": "逐單元列出版本研究缺口；不把章節名稱或書冊存在性提升為完整教材研究。",
        "source": "implementation/reports/version-research-readiness.json",
        "summary": {
            "queuedLessons": len(queue),
            "excludedFrameworkLessons": sum(1 for unit in data["units"] if unit.get("scope") == "framework"),
            "subjectCounts": dict(sorted(by_subject.items())),
            "publisherGapCounts": dict(sorted(by_publisher.items())),
            "gapKindCounts": dict(sorted(by_kind.items())),
            "missingFieldCounts": dict(sorted(by_missing_field.items())),
            "allQueuedLessonsRemainDraft": True,
            "frameworkExclusionRule": "performance/domain nodes are tracked separately and are not treated as version-fused content lessons",
        },
        "queue": queue,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
