#!/usr/bin/env python3
"""Verify exact Bihua source locators and prevent index-only auto-promotion."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "implementation/reports/bihua-114-2-3-paper-audit.json"
LEDGER = ROOT / "implementation/reports/question-exam-pattern-ledger.json"
OUTPUT = ROOT / "implementation/reports/bihua-114-2-3-mapping-audit.json"
SOURCE_URL = "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    questions = {item["id"]: item for item in ledger["questions"]}
    errors: list[str] = []
    verified_ids: set[str] = set()
    mappings = []

    for paper in manifest["papers"]:
        path = ROOT / manifest["localCache"] / paper["filename"]
        if not path.is_file():
            errors.append(f"missing cached paper: {paper['filename']}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != paper["sha256"]:
            errors.append(f"paper hash mismatch: {paper['filename']}")
        for mapping in paper.get("verifiedMappings", []):
            question_id = mapping["questionId"]
            q = questions.get(question_id)
            if not q:
                errors.append(f"question missing from ledger: {question_id}")
                continue
            refs = [r for r in q["examPatternRefs"] if r.get("url") == SOURCE_URL]
            if len(refs) != 1:
                errors.append(f"{question_id}: expected exactly one Bihua source ref")
                continue
            ref = refs[0]
            expected = {
                "year": "114-2",
                "status": "recorded",
                "locatorLevel": "item",
                "reuseDecision": "pattern-only",
                "locator": f"校方附件「{paper['filename']}」{mapping['paperLocator'].replace('第', '第', 1)}",
            }
            for field, value in expected.items():
                if ref.get(field) != value:
                    errors.append(f"{question_id}: {field} mismatch")
            if "碧華" not in ref.get("title", "") or ref.get("pattern") != ref.get("observedPattern"):
                errors.append(f"{question_id}: title/pattern attribution mismatch")
            if not mapping.get("matchBasis"):
                errors.append(f"{question_id}: missing match basis")
            if question_id in verified_ids:
                errors.append(f"duplicate verified question mapping: {question_id}")
            verified_ids.add(question_id)
            mappings.append({"questionId": question_id, "paper": paper["filename"], "locator": ref.get("locator")})

    bihua_refs = [
        (q, ref)
        for q in ledger["questions"]
        for ref in q.get("examPatternRefs", [])
        if ref.get("url") == SOURCE_URL
    ]
    for q, ref in bihua_refs:
        if q["id"] in verified_ids:
            continue
        if ref.get("status") != "pending-item-locator" or ref.get("locatorLevel") != "page":
            errors.append(f"unmapped Bihua ref must remain pending/page: {q['id']}")

    report = {
        "status": "pass" if not errors else "fail",
        "cataloguedPapers": len(manifest["papers"]),
        "verifiedQuestionMappings": len(mappings),
        "bihuaQuestionRefs": len(bihua_refs),
        "verifiedBihuaRefs": len(verified_ids),
        "pendingBihuaRefs": len(bihua_refs) - len(verified_ids),
        "mappings": mappings,
        "errors": errors,
        "scopeNote": "This verifies source-file hashes and exact provenance locators, not answer correctness, copyright review, or lesson publication readiness.",
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "cataloguedPapers", "verifiedQuestionMappings", "bihuaQuestionRefs", "verifiedBihuaRefs", "pendingBihuaRefs", "errors")}, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
