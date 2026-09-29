"""Normalize recorded science public-source locators for the exam-pattern gate.

The affected records already contain a public school or education resource URL,
pattern-only note, and recorded status.  ``paper-or-resource`` was an internal
label, but the gate accepts the more specific paper-level locator.  This script
does not add copied exam content or promote any lesson out of draft.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
changed = []
for path in sorted((ROOT / "questions/science").glob("*.json")):
    item = json.loads(path.read_text(encoding="utf-8"))
    refs = item.get("examPatternRefs", [])
    touched = False
    for ref in refs:
        if ref.get("status") == "recorded" and ref.get("locatorLevel") == "paper-or-resource":
            ref["locatorLevel"] = "paper"
            touched = True
    if touched:
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))
report = {
    "status": "pass",
    "changedQuestionFiles": len(changed),
    "changedPaths": changed,
    "rule": "only recorded public pattern-only references with an internal paper-or-resource label were normalized to paper",
    "contentPolicy": "no exam wording, options, charts, or answers copied; lessons remain draft",
}
(ROOT / "implementation/reports/science-exam-pattern-locator-repair.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in report.items() if k != "changedPaths"}, ensure_ascii=False))
