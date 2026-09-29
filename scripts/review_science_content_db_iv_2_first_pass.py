import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "science"
REPORT = ROOT / "implementation" / "reports" / "science-content-db-iv-2-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-science-content-db-iv-2-*.json"))
errors = []
answers = set()
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-db-iv-2": errors.append(f"{path.name}: lessonId")
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
REPORT.write_text(json.dumps({"unit": "Db-Ⅳ-2：循環系統的物質運輸與交換", "status": "first-pass-ai-review-complete", "reviewStatus": "draft", "questionCount": len(files), "passed": len(files), "notes": ["逐題核對血液成分、心臟瓣膜、心肺循環、微血管交換、抽血與運動情境、淋巴回流及循環系統模型。", "特別檢查動脈／靜脈以相對心臟流向定義，不把血管名稱直接等同含氧量；並區分微血管交換與大血管輸送。", "公立學校公開生物科試題僅作能力方向與資料型態研究，題幹、選項、答案、解析與五步解法均為原創改寫。", "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
