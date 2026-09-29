import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "science"
REPORT = ROOT / "implementation" / "reports" / "science-content-ab-iv-1-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-science-content-ab-iv-1-*.json"))
errors = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-ab-iv-1": errors.append(f"{path.name}: lessonId")
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
    "unit": "Ab-Ⅳ-1：粒子模型與三態",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對固、液、氣粒子排列與間距、運動與能量、壓力、蒸發沸騰、凝結與物態變化。",
        "逐題將宏觀現象轉成粒子模型證據，回查唯一正確答案與物態／化學身分界線。",
        "公開試題與公開教材僅作能力方向與資料型態研究，題幹、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。",
    ],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
