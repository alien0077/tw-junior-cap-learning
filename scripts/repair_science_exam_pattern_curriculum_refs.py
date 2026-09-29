"""Separate curriculum references from the public-exam pattern ledger.

Four legacy science batches mixed curriculum anchors into ``examPatternRefs``.
The exam gate must contain traceable public exam sources, while curriculum
anchors belong in lesson/source evidence.  Keep recorded public-school exam
refs, remove only curriculum-only refs from this field, and normalize the
remaining paper-level locator.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITS = {"gc-iv-2", "gc-iv-3", "gc-iv-4", "inc-iv-6"}
CURRICULUM_MARKERS = ("課綱", "課程文件", "學習內容", "新舊課綱", "curriculum")
changed = []
removed = 0
for path in sorted((ROOT / "questions/science").glob("question-science-content-*.json")):
    stem = path.stem.removeprefix("question-science-content-")
    unit = stem.rsplit("-", 1)[0]
    if unit not in UNITS:
        continue
    item = json.loads(path.read_text(encoding="utf-8"))
    refs = item.get("examPatternRefs", [])
    kept = []
    touched = False
    for ref in refs:
        label = f"{ref.get('title', '')} {ref.get('locator', '')} {ref.get('url', '')}"
        if any(marker in label for marker in CURRICULUM_MARKERS):
            removed += 1
            touched = True
            continue
        if ref.get("status") == "recorded" and ref.get("locatorLevel") == "paper-or-curriculum":
            ref["locatorLevel"] = "paper"
            touched = True
        kept.append(ref)
    if touched:
        item["examPatternRefs"] = kept
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(str(path.relative_to(ROOT)))
report = {"status": "pass", "changedQuestionFiles": len(changed), "removedCurriculumOnlyRefs": removed, "units": sorted(UNITS), "rule": "examPatternRefs keeps traceable public exam sources; curriculum evidence remains in sourceRefs/studyReferences", "contentPolicy": "no exam wording, options, charts, or answers copied; lessons remain draft"}
(ROOT / "implementation/reports/science-exam-pattern-curriculum-ref-repair.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
