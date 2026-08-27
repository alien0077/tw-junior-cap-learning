#!/usr/bin/env python3
"""Build reversible draft canonical-unit and question migration manifests."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ("chinese", "english", "science", "social")


def load_all(directory: Path):
    return [json.loads(path.read_text()) for path in sorted(directory.glob("*.json"))]


def main() -> None:
    for subject in SUBJECTS:
        curriculum = load_all(ROOT / "curriculum" / subject)
        by_id = {item["id"]: item for item in curriculum}
        children = defaultdict(list)
        for item in curriculum:
            if item.get("level") == "learning-content" and item.get("parentId"):
                children[item["parentId"]].append(item["id"])
        out_dir = ROOT / "canonical-units" / subject
        mapping_dir = out_dir / "mappings"
        out_dir.mkdir(parents=True, exist_ok=True)
        mapping_dir.mkdir(parents=True, exist_ok=True)
        source_url = next((item.get("source", {}).get("url") for item in curriculum if item.get("source", {}).get("url")), "")
        units = {}
        for parent_id, curriculum_ids in sorted(children.items()):
            parent = by_id.get(parent_id, {})
            suffix = parent_id.removeprefix(f"cur-{subject}-").replace("_", "-")
            unit_id = f"canonical-unit-{subject}-{suffix}"
            units[unit_id] = curriculum_ids
            unit = {
                "id": unit_id,
                "subject": subject,
                "title": parent.get("title", f"{subject} 課綱單元 {suffix}"),
                "teachable": True,
                "gradeRange": ["7", "8", "9"],
                "curriculumIds": curriculum_ids,
                "status": "draft",
                "source": {
                    "type": "canonical-design",
                    "url": source_url,
                    "locator": "Draft grouping by official curriculum parentId; unit boundary and publisher alignment pending review.",
                    "verifiedAt": "2026-08-26",
                    "confidence": "low",
                },
            }
            (out_dir / f"{unit_id}.json").write_text(json.dumps(unit, ensure_ascii=False, indent=2) + "\n")
            mapping = {
                "id": f"unit-map-{subject}-{suffix}",
                "subject": subject,
                "unitId": unit_id,
                "curriculumIds": curriculum_ids,
                "relation": "covers",
                "status": "draft",
                "evidence": {
                    "type": "canonical-design",
                    "url": source_url,
                    "locator": "Draft parentId grouping only; not a claim about publisher chapter boundaries.",
                    "verifiedAt": "2026-08-26",
                    "confidence": "low",
                },
            }
            (mapping_dir / f"unit-map-{subject}-{suffix}.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n")

        kg_to_units = defaultdict(set)
        kg_files = load_all(ROOT / "knowledge" / subject)
        for graph in kg_files:
            for item in graph.get("nodes", []):
                for curriculum_id in item.get("curriculumIds", []):
                    for unit_id, ids in units.items():
                        if curriculum_id in ids:
                            kg_to_units[item["id"]].add(unit_id)
        lesson_units = {}
        for lesson in load_all(ROOT / "lessons" / subject):
            targets = sorted({unit for kg in lesson.get("knowledgeIds", []) for unit in kg_to_units.get(kg, set())})
            lesson_units[lesson["id"]] = targets[0] if len(targets) == 1 else None
        questions = load_all(ROOT / "questions" / subject)
        manifest_items = []
        for question in questions:
            target = lesson_units.get(question["lessonId"])
            status = "pending-review" if target else "not-applicable"
            note = "候選 unit 由官方 parentId 分群，待逐課綱／教材核對。" if target else "來源 lesson 尚無唯一 parentId unit 對應；保留原題，待人工判定。"
            manifest_items.append({"questionId": question["id"], "sourceLessonId": question["lessonId"], "targetUnitId": target, "migrationStatus": status, "notes": note})
        manifest = {"id": f"{subject}-question-migration-pilot", "subject": subject, "status": "in-progress", "items": manifest_items}
        (ROOT / "migrations" / f"{subject}-question-migration-pilot.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        print(f"{subject}: {len(units)} units, {len(questions)} questions, {sum(i['migrationStatus']=='pending-review' for i in manifest_items)} pending-review")


if __name__ == "__main__":
    main()
