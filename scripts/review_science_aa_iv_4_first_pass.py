#!/usr/bin/env python3
"""Verify Aa-IV-4 answers, worked reasoning, and exact public-exam items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    "neihu": "https://www.nhjh.tp.edu.tw/uploads/1706771265848lZjHm7hJ.pdf",
    "dawan": "https://www.dwm.kh.edu.tw/upload/344/104_64184/114%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
    "fuhe": "https://www.fhjh.ntpc.edu.tw/var/file/0/1000/img/156/149796265.pdf",
    "kc114": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E7%90%86%E5%8C%96_2.pdf",
    "tnfsh": "https://www.tnfsh.tn.edu.tw/df_ufiles/256/108-%E8%A4%87%E9%81%B82-%E6%95%B8%E7%90%86%E8%B3%87%E5%84%AA%E7%8F%AD-%E5%8C%96%E5%AD%B8%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
}
EXPECTED = {
    1: {"neihu": "28", "dawan": "26", "fuhe": "32"},
    2: {"neihu": "28", "dawan": "26", "fuhe": "32"},
    3: {"neihu": "29", "dawan": "27", "fuhe": "32"},
    4: {"dawan": "21", "neihu": "30", "kc114": "24"},
    5: {"neihu": "30", "dawan": "29", "fuhe": "32"},
    6: {"kc114": "28", "neihu": "28", "dawan": "26"},
    7: {"neihu": "29", "dawan": "27", "fuhe": "32"},
    8: {"neihu": "28", "dawan": "26", "fuhe": "32"},
    9: {"tnfsh": "第二大題第(1)小題", "fuhe": "32", "dawan": "26"},
    10: {"neihu": "30", "dawan": "29", "fuhe": "32"},
}
ANSWERS = {1: "C", 2: "A", 3: "D", 4: "B", 5: "C", 6: "A", 7: "D", 8: "B", 9: "C", 10: "D"}


def main() -> int:
    failures: list[str] = []
    ref_count = 0
    for number in range(1, 11):
        path = ROOT / f"questions/science/question-science-content-aa-iv-4-{number}.json"
        question = json.loads(path.read_text(encoding="utf-8"))
        refs = question.get("examPatternRefs", [])
        ref_count += len(refs)
        if question.get("reviewStatus") != "draft":
            failures.append(f"{question['id']}: must remain draft")
        if question.get("answer", {}).get("value") != ANSWERS[number]:
            failures.append(f"{question['id']}: answer differs from the manually checked key")
        if len(question.get("options", [])) != 4 or ANSWERS[number] not in {o.get("id") for o in question.get("options", [])}:
            failures.append(f"{question['id']}: answer does not map to four choices")
        explanation = question.get("answer", {}).get("explanation", "")
        steps = question.get("solutionSteps", [])
        strategy = question.get("solutionStrategy", "")
        if len(explanation) < 45 or len(strategy) < 20 or len(steps) != 5 or any(len(s.strip()) < 12 for s in steps):
            failures.append(f"{question['id']}: explanation, strategy, or five-step solution is incomplete")
        actual: dict[str, str] = {}
        for index, ref in enumerate(refs):
            key = next((k for k, url in PAPERS.items() if url == ref.get("url")), None)
            if not key:
                failures.append(f"{question['id']} ref {index}: unverified paper URL")
                continue
            actual[key] = ref.get("locator", "")
            if ref.get("locatorLevel") != "item" or ref.get("status") != "recorded":
                failures.append(f"{question['id']} ref {index}: item-level locator/status missing")
            if ref.get("reuseDecision") != "pattern-only" or ref.get("pattern") != ref.get("observedPattern"):
                failures.append(f"{question['id']} ref {index}: pattern-only provenance contract failed")
            if not ref.get("pattern", "").startswith("原卷PDF第") and key != "tnfsh":
                failures.append(f"{question['id']} ref {index}: locator lacks page/item description")
        if set(actual) != set(EXPECTED[number]):
            failures.append(f"{question['id']}: expected papers {sorted(EXPECTED[number])}, got {sorted(actual)}")
        for key, item in EXPECTED[number].items():
            locator = actual.get(key, "")
            if item not in locator:
                failures.append(f"{question['id']}: {key} expected item {item}, got {locator!r}")
        if len(set(actual.values())) < 3:
            failures.append(f"{question['id']}: three distinct item locators required")

    report = {
        "unit": "Aa-Ⅳ-4：元素性質週期性", "checked": 10,
        "passed": 10 if not failures else 0, "itemLevelSourceRefs": ref_count,
        "status": "pass" if not failures and ref_count == 30 else "fail",
        "checks": ["fixed answer key", "four-choice answer mapping", "substantive explanation/strategy/five steps", "three expected public-school paper-item pairs per question", "item-level pattern-only", "draft retained"],
        "failures": failures, "reviewedAt": "2026-09-24",
    }
    out = ROOT / "implementation/reports/science-aa-iv-4-first-pass-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
