import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
files = sorted((ROOT / "questions/social").glob("question-social-content-civ-ba-iv-4-*.json"))
failures = []
for path in files:
    data = json.loads(path.read_text(encoding="utf-8"))
    ids = {item.get("id") for item in data.get("options", [])}
    refs = data.get("examPatternRefs", [])
    checks = [len(data.get("options", [])) == 4, data.get("answer", {}).get("value") in ids,
              bool(data.get("answer", {}).get("explanation")), bool(data.get("solutionStrategy")),
              len(data.get("solutionSteps", [])) == 5, data.get("reviewStatus") == "draft",
              data.get("lessonId") == "lesson-social-content-civ-ba-iv-4", len(refs) == 3,
              all(ref.get("status") == "recorded" and ref.get("reuseDecision") == "pattern-only" for ref in refs)]
    if not all(checks): failures.append(path.name)
result = {"unit": "公 Ba-Ⅳ-4", "checked": len(files), "passed": len(files)-len(failures), "failures": failures,
          "status": "pass" if len(files) == 10 and not failures else "fail",
          "notes": "每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。"}
(ROOT / "implementation/reports/social-civ-ba-iv-4-first-pass-review.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
