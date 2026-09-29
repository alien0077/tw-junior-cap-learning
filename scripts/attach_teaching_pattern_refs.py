#!/usr/bin/env python3
"""將互動教學參照 ledger 逐課接到 unit spec，保留 draft/QA 狀態。"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = ROOT / "implementation" / "unit-specs"
REF_IDS = ("phet-ild", "phet-activity", "w3c-aria", "w3c-landmarks")


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> int:
    changed = 0
    skipped = 0
    failures: list[str] = []
    for path in sorted(SPEC_ROOT.glob("**/*.yaml")):
        text = path.read_text(encoding="utf-8")
        if "  teachingPatternRefs:" in text:
            skipped += 1
            continue
        title_match = re.search(r"^  title: (.+)$", text, flags=re.MULTILINE)
        component_match = re.search(r"^    component: (.+)$", text, flags=re.MULTILINE)
        if not title_match or not component_match or "  capTransfer:\n" not in text:
            failures.append(str(path.relative_to(ROOT)))
            continue
        title = title_match.group(1).strip().strip("'")
        component = component_match.group(1).strip()
        lines = [
            "  teachingPatternRefs:",
            *[line for ref_id in REF_IDS for line in (
                f"  - refId: {ref_id}",
                "    reuseDecision: inspiration-only",
                f"    application: {yaml_string(f'本課「{title}」的 {component} 只吸收預測、操作、證據表達或可及性呈現方法；資料、文字、題目與視覺內容由本課自行設計。')}",
            )],
        ]
        block = "\n".join(lines) + "\n"
        path.write_text(text.replace("  capTransfer:\n", block + "  capTransfer:\n", 1), encoding="utf-8")
        changed += 1
    report = {
        "status": "pass" if not failures else "fail",
        "specFiles": changed + skipped + len(failures),
        "changed": changed,
        "alreadyHadRefs": skipped,
        "failureCount": len(failures),
        "referenceIds": list(REF_IDS),
        "failures": failures,
        "boundary": "metadata linkage only; does not promote publisher, content or QA status",
    }
    out = ROOT / "implementation" / "reports" / "teaching-pattern-ref-attachment.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "specFiles", "changed", "alreadyHadRefs", "failureCount")}, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
