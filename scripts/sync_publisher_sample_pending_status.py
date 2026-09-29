#!/usr/bin/env python3
"""Synchronize spec status with recorded chapter samples without promoting fusion."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
changed = 0
publisher_slots = 0
for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
    text = path.read_text(encoding="utf-8")
    old = text
    publisher_slots += text.count("status: book-level-only")
    text = text.replace("status: book-level-only", "status: pending")
    text = text.replace(
        "currentEvidenceStatus: curriculum-and-kg-grounded; publisher-unit-scope-pending",
        "currentEvidenceStatus: curriculum-and-kg-grounded; publisher-chapter-evidence-recorded; fusion-review-pending",
    )
    text = text.replace(
        "章節級證據完成前不得聲稱已完成版本融合",
        "章節級證據雖已記錄，融合審查前不得聲稱已完成版本融合",
    )
    if text != old:
        path.write_text(text, encoding="utf-8")
        changed += 1
print({"changedSpecFiles": changed, "publisherSlotsMovedToPending": publisher_slots})
