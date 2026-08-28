#!/usr/bin/env python3
"""Attach the exact official curriculum document URL to each lesson.

This only improves provenance and deliberately leaves reviewStatus unchanged.
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
curriculum = {}
for filename in glob.glob(str(ROOT / "curriculum" / "*" / "*.json")):
    path = Path(filename)
    data = json.loads(path.read_text(encoding="utf-8"))
    prefix = f"cur-{data['subject']}-"
    curriculum[f"kg-{data['subject']}-{data['id'].removeprefix(prefix)}"] = data

changed = 0
matched = 0
for filename in glob.glob(str(ROOT / "lessons" / "*" / "*.json")):
    path = Path(filename)
    lesson = json.loads(path.read_text(encoding="utf-8"))
    source_urls = set(lesson.get("studyReferences", []))
    source = None
    for kg_id in lesson.get("knowledgeIds", []):
        if kg_id in curriculum:
            source = curriculum[kg_id].get("source")
            break
    if not source or not source.get("url"):
        continue
    matched += 1
    source_urls.add(source["url"])
    updated = sorted(source_urls)
    if updated != lesson.get("studyReferences", []):
        lesson["studyReferences"] = updated
        path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed += 1

print(f"matched lessons={matched}; updated lessons={changed}")
