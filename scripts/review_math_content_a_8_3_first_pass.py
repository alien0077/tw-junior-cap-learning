import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-a-8-3-*.json"))
failures = []
expected_sources = {
    1: [("至善國民中學 112", "計算題1(甲)"), ("至善國民中學 114", "第9題"), ("大道國民中學 114", "第28題"), ("豐東", "第12題")],
    2: [("至善國民中學 112", "計算題1(甲)"), ("至善國民中學 114", "第10題"), ("大甲國中", "第18題"), ("豐東", "第11題")],
    3: [("至善國民中學 112", "計算題1(甲)"), ("大道國中數學科八年級補行評量題庫", "第7題"), ("大道國民中學 114", "第4題"), ("豐東", "第11題")],
    4: [("至善國民中學 112", "計算題1(甲)"), ("大道國中數學科八年級補行評量題庫", "第7題"), ("大道國民中學 114", "第4題"), ("豐東", "第11題")],
    5: [("至善國民中學 112", "計算題1(甲)"), ("大道國中數學科八年級補行評量題庫", "第7題"), ("大道國民中學 114", "第4題"), ("豐東", "第16題")],
    6: [("至善國民中學 114", "第12題"), ("大道國民中學 114", "第29題"), ("豐東", "第15題")],
    7: [("至善國民中學 112", "計算題1(甲)"), ("至善國民中學 114", "第9題"), ("大道國民中學 114", "第28題"), ("豐東", "第12題")],
    8: [("至善國民中學 112", "計算題1(甲)"), ("至善國民中學 114", "第10題"), ("大道國民中學 114", "第28題"), ("豐東", "第11題")],
    9: [("至善國民中學 112", "計算題1(甲)"), ("至善國民中學 114", "第9題"), ("大道國民中學 114", "第28題"), ("豐東", "第16題")],
    10: [("大道國中數學科八年級補行評量題庫", "第7題"), ("至善國民中學 114", "第10題"), ("豐東", "第23題")],
}
expected_answers = {
    1: "4x²−3x＋3",
    2: "3a²−4a＋8",
    3: "8y²−4y＋12",
    4: "−6x³＋3x²−12x",
    5: "x³−x²−2x＋8",
    6: "2m²−3m＋1",
    7: "3x²＋3x＋2",
    8: "x²−5x−4",
    9: "6x−2",
    10: "7",
}
source_items_checked = 0
math_answers_checked = 0
domain_conditions_checked = 0

for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    number = int(path.stem.rsplit("-", 1)[1])
    if data.get("lessonId") != "lesson-math-content-a-8-3": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    answer_text = next((option.get("text") for option in data.get("options", []) if option.get("id") == data.get("answer", {}).get("value")), None)
    exact_answer = answer_text == expected_answers.get(number)
    unique_answer = sum(option.get("text") == expected_answers.get(number) for option in data.get("options", [])) == 1
    math_answers_checked += int(exact_answer and unique_answer)
    if not exact_answer: failures.append(f"{path.name}:math-answer")
    if not unique_answer:
        failures.append(f"{path.name}:unique-mathematical-answer")
    if number == 6 and "m≠0" not in data.get("prompt", ""):
        failures.append(f"{path.name}:division-domain")
    elif number == 6:
        domain_conditions_checked += 1
    if number == 9 and "x＞2" not in data.get("prompt", ""):
        failures.append(f"{path.name}:rectangle-domain")
    elif number == 9:
        domain_conditions_checked += 1
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")

    refs = data.get("examPatternRefs", [])
    if len(refs) < 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs):
        failures.append(f"{path.name}:examPatternRefs")
    if len({ref.get("url") for ref in refs}) < 3: failures.append(f"{path.name}:distinctPublicExamSources")
    for index, ref in enumerate(refs, 1):
        locator = ref.get("locator", "")
        if not locator or "第" not in locator or not any(char.isdigit() for char in locator):
            failures.append(f"{path.name}:ref{index}:itemLocator")
        if re.search(r"\d+\s*(?:–|－|至|-)\s*\d+", locator) or "等題" in locator:
            failures.append(f"{path.name}:ref{index}:broadLocator")
        if "多項式加法、減法、項的係數及除法" in locator or "括號化簡、多項式加減與除法" in locator:
            failures.append(f"{path.name}:ref{index}:nonSpecificSkillClaim")

    for school_token, item_token in expected_sources.get(number, []):
        matched = any(school_token in ref.get("title", "") and item_token in ref.get("locator", "") for ref in refs)
        source_items_checked += int(matched)
        if not matched: failures.append(f"{path.name}:expected-source-item:{school_token}:{item_token}")

report = {
    "unit": "A-8-3：多項式的四則運算",
    "checked": len(paths),
    "passed": len(paths) - len(failures),
    "sourceItemsChecked": source_items_checked,
    "sourceItemsExpected": sum(len(items) for items in expected_sources.values()),
    "mathAnswersChecked": math_answers_checked,
    "mathAnswersExpected": len(expected_answers),
    "domainConditionsChecked": domain_conditions_checked,
    "domainConditionsExpected": 2,
    "failures": failures,
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "notes": "逐題檢查答案選項結構、原創性、五步詳解、逐題預期學校及題號定位。此契約不替代人工判讀來源考點適配；所有題目維持 draft。",
}
out = ROOT / "implementation" / "reports" / "math-a-8-3-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
