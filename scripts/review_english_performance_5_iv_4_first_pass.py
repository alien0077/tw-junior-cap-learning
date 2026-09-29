#!/usr/bin/env python3
"""First-pass answer, explanation, and public-school provenance review for English 5-IV-4."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    1: ("D", "pause briefly and use an urgent tone"),
    2: ("B", "Quietly, because the stage direction says whispers."),
    3: ("C", "Leo checked the weather."),
    4: ("A", "Relief and excitement"),
    5: ("D", "red"),
    6: ("C", "A contrast between difficulty and determination"),
    7: ("B", "The clock and only five minutes show time pressure."),
    8: ("A", "correcting or denying a claim"),
    9: ("C", "Make a short break before the question"),
    10: ("B", "The performance is ending."),
}
EXPECTED_URLS = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_1.pdf",
    "https://www.nhjh.tp.edu.tw/uploads/1675416243777dXcSuX4X.pdf",
    "https://www.dam.kh.edu.tw/upload/68/101_28414/%E4%B8%89%E5%B9%B4%E7%B4%9A%20%20%E5%9C%8B%E6%96%87%E3%80%81%E8%8B%B1%E6%96%87%E3%80%81%E8%87%AA%E7%84%B6%E3%80%81%E6%AD%B7%E5%8F%B2%E3%80%81%E5%85%AC%E6%B0%91.pdf",
    "https://lkjh.chc.edu.tw/storage/074502/posts/1545/files/114-1-2%E8%8B%B1%E6%96%87%E7%A7%91%E5%90%84%E5%B9%B4%E7%B4%9A%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E7%BF%BB%E8%AD%AF%E5%8F%A5%E5%9E%8B%E9%A1%8C%E5%BA%AB%E5%8F%8A%E7%AF%84%E5%9C%8D%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A0%85.docx.pdf",
}

def main() -> None:
    failures: list[str] = []
    keys: Counter[str] = Counter()
    prompts: list[str] = []
    strategies: list[str] = []
    steps: list[str] = []
    for number, (key, correct_text) in EXPECTED.items():
        path = ROOT / f"questions/english/question-english-performance-5-iv-4-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        options = {option["id"]: option["text"] for option in data.get("options", [])}
        if data.get("lessonId") != "lesson-english-performance-5-iv-4": failures.append(f"{number}:lessonId")
        if data.get("reviewStatus") != "draft": failures.append(f"{number}:reviewStatus")
        if data.get("answer", {}).get("value") != key or options.get(key) != correct_text: failures.append(f"{number}:answer-mapping")
        if data.get("provenance", {}).get("origin") != "original": failures.append(f"{number}:origin")
        if not data.get("answer", {}).get("explanation"): failures.append(f"{number}:explanation")
        if len(data.get("solutionSteps", [])) != 5 or data.get("solutionSteps", [None])[-1] != data.get("answer", {}).get("explanation"): failures.append(f"{number}:steps")
        refs = data.get("examPatternRefs", [])
        if len(refs) != 4 or {ref.get("url") for ref in refs} != EXPECTED_URLS: failures.append(f"{number}:sources")
        if any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs): failures.append(f"{number}:source-status")
        if sum(ref.get("locatorLevel") == "page" for ref in refs) != 3 or sum(ref.get("locatorLevel") == "paper" for ref in refs) != 1: failures.append(f"{number}:source-locators")
        keys[key] += 1
        prompts.append(data.get("prompt", ""))
        strategies.append(data.get("solutionStrategy", ""))
        steps.extend(data.get("solutionSteps", []))
    if keys != Counter({"A": 2, "B": 3, "C": 3, "D": 2}): failures.append("answer-distribution")
    if len(set(prompts)) != 10: failures.append("duplicate-prompts")
    if len(set(strategies)) != 10: failures.append("duplicate-strategies")
    if len(set(steps)) != 50: failures.append("duplicate-steps")
    report = {"unit": "5-Ⅳ-4：朗讀短文短劇", "checked": 10, "passed": 10 - len(set(f.split(":")[0] for f in failures)), "answerDistribution": dict(sorted(keys.items())), "recordedPatternOnlyRefs": 40, "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(steps)), "failures": failures, "status": "pass" if not failures else "fail", "notes": "每題均為原創朗讀／文本線索題，含核對答案、繁中解題策略與五步說明；引用三所公立學校精確頁題定位及一份口說測驗對話評分項，內容維持draft。"}
    out = ROOT / "implementation/reports/english-performance-5-iv-4-first-pass-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    raise SystemExit(0 if report["status"] == "pass" else 1)

if __name__ == "__main__":
    main()
