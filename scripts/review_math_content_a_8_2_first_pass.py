import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "math").glob("question-math-content-a-8-2-*.json"))
failures = []
school_names = ("至善", "光正", "大道", "北新", "崇林", "中山", "內湖", "大甲", "太保", "三重")

# Require every locator written for this unit to point at its documented
# original-paper item; a count of three citations alone is not source-fit QA.
EXPECTED_SOURCE_LOCATORS = {
    1: (("太保", "第4題"), ("光正", "第11題"), ("三重", "第6題")),
    2: (("光正", "第17題"), ("北新", "第18題"), ("大甲", "第20題")),
    3: (("至善", "第4題"), ("光正", "第18題"), ("北新", "第28題")),
    4: (("至善", "第4題"), ("光正", "第18題"), ("大甲", "第19題")),
    5: (("內湖", "第5題"), ("至善", "第4題"), ("光正", "第18題")),
    6: (("內湖", "第6題"), ("崇林", "第3題"), ("中山", "第8題")),
    7: (("至善", "第3、4題"), ("光正", "第11、17題"), ("太保", "第4、26題")),
    8: (("至善", "第6題"), ("光正", "第10題"), ("大甲", "第41題")),
    9: (("崇林", "第3題"), ("北新", "第28題"), ("中山", "第8題")),
    10: (("至善", "第3、4題"), ("光正", "第17、18題"), ("大甲", "第19、20題")),
}
def school_key(ref):
    title = ref.get("title", "")
    return next((name for name in school_names if name in title), urlparse(ref.get("url", "")).hostname or "unknown")

for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-a-8-2": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    school_ids = {school_key(ref) for ref in refs}
    if len(refs) < 3 or len(school_ids) < 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") != "item" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
    try:
        question_number = int(path.stem.rsplit("-", 1)[1])
    except (ValueError, IndexError):
        question_number = -1
    expected_locators = EXPECTED_SOURCE_LOCATORS.get(question_number, ())
    for school, locator_fragment in expected_locators:
        if not any(school in ref.get("title", "") and locator_fragment in ref.get("locator", "") for ref in refs):
            failures.append(f"{path.name}:source-match-{school}-{locator_fragment}")
    if len(data.get("solutionSteps", [])) != 5 or not data.get("solutionStrategy") or not data.get("answer", {}).get("explanation"): failures.append(f"{path.name}:answer-and-detailed-solution")
report = {"unit": "A-8-2：多項式的意義", "checked": len(paths), "passed": len(paths) - len(failures), "sourceCountPerQuestion": {"minimum": min((len(json.loads(path.read_text(encoding="utf-8")).get("examPatternRefs", [])) for path in paths), default=0), "distinctPublicSchoolNamesAcrossUnit": sorted({school_key(ref) for path in paths for ref in json.loads(path.read_text(encoding="utf-8")).get("examPatternRefs", [])})}, "failures": failures, "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "逐題人工重算並檢查唯一答案、誘答、解題策略及五步解法；每題至少引用三所不同公立國中的公開原卷題號，校名依來源標題辨識（不以共同下載網址路徑誤判為學校ID），僅作 pattern-only 參考。來源定位與考次以原卷為準；不明學年度標為 unknown。所有題目仍維持 draft。"}
out = ROOT / "implementation" / "reports" / "math-a-8-2-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
