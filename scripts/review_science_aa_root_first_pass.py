#!/usr/bin/env python3
"""Verify AA-root question answers, detailed solutions and public-exam locators."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    "https://www.klm.kh.edu.tw/upload/310/101_83606/114-1-3%E8%87%AA8A.pdf",
    "https://www.pljhs.ntpc.edu.tw/var/file/0/1000/attach/86/pta_4170_158052_68738.pdf",
    "https://www.jhsh.ntpc.edu.tw/var/file/0/1000/attach/77/pta_22725_1030925_35628.pdf",
    "https://www.mljh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=240&cfsn=1060&name=112-2-8%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf&op=dlfile",
    "https://www.chhs.tp.edu.tw/uploads/1595570220266AAUtVeTk.pdf",
    "https://www.tcjh.tyc.edu.tw/uploads/1556760247155p1mmNx8J.pdf",
}


def main() -> int:
    failures: list[str] = []
    for n in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-aa-{n}.json"
        q = json.loads(path.read_text(encoding="utf-8"))
        refs = q.get("examPatternRefs", [])
        urls = {ref.get("url") for ref in refs}
        if q.get("reviewStatus") != "draft":
            failures.append(f"{q['id']}: record must remain draft")
        if len(refs) != 3 or len(urls) != 3 or not urls <= ALLOWED:
            failures.append(f"{q['id']}: expected three distinct official public-school papers")
        for i, ref in enumerate(refs):
            if ref.get("locatorLevel") != "item" or ref.get("status") != "recorded" or "第" not in ref.get("locator", ""):
                failures.append(f"{q['id']} ref {i}: exact item locator missing")
            if ref.get("reuseDecision") != "pattern-only" or ref.get("pattern") != ref.get("observedPattern"):
                failures.append(f"{q['id']} ref {i}: pattern-only observation contract failed")
        option_ids = {option["id"] for option in q.get("options", [])}
        if q.get("answer", {}).get("value") not in option_ids:
            failures.append(f"{q['id']}: answer key does not map to an option")
        steps = q.get("solutionSteps", [])
        if len(steps) != 5 or any(len(step.strip()) < 12 for step in steps):
            failures.append(f"{q['id']}: five substantive steps required")
        if len(q.get("answer", {}).get("explanation", "")) < 40:
            failures.append(f"{q['id']}: explanation must show the reasoning")
    report = {"unit": "Aa：物質組成與元素週期性", "questionCount": 10, "itemLevelSourceRefs": 30, "status": "pass" if not failures else "fail", "checks": ["three distinct public-school exam papers per question", "item-level pattern-only locator", "answer maps to choice", "five detailed solution steps", "draft retained"], "failures": failures, "reviewedAt": "2026-09-24"}
    (ROOT / "implementation/reports/science-aa-root-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
