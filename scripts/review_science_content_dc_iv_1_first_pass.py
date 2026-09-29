import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions" / "science"
REPORT = ROOT / "implementation" / "reports" / "science-content-dc-iv-1-first-pass-review.json"
files = sorted(QUESTION_DIR.glob("question-science-content-dc-iv-1-*.json"))
errors = []
answers = set()
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-science-content-dc-iv-1":
        errors.append(f"{path.name}: lessonId")
    if data.get("reviewStatus") != "draft":
        errors.append(f"{path.name}: reviewStatus")
    if data.get("provenance", {}).get("origin") != "original":
        errors.append(f"{path.name}: origin")
    if len(data.get("options", [])) != 4 or not data.get("answer", {}).get("value"):
        errors.append(f"{path.name}: answer/options")
    if not data.get("answer", {}).get("explanation") or not data.get("solutionStrategy"):
        errors.append(f"{path.name}: explanation/strategy")
    if len(data.get("solutionSteps", [])) != 5:
        errors.append(f"{path.name}: solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(r.get("reuseDecision") != "pattern-only" or r.get("status") != "recorded" for r in refs):
        errors.append(f"{path.name}: refs")
    answers.add(data.get("answer", {}).get("value"))
if len(files) != 10:
    errors.append(f"expected 10 questions, found {len(files)}")
if len(answers) < 3:
    errors.append("answer distribution is not varied enough")
if errors:
    raise SystemExit("\n".join(errors))
REPORT.parent.mkdir(parents=True, exist_ok=True)
REPORT.write_text(json.dumps({
    "unit": "Dc-Ⅳ-1：神經系統察覺環境變動並產生反應",
    "status": "first-pass-ai-review-complete",
    "reviewStatus": "draft",
    "questionCount": len(files),
    "passed": len(files),
    "notes": [
        "逐題核對刺激、受器、感覺神經元、中樞、運動神經元、反應器官、反射與意識反應。",
        "特別檢查反射可由脊髓先行、疼痛感覺仍可由大腦形成，以及接尺實驗不能外推成整個神經系統發達程度。",
        "公立學校公開自然／生物科資料僅作能力方向與資料型態研究，題幹、選項、答案、解析與五步解法均為原創改寫。",
        "版本研究、第二輪 AI／Terra 複核與發布門檻尚未完成，因此維持 draft。",
    ],
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"reviewed {len(files)}/{len(files)} questions")
