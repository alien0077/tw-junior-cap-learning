#!/usr/bin/env python3
"""First-pass content/provenance contract for the rewritten 2-IV-6 items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("104_64184", "question 6"),
    2: ("104_64184", "question 1"),
    3: ("104_64184", "question 3"),
    4: ("104_64184", "question 4"),
    5: ("Logo_990.pdf", "question 1"),
    6: ("104_64184", "question 7"),
    7: ("42022-1-27-13-49-5-nf1.pdf", "question 36"),
    8: ("Logo_990.pdf", "question 13"),
    9: ("Logo_990.pdf", "question 30"),
    10: ("104_64184", "question 7"),
}


def main() -> int:
    failures = []
    rows = []
    steps_seen = {}
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
    catalog_urls = {row.get("url") for row in catalog.get("sources", [])}
    for number, (url_fragment, locator_fragment) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-2-iv-6-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8")) if path.is_file() else {}
        issues = []
        if not data:
            issues.append("missing-question")
        else:
            options = data.get("options", [])
            keys = {option.get("id") for option in options}
            if len(options) != 4 or len({option.get("text", "").strip() for option in options}) != 4:
                issues.append("four-unique-options-required")
            if data.get("answer", {}).get("value") not in keys:
                issues.append("answer-option-mismatch")
            if len(data.get("answer", {}).get("explanation", "").strip()) < 35:
                issues.append("detailed-explanation-required")
            if len(data.get("solutionStrategy", "").strip()) < 24:
                issues.append("specific-strategy-required")
            steps = data.get("solutionSteps", [])
            if len(steps) != 5 or any(len(step.strip()) < 20 for step in steps):
                issues.append("five-detailed-steps-required")
            for step in steps:
                if step in steps_seen:
                    issues.append(f"reused-step:{steps_seen[step]}")
                else:
                    steps_seen[step] = data.get("id")
            refs = data.get("examPatternRefs", [])
            if len(refs) != 1:
                issues.append("exactly-one-item-source-required")
            if not any(
                url_fragment in ref.get("url", "")
                and locator_fragment in ref.get("locator", "")
                and ref.get("status") == "recorded"
                and ref.get("locatorLevel") == "item"
                and ref.get("reuseDecision") == "pattern-only"
                for ref in refs
            ):
                issues.append("exact-recorded-item-pattern-ref-required")
            if refs and refs[0].get("url") not in catalog_urls:
                issues.append("source-not-in-catalog")
            provenance = data.get("provenance", {})
            if refs and provenance.get("sourceUrl") != refs[0].get("url"):
                issues.append("provenance-source-mismatch")
            if data.get("reviewStatus") != "draft":
                issues.append("must-remain-draft")
            if "未複製原題" not in provenance.get("authoringNote", ""):
                issues.append("originality-boundary-missing")
        if issues:
            failures.append({"id": data.get("id", path.name), "issues": issues})
        rows.append({"id": data.get("id", path.name), "status": "pass" if not issues else "fail", "issues": issues})

    report = {
        "unit": "2-IV-6",
        "checked": len(rows),
        "passed": len(rows) - len(failures),
        "uniqueSolutionSteps": len(steps_seen),
        "sourceInstitutions": ["高雄市立大灣國中", "臺北市立內湖國中"],
        "rows": rows,
        "failures": failures,
        "status": "pass" if len(rows) == 10 and not failures and len(steps_seen) == 50 else "fail",
        "scopeBoundary": "首輪檢查本單元十題之答案、詳解、來源題號、原創界線與 draft 狀態；不代表版本融合、lesson 完整度、螢幕閱讀器或最終發布審核完成。",
    }
    out = ROOT / "implementation/reports/english-performance-2-iv-6-first-pass.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("unit", "checked", "passed", "uniqueSolutionSteps", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
