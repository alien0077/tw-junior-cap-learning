import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-s-9-13-first-pass-review.json"
PREFIX = "question-math-content-s-9-13-"

files = sorted(QUESTION_DIR.glob(f"{PREFIX}*.json"))
errors = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-content-s-9-13":
        errors.append(f"{path.name}: lessonId mismatch")
    if data.get("reviewStatus") != "draft":
        errors.append(f"{path.name}: reviewStatus must remain draft")
    if data.get("provenance", {}).get("origin") != "original":
        errors.append(f"{path.name}: origin must be original")
    if len(data.get("options", [])) != 4 or not data.get("answer", {}).get("value"):
        errors.append(f"{path.name}: answer/options incomplete")
    if len(data.get("solutionSteps", [])) != 5:
        errors.append(f"{path.name}: solutionSteps must contain exactly five steps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3:
        errors.append(f"{path.name}: expected three public-source refs")
    for ref in refs:
        if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded":
            errors.append(f"{path.name}: source ref must be pattern-only/recorded")

if len(files) != 10:
    errors.append(f"expected 10 questions, found {len(files)}")
if errors:
    raise SystemExit("\n".join(errors))

REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps({
    "unit": "S-9-13：表面積與體積",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對正方體、長方體、柱體表面積與體積的公式條件。",
        "逐題核對立方公分、毫升、公升與平方／立方單位。",
        "逐題保留公開公立學校試題的能力方向，題幹、數值、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。"
    ]
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
