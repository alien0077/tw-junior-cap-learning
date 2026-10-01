#!/usr/bin/env python3
"""Audit social question-to-unit links without treating cross-domain vocabulary as an error."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# These patterns are retained only as descriptive coverage counters. Social-studies
# questions legitimately combine history, geography, civics and economics, so a
# keyword appearing outside a title token is not by itself a unit mismatch.
RULES = {
    "historical-timeline": r"史料|年代分別|建立時間線",
    "civ-budget": r"預算|居民意見|決策方式",
    "geography-map": r"地圖|地形|經緯度|人口密度|雨量|氣候",
    "economic-market": r"價格|供需|市場|成本|利潤",
}


def expected_lesson_id(path: Path):
    stem = path.stem
    m = re.fullmatch(r"question-(social-(?:content|performance)-.+)-([0-9]+)", stem)
    return f"lesson-{m.group(1)}" if m else None


def main():
    lessons = {}
    for p in (ROOT / "lessons" / "social").glob("*.json"):
        try:
            x = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if x.get("id"):
            lessons[x["id"]] = x.get("title", "")

    mismatches = []
    counts = {k: 0 for k in RULES}
    questions = sorted((ROOT / "questions" / "social").glob("*.json"))

    for p in questions:
        x = json.loads(p.read_text(encoding="utf-8"))
        prompt = str(x.get("prompt", ""))
        for kind, pattern in RULES.items():
            if re.search(pattern, prompt):
                counts[kind] += 1
                break

        rel = str(p.relative_to(ROOT))
        lesson_id = str(x.get("lessonId", "")).strip()
        expected = expected_lesson_id(p)

        if x.get("subject") != "social":
            mismatches.append({"path": rel, "kind": "subject", "actual": x.get("subject")})
        if not lesson_id or lesson_id not in lessons:
            mismatches.append({"path": rel, "kind": "lesson-missing", "lessonId": lesson_id})
        if expected and lesson_id != expected:
            mismatches.append({"path": rel, "kind": "lesson-link", "expected": expected, "actual": lesson_id})

        if lesson_id:
            expected_kg = "kg-" + lesson_id.removeprefix("lesson-")
            kg_ids = [str(v) for v in x.get("knowledgeIds", [])]
            if expected_kg not in kg_ids:
                mismatches.append({
                    "path": rel,
                    "kind": "knowledge-link",
                    "expected": expected_kg,
                    "actual": kg_ids,
                })

        locator = str(x.get("provenance", {}).get("sourceLocator", "")).strip()
        if not locator:
            mismatches.append({"path": rel, "kind": "source-locator-missing"})

    out = {
        "status": "pass" if not mismatches else "mismatch-found",
        "questionCount": len(questions),
        "archetypeCounts": counts,
        "mismatchCount": len(mismatches),
        "mismatches": mismatches,
        "note": (
            "Unit fit is gated by structural lesson/knowledge links and provenance locator. "
            "Cross-domain lexical archetypes are informational only because valid social-studies "
            "items routinely combine economic, historical, geographic and civic evidence."
        ),
    }
    (ROOT / "implementation" / "reports" / "social-question-unit-fit.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "status": out["status"],
        "questionCount": out["questionCount"],
        "archetypeCounts": out["archetypeCounts"],
        "mismatchCount": out["mismatchCount"],
        "firstMismatches": mismatches[:80],
    }, ensure_ascii=False))
    raise SystemExit(0 if not mismatches else 1)


if __name__ == "__main__":
    main()
