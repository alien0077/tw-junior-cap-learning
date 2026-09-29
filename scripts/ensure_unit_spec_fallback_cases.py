#!/usr/bin/env python3
"""Add a unit-specific external-resource fallback case to every spec."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    changed = 0
    specs = []
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        text = path.read_text(encoding="utf-8")
        spec = yaml.safe_load(text)["unitImplementationSpec"]
        if not any("fallback" in str(case).lower() for case in spec.get("testCases", [])):
            title = spec["title"]
            component = spec["interactiveBlocks"][0]["component"]
            case = f"外部資料失效時，{component} 仍須以「{title}」的文字與資料 fallback 完成預測、操作、觀察、解釋與 transfer，不得阻塞本課。"
            marker = "  definitionOfDone:\n"
            if marker not in text:
                raise RuntimeError(f"missing definitionOfDone marker: {path}")
            text = text.replace(marker, f"  - {case}\n{marker}", 1)
            path.write_text(text, encoding="utf-8")
            changed += 1
        specs.append(yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"])

    bundle = {"specVersion": "1.0", "units": specs}
    (ROOT / "implementation/unit-specs.bundle.json").write_text(
        json.dumps(bundle, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8"
    )
    manifest = json.loads((ROOT / "implementation/unit-specs.manifest.json").read_text(encoding="utf-8"))
    by_id = {s["lessonId"]: s for s in specs}
    for item in manifest["units"]:
        item["status"] = by_id[item["lessonId"]]["status"]
    (ROOT / "implementation/unit-specs.manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {"specCount": len(specs), "changedYamlFiles": changed, "fallbackCases": len(specs), "status": "pass" if len(specs) == 1027 else "fail", "note": "Fallback cases are unit-specific and do not promote qaStatus."}
    (ROOT / "implementation/reports/unit-spec-fallback-cases.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
