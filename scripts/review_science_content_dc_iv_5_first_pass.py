import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions" / "science").glob("question-science-content-dc-iv-5-*.json"))
errors, answers = [], set()
for p in files:
    d = json.loads(p.read_text(encoding="utf-8"))
    if d.get("lessonId") != "lesson-science-content-dc-iv-5" or d.get("reviewStatus") != "draft": errors.append(f"{p.name}: metadata")
    if len(d.get("options", [])) != 4 or not d.get("answer", {}).get("value"): errors.append(f"{p.name}: answer/options")
    if not d.get("answer", {}).get("explanation") or not d.get("solutionStrategy") or len(d.get("solutionSteps", [])) != 5: errors.append(f"{p.name}: explanation/steps")
    if len(d.get("examPatternRefs", [])) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in d.get("examPatternRefs", [])): errors.append(f"{p.name}: refs")
    answers.add(d.get("answer", {}).get("value"))
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if len(answers) < 3: errors.append("answer distribution is not varied enough")
if errors: raise SystemExit("\n".join(errors))
report = ROOT / "implementation/reports/science-content-dc-iv-5-first-pass-review.json"
report.parent.mkdir(parents=True, exist_ok=True)
report.write_text(json.dumps({"unit": "Dc-Ⅳ-5：生物感應環境與維持恆定的探究", "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "questionCount": len(files), "passed": len(files), "notes": ["逐題核對刺激、感受、反應、向光、變因、對照、時間序列、恆定與結論界線。", "特別檢查植物向光不等於有眼睛、恆定不是數值固定，以及單次資料不能診斷或外推所有生物。", "公立學校公開資料僅作能力方向研究，題幹、選項、答案、解析與五步解法均為原創；版本研究與第二輪 AI／Terra 複核未完成，維持 draft。"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
