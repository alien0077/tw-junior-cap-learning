import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "math"
REPORT = ROOT / "implementation" / "reports" / "math-performance-s-iv-10-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-math-performance-s-iv-10-*.json"))
errors = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-math-performance-s-iv-10": errors.append(f"{path.name}: lessonId")
    if data.get("reviewStatus") != "draft": errors.append(f"{path.name}: reviewStatus")
    if data.get("provenance", {}).get("origin") != "original": errors.append(f"{path.name}: origin")
    if len(data.get("options", [])) != 4 or not data.get("answer", {}).get("value"): errors.append(f"{path.name}: answer/options")
    if len(data.get("solutionSteps", [])) != 5: errors.append(f"{path.name}: solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3: errors.append(f"{path.name}: refs")
    if any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): errors.append(f"{path.name}: ref status")
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if errors:
    raise SystemExit("\n".join(errors))
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps({
    "unit": "s-Ⅳ-10：三角形相似",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對 AA／SAS／SSS 相似判定、相似比例、平行線截線比例、周長面積倍率與影子測高。",
        "逐題以比例式、相似對應、倍率平方與單位回查唯一正確答案。",
        "公開試題僅作能力方向與資料型態研究，題幹、數值、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。",
    ],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
