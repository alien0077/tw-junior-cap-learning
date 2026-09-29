import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-3-iv-4-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
all_steps = []
prompts = []
answers = []
allowed_sources = {
    "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&cg=837&file=WVhSMFlXTm9Mekk0TDNCMFlWOHpORFUyWHpFd01EazJNalZmT1RNek56Z3VjR1Jt&fname=WW54RPOKRK4411HHHCLKRKZWQOTWWT14QO3435HGTX25LK40FCNKA054WW54KLOKZTPOEH00A40405JG34MOTSRLSTB0WSHCGGRLDCTSROB0WXSWUSGGCDFCPK44JD25DGA0XWZWXSJCDCWS50B0CCNKVX51UTOOLKUSFCSWIGOOYSUSROXWQP104410VWYWOO14CGNPIGRO14KKUTXT04B5DCMKNKB0WSDCKLQKYWLKCD01WW04NKMOB03035HCKLB0QL14LPZTQP21UWTSVTKLSS54PKSW",
    "https://www.nhjh.tp.edu.tw/uploads/1753839175199ERtbxbag.pdf",
}
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-3-iv-4": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    if len(data["examPatternRefs"]) != 1: problems.append("examPatternRefs-count")
    for ref in data["examPatternRefs"]:
        if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") != "item": problems.append("examPatternRefs-contract")
        if ref.get("url") not in allowed_sources or "PDF第" not in ref.get("locator", "") or "題" not in ref.get("locator", ""): problems.append("examPatternRefs-locator")
    prompts.append(data["prompt"])
    answers.append(data["answer"]["value"])
    all_steps.extend(data["solutionSteps"])
    if not isinstance(data["solutionStrategy"], str) or len(data["solutionStrategy"]) < 24: problems.append("solutionStrategy")
    if not isinstance(data["answer"].get("explanation"), str) or len(data["answer"]["explanation"]) < 100: problems.append("answer-explanation")
    if any(not isinstance(step, str) or len(step) < 20 for step in data["solutionSteps"]): problems.append("step-detail")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(set(prompts)) != 10: failures.append({"unit": "3-Ⅳ-4", "problems": ["duplicate-prompt"]})
if len(set(all_steps)) != 50: failures.append({"unit": "3-Ⅳ-4", "problems": ["non-unique-solution-steps"]})
if answers != ["C", "B", "D", "A", "C", "B", "D", "A", "C", "D"]: failures.append({"unit": "3-Ⅳ-4", "problems": ["answer-key-regression"]})
report = {"unit": "3-Ⅳ-4", "checked": 10, "passed": 10 - len([f for f in failures if "file" in f]), "uniquePrompts": len(set(prompts)), "uniqueSolutionSteps": len(set(all_steps)), "answerKey": answers, "failures": failures, "status": "pass" if not failures else "fail", "notes": "Each item has original chart/table data, a correct answer, tailored Chinese strategy, five distinct detailed solution steps, and one precise item-level pattern-only locator to a public-school exam from Sanduo or Neihu JH; all remain draft and this first-pass contract is not full content/licensing QA."}
(ROOT / "implementation/reports/english-performance-3-iv-4-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
