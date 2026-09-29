#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    golden = json.loads((ROOT / "implementation/golden-reference.json").read_text(encoding="utf-8"))
    spec = yaml.safe_load((ROOT / "implementation/unit-specs/math/cur-math-content-a-8-1.yaml").read_text(encoding="utf-8"))["unitImplementationSpec"]
    block = spec["interactiveBlocks"][0]
    joined = " ".join(spec["coreConcepts"] + spec["learningGoals"] + spec["contentFlow"])
    checks = {
        "lessonId": spec["lessonId"] == golden["lessonId"],
        "kg": golden["knowledgeGraphIds"][0] in spec["knowledgeGraphIds"],
        "component": block["component"] == golden["requiredComponent"],
        "concepts": all(x in joined for x in golden["requiredConcepts"]),
        "formulas": all(x in spec["coreConcepts"] for x in golden["requiredFormulas"]),
        "predict": any("predict" in x for x in spec["contentFlow"]),
        "manipulate": any("manipulate" in x for x in spec["contentFlow"]),
        "observe": any("observe" in x for x in spec["contentFlow"]),
        "explain": any("explain" in x for x in spec["contentFlow"]),
        "transfer": any("transfer" in x for x in spec["contentFlow"]),
        # The golden block is already wired, but content/runtime QA is intentionally
        # still open. Preserve that real state instead of requiring the obsolete
        # pre-implementation value "missing".
        "status_preserved": spec["status"] == {"designStatus": "specified", "implementationStatus": "implemented", "qaStatus": "untested"},
    }
    out = ROOT / "implementation/reports/golden-reference.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"checks": checks, "passed": all(checks.values())}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(checks, ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
