import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-a-8-7-*.json"))
failures = []
expected_answers = {
    1: ("C", "3、4"), 2: ("C", "x＝2 或 x＝−2"),
    3: ("A", "2 或 −4"), 4: ("B", "x＝5 或 −1"),
    5: ("B", "3"), 6: ("B", "7"),
    7: ("C", "x＝7 或 x＝−1"), 8: ("B", "1／3、3"),
    9: ("C", "6"), 10: ("A", "2"),
}
expected_refs = {
    1: {"至善國中": "原卷第 1 頁第 10 題", "北新國中": "原卷第 2 頁第 15 題", "大道國民中學": "原卷第 1 頁第 15 題"},
    2: {"漢口國民中學": "原卷第 1 頁第 7 題", "至善國中": "原卷第 2 頁第 19 題", "大道國民中學": "原卷第 2 頁第 19 題"},
    3: {"至善國中": "原卷第 1 頁第 10 題", "北新國中": "原卷第 2 頁第 15 題", "大道國民中學": "原卷第 1 頁第 15 題"},
    4: {"至善國中": "原卷第 1 頁第 10 題", "北新國中": "原卷第 2 頁第 15 題", "大道國民中學": "原卷第 1 頁第 15 題"},
    5: {"至善國中": "原卷第 1 頁第 9 題", "大甲國中": "原卷第 2 頁第 27 題", "大道國民中學": "原卷第 2 頁第 20 題"},
    6: {"大道國民中學": "原卷第 1 頁第 12 題", "大甲國中": "原卷第 2 頁第 30 題", "至善國中": "原卷第 2 頁第 16 題"},
    7: {"至善國中": "原卷第 2 頁第 19 題", "大道國民中學": "原卷第 2 頁第 19 題", "漢口國民中學": "原卷第 1 頁第 7 題"},
    8: {"大道國民中學": "原卷第 1 頁第 3 題", "北新國中": "原卷第 1 頁第 7 題", "大甲國中": "原卷第 2 頁第 26 題"},
    9: {"漢口國民中學": "原卷第 1 頁第 3 題", "至善國中": "原卷第 1 頁第 10 題", "北新國中": "原卷第 2 頁第 15 題"},
    10: {"至善國中": "原卷第 1 頁第 9 題", "大甲國中": "原卷第 2 頁第 27 題", "大道國民中學": "原卷第 2 頁第 20 題"},
}
answer_checks = 0
source_checks = 0
for path in paths:
    number = int(path.stem.rsplit("-", 1)[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-a-8-7": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") != "item" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
    answer_id, answer_text = expected_answers.get(number, (None, None))
    selected = [option.get("text", "").replace(" ", "") for option in data.get("options", []) if option.get("id") == answer_id]
    if data.get("answer", {}).get("value") != answer_id or len(selected) != 1 or selected[0] != answer_text.replace(" ", ""):
        failures.append(f"{path.name}:expected-answer-option")
    else:
        answer_checks += 1
    if len({ref.get("url") for ref in refs}) != 3:
        failures.append(f"{path.name}:three-distinct-public-schools")
    for school, locator in expected_refs.get(number, {}).items():
        matching = [ref for ref in refs if school in ref.get("title", "")]
        if len(matching) != 1 or not matching[0].get("locator", "").startswith(locator):
            failures.append(f"{path.name}:source-item-{school}")
        else:
            source_checks += 1
report = {"unit": "A-8-7：一元二次方程式的解法與應用", "checked": len(paths), "passed": len(paths) - len(failures), "mathAnswersChecked": answer_checks, "mathAnswersExpected": 10, "sourceItemsChecked": source_checks, "sourceItemsExpected": 30, "failures": failures, "status": "pass" if len(paths) == 10 and answer_checks == 10 and source_checks == 30 and not failures else "fail", "notes": "逐題固定比對答案選項，並要求三所公校原卷的單題題號 locator；僅使用公開試題作 pattern-only 改寫，不重製題目，維持 draft。"}
out = ROOT / "implementation" / "reports" / "math-a-8-7-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
