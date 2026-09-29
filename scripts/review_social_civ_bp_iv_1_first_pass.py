import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/social").glob("question-social-content-civ-bp-iv-1-*.json"))
assert len(paths) == 10, len(paths)
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["lessonId"] == "lesson-social-content-civ-bp-iv-1"
    assert data["reviewStatus"] == "draft"
    assert len(data["options"]) == 4
    assert data["answer"]["value"] in {option["id"] for option in data["options"]}
    assert len(data["solutionSteps"]) == 5
    assert len(data["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" and ref["status"] == "recorded" for ref in data["examPatternRefs"])
    assert data["provenance"]["origin"] == "original"
report = {
    "unit": "公 Bp-Ⅳ-1",
    "checked": len(paths),
    "passed": len(paths),
    "failures": [],
    "status": "pass",
    "notes": "每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。",
}
(ROOT / "implementation/reports/social-civ-bp-iv-1-first-pass-review.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "pass", "unit": "公 Bp-Ⅳ-1：貨幣出現的原因", "questions": len(paths), "reviewStatus": "draft", "checks": ["答案", "四選一", "五步解題", "三筆公開來源", "原創與來源界線"]}, ensure_ascii=False))
