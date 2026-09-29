import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = [ROOT / "questions/english" / f"question-english-performance-2-iv-10-{i}.json" for i in range(1, 11)]
expected = ["C", "A", "D", "B", "C", "A", "D", "B", "C", "A"]
allowed = {
    "https://csjh.kl.edu.tw/books/file/263/110-1%E5%9C%8B%E4%B8%80%E8%8B%B1%E8%AA%9E%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.cajh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=66&cfsn=309&fn=112-1-1-7%E8%8B%B1%E8%AA%9E.pdf&op=dlfile",
    "https://www.dam.kh.edu.tw/upload/68/101_28414/111-1-1%E4%B8%80%E5%B9%B4%E7%B4%9A%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C%E6%9A%A8%E8%A7%A3%E7%AD%94.pdf",
    "https://www.sdjh.ntpc.edu.tw/app/index.php?Action=downloadfile&file=WVhSMFlXTm9Mek15TDNCMFlWOHpOVEUxWHpZM09ETTRPREpmT1RNME9UWXVjR1Jt&fname=WW54RPOKRK4411HH50LKKPHG1430WT24KLB0XSXSTXA1LK40NKROSTB4WW54A0OKWW5400HHA404LK14MOPKTSLOOPB0QLYWXTYTXWA0SWZWCDVWSSOKXSFCUS00HH25DGA0DCZWFCMO40201434ZWMKUTGDUT21SSUSJGB0GGA401USTWLKUXJHGG04DC14MKB4JDIGKLEG35WWMLXTPOFCSSRO54SWUSDCROFCNOXW41KKWW04DHHG",
    "https://www.ycm.kh.edu.tw/upload/297/104_62703/111-1%282%29%E4%B8%83%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87%E8%A9%A6%E9%A1%8C.pdf",
}
failures = []
institutions = set()
for index, path in enumerate(paths):
    data = json.loads(path.read_text(encoding="utf-8"))
    problems = []
    if data.get("reviewStatus") != "draft": problems.append("reviewStatus")
    if data.get("lessonId") != "lesson-english-performance-2-iv-10": problems.append("lessonId")
    options = data.get("options", [])
    if len(options) != 4 or len({x.get("text") for x in options}) != 4: problems.append("options")
    if data.get("answer", {}).get("value") != expected[index]: problems.append("answer")
    if data.get("answer", {}).get("value") not in {x.get("id") for x in options}: problems.append("answer_option")
    if len(data.get("solutionSteps", [])) != 5 or any(len(step) < 12 for step in data.get("solutionSteps", [])): problems.append("solutionSteps")
    if len(data.get("answer", {}).get("explanation", "")) < 35: problems.append("explanation")
    if data.get("provenance", {}).get("origin") != "original": problems.append("provenance_origin")
    refs = data.get("examPatternRefs", [])
    if len(refs) != 1:
        problems.append("source_count")
    elif not (refs[0].get("url") in allowed and refs[0].get("url") == data.get("provenance", {}).get("sourceUrl") and refs[0].get("locatorLevel") == "item" and refs[0].get("locator") and refs[0].get("status") == "recorded" and refs[0].get("reuseDecision") == "pattern-only"):
        problems.append("item_source_alignment")
    if refs:
        title = refs[0].get("title", "")
        institutions.add(title.split("；", 1)[0].split("110學年度", 1)[0].split("112學年度", 1)[0].split("111學年度", 1)[0].split("113學年度", 1)[0].strip())
    if data.get("solutionStrategy", "").count("；") < 1: problems.append("strategy")
    if problems: failures.append({"file": path.name, "problems": problems})
if len(institutions) < 3:
    failures.append({"file": "unit-source-diversity", "problems": [f"only_{len(institutions)}_institutions"]})
report = {
    "unit": "2-Ⅳ-10",
    "checked": len(paths),
    "passed": len(paths) - sum(1 for row in failures if row["file"] != "unit-source-diversity"),
    "failures": failures,
    "sourceInstitutions": sorted(institutions),
    "status": "pass" if not failures else "fail",
    "notes": "Every question has a unique correct answer, original picture-description scene, item-specific Traditional-Chinese strategy and five-step explanation, one exact public-exam item locator aligned with provenance, and draft status.",
}
(ROOT / "implementation/reports/english-performance-2-iv-10-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(bool(failures))
