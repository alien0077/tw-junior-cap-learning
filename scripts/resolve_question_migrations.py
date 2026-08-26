#!/usr/bin/env python3
"""Resolve migration candidates from explicit KG/curriculum membership (audit only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
kg_to_cur = {}
for p in (ROOT / "knowledge").glob("*/foundational-graph.json"):
    for node in json.loads(p.read_text()).get("nodes", []):
        kg_to_cur[node["id"]] = set(node.get("curriculumIds", []))
units = {}
for p in (ROOT / "canonical-units").glob("*/canonical-unit-*.json"):
    d = json.loads(p.read_text())
    if d.get("teachable"):
        units[d["id"]] = set()
for p in (ROOT / "canonical-units").glob("*/mappings/unit-map-*.json"):
    d = json.loads(p.read_text())
    if d.get("unitId") in units:
        units[d["unitId"]].update(d.get("curriculumIds", []))
lesson_by_id = {}
question_by_id = {}
for p in (ROOT / "lessons").glob("*/*.json"):
    d = json.loads(p.read_text()); lesson_by_id[d["id"]] = d
for p in (ROOT / "questions").glob("*/*.json"):
    d = json.loads(p.read_text()); question_by_id[d["id"]] = d
results = []
for p in (ROOT / "migrations").glob("*-question-migration-pilot.json"):
    manifest = json.loads(p.read_text())
    for item in manifest.get("items", []):
        if item.get("targetUnitId") is not None:
            continue
        q = question_by_id.get(item["questionId"], {})
        lesson = lesson_by_id.get(item["sourceLessonId"], {})
        qkgs = list(q.get("knowledgeIds") or [])
        lkgs = list(lesson.get("knowledgeIds") or [])
        kgids = qkgs or lkgs
        curids = set().union(*(kg_to_cur.get(k, set()) for k in kgids))
        candidates = sorted(u for u, cids in units.items() if cids & curids and u.startswith(f"canonical-unit-{manifest['subject']}-"))
        if len(candidates) == 1:
            decision, target, reason, confidence = "map", candidates[0], "唯一 teachable canonical unit from explicit KG curriculum membership", 0.98
        else:
            decision, target = "blocked", None
            reason = "無唯一 teachable canonical unit；需外部語意核對" if candidates else "KG leaf 未對應 teachable canonical unit；需外部語意核對"
            confidence = 0.0
        results.append({"subject": manifest["subject"], "questionId": item["questionId"], "sourceLessonId": item["sourceLessonId"], "questionKnowledgeIds": qkgs, "lessonKnowledgeIds": lkgs, "candidateUnitIds": candidates, "decision": decision, "targetUnitId": target, "reason": reason, "confidence": confidence})
(ROOT / "migrations/m4-question-resolution.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
from collections import Counter
print(f"wrote migration audit: {len(results)} items; {Counter(x['decision'] for x in results)}")
