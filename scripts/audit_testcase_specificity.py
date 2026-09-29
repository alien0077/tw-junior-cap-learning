#!/usr/bin/env python3
"""Report whether implementation test cases are unit-specific, without fabricating QA."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    signatures = Counter()
    subject_signatures = defaultdict(Counter)
    units = []
    for path in sorted((ROOT / "implementation/unit-specs").glob("*/*.yaml")):
        spec = yaml.safe_load(path.read_text(encoding="utf-8"))["unitImplementationSpec"]
        signature = tuple(spec["testCases"])
        signatures[signature] += 1
        subject_signatures[spec["subject"]][signature] += 1
        units.append(spec)
    repeated = sum(count for count in signatures.values() if count > 1)
    report = {
        "unitCount": len(units),
        "uniqueTestCaseSignatures": len(signatures),
        "repeatedTemplateUnits": repeated,
        "subjectUniqueSignatures": {subject: len(values) for subject, values in sorted(subject_signatures.items())},
        "status": "specificity-pending" if repeated else "specificity-ready",
        "note": "Repeated test-case wording is reported as a content/pedagogical review gap; this audit never promotes qaStatus.",
    }
    out = ROOT / "implementation/reports/testcase-specificity.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
