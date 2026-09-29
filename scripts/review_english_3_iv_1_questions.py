#!/usr/bin/env python3
"""First-pass item, answer, solution, and provenance QA for English 3-IV-1."""
import json
import hashlib
from pathlib import Path
from rewrite_english_3_iv_1_questions import DASHE, SOURCES, XIAOGANG, YICHANG109, YICHANG110

ROOT = Path(__file__).resolve().parents[1]
CACHE = {
    YICHANG110: ("yichang-110-1-grade7-english.pdf", "downloaded-and-verified"),
    YICHANG109: ("yichang-109-1-grade7-english.pdf", "downloaded-and-verified"),
    DASHE: ("dashe-grade7-english.pdf", "downloaded-and-verified"),
    XIAOGANG: ("xiaogang-111-1-grade7-english.pdf", "download-timeout-20s"),
}
EXPECTED = {
    1: ("hkjh.kh.edu.tw", "item 1", "C"),
    2: ("hkjh.kh.edu.tw", "item 2", "A"),
    3: ("hkjh.kh.edu.tw", "item 3", "D"),
    4: ("ycjh.hlc.edu.tw", "item 1", "B"),
    5: ("ycjh.hlc.edu.tw", "item 2", "C"),
    6: ("ycjh.hlc.edu.tw", "item 3", "D"),
    7: ("dam.kh.edu.tw", "item 1", "A"),
    8: ("dam.kh.edu.tw", "item 2", "B"),
    9: ("ycjh.hlc.edu.tw", "question 21", "C"),
    10: ("ycjh.hlc.edu.tw", "question 22", "B"),
}


def main() -> int:
    errors = []
    rows = []
    steps_seen = set()
    urls = set()
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text())
    catalog_urls = {row.get("url") for row in catalog.get("sources", [])}
    source_cache = []
    cache_root = ROOT / ".cache/public-exams/english-performance-3-iv-1"
    for url, (filename, attempt_status) in CACHE.items():
        cached_file = cache_root / filename
        exists = cached_file.is_file()
        source_cache.append({
            "url": url,
            "school": SOURCES[url][0],
            "localPath": str(cached_file.relative_to(ROOT)) if exists else None,
            "status": "cached" if exists else attempt_status,
            "sha256": hashlib.sha256(cached_file.read_bytes()).hexdigest() if exists else None,
        })
    for number, (host, locator_fragment, expected_answer) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-3-iv-1-{number}.json"
        data = json.loads(path.read_text()) if path.is_file() else {}
        issues = []
        options = data.get("options", [])
        ids = [item.get("id") for item in options]
        texts = [item.get("text", "").strip() for item in options]
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
            if step in steps_seen:
                issues.append("duplicate-solution-step")
            steps_seen.add(step)
        refs = data.get("examPatternRefs", [])
        if len(refs) != 1:
            issues.append("one-item-level-ref-required")
        elif not (
            host in refs[0].get("url", "")
            and locator_fragment in refs[0].get("locator", "")
            and refs[0].get("status") == "recorded"
            and refs[0].get("locatorLevel") == "item"
            and refs[0].get("reuseDecision") == "pattern-only"
        ):
            issues.append("verified-item-pattern-ref-mismatch")
        if refs:
            urls.add(refs[0].get("url", ""))
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
        "unit": "3-IV-1",
        "checked": len(rows),
        "passed": len(rows) - len(errors),
        "uniqueSolutionSteps": len(steps_seen),
        "sourceUrls": len(urls),
        "sourceCache": source_cache,
        "rows": rows,
        "failures": errors,
        "status": "pass" if len(rows) == 10 and not errors and len(steps_seen) == 50 else "fail",
        "scopeBoundary": "題目首輪契約稽核；不等同三版本教材融合、發布級內容審查或教師審定。",
    }
    report_path = ROOT / "implementation/reports/english-performance-3-iv-1-first-pass.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("unit", "checked", "passed", "uniqueSolutionSteps", "sourceUrls", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
