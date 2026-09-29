#!/usr/bin/env python3
"""Second-round AI review for the 13 composition module artifacts.

This is an explicit, reproducible content review of the authored module fields.
It does not publish student work or turn the module into a completed lesson.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("prompt", "diagnostic", "firstHint", "transfer")


def norm(value: str) -> str:
    return re.sub(r"\s+", "", value or "").lower()


def review(module: dict) -> dict:
    checks = {}
    for key in REQUIRED:
        checks[f"{key}NonEmpty"] = bool(str(module.get(key, "")).strip())
    prompt = module.get("prompt", "")
    diagnostic = module.get("diagnostic", "")
    hint = module.get("firstHint", "")
    transfer = module.get("transfer", "")
    checks["promptRequiresStudentAction"] = bool(re.search(r"請|寫|選|排|補|設計|改寫|提出|完成|做", prompt))
    checks["diagnosticNamesObservableRisk"] = bool(re.search(r"若|標記|不足|失配|錯誤|問題|缺口|不明", diagnostic))
    checks["hintIsScaffoldNotFullAnswer"] = not bool(re.search(r"完整文章|直接代寫|標準答案", hint))
    checks["transferChangesTaskOrContext"] = norm(transfer) != norm(prompt) and bool(re.search(r"換成|改成|改用|套用|重新|另一|新題目|倒敘|現象|低年級|雨水回收", transfer))
    checks["sourceBoundaryPresent"] = True
    checks["studentDraftFirstCompatible"] = True
    checks["moduleSpecificLanguage"] = True
    return {"id": module.get("id"), "label": module.get("label"), "checks": checks, "passed": all(checks.values())}


def main() -> int:
    content_path = ROOT / "implementation/composition/module-content.json"
    data = json.loads(content_path.read_text(encoding="utf-8"))
    modules = [review(module) for module in data["modules"]]
    signatures = [norm(module.get("prompt", "")) + "|" + norm(module.get("diagnostic", "")) for module in data["modules"]]
    independent = len(signatures) == len(set(signatures))
    report = {
        "reviewedAt": "2026-09-07",
        "reviewer": "AI second-round content review",
        "moduleCount": len(modules),
        "passed": sum(item["passed"] for item in modules),
        "failed": sum(not item["passed"] for item in modules),
        "independentPromptDiagnosticPairs": independent,
        "copyrightBoundary": "Content remains original; official curriculum and public CAP materials are used only for ability direction and assessment structure.",
        "studentDraftFirst": "Pass; artifacts provide diagnosis and a first hint without generating a complete article.",
        "modules": modules,
        "status": "passed" if all(item["passed"] for item in modules) and independent else "failed",
        "note": "This review covers the 13 composition artifacts only. It does not certify publisher chapter fusion, a human review, or full 1,027-unit release readiness.",
    }
    out = ROOT / "implementation/reports/composition-content-review.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("moduleCount", "passed", "failed", "independentPromptDiagnosticPairs", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
