import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-2-iv-12-{i}.json" for i in range(1, 11)]
expected = ["D", "B", "A", "C", "B", "D", "A", "C", "D", "B"]
allowed = {
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-3%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/3-%E8%8B%B1%E6%96%87.pdf",
    "https://www.dam.kh.edu.tw/upload/68/101_28414/104-1-1%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%A9%A6%E5%8D%B7.pdf",
}
failures = []
for index, path in enumerate(paths):
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = []
    options = data.get("options", [])
    answer = data.get("answer", {}).get("value")
    if data.get("reviewStatus") != "draft": problems.append("reviewStatus")
    if data.get("lessonId") != "lesson-english-performance-2-iv-12": problems.append("lessonId")
    if len(options) != 4 or len({option.get("text") for option in options}) != 4: problems.append("options")
    if answer != expected[index] or answer not in {option.get("id") for option in options}: problems.append("answer")
    if len(data.get("solutionSteps", [])) != 5 or any(len(step) < 12 for step in data.get("solutionSteps", [])): problems.append("solutionSteps")
    if len(data.get("answer", {}).get("explanation", "")) < 35: problems.append("explanation")
    if data.get("provenance", {}).get("origin") != "original": problems.append("origin")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 1:
        problems.append("source_count")
    elif not (refs[0].get("url") in allowed and refs[0].get("url") == data.get("provenance", {}).get("sourceUrl") and refs[0].get("locatorLevel") == "item" and refs[0].get("locator") and refs[0].get("status") == "recorded" and refs[0].get("reuseDecision") == "pattern-only"):
        problems.append("source_alignment")
    if problems: failures.append({"file": path.name, "problems": problems})
institutions = {"高雄市立大灣國民中學", "高雄市立國昌國民中學", "高雄市立大社國民中學"}
represented = sorted(name for name in institutions if any(name in json.loads(path.read_text(encoding="utf-8"))["examPatternRefs"][0]["title"] for path in paths))
if len(represented) < 3: failures.append({"file": "unit-source-diversity", "problems": [f"only_{len(represented)}_institutions"]})
report = {
    "unit": "2-Ⅳ-12",
    "checked": len(paths),
    "passed": len(paths) - sum(1 for row in failures if row["file"] != "unit-source-diversity"),
    "failures": failures,
    "sourceInstitutions": represented,
    "status": "pass" if not failures else "fail",
    "notes": "Original guided-discussion scenarios with varied answer keys, explanations, individualized Traditional-Chinese strategies and five detailed steps; exact item-level public-exam pattern ref aligned with provenance; draft only.",
}
(ROOT / "implementation/reports/english-performance-2-iv-12-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
