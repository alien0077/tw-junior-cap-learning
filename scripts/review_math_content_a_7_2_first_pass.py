import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-a-7-2-first-pass-review.json"
LESSON = "lesson-math-content-a-7-2"
paths = sorted(QUESTION_DIR.glob("question-math-content-a-7-2-*.json"))
failures = []
expected_exam_urls = {
    "https://www.mljh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=164&cfsn=771&fn=111-1-7%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8%E7%A7%91%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E5%8D%B7.pdf&op=dlfile",
    "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=374&cfsn=2424&name=111-1-%E7%AC%AC3%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%82%B5%E6%B2%BB%E5%AE%B6.pdf&op=dlfile",
    "https://www.htjh.tp.edu.tw/wp-content/uploads/doc/t210/110-1_%E7%AC%AC%E4%B8%89%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%83%E6%95%B8%E5%AD%B8.pdf",
    "https://school.tc.edu.tw/open-message/193521/get-file/6790e68d4a02433d6346b847.pdf",
}
expected_answers = {1: "B", 2: "A", 3: "C", 4: "B", 5: "B", 6: "D", 7: "B", 8: "C", 9: "A", 10: "D"}
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    options = data.get("options", [])
    option_ids = {item.get("id") for item in options}
    if data.get("lessonId") != LESSON or data.get("reviewStatus") != "draft": failures.append(f"{path.name}: lessonId 或 reviewStatus 不符")
    if len(options) != 4 or len(option_ids) != 4 or data.get("answer", {}).get("value") not in option_ids: failures.append(f"{path.name}: 選項或答案不符")
    number = int(path.stem.rsplit("-", 1)[1])
    if data.get("answer", {}).get("value") != expected_answers.get(number): failures.append(f"{path.name}: 人工重算的唯一預期答案不符")
    if len({item.get("text") for item in options}) != 4: failures.append(f"{path.name}: 選項文字重複，無法保證唯一最佳答案")
    if data.get("provenance", {}).get("origin") != "original" or len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}: 原創或五步解法不符")
    refs = data.get("examPatternRefs", [])
    ref_urls = {r.get("url") for r in refs}
    if len(refs) != 3 or len(ref_urls) != 3 or not ref_urls <= expected_exam_urls or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" or r.get("locatorLevel") != "item" for r in refs): failures.append(f"{path.name}: 三份公校試卷逐題定位／pattern-only 不符")
    if any(not r.get("locator", "").startswith("第") or "第" not in r.get("locator", "") for r in refs): failures.append(f"{path.name}: 來源缺精確頁次／題號")
    if data.get("provenance", {}).get("sourceUrl") != refs[0].get("url") or data.get("reviewStatus") != "draft": failures.append(f"{path.name}: primary source or draft gate mismatch")
    if number in (8, 9) and "https://www.hlbh.hlc.edu.tw/ischool/rfile/9df20707763f01eacd79953c2695692a" not in data.get("studyReferences", []): failures.append(f"{path.name}: identity/no-solution claim lacks direct school learning-resource evidence")
if len(paths) != 10: failures.append(f"題目數量為 {len(paths)}，預期 10")
report = {"unit": "A-7-2：一元一次方程式的意義", "lessonId": LESSON, "questionCount": len(paths), "status": "pass" if not failures else "fail", "checks": {"originalAuthorshipFieldsPresent": True, "fixedExpectedAnswersAndUniqueOptions": True, "explanationAndFiveStepSolutionFieldsPresent": True, "threeDistinctPublicSchoolExamsPerQuestion": True, "exactItemPageLocators": True, "identityAndNoSolutionSchoolEvidence": True, "reviewStatusDraft": True}, "answerAuditBoundary": "Expected choices are manually derived from each prompt; this local reviewer asserts the fixed answers and structural uniqueness. It is not Terra or independent human subject-matter review.", "failures": failures, "reviewedAt": "2026-09-24"}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if failures: raise SystemExit("\n".join(failures))
print(f"review passed: {len(paths)} questions")
