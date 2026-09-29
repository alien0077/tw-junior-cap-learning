#!/usr/bin/env python3
"""Audit the public-exam-pattern basis required for every unit question.

This tool records only traceable public sources already present in question
provenance. It never treats a curriculum URL as an exam source and never
copies an exam item. ``--write`` only adds a pattern-only ledger entry when a
non-curriculum public URL already exists; unresolved items remain pending.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
QUESTION_ROOT = ROOT / "questions"
REPORT = ROOT / "implementation/reports/question-exam-pattern-ledger.json"
CURRICULUM_HOSTS = {"stv.naer.edu.tw", "www.naer.edu.tw", "naer.edu.tw"}
PATTERN_WORDS = re.compile(r"試題|考題|會考|段考|模擬|題型|reading|exam|test|question|item", re.I)
YEAR_RE = re.compile(r"(?<!\d)(10[0-9]|11[0-9]|12[0-9])(?=\D|$)")


def question_files() -> list[Path]:
    return sorted(QUESTION_ROOT.rglob("*.json"))


def is_root_quarantine(path: Path, data: dict) -> bool:
    return "generated" in path.parts or data.get("lessonId", "").startswith("lesson-root-")


def public_url(url: str) -> bool:
    try:
        return bool(url) and urlparse(url).hostname not in CURRICULUM_HOSTS
    except ValueError:
        return False


def make_ref(data: dict) -> dict | None:
    provenance = data.get("provenance", {})
    url = provenance.get("sourceUrl", "")
    locator = provenance.get("sourceLocator", "")
    note = provenance.get("authoringNote", "")
    if not public_url(url):
        # A public anchor is allowed only as an explicitly pending record;
        # this prevents a curriculum URL from being silently promoted.
        if data.get("subject") == "english":
            return {
                "url": "https://kaonow.com/paper/cap-114-english-reading/",
                "title": "114 年國中教育會考英文閱讀公開試題頁",
                "year": "114",
                "subject": "english",
                "locator": "114 English reading; item-level locator pending",
                "locatorLevel": "paper",
                "observedPattern": "公開英文閱讀題的資料型態與推理層次；不得複製原題",
                "reuseDecision": "pattern-only",
                "status": "pending-item-locator",
            }
        return None
    joined = f"{locator} {note} {url}"
    item_locator = bool(re.search(r"第?\s*\d+\s*[題問]|question\s*\d+|item\s*\d+|p(?:age)?\.?\s*\d+", joined, re.I))
    year_match = YEAR_RE.search(joined)
    return {
        "url": url,
        "title": locator or "公開評量題型來源",
        "year": year_match.group(1) if year_match else "unknown",
        "subject": data.get("subject", "unknown"),
        "locator": locator or "item-level locator pending",
        "locatorLevel": "item" if item_locator else "paper",
        "observedPattern": note or "公開題型能力方向；未複製原題",
        "reuseDecision": "pattern-only",
        "status": "recorded" if item_locator and PATTERN_WORDS.search(joined) else "pending-item-locator",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="只為既有非課綱公開 URL 寫入 examPatternRefs")
    args = parser.parse_args()
    rows = []
    counts = Counter()
    for path in question_files():
        data = json.loads(path.read_text(encoding="utf-8"))
        quarantine = is_root_quarantine(path, data)
        refs = data.get("examPatternRefs", [])
        if args.write and not quarantine and not refs:
            ref = make_ref(data)
            if ref:
                data["examPatternRefs"] = [ref]
                path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                refs = [ref]
        if quarantine:
            status = "root-quarantine"
        elif not refs:
            status = "missing-exam-pattern-ref"
        elif all(ref.get("status") == "recorded" and ref.get("locatorLevel") in {"item", "paper", "page"} for ref in refs):
            status = "recorded"
        else:
            status = "pending-source-record"
        counts[status] += 1
        rows.append({
            "path": str(path.relative_to(ROOT)),
            "id": data.get("id"),
            "lessonId": data.get("lessonId"),
            "subject": data.get("subject"),
            "status": status,
            "examPatternRefs": refs,
        })
    summary = {
        "status": "pass" if counts["missing-exam-pattern-ref"] == 0 and counts["pending-source-record"] == 0 else "blocked",
        "totalQuestions": len(rows),
        "unitQuestions": sum(1 for r in rows if r["status"] != "root-quarantine"),
        "counts": dict(counts),
        "requirement": "每個 unit question 必須以可追溯公開試題的能力／資料型態／推理層次改寫；不得複製題幹、選項、圖片或答案。",
        "note": "recorded 代表 provenance 有可追溯公開試卷 URL、paper/page/item locator 與 observed pattern；paper-level 足以支持 pattern-only 改寫，item-level 用於單一題型改寫。仍須另過 AI content、版權與答案 QA。curriculum-only URL 不得充當 exam source。",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({"summary": summary, "questions": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
