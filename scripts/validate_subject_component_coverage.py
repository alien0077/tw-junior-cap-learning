#!/usr/bin/env python3
"""Validate the guide's subject-appropriate active interaction coverage."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "chinese": {"TextEvidenceBlock"},
    "english": {"LanguageTimelineBlock", "TextEvidenceBlock", "DataExplorerBlock", "SignageReadingLab", "GenreReadingBlock"},
    "math": {"FunctionRepresentationBlock", "GeometryManipulationBlock", "DataExplorerBlock", "AlgebraBalanceBlock", "NumberLineBlock", "StepwiseReasoningBlock"},
    "science": {"PhenomenonSimulationBlock", "ParticleModelBlock", "SystemRelationshipBlock", "EarthSystemBlock", "EvidenceLabBlock"},
    "social": {"TimelineCausalBlock", "MapDataBlock", "ScenarioDecisionBlock"},
}


def main() -> int:
    counts = defaultdict(Counter)
    errors = []
    curriculum_ids = set()
    for curriculum_path in (ROOT / "curriculum").glob("*/*.json"):
        obj = json.loads(curriculum_path.read_text(encoding="utf-8"))
        if isinstance(obj, dict) and str(obj.get("id", "")).startswith("cur-"):
            curriculum_ids.add(obj["id"])
    curriculum_unit_count = 0
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        # Direct supplemental specs intentionally live beside curriculum-backed specs,
        # but this validator measures the 1027 curriculum implementation units only.
        if spec.get("lessonId") not in curriculum_ids:
            continue
        curriculum_unit_count += 1
        subject = spec["subject"]
        components = [block["component"] for block in spec["interactiveBlocks"]]
        counts[subject].update(components)
        unexpected = sorted(set(components) - EXPECTED.get(subject, set()))
        if unexpected:
            errors.append({"lessonId": spec["lessonId"], "subject": subject, "unexpected": unexpected})
        if not components:
            errors.append({"lessonId": spec["lessonId"], "subject": subject, "unexpected": ["no component"]})
    report = {
        "expected": {key: sorted(value) for key, value in EXPECTED.items()},
        "counts": {key: dict(value) for key, value in sorted(counts.items())},
        "errors": errors,
        "unitCount": curriculum_unit_count,
        "status": "passed" if not errors and set(counts) == set(EXPECTED) and curriculum_unit_count == 1027 else "failed",
        "note": "Coverage mapping only; component implementation and unit-specific pedagogical content remain separate gates.",
    }
    out = ROOT / "implementation/reports/subject-component-coverage.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"unitCount": report["unitCount"], "errors": len(errors), "status": report["status"]}, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
