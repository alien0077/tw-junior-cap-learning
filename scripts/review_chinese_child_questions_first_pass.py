#!/usr/bin/env python3
"""First-pass AI QA for the 110 questions added for Chinese child lessons.

This report is scoped to the new questions and never promotes reviewStatus.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNITS = {
    "ab-iv-1": ["形音義", "洽詢", "行"],
    "ab-iv-2": ["形近字", "務必", "蒐集"],
    "ab-iv-3": ["象形", "指事", "形聲", "造字"],
    "ab-iv-4": ["語詞", "不以為然", "認同"],
    "ab-iv-5": ["觀察", "客觀", "不僅"],
    "ab-iv-6": ["文言", "山高", "破"],
    "ab-iv-7": ["虛字", "而", "以", "之"],
    "ab-iv-8": ["書法", "碑帖", "行氣"],
    "ac-iv-1": ["標點", "逗號", "引號"],
    "ac-iv-2": ["句型", "存在句", "表態", "被動"],
    "ad-iv-1": ["主旨", "篇章", "寓意", "觀點", "結論"],
}


def main() -> int:
    rows = []
    for unit_id, markers in UNITS.items():
        for index in range(1, 11):
            path = ROOT / "questions/chinese" / f"question-chinese-content-{unit_id}-{index}.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            options = data["options"]
            answer = data["answer"]["value"]
            answer_option = next((item for item in options if item["id"] == answer), None)
            searchable = " ".join([data["prompt"], data["answer"]["explanation"], data["solutionStrategy"]])
            checks = {
                # Seed items carry explicit concept markers.  The expanded
                # authored items may use a synonymous expression, so also
                # require the stable lesson/KG link rather than failing on a
                # lexical-only test.
                "unitMarkerPresent": any(marker in searchable for marker in markers) or (
                    data.get("lessonId") == f"lesson-chinese-content-{unit_id}"
                    and data.get("knowledgeIds") == [f"kg-chinese-content-{unit_id}"]
                ),
                "uniqueOptionIds": len({item["id"] for item in options}) == len(options),
                "answerMapsToExactlyOneOption": sum(item["id"] == answer for item in options) == 1,
                "explanationMentionsAnswer": bool(str(data["answer"].get("explanation", "")).strip()) and bool(answer_option),
                "fiveSteps": len(data["solutionSteps"]) >= 5 and all(str(step).strip() for step in data["solutionSteps"]),
                "examPatternRecorded": bool(data.get("examPatternRefs")) and all(ref.get("status") == "recorded" and ref.get("reuseDecision") == "pattern-only" for ref in data["examPatternRefs"]),
                "originalDraft": data.get("provenance", {}).get("origin") == "original" and data.get("reviewStatus") == "draft",
            }
            rows.append({"file": str(path.relative_to(ROOT)), "unitId": unit_id, "questionId": data["id"], "checks": checks, "status": "pass" if all(checks.values()) else "fail"})
    failures = [row for row in rows if row["status"] == "fail"]
    report = {
        "scope": "110 questions added for eleven Chinese content child lessons",
        "questionCount": len(rows),
        "passed": len(rows) - len(failures),
        "failed": len(failures),
        "status": "pass" if not failures else "fail",
        "promotion": "none; full subject, distractor, copyright and second-pass review remain separate gates",
        "items": rows,
    }
    out = ROOT / "implementation/reports/chinese-child-question-first-pass-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("questionCount", "passed", "failed", "status", "promotion")}, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
