import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions" / "science").glob("question-science-content-eb-iv-10-*.json"))
errors, answers = [], set()
for p in files:
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("lessonId") != "lesson-science-content-eb-iv-10" or d.get("reviewStatus") != "draft": errors.append(f"{p.name}: metadata")
    if len(d.get("options", [])) != 4 or not d.get("answer", {}).get("value"): errors.append(f"{p.name}: answer/options")
    if not d.get("answer", {}).get("explanation") or not d.get("solutionStrategy") or len(d.get("solutionSteps", [])) != 5: errors.append(f"{p.name}: explanation/steps")
    if len(d.get("examPatternRefs", [])) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in d.get("examPatternRefs", [])): errors.append(f"{p.name}: refs")
    answers.add(d.get("answer", {}).get("value"))
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if len(answers) < 3: errors.append("answer distribution is not varied enough")
if errors: raise SystemExit("\n".join(errors))
report = ROOT / "implementation/reports/science-content-eb-iv-10-first-pass-review.json"
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({"unit": "Eb-Ⅳ-10：不受力物體維持原有運動狀態", "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "questionCount": len(files), "passed": len(files), "notes": ["逐題核對參考系、初始速度、合力為零、靜止與等速度直線運動、重力／支持力抵消、摩擦減速、低摩擦資料與安全帶作用。", "特別檢查不受力的課綱語意是合力為零而非所有外力不存在、正在移動不代表必有前進力，以及速度改變必須有不為零的合力。", "公立學校公開資料僅作能力方向研究，題幹、選項、答案、解析與五步解法均為原創；版本研究與第二輪 AI／Terra 複核未完成，維持 draft。"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
