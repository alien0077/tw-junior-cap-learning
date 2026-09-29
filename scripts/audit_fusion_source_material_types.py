#!/usr/bin/env python3
"""Report whether publisher evidence records identify substantive source types.

This is a conservative inventory only. It never promotes publisher evidence or
claims that an identified source was fully read or fused.
"""
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "implementation/reports/publisher-chapter-evidence-samples.json"
OUTPUT = ROOT / "implementation/reports/fusion-source-material-type-audit.json"
PUBLISHERS = {"nani", "kanghsuan", "hanlin"}
NON_SUBSTANTIVE_MARKERS = (
    "course-plan", "curriculum-plan", "teaching-progress-plan",
    "sequence-record", "structure", "identifying-publisher-material",
)
DIRECT_MARKERS = (
    "publisher-textbook", "publisher-ebook", "publisher-chapter",
    "publisher-authored-lesson", "publisher-instructional-video",
)


def classify(source):
    kind = str(source.get("sourceKind", "")).lower()
    if "third-party-shared" in kind:
        return "third_party_shared_material_read_scope_recorded_provenance_unverified"
    if any(marker in kind for marker in NON_SUBSTANTIVE_MARKERS):
        return "locator_or_curriculum_context_only"
    if any(marker in kind for marker in DIRECT_MARKERS):
        return "publisher_material_type_identified_reading_unverified"
    return "substantive_material_not_demonstrated"


def main():
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    rows = []
    kind_counts = Counter()
    source_class_counts = Counter()
    triple_direct_candidates = 0
    for unit in data.get("units", []):
        by_publisher = {p: [] for p in PUBLISHERS}
        for source in unit.get("sources", []):
            publisher = source.get("publisher")
            if publisher not in PUBLISHERS:
                continue
            kind = source.get("sourceKind", "")
            classification = classify(source)
            kind_counts[kind or "(missing)"] += 1
            source_class_counts[classification] += 1
            by_publisher[publisher].append({
                "sourceKind": kind or None,
                "classification": classification,
                "sourceUrl": source.get("sourceUrl"),
                "locator": source.get("locator"),
                "accessedAt": source.get("accessedAt"),
            })
        complete_three = all(by_publisher[p] for p in PUBLISHERS)
        direct_three = complete_three and all(
            any(s["classification"] == "publisher_material_type_identified_reading_unverified"
                for s in by_publisher[p])
            for p in PUBLISHERS
        )
        triple_direct_candidates += int(direct_three)
        rows.append({
            "lessonId": unit.get("lessonId"),
            "title": unit.get("title"),
            "threePublishersHaveRecords": complete_three,
            "threePublishersHaveIdentifiedPublisherMaterialTypes": direct_three,
            "publisherSources": by_publisher,
            "fusionStatus": "not_proven_by_source_type_inventory",
        })
    report = {
        "updatedAt": date.today().isoformat(),
        "scope": "inventory of existing publisher chapter-sample records; no reading/fusion/status promotion inferred",
        "unitCount": len(rows),
        "sourceCount": sum(kind_counts.values()),
        "sourceKindCounts": dict(sorted(kind_counts.items())),
        "sourceClassCounts": dict(sorted(source_class_counts.items())),
        "threePublisherRecordUnits": sum(r["threePublishersHaveRecords"] for r in rows),
        "threePublisherDirectMaterialTypeCandidates": triple_direct_candidates,
        "warning": "A direct-material type label would still not prove the chapter was read or fused; each unit needs source-content review and an original fusion record.",
        "units": rows,
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "units"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
