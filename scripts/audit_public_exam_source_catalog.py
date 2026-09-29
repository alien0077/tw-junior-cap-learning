#!/usr/bin/env python3
"""Ensure every question-level public source is represented in the catalog."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
    known = set(catalog.get("questionSourceUrls", []))
    source_counts = Counter()
    questions = 0
    for path in sorted((ROOT / "questions").rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for ref in data.get("examPatternRefs", []):
            source_counts[ref.get("url", "")] += 1
            questions += 1
    missing = sorted(url for url in source_counts if url not in known)
    report = {
        "status": "pass" if not missing else "blocked",
        "catalogEntries": len(catalog.get("sources", [])),
        "questionSourceUrls": len(source_counts),
        "questionRefs": questions,
        "catalogCoveredUrls": len(source_counts) - len(missing),
        "missingCatalogUrls": missing,
        "countsByUrl": dict(source_counts),
        "note": "Catalog membership proves only that the public source entry is registered; question-level item locator and content QA remain separate gates.",
    }
    out = ROOT / "implementation/reports/public-exam-source-catalog-audit.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "catalogEntries", "questionSourceUrls", "questionRefs", "catalogCoveredUrls", "missingCatalogUrls")}, ensure_ascii=False))
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
