#!/usr/bin/env python3
"""Scoped first-pass QA for the eleven newly materialized Chinese child lessons."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [
    "ab-iv-1", "ab-iv-2", "ab-iv-3", "ab-iv-4", "ab-iv-5", "ab-iv-6", "ab-iv-7", "ab-iv-8",
    "ac-iv-1", "ac-iv-2", "ad-iv-1",
]
REQUIRED_PHASES = {"hook", "explain", "worked-example", "guided-practice", "transfer", "reflect"}


def main() -> int:
    rows = []
    for unit_id in TARGETS:
        path = ROOT / "lessons/chinese" / f"lesson-chinese-content-{unit_id}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        body = data["teaching"]["body"]
        full_text = " ".join([data["title"], data["content"]["summary"]] + [item["body"] for item in body])
        checks = {
            "unitTitleInTeaching": data["title"].split("：", 1)[0] in full_text,
            "sixTeachingPhases": {item["phase"] for item in body} == REQUIRED_PHASES,
            "phaseLengthAtLeast80": all(len(item["body"]) >= 80 for item in body),
            "contentHasCoreMisconceptionTransfer": len(data["content"]["sections"]) >= 3,
            "threePublisherResearchRecords": len(data["publisherResearch"]) == 3,
            "threeVersionResearchRecords": len(data["versionResearch"]) == 3,
            "fusionRecordPresent": bool(data["fusionRecord"].get("commonCore")) and bool(data["fusionRecord"].get("originalAdditions")),
            "interactiveHasThreeSteps": len(data["interactive"]["steps"]) >= 3,
            "interactiveOptionsAndFeedback": all(step["options"] and step["feedback"] for step in data["interactive"]["steps"]),
            "originalDraftBoundary": data["provenance"]["origin"] == "original" and data["reviewStatus"] == "draft",
        }
        rows.append({"unitId": unit_id, "file": str(path.relative_to(ROOT)), "checks": checks, "status": "pass" if all(checks.values()) else "fail"})
    failures = [row for row in rows if row["status"] == "fail"]
    report = {
        "scope": "eleven Chinese content child lessons materialized on 2026-09-08",
        "lessonCount": len(rows),
        "passed": len(rows) - len(failures),
        "failed": len(failures),
        "status": "pass" if not failures else "fail",
        "promotion": "none; full source reading, pedagogical review, copyright review and second-pass AI/Terra review remain separate gates",
        "items": rows,
    }
    out = ROOT / "implementation/reports/chinese-child-lesson-first-pass-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("lessonCount", "passed", "failed", "status", "promotion")}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
