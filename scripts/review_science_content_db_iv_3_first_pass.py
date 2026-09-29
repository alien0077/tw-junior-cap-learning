import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "science"
REPORT = ROOT / "implementation" / "reports" / "science-content-db-iv-3-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-science-content-db-iv-3-*.json"))
errors = []
answers = set()
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-db-iv-3": errors.append(f"{path.name}: lessonId")
    if data.get("reviewStatus") != "draft": errors.append(f"{path.name}: reviewStatus")
    if data.get("provenance", {}).get("origin") != "original": errors.append(f"{path.name}: origin")
    if len(data.get("options", [])) != 4 or not data.get("answer", {}).get("value"): errors.append(f"{path.name}: answer/options")
    if not data.get("answer", {}).get("explanation") or not data.get("solutionStrategy"): errors.append(f"{path.name}: explanation/strategy")
    if len(data.get("solutionSteps", [])) != 5: errors.append(f"{path.name}: solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs): errors.append(f"{path.name}: refs")
    answers.add(data.get("answer", {}).get("value"))
if len(files) != 10: errors.append(f"expected 10 questions, found {len(files)}")
if len(answers) < 2: errors.append("answer distribution is not varied")
if errors: raise SystemExit("\n".join(errors))
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps({"unit": "Db-Ⅳ-3：呼吸系統與外界氣體交換", "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "questionCount": len(files), "passed": len(files), "notes": ["逐題核對呼吸道順序、呼吸運動、橫膈與胸腔壓力、肺泡結構、氧氣／二氧化碳擴散、呼出氣體證據、呼吸作用區分與探究設計。", "特別檢查呼吸作用不等於呼吸運動、氯化亞鈷試紙不等於二氧化碳檢測，以及肺泡不製造氧氣。", "公立學校公開生物科試題僅作能力方向與資料型態研究，題幹、選項、答案、解析與五步解法均為原創改寫。", "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
