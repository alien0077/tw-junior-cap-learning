import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-s-9-4-first-pass-review.json"
LESSON = "lesson-math-content-s-9-4"
paths = sorted(QUESTION_DIR.glob("question-math-content-s-9-4-*.json"))
failures = []

for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != LESSON:
        failures.append(f"{path.name}: lessonId 不符")
    if data.get("reviewStatus") != "draft":
        failures.append(f"{path.name}: reviewStatus 必須維持 draft")
    options = data.get("options", [])
    option_ids = {option.get("id") for option in options}
    if len(options) != 4 or len(option_ids) != 4:
        failures.append(f"{path.name}: 必須有四個唯一選項")
    if data.get("answer", {}).get("value") not in option_ids:
        failures.append(f"{path.name}: answer 不在選項中")
    if data.get("provenance", {}).get("origin") != "original":
        failures.append(f"{path.name}: origin 必須為 original")
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(not isinstance(step, str) or not step.strip() for step in steps):
        failures.append(f"{path.name}: 必須有五個非空 solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3:
        failures.append(f"{path.name}: 必須有三筆 examPatternRefs")
    for index, ref in enumerate(refs, start=1):
        if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded":
            failures.append(f"{path.name}: 第 {index} 筆來源界線不符")

if len(paths) != 10:
    failures.append(f"題目數量為 {len(paths)}，預期 10")

report = {
    "unit": "S-9-4：相似直角三角形邊長比值的不變性",
    "lessonId": LESSON,
    "questionCount": len(paths),
    "status": "pass" if not failures else "fail",
    "checks": {
        "originalRewrites": True,
        "answerAndExplanation": True,
        "solutionStepsExactlyFive": True,
        "publicExamPatternRefsExactlyThree": True,
        "reviewStatusDraft": True,
    },
    "failures": failures,
    "reviewedAt": "2026-09-10",
}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if failures:
    raise SystemExit("\n".join(failures))
print(f"review passed: {len(paths)} questions")
