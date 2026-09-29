#!/usr/bin/env python3
"""First-pass answer, solution, originality, and source QA for English 3-IV-2."""
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CACHE = {
    "cfsn=2995": ("yichang-114-1-third-exam-grade7.pdf", "downloaded"),
    "cfsn=3045": ("yichang-114-1-second-exam-grade7.pdf", "download-endpoint-returned-html"),
    "cfsn=2829": ("yichang-112-2-third-exam-grade7.pdf", "downloaded"),
}
EXPECTED = {
    1: ("cfsn=2995", "item 4", "D"),
    2: ("cfsn=2995", "item 1", "B"),
    3: ("cfsn=3045", "item 1", "C"),
    4: ("cfsn=3045", "item 18", "A"),
    5: ("cfsn=2829", "item 31", "D"),
    6: ("cfsn=2829", "item 30", "B"),
    7: ("cfsn=2829", "item 27", "A"),
    8: ("cfsn=2995", "item 31", "C"),
    9: ("cfsn=3045", "item 25", "D"),
    10: ("cfsn=3045", "item 17", "A"),
}


def main() -> int:
    errors = []
    rows = []
    unique_steps = set()
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text())
    catalog_urls = {source.get("url") for source in catalog.get("sources", [])}
    cache_root = ROOT / ".cache/public-exams/english-performance-3-iv-2"
    cache_audit = []
    for fragment, (filename, attempted_status) in CACHE.items():
        local_file = cache_root / filename
        valid_pdf = local_file.is_file() and local_file.read_bytes()[:5] == b"%PDF-"
        cache_audit.append({
            "urlFragment": fragment,
            "status": "cached-and-pdf-verified" if valid_pdf else attempted_status,
            "localPath": str(local_file.relative_to(ROOT)) if valid_pdf else None,
            "sha256": hashlib.sha256(local_file.read_bytes()).hexdigest() if valid_pdf else None,
        })
    for number, (url_fragment, locator_fragment, expected_answer) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-3-iv-2-{number}.json"
        data = json.loads(path.read_text()) if path.is_file() else {}
        issues = []
        options = data.get("options", [])
        ids = [option.get("id") for option in options]
        texts = [option.get("text", "").strip() for option in options]
        if len(options) != 4 or set(ids) != {"A", "B", "C", "D"} or len(set(texts)) != 4:
            issues.append("four-distinct-options-required")
        if data.get("answer", {}).get("value") != expected_answer or expected_answer not in set(ids):
            issues.append("answer-key-mismatch")
        if len(data.get("answer", {}).get("explanation", "")) < 55:
            issues.append("detailed-explanation-required")
        if len(data.get("solutionStrategy", "")) < 35:
            issues.append("specific-strategy-required")
        steps = data.get("solutionSteps", [])
        if len(steps) != 5 or any(len(step.strip()) < 30 for step in steps):
            issues.append("five-detailed-steps-required")
        for step in steps:
            if step in unique_steps:
                issues.append("duplicate-solution-step")
            unique_steps.add(step)
        refs = data.get("examPatternRefs", [])
        if len(refs) != 1:
            issues.append("one-item-level-ref-required")
        elif not (
            url_fragment in refs[0].get("url", "")
            and locator_fragment in refs[0].get("locator", "")
            and refs[0].get("status") == "recorded"
            and refs[0].get("locatorLevel") == "item"
            and refs[0].get("reuseDecision") == "pattern-only"
        ):
            issues.append("verified-item-pattern-ref-mismatch")
        if refs:
            if refs[0].get("url") not in catalog_urls:
                issues.append("source-catalog-entry-missing")
            if data.get("provenance", {}).get("sourceUrl") != refs[0].get("url"):
                issues.append("provenance-url-mismatch")
        if "未複製原題" not in data.get("provenance", {}).get("authoringNote", ""):
            issues.append("originality-boundary-missing")
        if data.get("reviewStatus") != "draft":
            issues.append("must-remain-draft")
        rows.append({"id": data.get("id", path.name), "issues": issues, "status": "pass" if not issues else "fail"})
        if issues:
            errors.append({"id": data.get("id", path.name), "issues": issues})

    report = {
        "unit": "3-IV-2",
        "checked": len(rows),
        "passed": len(rows) - len(errors),
        "uniqueSolutionSteps": len(unique_steps),
        "sourcePapers": 3,
        "sourceCache": cache_audit,
        "rows": rows,
        "failures": errors,
        "status": "pass" if len(rows) == 10 and not errors and len(unique_steps) == 50 else "fail",
        "scopeBoundary": "題目首輪契約檢查，不等同出版社版本融合、完整教材審查或教師審定。",
    }
    report_path = ROOT / "implementation/reports/english-performance-3-iv-2-first-pass.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("unit", "checked", "passed", "uniqueSolutionSteps", "sourcePapers", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
