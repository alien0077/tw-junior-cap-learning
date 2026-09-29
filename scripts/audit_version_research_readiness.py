#!/usr/bin/env python3
"""Inventory version-research records without promoting release status.

The report separates structured research readiness from actual chapter-level
source review. It deliberately never changes publisherEvidence.status.
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLISHERS = ("nani", "kanghsuan", "hanlin")
PUBLISHER_ALIASES = {"jiayin-hanlin": "hanlin"}
FINDING_KEYS = ("concepts", "representations", "examplesOrEvidence", "misconceptions", "assessmentEmphasis")


def has_url(text):
    return bool(re.search(r"https?://", str(text or "")))


def inspect(item):
    records = {
        PUBLISHER_ALIASES.get(r.get("publisher"), r.get("publisher")): r
        for r in item.get("versionResearch", [])
    }
    details = {}
    for publisher in PUBLISHERS:
        record = records.get(publisher, {})
        findings = record.get("findings", {}) or {}
        checks = {
            "url": has_url(record.get("sourceLocator")),
            "reviewedAt": bool(record.get("reviewedAt")),
            "concepts": bool(findings.get("concepts")),
            "representations": bool(findings.get("representations")),
            "examplesOrEvidence": bool(findings.get("examplesOrEvidence")),
            "misconceptions": bool(findings.get("misconceptions")),
            "assessmentEmphasis": bool(findings.get("assessmentEmphasis")),
            "licenseBoundary": bool(record.get("licenseBoundary")),
        }
        details[publisher] = {"ready": all(checks.values()), "checks": checks, "sourceLocator": record.get("sourceLocator", "")}
    return details


def scope_for(lesson_id):
    lesson_id = str(lesson_id or "")
    if "-performance" in lesson_id or "-domain" in lesson_id:
        return "framework"
    return "content"


def main():
    units = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        try:
            item = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        if item.get("subject") not in {"chinese", "english", "math", "science", "social"}:
            continue
        details = inspect(item)
        all_ready = all(details[p]["ready"] for p in PUBLISHERS)
        units.append({
            "lessonId": item.get("id"),
            "subject": item.get("subject"),
            "title": item.get("title"),
            "scope": scope_for(item.get("id")),
            "allThreeStructuredRecordsReady": all_ready,
            "publisherDetails": details,
            "sourceStatus": "research-record-ready-pending-chapter-fusion-review" if all_ready else "research-record-incomplete",
        })
    summary = {
        "lessonCount": len(units),
        "allThreeStructuredRecordsReady": sum(u["allThreeStructuredRecordsReady"] for u in units),
        "incompleteStructuredRecords": sum(not u["allThreeStructuredRecordsReady"] for u in units),
        "contentScope": {
            "lessonCount": sum(u["scope"] == "content" for u in units),
            "ready": sum(u["scope"] == "content" and u["allThreeStructuredRecordsReady"] for u in units),
            "incomplete": sum(u["scope"] == "content" and not u["allThreeStructuredRecordsReady"] for u in units),
        },
        "frameworkScope": {
            "lessonCount": sum(u["scope"] == "framework" for u in units),
            "note": "performance/domain nodes are curriculum framework records, not version-fused content lessons",
        },
        "publisherEvidencePromotion": "none; publisherEvidence.status remains unchanged",
        "note": "Readiness is field-and-source inventory only. It does not prove the model read the full publisher chapter, does not prove chapter-level locator quality, and does not replace fusion/content/copyright review.",
    }
    out = {"updatedAt": date.today().isoformat(), "summary": summary, "units": units}
    report = ROOT / "implementation" / "reports" / "version-research-readiness.json"
    report.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
