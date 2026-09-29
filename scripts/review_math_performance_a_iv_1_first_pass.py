import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-performance-a-iv-1-first-pass-review.json"
PREFIX = "question-math-performance-a-iv-1-"

files = sorted(QUESTION_DIR.glob(f"{PREFIX}*.json"))
errors = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-performance-a-iv-1":
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
    "unit": "a-Ⅳ-1：符號文字表達概念運算推理證明",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對偶數與奇數的一般表示、代入運算、符號不等式、分配律與聯立消去。",
        "逐題核對奇偶性與整除推理、反例否證及文字條件轉成代數式的步驟。",
        "逐題保留公開數學試題的能力方向，題幹、數值、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。",
    ],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
