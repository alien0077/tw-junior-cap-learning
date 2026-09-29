#!/usr/bin/env python3
"""Check every extracted spec's non-content QA contract without promoting status."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    results = []
    bundle = json.loads((ROOT / "implementation/unit-specs.bundle.json").read_text(encoding="utf-8"))
    for spec in bundle["units"]:
        block = spec["interactiveBlocks"][0]
        flow = " ".join(spec["contentFlow"])
        checks = {
            "touchTargetMinPx": spec["mobileA11y"].get("touchTargetMinPx", 0) >= 44,
            "keyboardAlternative": spec["mobileA11y"].get("keyboardAlternative") is True,
            "reducedMotion": bool(spec["mobileA11y"].get("reducedMotion")),
            "screenReader": bool(spec["mobileA11y"].get("screenReader")),
            "fallbackTest": any("fallback" in x.lower() for x in spec["testCases"]),
            "predict": "predict" in flow,
            "manipulate": "manipulate" in flow,
            "observe": "observe" in flow,
            "explain": "explain" in flow,
            "transfer": "transfer" in flow,
            "misconceptionFeedback": bool(block["misconceptionChecks"]) and all(block.get("feedback", {}).get("incorrect") for block in [block]),
            "studentActions": bool(block["studentActions"]),
        }
        results.append({"lessonId": spec["lessonId"], "passed": all(checks.values()), "checks": checks})
    failed = [r for r in results if not r["passed"]]
    report = {
        "units": len(results),
        "passed": len(results) - len(failed),
        "failed": len(failed),
        "failedLessonIds": [r["lessonId"] for r in failed],
        "checkCounts": dict(Counter(k for r in results for k, value in r["checks"].items() if value)),
        "status": "contract-passed" if not failed else "contract-failed",
        "note": "This is contract coverage only; runtime, content, source, copyright and pedagogical QA remain separate gates.",
    }
    out = ROOT / "implementation/reports/qa-contract.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"summary": report, "units": results}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
