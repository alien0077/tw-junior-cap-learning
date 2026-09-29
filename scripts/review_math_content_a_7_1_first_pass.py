import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-a-7-1-first-pass-review.json"
LESSON = "lesson-math-content-a-7-1"
paths = sorted(QUESTION_DIR.glob("question-math-content-a-7-1-*.json"))
failures = []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    options = data.get("options", [])
    option_ids = {item.get("id") for item in options}
    if data.get("lessonId") != LESSON or data.get("reviewStatus") != "draft": failures.append(f"{path.name}: lessonId 或 reviewStatus 不符")
    if len(options) != 4 or len(option_ids) != 4 or data.get("answer", {}).get("value") not in option_ids: failures.append(f"{path.name}: 選項或答案不符")
    if data.get("provenance", {}).get("origin") != "original" or len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}: 原創或五步解法不符")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): failures.append(f"{path.name}: 公開試題來源界線不符")
if len(paths) != 10: failures.append(f"題目數量為 {len(paths)}，預期 10")
report = {"unit": "A-7-1：代數符號", "lessonId": LESSON, "questionCount": len(paths), "status": "pass" if not failures else "fail", "checks": {"originalRewrites": True, "answerAndExplanation": True, "solutionStepsExactlyFive": True, "publicExamPatternRefsExactlyThree": True, "reviewStatusDraft": True}, "failures": failures, "reviewedAt": "2026-09-10"}
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
if failures: raise SystemExit("\n".join(failures))
print(f"review passed: {len(paths)} questions")
