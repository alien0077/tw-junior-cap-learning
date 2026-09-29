#!/usr/bin/env python3
"""Unit-scoped answer, solution and item-level exam provenance contract."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "https://www.nhjh.tp.edu.tw/uploads/1659511832163bbfokDfl.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E7%90%86%E5%8C%96_1.pdf",
    "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%87%AA%E7%84%B6/108-2-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6%E7%A7%91%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf",
    "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/22%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%87%AA%E7%84%B6/104-2-3%202%E5%B9%B4%E5%8F%8A%E8%87%AA%E7%84%B6%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw",
}
BIHUA_LOCATORS = {
    "question-science-content-jf-iv-2-4": "校方附件「114-2-3-八年級理化試題卷.pdf」第2頁第14題",
    "question-science-content-jf-iv-2-7": "校方附件「114-2-3-八年級理化試題卷.pdf」第3頁第18題",
    "question-science-content-jf-iv-2-8": "校方附件「114-2-3-八年級理化試題卷.pdf」第3頁第23題",
}


def main() -> int:
    errors: list[str] = []
    checked = 0
    source_ref_count = 0
    for number in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-jf-iv-2-{number}.json"
        item = json.loads(path.read_text(encoding="utf-8"))
        checked += 1
        refs = item.get("examPatternRefs", [])
        urls = {ref.get("url") for ref in refs}
        source_ref_count += len(refs)
        if item.get("reviewStatus") != "draft":
            errors.append(f"{item['id']}: must remain draft")
        if len(refs) < 3 or len(urls) < 3 or not urls <= EXPECTED:
            errors.append(f"{item['id']}: expected at least three verified public-school exam sources")
        for index, ref in enumerate(refs):
            if ref.get("locatorLevel") != "item" or ref.get("status") != "recorded":
                errors.append(f"{item['id']} ref {index}: missing recorded item-level locator")
            if not any(token in ref.get("locator", "") for token in ("第", "題")):
                errors.append(f"{item['id']} ref {index}: locator does not identify an item")
            if ref.get("reuseDecision") != "pattern-only" or ref.get("pattern") != ref.get("observedPattern"):
                errors.append(f"{item['id']} ref {index}: reuse or observed-pattern contract failed")
        expected_bihua_locator = BIHUA_LOCATORS.get(item["id"])
        bihua_refs = [ref for ref in refs if ref.get("url") == "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw"]
        if expected_bihua_locator:
            if len(bihua_refs) != 1 or bihua_refs[0].get("locator") != expected_bihua_locator:
                errors.append(f"{item['id']}: verified Bihua item locator missing or mismatched")
        elif bihua_refs:
            errors.append(f"{item['id']}: unexpected Bihua source mapping")
        option_ids = {option["id"] for option in item.get("options", [])}
        if item.get("answer", {}).get("value") not in option_ids:
            errors.append(f"{item['id']}: answer does not identify an option")
        if len(item.get("solutionSteps", [])) != 5 or any(len(step.strip()) < 8 for step in item.get("solutionSteps", [])):
            errors.append(f"{item['id']}: five substantive solution steps required")
        if len(item.get("answer", {}).get("explanation", "")) < 35:
            errors.append(f"{item['id']}: answer explanation is too short")
    report = {
        "unit": "Jf-Ⅳ-2：常見烷類、醇類、有機酸與酯類",
        "questionCount": checked,
        "sourceRefs": source_ref_count,
        "status": "pass" if not errors else "fail",
        "checks": ["three official public-school exam papers per question", "item-level locator", "pattern-only attribution", "answer maps to option", "substantive five-step solution", "draft status retained"],
        "failures": errors,
        "reviewedAt": "2026-09-24",
    }
    out = ROOT / "implementation/reports/science-jf-iv-2-first-pass-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
