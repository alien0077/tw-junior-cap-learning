#!/usr/bin/env python3
"""Audit the required teaching-body shape for every content-scope lesson."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["hook", "explain", "worked-example", "guided-practice", "transfer", "reflect"]


def records():
    found = {}
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if "-performance" not in data.get("id", "") and "-domain" not in data.get("id", ""):
            found[data["id"]] = (path, data)
    return found


def main() -> int:
    rows = []
    failures = []
    for lesson_id, (path, data) in sorted(records().items()):
        body = data.get("teaching", {}).get("body", [])
        phases = [item.get("phase") for item in body]
        headings = [item.get("heading", "").strip() for item in body]
        texts = [item.get("body", "").strip() for item in body]
        valid = (
            len(body) >= len(REQUIRED)
            and all(phase in phases for phase in REQUIRED)
            and all(headings)
            and all(texts)
            and len(set(headings)) == len(headings)
            and len(set(texts)) == len(texts)
        )
        row = {
            "lessonId": lesson_id,
            "file": str(path.relative_to(ROOT)),
            "bodyCount": len(body),
            "phases": phases,
            "bodyCharacters": sum(len(text) for text in texts),
            "status": "pass" if valid else "fail",
        }
        rows.append(row)
        if not valid:
            failures.append(row)
    report = {
        "updatedAt": "2026-09-07",
        "scope": "canonical lessons/*/*.json non-framework lesson ids (excluding -performance and -domain)",
        "lessonCount": len(rows),
        "passed": len(rows) - len(failures),
        "failed": len(failures),
        "requiredPhases": REQUIRED,
        "minBodyCharacters": min((row["bodyCharacters"] for row in rows), default=0),
        "maxBodyCharacters": max((row["bodyCharacters"] for row in rows), default=0),
        "failures": failures,
    }
    out = ROOT / "implementation/reports/content-teaching-coverage.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
