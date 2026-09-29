import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "english").glob("question-english-performance-6-iv-4-*.json"))
failures = []
answer_counts = {key: 0 for key in "ABCD"}
prompts = set()
strategies = set()
all_steps = []
source_urls = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("lessonId") != "lesson-english-performance-6-iv-4": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    if data.get("prompt") in prompts: failures.append(f"{path.name}:duplicate-prompt")
    prompts.add(data.get("prompt"))
    strategies.add(data.get("solutionStrategy"))
    all_steps.extend(data.get("solutionSteps", []))
    if data.get("answer", {}).get("explanation") != (data.get("solutionSteps") or [None])[-1]: failures.append(f"{path.name}:answer-explanation-step-mismatch")
    if data.get("solutionSteps", []) and data["answer"]["value"] not in data["solutionSteps"][-1]: failures.append(f"{path.name}:final-key-mismatch")
    if data.get("answer", {}).get("value") in answer_counts: answer_counts[data["answer"]["value"]] += 1
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" for ref in refs): failures.append(f"{path.name}:examPatternRefs")
    source_urls.update(ref.get("url") for ref in refs)
    if any("bhjh.ntpc.edu.tw" in ref.get("url", "") or "pending-item-locator" in ref.get("status", "") for ref in refs): failures.append(f"{path.name}:unverified-source")
    if any(not ref.get("locator") or not ref.get("observedPattern") for ref in refs): failures.append(f"{path.name}:source-locator-pattern")
if len(prompts) != 10: failures.append("unit:prompt-uniqueness")
if len(strategies) != 10: failures.append("unit:strategy-uniqueness")
if len(all_steps) != 50 or len(set(all_steps)) != 50: failures.append("unit:solution-step-independence")
if answer_counts != {"A": 2, "B": 2, "C": 3, "D": 3}: failures.append(f"unit:answer-distribution:{answer_counts}")
if len(source_urls) != 3: failures.append(f"unit:source-diversity:{len(source_urls)}")
report = {"unit": "6-Ⅳ-4：接觸課外多元素材", "checked": len(paths), "passed": len(paths) - len(failures), "failures": failures, "answerDistribution": answer_counts, "distinctSourceUrls": len(source_urls), "distinctStrategies": len(strategies), "uniqueSolutionSteps": len(set(all_steps)), "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "逐題核答案鍵、解說、策略與步驟互異、來源定位及 pattern-only 界線；內容維持 draft。"}
out = ROOT / "implementation" / "reports" / "english-performance-6-iv-4-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
