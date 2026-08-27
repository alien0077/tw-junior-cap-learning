#!/usr/bin/env python3
"""Build an evidence-first queue for web-source comparison QA.

This script never changes lesson/question reviewStatus. It only records the
public source already declared by each draft item and the checks still needed.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "m4-web-review-queue.json"
items = []

for kind, pattern in (("lesson", "lessons/*/*.json"), ("question", "questions/*/*.json")):
    for path in sorted(ROOT.glob(pattern)):
        data = json.loads(path.read_text())
        if data.get("reviewStatus") != "draft":
            continue
        prov = data.get("provenance") or {}
        items.append({
            "id": data.get("id"),
            "kind": kind,
            "subject": data.get("subject"),
            "lessonId": data.get("lessonId", data.get("id")),
            "knowledgeIds": data.get("knowledgeIds", []),
            "sourceUrl": prov.get("sourceUrl"),
            "sourceLocator": prov.get("sourceLocator"),
            "reviewMethod": "web-source-comparison",
            "status": "pending-review",
            "checks": [
                "source-url-publicly-openable",
                "locator-identifies-relevant-curriculum",
                "claims-and-answer-match-source",
                "original-wording-and-copyright-safe",
            ],
        })

result = {
    "schemaVersion": "1.0.0",
    "generatedAt": "2026-08-27",
    "reviewMethod": "web-source-comparison",
    "policy": "Queue generation does not upgrade reviewStatus; each item needs recorded evidence.",
    "items": items,
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(f"queued {len(items)} draft items -> {OUT}")
