import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/english").glob("question-english-performance-4-iv-6-*.json"))
expected_keys = {"A": 2, "B": 2, "C": 4, "D": 2}
expected_urls = {
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-2%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/108-1-2%E8%8B%B1%E6%96%87%E4%B8%80%E5%B9%B4%E7%B4%9A%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf",
}
failures = []
answers = {}
prompts = set()
strategies = set()
for path in paths:
    data = json.loads(path.read_text())
    stem = path.stem.rsplit("-", 1)[-1]
    if data.get("id") != path.stem:
        failures.append(f"{path.name}:id-mismatch")
    if data.get("lessonId") != "lesson-english-performance-4-iv-6":
        failures.append(f"{path.name}:lessonId")
    if data.get("knowledgeIds") != ["kg-english-performance-4-iv-6"]:
        failures.append(f"{path.name}:knowledgeIds")
    if data.get("reviewStatus") != "draft":
        failures.append(f"{path.name}:reviewStatus")
    if data.get("provenance", {}).get("origin") != "original":
        failures.append(f"{path.name}:origin")
    if data.get("type") != "single-choice":
        failures.append(f"{path.name}:type")
    options = data.get("options", [])
    option_ids = [option.get("id") for option in options]
    if len(options) != 4 or set(option_ids) != {"A", "B", "C", "D"}:
        failures.append(f"{path.name}:options")
    answer = data.get("answer", {}).get("value")
    if answer not in option_ids:
        failures.append(f"{path.name}:answer-not-option")
    answers[answer] = answers.get(answer, 0) + 1
    prompt = data.get("prompt", "")
    if prompt in prompts:
        failures.append(f"{path.name}:duplicate-prompt")
    prompts.add(prompt)
    explanation = data.get("answer", {}).get("explanation", "")
    if len(explanation) < 100:
        failures.append(f"{path.name}:explanation-too-short")
    strategy = data.get("solutionStrategy", "")
    if len(strategy) < 30:
        failures.append(f"{path.name}:strategy-too-short")
    strategies.add(strategy)
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(len(step) < 14 for step in steps):
        failures.append(f"{path.name}:solution-steps")
    refs = data.get("examPatternRefs", [])
    ref_urls = {ref.get("url") for ref in refs}
    if len(refs) != 4 or ref_urls != expected_urls:
        failures.append(f"{path.name}:source-count-or-url-coverage")
    for ref in refs:
        if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded":
            failures.append(f"{path.name}:source-reuse-or-status")
        if ref.get("locatorLevel") != "item" or "PDF第" not in ref.get("locator", "") or "第" not in ref.get("locator", "題"):
            failures.append(f"{path.name}:source-item-locator")
        if ref.get("subject") != "english" or not ref.get("observedPattern"):
            failures.append(f"{path.name}:source-metadata")
    if data.get("provenance", {}).get("sourceUrl") not in expected_urls:
        failures.append(f"{path.name}:provenance-source-url")

if len(paths) != 10:
    failures.append(f"question-count:{len(paths)}")
if answers != expected_keys:
    failures.append(f"answer-key-balance:{answers}")
if len(strategies) != 10:
    failures.append(f"strategy-reuse:{len(strategies)}")

report = {
    "unit": "4-Ⅳ-6：句意轉換、時態與句型功能",
    "checked": len(paths),
    "passed": len(paths) - len(failures),
    "answerKeyDistribution": answers,
    "publicSchoolSourceUrls": len(expected_urls),
    "publicExamItemRefsPerQuestion": 4,
    "failures": failures,
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "notes": "逐題檢查答案選項、詳解、五步解題、原創題幹、四份公立學校精確試題定位與 pattern-only 界線；reviewStatus 保持 draft，未代表版本融合或發布審查完成。",
}
out = ROOT / "implementation/reports/english-performance-4-iv-6-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
