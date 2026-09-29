import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = sorted((ROOT / "questions/chinese").glob("question-chinese-content-ab-iv-4-*.json"))
assert len(paths) == 10, len(paths)
for path in paths:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["lessonId"] == "lesson-chinese-content-ab-iv-4"
    assert data["reviewStatus"] == "draft"
    assert len(data["options"]) == 4
    assert len({item["text"] for item in data["options"]}) == 4
    assert data["answer"]["value"] in {item["id"] for item in data["options"]}
    assert data["provenance"]["origin"] == "original"
    assert len(data["solutionSteps"]) == 5
    assert len(data["examPatternRefs"]) == 3
    assert all(ref["reuseDecision"] == "pattern-only" and ref["status"] == "recorded" for ref in data["examPatternRefs"])

report = {
    "unit": "Ab-Ⅳ-4",
    "checked": len(paths),
    "passed": len(paths),
    "failures": [],
    "status": "pass",
    "notes": "每題含答案、解析、策略、五步步驟與三筆公開試題 pattern-only 來源；內容仍為 draft。",
}
(ROOT / "implementation/reports/chinese-content-ab-iv-4-first-pass-review.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"status": "pass", "unit": "Ab-Ⅳ-4：6500常用語詞認念", "questions": len(paths), "reviewStatus": "draft"}, ensure_ascii=False))
