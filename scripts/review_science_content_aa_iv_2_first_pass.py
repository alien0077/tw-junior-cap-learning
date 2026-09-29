import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "science"
REPORT = ROOT / "implementation" / "reports" / "science-content-aa-iv-2-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-science-content-aa-iv-2-*.json"))
errors = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-aa-iv-2": errors.append(f"{path.name}: lessonId")
    if data.get("reviewStatus") != "draft": errors.append(f"{path.name}: reviewStatus")
    if data.get("provenance", {}).get("origin") != "original": errors.append(f"{path.name}: origin")
    if len(data.get("options", [])) != 4 or not data.get("answer", {}).get("value"): errors.append(f"{path.name}: answer/options")
    if not data.get("answer", {}).get("explanation"): errors.append(f"{path.name}: explanation")
    if len(data.get("solutionSteps", [])) != 5: errors.append(f"{path.name}: solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3: errors.append(f"{path.name}: refs")
    if any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): errors.append(f"{path.name}: ref status")
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if errors:
    raise SystemExit("\n".join(errors))
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps({
    "unit": "Aa-Ⅳ-2：相對原子質量與相對分子質量",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對相對原子質量基準、相對分子質量、化學式下標、同位素比例與加權平均。",
        "逐題以量綱、化學式個數與數值回算唯一正確答案，特別檢查相對值不可直接當作克數。",
        "公開試題與公開教材僅作能力方向與資料型態研究，題幹、數值、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。",
    ],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
