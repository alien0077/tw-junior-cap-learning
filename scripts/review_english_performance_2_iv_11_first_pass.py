import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-2-iv-11-{i}.json" for i in range(1, 11)]
expected = ["C", "B", "A", "D", "C", "B", "A", "D", "C", "B"]
allowed = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%8B%B1%E6%96%87_4.pdf",
    "https://www.fjm.kh.edu.tw/upload/226/101_44845/113%E5%B9%B4%E5%9C%8B%E4%B8%AD%E7%B5%84%E9%96%B1%E8%AE%80%E7%B4%A0%E9%A4%8A%E8%A9%A6%E9%A1%8C%28%E7%AD%94%E6%A1%88%E5%85%AC%E5%91%8A%29.pdf",
    "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
}
failures = []
for index, path in enumerate(paths):
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = []
    if data.get("reviewStatus") != "draft": problems.append("reviewStatus")
    if data.get("lessonId") != "lesson-english-performance-2-iv-11": problems.append("lessonId")
    options = data.get("options", [])
    if len(options) != 4 or len({item.get("text") for item in options}) != 4: problems.append("options")
    answer = data.get("answer", {}).get("value")
    if answer != expected[index] or answer not in {item.get("id") for item in options}: problems.append("answer")
    if len(data.get("solutionSteps", [])) != 5 or any(len(step) < 12 for step in data.get("solutionSteps", [])): problems.append("solutionSteps")
    if len(data.get("answer", {}).get("explanation", "")) < 35: problems.append("explanation")
    if data.get("provenance", {}).get("origin") != "original": problems.append("origin")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 1:
        problems.append("source_count")
    elif not (refs[0].get("url") in allowed and refs[0].get("url") == data.get("provenance", {}).get("sourceUrl") and refs[0].get("locatorLevel") == "item" and refs[0].get("locator") and refs[0].get("status") == "recorded" and refs[0].get("reuseDecision") == "pattern-only"):
        problems.append("source_alignment")
    if problems: failures.append({"file": path.name, "problems": problems})
institutions = {
    "高雄市立國昌國民中學": "guochang",
    "鳳甲國中": "fengjia",
    "高雄市立燕巢國民中學": "yanchao",
}
represented = sorted(name for name in institutions if any(name in json.loads(p.read_text(encoding="utf-8"))["examPatternRefs"][0]["title"] for p in paths))
if len(represented) < 3: failures.append({"file": "unit-source-diversity", "problems": [f"only_{len(represented)}_institutions"]})
report = {
    "unit": "2-Ⅳ-11",
    "checked": len(paths),
    "passed": len(paths) - sum(1 for row in failures if row["file"] != "unit-source-diversity"),
    "failures": failures,
    "sourceInstitutions": represented,
    "status": "pass" if not failures else "fail",
    "notes": "Original dramatic scenes with answer, tailored Traditional-Chinese strategy and five detailed steps; one exact item-level public-school exam pattern ref aligned with provenance; all remain draft.",
}
(ROOT / "implementation/reports/english-performance-2-iv-11-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
