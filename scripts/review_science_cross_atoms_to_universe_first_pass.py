#!/usr/bin/env python3
"""Verify item-level source, answer, explanation, and uniqueness contracts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("1675416611615Uti9exJs.pdf", "question 8"),
    2: ("1675416611615Uti9exJs.pdf", "question 11"),
    3: ("1675416611615Uti9exJs.pdf", "question 7"),
    4: ("1675416611615Uti9exJs.pdf", "question 9"),
    5: ("1675416611615Uti9exJs.pdf", "question 12"),
    6: ("www.dwm.kh.edu.tw", "question 27"),
    7: ("www.kcjh.kh.edu.tw", "question 36"),
    8: ("www.dwm.kh.edu.tw", "question 28"),
    9: ("www.dwm.kh.edu.tw", "question 33"),
    10: ("www.dwm.kh.edu.tw", "question 26"),
}


def main() -> int:
    failures = []
    rows = []
    steps_seen = {}
    for number, (filename, item_locator) in EXPECTED.items():
        path = ROOT / f"questions/science/question-science-content-cross-atoms-to-universe-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
        issues = []
        if not data:
            issues.append("missing-file")
        else:
            options = data.get("options", [])
            option_ids = {option.get("id") for option in options}
            if len(options) != 4 or len({option.get("text", "").strip() for option in options}) != 4:
                issues.append("four-unique-options-required")
            if data.get("answer", {}).get("value") not in option_ids:
                issues.append("answer-option-mismatch")
            if len(data.get("answer", {}).get("explanation", "").strip()) < 40:
                issues.append("detailed-explanation-required")
            if len(data.get("solutionStrategy", "").strip()) < 25:
                issues.append("specific-strategy-required")
            steps = data.get("solutionSteps", [])
            if len(steps) != 5 or any(len(step.strip()) < 20 for step in steps):
                issues.append("five-detailed-steps-required")
            for step in steps:
                if step in steps_seen:
                    issues.append(f"step-reused:{steps_seen[step]}")
                else:
                    steps_seen[step] = data.get("id")
            refs = data.get("examPatternRefs", [])
            if len(refs) != 1:
                issues.append("exactly-one-reviewed-source-required")
            if not any(
                filename in ref.get("url", "")
                and item_locator in ref.get("locator", "")
                and ref.get("status") == "recorded"
                and ref.get("locatorLevel") == "item"
                and ref.get("reuseDecision") == "pattern-only"
                for ref in refs
            ):
                issues.append("exact-item-level-pattern-ref-required")
            provenance = data.get("provenance", {})
            if provenance.get("sourceUrl") != (refs[0].get("url") if refs else None):
                issues.append("source-provenance-mismatch")
            if data.get("reviewStatus") != "draft":
                issues.append("must-remain-draft")
            if "沒有複製原題" not in provenance.get("authoringNote", ""):
                issues.append("originality-boundary-missing")
        if issues:
            failures.append({"question": number, "issues": issues})
        rows.append({"question": number, "status": "pass" if not issues else "fail", "itemLocator": item_locator, "issues": issues})

    report = {
        "unit": "science-content-cross-atoms-to-universe",
        "checked": len(rows),
        "passed": len(rows) - len(failures),
        "uniqueSolutionSteps": len(steps_seen),
        "sourceInstitutions": ["臺北市立內湖國中", "高雄市立大灣國中", "高雄市立國昌國中"],
        "rows": rows,
        "failures": failures,
        "status": "pass" if len(rows) == 10 and not failures and len(steps_seen) == 50 else "fail",
        "scopeBoundary": "核對本輪十題的來源題號、答案欄位、詳解步驟、原創界線及 draft 狀態；不代表出版社版本融合、lesson 完整度或最終發布 QA 已完成。",
    }
    out = ROOT / "implementation/reports/science-cross-atoms-to-universe-first-pass.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("unit", "checked", "passed", "uniqueSolutionSteps", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
