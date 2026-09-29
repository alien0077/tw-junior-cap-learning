import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions/social").glob("question-social-content-geo-ba-iv-3-*.json"))
failures = []
for path in files:
    item = json.loads(path.read_text(encoding="utf-8"))
    opts = item.get("options", [])
    refs = item.get("examPatternRefs", [])
    if (
        len(opts) != 4
        or item.get("answer", {}).get("value") not in {option.get("id") for option in opts}
        or not item.get("answer", {}).get("explanation")
        or not item.get("solutionStrategy")
        or len(item.get("solutionSteps", [])) != 5
        or len(refs) < 3
        or any(ref.get("status") != "recorded" or ref.get("reuseDecision") != "pattern-only" for ref in refs)
        or item.get("reviewStatus") != "draft"
        or item.get("lessonId") != "lesson-social-content-geo-ba-iv-3"
    ):
        failures.append(path.name)
report = {
    "unit": "地 Ba-Ⅳ-3",
    "checked": len(files),
    "passed": len(files) - len(failures),
    "failures": failures,
    "status": "pass" if len(files) == 10 and not failures else "fail",
    "sourceCountPerQuestion": 3,
    "note": "第一輪逐題契約檢查；題目以公立學校公開試題的能力與資料型態 pattern-only 參照，重新設計人口成長遷移與文化擴散情境，未複製原題。",
}
(ROOT / "implementation/reports/social-geo-ba-iv-3-first-pass-review.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(report, ensure_ascii=False))
raise SystemExit(0 if report["status"] == "pass" else 1)
