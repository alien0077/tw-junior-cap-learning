#!/usr/bin/env python3
"""Audit social question-to-unit links without treating cross-domain vocabulary as an error."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Descriptive coverage counters only. Social-studies items legitimately combine
# historical, geographic, civic and economic evidence, so keywords are not a
# sufficient reason to call an item off-unit.
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
        lesson_id = str(x.get("id", "")).strip()
        if lesson_id:
            lessons[lesson_id] = {
                "title": x.get("title", ""),
                "knowledgeIds": {str(v) for v in x.get("knowledgeIds", []) if str(v).strip()},
            }

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
        lesson = lessons.get(lesson_id)

        if x.get("subject") != "social":
            mismatches.append({"path": rel, "kind": "subject", "actual": x.get("subject")})
        if not lesson:
            mismatches.append({"path": rel, "kind": "lesson-missing", "lessonId": lesson_id})
        if expected and lesson_id != expected:
            mismatches.append({"path": rel, "kind": "lesson-link", "expected": expected, "actual": lesson_id})

        # Legacy alias lessons may intentionally bridge to a formal curriculum KG.
        # Validate the question against the KG mapping declared by its linked lesson.
        if lesson:
            q_kgs = {str(v) for v in x.get("knowledgeIds", []) if str(v).strip()}
            lesson_kgs = lesson["knowledgeIds"]
            if not q_kgs or not lesson_kgs or q_kgs.isdisjoint(lesson_kgs):
                mismatches.append({
                    "path": rel,
                    "kind": "knowledge-link",
                    "lessonId": lesson_id,
                    "lessonKnowledgeIds": sorted(lesson_kgs),
                    "questionKnowledgeIds": sorted(q_kgs),
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
            "Unit fit is gated by file/lesson linkage, the lesson-declared KG mapping and provenance locator. "
            "Cross-domain lexical archetypes are informational only. Legacy alias lessons may intentionally "
            "bridge to formal curriculum KGs."
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
