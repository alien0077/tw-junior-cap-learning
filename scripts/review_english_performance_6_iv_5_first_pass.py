import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions" / "english").glob("question-english-performance-6-iv-5-*.json"))
expected_keys = ["B", "D", "A", "C", "B", "D", "C", "A", "D", "B"]
expected_answer_fragments = [
    "meaning and part of speech in that context",
    "sustainable meaning environmental example",
    "which word function and meaning fit",
    "source, evidence, date, and another reliable source",
    "audio button and phonetic transcription",
    "noun meaning 'edition'",
    "exact keywords, useful URL, access date",
    "meaning, part of speech, tone, and example usage",
    "Open both sources, compare context and authority",
    "Author or organization, title, URL",
]
expected_urls = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf",
    "https://w3.hkjh.kh.edu.tw/%E5%B0%8F%E6%B8%AF%E5%9C%8B%E4%B8%AD%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/32%E4%B8%89%E5%B9%B4%E7%B4%9A%E4%B8%8B%E5%AD%B8%E6%9C%9F/1%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C/%E8%8B%B1%E8%AA%9E/105-2-1%20%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E7%A7%91%E8%A9%A6%E9%A1%8C.pdf",
    "https://jweb.kl.edu.tw/userfiles/1389/document/39208_0524%E7%AC%AC%E4%BA%94%E7%AF%80--%E4%B9%9D%E4%B8%8B%E8%8B%B1%E6%96%87%E4%BA%8C%E6%AE%B5.pdf",
}
primary_url = "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%80%E5%B9%B4%E7%B4%9A-%E8%8B%B1%E6%96%87_1.pdf"
expected_locators = [
    "PDF第4頁第24至26題",
    "PDF第5頁第51至53題",
    "PDF第2頁第13至27題",
]
failures = []
answer_counts = {key: 0 for key in "ABCD"}
prompts = set()
strategies = set()
all_steps = []
source_urls = set()

for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    question_number = int(path.stem.rsplit("-", 1)[1])
    if data.get("lessonId") != "lesson-english-performance-6-iv-5": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    options = data.get("options", [])
    option_ids = [option.get("id") for option in options]
    option_texts = [str(option.get("text", "")).strip() for option in options]
    if len(option_ids) != 4 or len(set(option_ids)) != 4: failures.append(f"{path.name}:option-ids")
    if len(option_texts) != 4 or any(not text for text in option_texts) or len(set(option_texts)) != 4:
        failures.append(f"{path.name}:option-texts")
    key = data.get("answer", {}).get("value")
    if key not in option_ids: failures.append(f"{path.name}:answer-key-not-an-option")
    if question_number < 1 or question_number > len(expected_keys):
        failures.append(f"{path.name}:unexpected-question-number")
    else:
        if key != expected_keys[question_number - 1]: failures.append(f"{path.name}:answer-key:{key}")
        correct_text = next((option.get("text", "") for option in options if option.get("id") == key), "")
        if expected_answer_fragments[question_number - 1].casefold() not in correct_text.casefold():
            failures.append(f"{path.name}:answer-text-mismatch")
    answer_counts[key] = answer_counts.get(key, 0) + 1
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if data.get("provenance", {}).get("sourceUrl") != primary_url:
        failures.append(f"{path.name}:primary-source-url")
    if not data.get("answer", {}).get("explanation", "").strip(): failures.append(f"{path.name}:missing-explanation")
    if data.get("answer", {}).get("explanation") != (data.get("solutionSteps") or [None])[-1]:
        failures.append(f"{path.name}:answer-explanation-step-mismatch")
    steps = data.get("solutionSteps", [])
    if len(steps) != 5 or any(not str(step).strip() for step in steps): failures.append(f"{path.name}:solution-steps")
    if steps and key not in steps[-1]: failures.append(f"{path.name}:final-step-key-mismatch")
    if not data.get("solutionStrategy", "").strip(): failures.append(f"{path.name}:missing-strategy")
    if data.get("prompt") in prompts: failures.append(f"{path.name}:duplicate-prompt")
    prompts.add(data.get("prompt"))
    strategies.add(data.get("solutionStrategy"))
    all_steps.extend(steps)

    refs = data.get("examPatternRefs", [])
    if len(refs) != 3: failures.append(f"{path.name}:reference-count")
    locators = [ref.get("locator", "") for ref in refs]
    if len(refs) == 3:
        for index, ref in enumerate(refs):
            if ref.get("url") not in expected_urls: failures.append(f"{path.name}:unverified-source-url")
            if ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only":
                failures.append(f"{path.name}:source-status-or-reuse")
            if ref.get("locatorLevel") != "page" or not ref.get("observedPattern"):
                failures.append(f"{path.name}:source-locator-or-pattern")
        for locator in expected_locators:
            if not any(locator in item for item in locators): failures.append(f"{path.name}:missing-locator:{locator}")
    if any("bhjh.ntpc.edu.tw" in ref.get("url", "") or "pending" in ref.get("status", "") for ref in refs):
        failures.append(f"{path.name}:pending-index-source")
    source_urls.update(ref.get("url") for ref in refs)

if len(paths) != 10: failures.append(f"unit:question-count:{len(paths)}")
if len(prompts) != 10: failures.append("unit:prompt-uniqueness")
if len(strategies) != 10: failures.append("unit:strategy-uniqueness")
if len(all_steps) != 50 or len(set(all_steps)) != 50: failures.append("unit:solution-step-independence")
if answer_counts != {"A": 2, "B": 3, "C": 2, "D": 3}: failures.append(f"unit:answer-distribution:{answer_counts}")
if source_urls != expected_urls: failures.append(f"unit:source-diversity:{len(source_urls)}")

report = {
    "unit": "6-Ⅳ-5：主動查詢工具書或網路",
    "checked": len(paths),
    "passed": len(paths) - len(failures),
    "failures": failures,
    "answerDistribution": answer_counts,
    "distinctSourceUrls": len(source_urls),
    "distinctStrategies": len(strategies),
    "uniqueSolutionSteps": len(set(all_steps)),
    "status": "pass" if len(paths) == 10 and not failures else "fail",
    "notes": "逐題核答案文字、選項、詳解末步與解析一致性、10種策略及50個步驟互異、三所公校試題精確頁題定位與pattern-only界線；內容維持draft。",
}
out = ROOT / "implementation" / "reports" / "english-performance-6-iv-5-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
