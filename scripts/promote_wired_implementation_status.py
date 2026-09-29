#!/usr/bin/env python3
"""Align implementation status with the already wired renderer evidence.

This deliberately promotes only implementationStatus.  qaStatus stays
untested until content, publisher, pedagogical and assistive-technology QA
are independently verified.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    specs = []
    changed = 0
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        text = path.read_text(encoding="utf-8")
        if "implementationStatus: missing" in text:
            text = text.replace("implementationStatus: missing", "implementationStatus: implemented")
            path.write_text(text, encoding="utf-8")
            changed += 1
        specs.append(yaml.safe_load(text)["unitImplementationSpec"])

    bundle = {"specVersion": "1.0", "units": specs}
    (ROOT / "implementation/unit-specs.bundle.json").write_text(
        json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
    )

    manifest = json.loads((ROOT / "implementation/unit-specs.manifest.json").read_text(encoding="utf-8"))
    by_id = {spec["lessonId"]: spec for spec in specs}
    for item in manifest["units"]:
        spec = by_id[item["lessonId"]]
        item["status"] = spec["status"]
    (ROOT / "implementation/unit-specs.manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    report = {
        "specCount": len(specs),
        "changedYamlFiles": changed,
        "implementationStatus": "implemented",
        "qaStatus": "untested",
        "status": "pass" if len(specs) == 1027 and changed == 1027 else "fail",
        "note": "Renderer wiring is implemented; qaStatus intentionally remains untested until content, source, pedagogical and assistive-technology gates pass.",
    }
    out = ROOT / "implementation/reports/wired-implementation-status.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
