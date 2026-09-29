import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-1-iv-9-{i}.json" for i in range(1, 11)]
assert all(path.exists() for path in paths)
failures = []
institutions = set()
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8")); problems = []
    if data["lessonId"] != "lesson-english-performance-1-iv-9": problems.append("lessonId")
    if data["reviewStatus"] != "draft": problems.append("reviewStatus")
    if len(data["options"]) != 4 or len({item["text"] for item in data["options"]}) != 4: problems.append("options")
    if data["answer"]["value"] not in {item["id"] for item in data["options"]}: problems.append("answer")
    if data["provenance"]["origin"] != "original": problems.append("origin")
    if len(data["solutionSteps"]) != 5: problems.append("solutionSteps")
    refs = data["examPatternRefs"]
    if len(refs) != 1:
        problems.append("examPatternRefs_count")
    elif not (
        refs[0].get("reuseDecision") == "pattern-only"
        and refs[0].get("status") == "recorded"
        and refs[0].get("locatorLevel") == "item"
        and refs[0].get("locator")
        and refs[0].get("url") == data["provenance"].get("sourceUrl")
        and refs[0].get("url") in {
            "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E9%AB%98%E9%9B%84%E5%B8%82%E5%9C%8B%E6%98%8C%E5%9C%8B%E4%B8%AD%E4%BA%8C%E4%B8%8B%E8%8B%B1%E6%96%87%E8%81%BD%E5%8A%9B%E8%A7%A3%E6%9E%90%E5%8D%B7.pdf",
            "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=360&cfsn=2619&op=dlfile",
            "https://csjh.kl.edu.tw/books/file/528/111-1%E7%AC%AC%E4%B8%89%E6%AC%A1%E5%9C%8B%E4%B8%89%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
        }
    ):
        problems.append("examPatternRefs_item_source_alignment")
    if refs:
        institutions.add(refs[0].get("title", "").split("；", 1)[0].split("110學年度", 1)[0].split("111學年度", 1)[0].strip())
    if not data["answer"].get("explanation") or len(data["answer"]["explanation"]) < 35: problems.append("explanation")
    if any(len(step) < 12 for step in data["solutionSteps"]): problems.append("solutionSteps_detail")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(institutions) < 3:
    failures.append({"file": "unit-source-diversity", "problems": [f"only_{len(institutions)}_institutions"]})
report = {"unit": "1-Ⅳ-9", "checked": 10, "passed": 10 - sum(1 for item in failures if item["file"] != "unit-source-diversity"), "failures": failures, "sourceInstitutions": sorted(institutions), "status": "pass" if not failures else "fail", "notes": "Each item has one exact item-level, pattern-only source URL aligned with provenance; across the unit at least three public schools are represented. Original prompts, answers, explanations, tailored strategies, five detailed steps, and draft status are checked."}
(ROOT / "implementation/reports/english-performance-1-iv-9-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False)); raise SystemExit(bool(failures))
