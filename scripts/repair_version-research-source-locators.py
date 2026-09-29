#!/usr/bin/env python3
"""Repair versionResearch locators using the same lesson's existing sourceUrl.

This is a traceability repair only.  It does not create findings, alter
reviewStatus, or promote publisherEvidence.  A URL is copied only when the
same publisher already has a sourceUrl in publisherResearch for that lesson.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/version-research-source-locator-repair.json"


def main() -> None:
    scanned = 0
    changed = []
    records_changed = 0
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        if item.get("subject") not in {"chinese", "english", "math", "science", "social"}:
            continue
        scanned += 1
        publisher_urls = {
            record.get("publisher"): record.get("sourceUrl")
            for record in item.get("publisherResearch", [])
            if record.get("publisher") and isinstance(record.get("sourceUrl"), str) and record.get("sourceUrl").startswith("http")
        }
        file_records = []
        for record in item.get("versionResearch", []):
            publisher = record.get("publisher")
            url = publisher_urls.get(publisher)
            locator = str(record.get("sourceLocator", ""))
            if url and "http://" not in locator and "https://" not in locator:
                record["sourceLocator"] = f"{url}；{locator}" if locator else url
                file_records.append(publisher)
                records_changed += 1
        if file_records:
            path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append({"file": str(path.relative_to(ROOT)), "publishers": file_records})
    result = {
        "updatedAt": "2026-09-07",
        "scannedLessons": scanned,
        "changedLessons": len(changed),
        "changedRecords": records_changed,
        "evidenceRule": "only same-lesson publisherResearch.sourceUrl is reused; no new source is inferred",
        "statusRule": "reviewStatus and publisherEvidence are unchanged",
        "changed": changed,
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "changed"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
