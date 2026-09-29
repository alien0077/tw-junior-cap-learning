#!/usr/bin/env python3
"""Focused first-pass QA for original English 2-IV-7 question items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("104_34764", "question 36"),
    2: ("104_34764", "question 37"),
    3: ("104_64184", "question 4"),
    4: ("104_64184", "question 4"),
    5: ("1548635646492gsGMmT1l.pdf", "question 2"),
    6: ("104_34764", "question 49"),
    7: ("104_34764", "question 35"),
    8: ("104_64184", "question 10"),
    9: ("104_34764", "question 44"),
    10: ("104_64184", "question 7"),
}


def main() -> int:
    errors, rows, unique_steps = [], [], set()
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text())
    urls = {r.get("url") for r in catalog.get("sources", [])}
    schools = set()
    for n, (fragment, item_fragment) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-2-iv-7-{n}.json"
        data = json.loads(path.read_text()) if path.is_file() else {}
        issues = []
        options = data.get("options", [])
        ids = [o.get("id") for o in options]
        texts = [o.get("text", "").strip() for o in options]
        if len(options) != 4 or set(ids) != {"A", "B", "C", "D"} or len(set(texts)) != 4:
            issues.append("four-distinct-options-required")
        if data.get("answer", {}).get("value") not in set(ids):
            issues.append("answer-must-match-option")
        if len(data.get("answer", {}).get("explanation", "")) < 55:
            issues.append("detailed-explanation-required")
        if len(data.get("solutionStrategy", "")) < 35:
            issues.append("specific-strategy-required")
        steps = data.get("solutionSteps", [])
        if len(steps) != 5 or any(len(s.strip()) < 30 for s in steps):
            issues.append("five-detailed-steps-required")
        for step in steps:
            if step in unique_steps:
                issues.append("duplicate-solution-step")
            unique_steps.add(step)
        refs = data.get("examPatternRefs", [])
        if len(refs) != 1:
            issues.append("one-item-level-ref-required")
        elif not (fragment in refs[0].get("url", "") and item_fragment in refs[0].get("locator", "") and refs[0].get("status") == "recorded" and refs[0].get("locatorLevel") == "item" and refs[0].get("reuseDecision") == "pattern-only"):
            issues.append("verified-item-pattern-ref-mismatch")
        if refs and refs[0].get("url") not in urls:
            issues.append("source-catalog-entry-missing")
        if refs and data.get("provenance", {}).get("sourceUrl") != refs[0].get("url"):
            issues.append("provenance-url-mismatch")
        if "未複製原題" not in data.get("provenance", {}).get("authoringNote", ""):
            issues.append("originality-boundary-missing")
        if data.get("reviewStatus") != "draft":
            issues.append("must-remain-draft")
        if refs:
            schools.add(refs[0].get("title", "").split("國中")[0])
        if issues:
            errors.append({"id": data.get("id", path.name), "issues": issues})
        rows.append({"id": data.get("id", path.name), "issues": issues, "status": "pass" if not issues else "fail"})
    report = {
        "unit": "2-IV-7", "checked": len(rows), "passed": len(rows) - len(errors),
        "uniqueSolutionSteps": len(unique_steps), "sourceSchools": sorted(schools),
        "rows": rows, "failures": errors,
        "status": "pass" if len(rows) == 10 and not errors and len(unique_steps) == 50 else "fail",
        "scopeBoundary": "逐題契約首輪稽核，不代表三版本教材融合、發布級內容審查或人工教師審定。",
    }
    out = ROOT / "implementation/reports/english-performance-2-iv-7-first-pass.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("unit", "checked", "passed", "uniqueSolutionSteps", "sourceSchools", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
