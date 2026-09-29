import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted(
    (ROOT / "questions/english").glob("question-english-performance-4-iv-7-*.json"),
    key=lambda path: int(path.stem.rsplit("-", 1)[-1]),
)
source_urls = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%80%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91.pdf",
    "https://www.csjh.kh.edu.tw/teach/exam/108%E4%B8%8B%E5%AD%B8%E6%9C%9F/%E7%AC%AC%E4%BA%8C%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%8B%B1%E6%96%87%E7%A7%91/%E4%B8%80%E5%B9%B4%E7%B4%9A/108%E4%B8%8B%E4%BA%8C%E6%AE%B5%E4%B8%80%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
    "https://www.csjh.kh.edu.tw/teach/exam/113%E4%B8%8A%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83/%E8%8B%B1%E8%AA%9E%E7%A7%91/%E4%B8%89%E5%B9%B4%E7%B4%9A/113%E4%B8%8A%E4%B8%89%E6%AE%B5%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E9%A1%8C%E7%9B%AE%E5%8D%B7.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-3%E5%B9%B4%E7%B4%9A%E6%9C%9F%E6%9C%AB-%E8%8B%B1%E6%96%87%E7%A7%91-%E8%A9%A6%E9%A1%8C.pdf",
}
expected_correct_texts = [
    "Bring the notebook to school tomorrow.",
    "To thank the aunt for the tickets.",
    "At the front desk.",
    "The arrival train is later.",
    "Send the museum's address.",
    "To ask about missed schoolwork.",
    "Return books before 4:30.",
    "The writer saw sea turtles this morning.",
    "The starting time.",
    "Thank you for your help. Best regards, Kai",
]
expected_distribution = {"A": 2, "B": 3, "C": 3, "D": 2}
failures = []
answers = {key: 0 for key in "ABCD"}
prompts, strategies, steps_seen = set(), set(), set()
for index, path in enumerate(paths):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("id") != path.stem or data.get("lessonId") != "lesson-english-performance-4-iv-7":
        failures.append(f"{path.name}:identity")
    if data.get("knowledgeIds") != ["kg-english-performance-4-iv-7"]:
        failures.append(f"{path.name}:knowledgeIds")
    if data.get("reviewStatus") != "draft" or data.get("provenance", {}).get("origin") != "original":
        failures.append(f"{path.name}:draft-or-origin")
    options = data.get("options", [])
    option_ids = [option.get("id") for option in options]
    if len(options) != 4 or set(option_ids) != set("ABCD"):
        failures.append(f"{path.name}:four-unique-options")
    answer = data.get("answer", {}).get("value")
    answers[answer] = answers.get(answer, 0) + 1
    matching = [option.get("text") for option in options if option.get("id") == answer]
    if matching != [expected_correct_texts[index]]:
        failures.append(f"{path.name}:answer-text-mismatch:{matching}")
    explanation = data.get("answer", {}).get("explanation", "")
    if len(explanation) < 70:
        failures.append(f"{path.name}:explanation-too-short")
    prompt = data.get("prompt", "")
    if not prompt or prompt in prompts:
        failures.append(f"{path.name}:empty-or-duplicate-prompt")
    prompts.add(prompt)
    strategy = data.get("solutionStrategy", "")
    if len(strategy) < 20:
        failures.append(f"{path.name}:strategy-too-short")
    strategies.add(strategy)
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(len(step) < 14 for step in steps):
        failures.append(f"{path.name}:five-detailed-steps")
    steps_seen.update(steps)
    refs = data.get("examPatternRefs", [])
    if len(refs) != 4 or {ref.get("url") for ref in refs} != source_urls:
        failures.append(f"{path.name}:four-exact-exam-sources")
    for ref in refs:
        if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only":
            failures.append(f"{path.name}:source-status-or-reuse")
        if ref.get("locatorLevel") != "item" or not re.search(r"PDF第\d+頁.*第\d+至\d+題", ref.get("locator", "")):
            failures.append(f"{path.name}:paper-page-item-locator")
        if not ref.get("observedPattern") or ref.get("subject") != "english":
            failures.append(f"{path.name}:source-pattern-or-subject")
    if data.get("provenance", {}).get("sourceUrl") not in source_urls:
        failures.append(f"{path.name}:provenance-source-url")

if len(paths) != 10:
    failures.append(f"question-count:{len(paths)}")
if answers != expected_distribution:
    failures.append(f"answer-distribution:{answers}")
if len(strategies) != 10:
    failures.append(f"strategy-reuse:{len(strategies)}")
if len(steps_seen) < 40:
    failures.append(f"solution-step-reuse:{len(steps_seen)}-unique-of-50")

report = {
    "unit": "4-Ⅳ-7：卡片、訊息、書信與電郵",
    "checked": len(paths),
    "passed": len(paths) if not failures else 0,
    "answerKeyDistribution": answers,
    "distinctStrategies": len(strategies),
    "uniqueDetailedSteps": len(steps_seen),
    "publicSchoolExamSources": len(source_urls),
    "itemLevelRefsPerQuestion": 4,
    "failures": failures,
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "notes": "逐題核對正解文字、選項、解析、不同策略、五步詳解、四份公校原卷頁碼及題號、pattern-only 界線與 draft 狀態；不代表出版社融合或發布審查完成。",
}
out = ROOT / "implementation/reports/english-performance-4-iv-7-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
