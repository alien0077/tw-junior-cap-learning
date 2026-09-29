import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-5-iv-7-first-pass-review.json"
SOURCES = {
    "xiaogang": "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/21%E4%BA%8C%E5%B9%B4%E7%B4%9A%E4%B8%8A%E5%AD%B8%E6%9C%9F/3%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/109-1-3%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87.pdf",
    "dawan": "https://www.dwm.kh.edu.tw/upload/344/104_64186/111%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%B8%80%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C%28%E4%BD%B3%E9%9F%B3%29.pdf",
    "guo110": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E9%AB%98%E9%9B%84%E5%B8%82%E5%9C%8B%E6%98%8C%E5%9C%8B%E4%B8%AD%E4%BA%8C%E4%B8%8B%E8%8B%B1%E6%96%87%E8%81%BD%E5%8A%9B%E8%A7%A3%E6%9E%90%E5%8D%B7.pdf",
    "guo113": "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%81%BD_10.pdf",
    "wuling": "https://www.whjhs.tyc.edu.tw/wp-content/uploads/doc/wh212/114%E5%AD%B8%E5%B9%B4%E8%8B%B1%E8%AA%9E9-3%E6%95%99%E8%82%B2%E6%9C%83%E8%80%83_%E8%81%BD%E5%8A%9B%E8%A7%A3%E6%9E%90.pdf",
}
expected = {
    1: ("B", "Arrange a rehearsal for Mia's presentation", {("guo110", "第三部分言談理解第17題"), ("xiaogang", "第三部分言談理解第15題"), ("dawan", "第三部分言談理解第10題")}),
    2: ("C", "Music room at 4:00", {("xiaogang", "第三部分言談理解第14題"), ("dawan", "第三部分言談理解第8題"), ("guo113", "第2頁第23題")}),
    3: ("D", "Ruler and colored pencils", {("xiaogang", "第三部分言談理解第14題"), ("guo110", "第四部分聽力題組第21題"), ("dawan", "第三部分言談理解第10題")}),
    4: ("A", "Departure time: 5:10 → 5:30", {("guo113", "第2頁第23題"), ("xiaogang", "第三部分言談理解第14題"), ("dawan", "第三部分言談理解第8題")}),
    5: ("B", "Sign the form", {("wuling", "第1頁第12題"), ("xiaogang", "第三部分言談理解第15題"), ("dawan", "第三部分言談理解第10題")}),
    6: ("D", "Folder missing → check beside the classroom computer", {("guo110", "第三部分言談理解第11題"), ("wuling", "第1頁第12題"), ("dawan", "第三部分言談理解第8題")}),
    7: ("C", "Relieved and still careful", {("guo113", "第2頁第16題"), ("guo110", "第三部分言談理解第13題"), ("xiaogang", "第三部分言談理解第15題")}),
    8: ("A", "Science club—Aquarium, Sat.; east gate 8:15 a.m.; student card", {("wuling", "第4頁第21題"), ("xiaogang", "第三部分言談理解第14題"), ("guo113", "第2頁第23題")}),
    9: ("D", "Join photography next week", {("xiaogang", "第三部分言談理解第11題"), ("xiaogang", "第三部分言談理解第12題"), ("wuling", "第4頁第21題")}),
    10: ("B", "Poster draft meeting—Room 302, 4:00; bring outline", {("xiaogang", "第三部分言談理解第14題"), ("dawan", "第三部分言談理解第10題"), ("wuling", "第4頁第21題")}),
}
source_key = {url: key for key, url in SOURCES.items()}
failures, keys, prompts, strategies, steps_all = [], Counter(), [], [], []
for index in range(1, 11):
    path = OUT / f"question-english-performance-5-iv-7-{index}.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        failures.append(f"{path.name}:json:{exc}")
        continue
    key, exact_answer, expected_refs = expected[index]
    options = {row.get("id"): row.get("text") for row in data.get("options", [])}
    if data.get("lessonId") != "lesson-english-performance-5-iv-7": failures.append(f"{path.name}:lesson")
    if data.get("reviewStatus") != "draft" or data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:draft-original")
    if data.get("answer", {}).get("value") != key or options.get(key) != exact_answer: failures.append(f"{path.name}:answer-key-text")
    if len(options) != 4 or set(options) != {"A", "B", "C", "D"}: failures.append(f"{path.name}:four-options")
    if len(data.get("answer", {}).get("explanation", "")) < 45 or data.get("answer", {}).get("explanation", "").isascii(): failures.append(f"{path.name}:explanation")
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(len(step) < 18 for step in steps): failures.append(f"{path.name}:five-detailed-steps")
    if len(data.get("solutionStrategy", "")) < 20: failures.append(f"{path.name}:strategy")
    refs = data.get("examPatternRefs", [])
    actual_refs = {(source_key.get(ref.get("url")), ref.get("locator")) for ref in refs}
    if len(refs) != 3 or actual_refs != expected_refs: failures.append(f"{path.name}:exact-source-items")
    if any(ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only" or ref.get("locatorLevel") != "item" for ref in refs): failures.append(f"{path.name}:source-contract")
    if any("均為原創" not in ref.get("observedPattern", "") for ref in refs): failures.append(f"{path.name}:reuse-boundary")
    keys[key] += 1
    prompts.append(data.get("prompt", ""))
    strategies.append(data.get("solutionStrategy", ""))
    steps_all.extend(steps)
if len(set(prompts)) != 10: failures.append("duplicate-prompts")
if len(set(strategies)) != 10: failures.append("duplicate-strategies")
if len(steps_all) != 50 or len(set(steps_all)) != 50: failures.append("duplicate-or-missing-solution-steps")
if keys != Counter({"A": 2, "B": 3, "C": 2, "D": 3}): failures.append("answer-distribution")
report = {"unit": "5-Ⅳ-7：聽日常對話筆記", "checked": 10, "passed": 10 if not failures else 0, "answerDistribution": dict(sorted(keys.items())), "sourceRefs": len(steps_all) // 5 * 3, "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(steps_all)), "failures": failures, "status": "pass" if not failures else "fail", "notes": "逐題比對唯一答案字串、繁中解析、專屬策略與五步詳解、精確校方試題題號及 pattern-only 界線；全題維持 draft。"}
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
