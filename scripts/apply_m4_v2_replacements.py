#!/usr/bin/env python3
"""Apply V2 replacement payloads non-destructively; blocked delete actions are retained."""
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ap = argparse.ArgumentParser(); ap.add_argument("source", type=Path); args = ap.parse_args()
src = args.source
def rows(name): return [json.loads(x) for x in (src / name).read_text().splitlines() if x.strip()]
lesson_paths = {p.stem: p for p in (ROOT / "lessons").glob("*/*.json")}
question_paths = {p.stem: p for p in (ROOT / "questions").glob("*/*.json")}
changed_l = changed_q = mapped = blocked = 0
for rec in rows("03_lessons_WITH_REPLACEMENTS.jsonl"):
    repl = rec.get("replacementLesson")
    if not isinstance(repl, dict) or rec.get("resolutionAction") != "replace-lesson-json": continue
    p = lesson_paths.get(rec["lessonId"])
    if not p: continue
    d = json.loads(p.read_text()); d["title"] = repl["title"]; d["content"] = {"summary": repl["summary"], "sections": repl["sections"]}
    d["studyHighlights"] = repl.get("studyHighlights", d.get("studyHighlights", []))
    if "interactive" in repl: d["interactive"] = repl["interactive"]
    d["reviewStatus"] = "draft"; d["updatedAt"] = "2026-08-27"
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n"); changed_l += 1
for rec in rows("04_questions_WITH_ACTUAL_REWRITES.jsonl"):
    repl = rec.get("replacementQuestion")
    if not isinstance(repl, dict) or rec.get("resolutionAction") != "replace-question-json": continue
    p = question_paths.get(rec["questionId"])
    if not p: continue
    d = json.loads(p.read_text()); d.update({"prompt": repl["prompt"], "options": repl["options"], "answer": repl["answer"], "difficulty": repl.get("difficulty", d.get("difficulty"))})
    d["reviewStatus"] = "draft"; d["updatedAt"] = "2026-08-27"; p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n"); changed_q += 1
manifests = [(p, json.loads(p.read_text())) for p in (ROOT / "migrations").glob("*-question-migration-pilot.json")]
for rec in rows("02_migration_FINAL_ACTIONS.jsonl"):
    if rec.get("resolutionAction") not in {"apply-targetUnitId", "rewrite-question-then-map"} or not rec.get("targetUnitId"): continue
    for p, d in manifests:
        hit = False
        for item in d.get("items", []):
            if item.get("questionId") == rec["questionId"]:
                item["targetUnitId"] = rec["targetUnitId"]; item["migrationStatus"] = "pending-review"; item["notes"] = rec.get("reason", "V2 target pending review"); hit = True
        if hit: mapped += 1
for p, d in manifests:
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
blocked = sum(1 for rec in rows("02_migration_FINAL_ACTIONS.jsonl") if rec.get("resolutionAction") == "delete-generated-question") + sum(1 for rec in rows("03_lessons_WITH_REPLACEMENTS.jsonl") if rec.get("resolutionAction", "").startswith("remove-")) + sum(1 for rec in rows("04_questions_WITH_ACTUAL_REWRITES.jsonl") if rec.get("resolutionAction") == "delete-question")
print(f"applied lessons={changed_l} questions={changed_q} migrations={mapped}; retained destructive candidates={blocked}")
