#!/usr/bin/env python3
"""Downgrade reviewed legacy non-content frames that lack version fusion.

The project constitution requires draft status when source research/fusion is
missing. This preserves all lesson content and only corrects the overstated
reviewStatus on historical performance/navigation frames.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {"learning-performance", "theme", "topic", "domain"}


def main():
    changed = []
    for path in sorted((ROOT / "lessons").glob("*/*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if (
            data.get("authoringStandard") == "full-lesson-v1"
            and data.get("reviewStatus") == "content-reviewed"
            and data.get("lessonScope") in SCOPES
            and not data.get("versionResearch")
            and not data.get("fusionRecord")
        ):
            data["reviewStatus"] = "draft"
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed.append({"lessonId": data.get("id"), "path": str(path.relative_to(ROOT)), "lessonScope": data.get("lessonScope")})
    report = {
        "updatedAt": "2026-09-07",
        "downgradedCount": len(changed),
        "reason": "Historical non-learning-content full-lesson frames lacked versionResearch/fusionRecord; constitution requires draft until source-aware fusion is complete.",
        "lessons": changed,
        "status": "downgraded-to-draft",
    }
    out = ROOT / "implementation" / "reports" / "legacy-noncontent-downgrade.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"downgradedCount": len(changed), "status": report["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
