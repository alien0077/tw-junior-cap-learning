#!/usr/bin/env python3
"""Verify public-evidence coverage for every publisher/subject/volume.

This verifies the project claim that every M3 mapping has a traceable public
source.  It deliberately does not turn school evidence into publisher
endorsement: confidence remains stored on each mapping set.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SUBJECTS = ("chinese", "english", "math", "science", "social")
PUBLISHERS = ("nani", "kanghsuan", "hanlin")
VOLUMES = {"1", "2", "3", "4", "5", "6"}


def main() -> int:
    coverage: dict[tuple[str, str], set[str]] = defaultdict(set)
    evidence: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    errors: list[str] = []
    for path in sorted((ROOT / "textbook-mapping").glob("*/*.json")):
        item = json.loads(path.read_text(encoding="utf-8"))
        if not str(item.get("id", "")).startswith("mapset-"):
            continue
        subject, publisher = item.get("subject"), item.get("publisher")
        if subject not in SUBJECTS or publisher not in PUBLISHERS:
            continue
        source = item.get("source", {})
        url = str(source.get("url", ""))
        if urlparse(url).scheme != "https" or not urlparse(url).netloc:
            errors.append(f"{path}: missing public HTTPS evidence URL")
            continue
        if source.get("confidence") not in {"medium", "high"}:
            errors.append(f"{path}: public mapping evidence must be medium/high confidence")
        for volume in item.get("volumes", []):
            volume_id = str(volume.get("volume", ""))
            entries = volume.get("entries", [])
            if volume_id not in VOLUMES or not entries:
                continue
            coverage[(subject, publisher)].add(volume_id)
            evidence[(subject, publisher, volume_id)].append(
                {"path": path.relative_to(ROOT).as_posix(), "type": source.get("type"), "confidence": source.get("confidence")}
            )
    for subject in SUBJECTS:
        for publisher in PUBLISHERS:
            missing = sorted(VOLUMES - coverage[(subject, publisher)], key=int)
            if missing:
                errors.append(f"{subject}/{publisher}: no public evidence for volumes {', '.join(missing)}")
    if errors:
        print("\n".join(errors))
        return 1
    total = sum(len(entries) for entries in evidence.values())
    print(f"M3 public evidence verified: {len(evidence)} publisher/subject/volume cells, {total} source bindings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
