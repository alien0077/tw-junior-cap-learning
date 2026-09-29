import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
from refine_english_performance_5_iv_5_questions import SOURCES
paths = sorted((ROOT / "questions" / "english").glob("question-english-performance-5-iv-5-*.json"))
failures = []
expected_keys = {1: ("D", "train"), 2: ("B", "library"), 3: ("C", "hope"), 4: ("A", "/t/"), 5: ("D", "cries"), 6: ("B", "making"), 7: ("C", "cat"), 8: ("A", "stop"), 9: ("D", "boxes"), 10: ("B", "cleaned")}
expected_urls = {
    "https://www.nhjh.tp.edu.tw/30/2133/news/19/2021-7/2021-7-30-9-57-24-nf1.pdf",
    "https://www.nhjh.tp.edu.tw/uploads/1675415417084qr49L1rs.pdf",
    "https://www.dam.kh.edu.tw/upload/68/101_28414/106-1%E4%B8%80%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%28%E5%90%AB%E解答%29.pdf",
}
expected_urls = {source["url"] for source in SOURCES}
keys = Counter()
prompts, strategies, all_steps = [], [], []
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    number = int(path.stem.rsplit("-", 1)[1])
    if data.get("lessonId") != "lesson-english-performance-5-iv-5": failures.append(f"{path.name}:lessonId")
    if data.get("reviewStatus") != "draft": failures.append(f"{path.name}:reviewStatus")
    ids = {option.get("id") for option in data.get("options", [])}
    if len(ids) != 4 or data.get("answer", {}).get("value") not in ids: failures.append(f"{path.name}:options-answer")
    if data.get("provenance", {}).get("origin") != "original": failures.append(f"{path.name}:origin")
    if len(data.get("solutionSteps", [])) != 5: failures.append(f"{path.name}:solutionSteps")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 3 or {ref.get("url") for ref in refs} != expected_urls: failures.append(f"{path.name}:examPatternRefs")
    if any(ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("locatorLevel") not in {"page", "item", "paper"} for ref in refs): failures.append(f"{path.name}:source-status-or-locator")
    key, answer_text = expected_keys[number]
    options = {item.get("id"): item.get("text") for item in data.get("options", [])}
    if data.get("answer", {}).get("value") != key or options.get(key) != answer_text: failures.append(f"{path.name}:answer-mapping")
    if not data.get("answer", {}).get("explanation") or data.get("solutionSteps", [None])[-1] != data.get("answer", {}).get("explanation"): failures.append(f"{path.name}:explanation-mapping")
    keys[key] += 1
    prompts.append(data.get("prompt", ""))
    strategies.append(data.get("solutionStrategy", ""))
    all_steps.extend(data.get("solutionSteps", []))
if len(set(prompts)) != 10: failures.append("duplicate-prompts")
if len(set(strategies)) != 10: failures.append("duplicate-strategies")
if len(set(all_steps)) != 50: failures.append("duplicate-steps")
if keys != Counter({"A": 2, "B": 3, "C": 2, "D": 3}): failures.append("answer-distribution")
report = {"unit": "5-Ⅳ-5：拼讀規則讀拼字", "checked": len(paths), "passed": 10 if len(paths) == 10 and not failures else len(paths) - len(failures), "answerDistribution": dict(sorted(keys.items())), "sourceRefs": len(paths) * 3, "distinctStrategies": len(set(strategies)), "uniqueSteps": len(set(all_steps)), "failures": failures, "status": "pass" if len(paths) == 10 and not failures else "fail", "notes": "每題答案鍵與正解逐項核對；10種策略及50步詳解均不重複，逐題引用內湖、大社三份可定位的公校公開英文評量 pattern-only，內容仍為draft。"}
out = ROOT / "implementation" / "reports" / "english-performance-5-iv-5-first-pass-review.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
