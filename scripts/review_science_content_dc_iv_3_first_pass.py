import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions" / "science").glob("question-science-content-dc-iv-3-*.json"))
errors, answers = [], set()
for path in files:
    d = json.loads(path.read_text(encoding="utf-8"))
    if d.get("lessonId") != "lesson-science-content-dc-iv-3" or d.get("reviewStatus") != "draft": errors.append(f"{path.name}: metadata")
    if len(d.get("options", [])) != 4 or not d.get("answer", {}).get("value"): errors.append(f"{path.name}: answer/options")
    if not d.get("answer", {}).get("explanation") or not d.get("solutionStrategy") or len(d.get("solutionSteps", [])) != 5: errors.append(f"{path.name}: explanation/steps")
    refs = d.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): errors.append(f"{path.name}: refs")
    answers.add(d.get("answer", {}).get("value"))
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if len(answers) < 3: errors.append("answer distribution is not varied enough")
if errors: raise SystemExit("\n".join(errors))
report = ROOT / "implementation/reports/science-content-dc-iv-3-first-pass-review.json"
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({"unit": "Dc-Ⅳ-3：皮膚與淋巴系統的防禦與免疫", "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "questionCount": len(files), "passed": len(files), "notes": ["逐題核對皮膚屏障、發炎、淋巴運輸、淋巴結、抗原、抗體、疫苗與免疫記憶。", "特別檢查非專一性與專一性防禦、單一觀察不能作診斷，以及疫苗效果不能外推成對所有病原保證有效。", "公立學校公開生物資料僅作能力方向研究，題幹、選項、答案、解析與五步解法均為原創；版本研究與第二輪 AI／Terra 複核未完成，維持 draft。"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
