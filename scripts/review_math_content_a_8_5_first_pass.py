import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-a-8-5-*.json"))
failures = []
expected_answers = {
    1: ("A", "分組分解法"), 2: ("B", "(x＋4)(x＋5)"),
    3: ("B", "(3x＋1)(2x＋3)"), 4: ("A", "(2x−1)(x−3)"),
    5: ("B", "完全平方公式逆用"), 6: ("A", "3x(2x−3)(2x＋3)"),
    7: ("A", "5(m−2)²"), 8: ("A", "(3x＋2)(x−1)"),
    9: ("B", "x＋4"), 10: ("A", "正確；展開後首項、一次項與常數項都相同"),
}
expected_refs = {
    1: {"大甲國民中學": "PDF 第 3 頁第 47 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 1 頁第 16 題"},
    2: {"大甲國民中學": "PDF 第 3 頁第 42 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 2 頁第 24 題"},
    3: {"大甲國民中學": "PDF 第 2 頁第 26 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 1 頁第 3 題"},
    4: {"大甲國民中學": "PDF 第 2 頁第 26 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 1 頁第 3 題"},
    5: {"大甲國民中學": "PDF 第 3 頁第 45 題", "北新國民中學": "PDF 第 1 頁第 4 題", "大道國民中學": "PDF 第 1 頁第 13 題"},
    6: {"大甲國民中學": "PDF 第 3 頁第 43 題", "北新國民中學": "PDF 第 1 頁第 3 題", "大道國民中學": "PDF 第 1 頁第 2 題"},
    7: {"大甲國民中學": "PDF 第 3 頁第 45 題", "北新國民中學": "PDF 第 1 頁第 4 題", "大道國民中學": "PDF 第 1 頁第 13 題"},
    8: {"大甲國民中學": "PDF 第 2 頁第 26 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 1 頁第 3 題"},
    9: {"大甲國民中學": "PDF 第 3 頁第 42 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 2 頁第 24 題"},
    10: {"大甲國民中學": "PDF 第 2 頁第 26 題", "北新國民中學": "PDF 第 1 頁第 7 題", "大道國民中學": "PDF 第 1 頁第 3 題"},
}
answer_checks = 0
source_checks = 0
for path in paths:
    number = int(path.stem.rsplit("-", 1)[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-a-8-5": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") != "item" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
    expected_answer, expected_text = expected_answers.get(number, (None, None))
    selected = [option.get("text", "").replace(" ", "") for option in data.get("options", []) if option.get("id") == expected_answer]
    if data.get("answer", {}).get("value") != expected_answer or len(selected) != 1 or selected[0] != expected_text.replace(" ", ""):
        failures.append(f"{path.name}:expected-mathematical-answer")
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
report = {"unit": "A-8-5：因式分解的方法", "checked": len(paths), "passed": len(paths) - len(failures), "mathAnswersChecked": answer_checks, "mathAnswersExpected": 10, "sourceItemsChecked": source_checks, "sourceItemsExpected": 30, "failures": failures, "status": "pass" if len(paths) == 10 and answer_checks == 10 and source_checks == 30 and not failures else "fail", "notes": "逐題固定比對唯一正解，要求大甲、北新、大道三校各自命中一筆精確題號 locator；校方原卷只作 pattern-only 能力參照，不複製題目內容，所有 lesson/questions 保持 draft。"}
out = ROOT / "implementation" / "reports" / "math-a-8-5-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
