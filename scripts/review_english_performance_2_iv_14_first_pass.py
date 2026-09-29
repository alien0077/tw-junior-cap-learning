#!/usr/bin/env python3
"""First-pass contract review for English performance unit 2-IV-14."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-2-iv-14-first-pass-review.json"
EXPECTED = ["C", "D", "B", "A", "C", "D", "B", "A", "C", "D"]
SOURCE_HINTS = {
    1: ("https://oldcsjh.kl.edu.tw/books/file/360/110-1-%E4%B8%83%E5%B9%B4%E7%B4%9A3%E6%AE%B5%E8%80%830111.pdf", "第33題"),
    2: ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=449&cfsn=2995&fn=114-1-%E7%AC%AC3%E6%AC%A1%E6%AE%B5%E8%80%837%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E5%8D%B7-%E6%89%B6%E5%BF%97%E6%81%A9.pdf&op=dlfile", "第33題"),
    3: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_2.pdf", "第34題"),
    4: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf", "第32題"),
    5: ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2751&name=112-2-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E5%90%AB%E7%AD%94%E6%A1%88-%E5%B4%94%E5%AE%8F%E4%BC%8A.pdf&op=dlfile", "第42題"),
    6: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%B8%89%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E6%96%87%E7%A7%91_5.pdf", "第32題"),
    7: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/2-%E8%8B%B1%E6%96%87_6.pdf", "第35題"),
    8: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E9%A1%8C%E7%9B%AE%E5%8D%B7-%E7%94%A8%E5%88%97%E5%8D%B0%E7%AC%A6%E5%90%88.pdf", "第29題"),
    9: ("https://oldcsjh.kl.edu.tw/books/file/360/110-1-%E4%B8%83%E5%B9%B4%E7%B4%9A3%E6%AE%B5%E8%80%830111.pdf", "第35題"),
    10: ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=354&cfsn=2032&fn=105-2%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E8%A9%A6%E9%A1%8C%E5%8F%8A%E7%AD%94%E6%A1%88.pdf&op=dlfile", "第39題"),
}


def main() -> int:
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
    institutions = {source["url"]: source.get("institution", "") for source in catalog.get("sources", [])}
    rows = []
    urls = set()
    for i, expected in enumerate(EXPECTED, 1):
        path = QDIR / f"question-english-performance-2-iv-14-{i}.json"
        issues: list[str] = []
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        if not data:
            issues.append("missing-question")
        else:
            if data.get("id") != f"question-english-performance-2-iv-14-{i}": issues.append("stable-id-mismatch")
            if data.get("lessonId") != "lesson-english-performance-2-iv-14": issues.append("lesson-mismatch")
            if data.get("knowledgeIds") != ["kg-english-performance-2-iv-14"]: issues.append("knowledge-id-mismatch")
            if data.get("reviewStatus") != "draft": issues.append("must-remain-draft")
            if data.get("answer", {}).get("value") != expected: issues.append("answer-key-mismatch")
            options = data.get("options", [])
            if len(options) != 4 or len({o.get("id") for o in options}) != 4: issues.append("option-count-or-id-error")
            elif len({o.get("text", "").strip() for o in options}) != 4: issues.append("duplicate-options")
            if len(data.get("solutionSteps", [])) != 5 or any(len(s.strip()) < 12 for s in data.get("solutionSteps", [])): issues.append("detailed-five-step-solution-required")
            if len(data.get("answer", {}).get("explanation", "").strip()) < 35: issues.append("explanation-too-short")
            if len(data.get("solutionStrategy", "").strip()) < 20: issues.append("missing-solution-strategy")
            refs = data.get("examPatternRefs", [])
            prov = data.get("provenance", {})
            if len(refs) != 1:
                issues.append("requires-one-item-level-source")
            else:
                ref = refs[0]
                expected_url, hint = SOURCE_HINTS[i]
                urls.add(expected_url)
                if ref.get("url") != expected_url or ref.get("url") != prov.get("sourceUrl"): issues.append("source-url-mismatch")
                if hint not in ref.get("locator", "") or ref.get("locatorLevel") != "item" or not re.search(r"第\s*\d+\s*題", ref.get("locator", "")): issues.append("source-locator-mismatch")
                if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded" or ref.get("subject") != "english": issues.append("source-policy-or-subject-error")
                if expected_url not in institutions: issues.append("source-catalog-url-missing")
            if prov.get("origin") != "original" or "未複製" not in prov.get("authoringNote", ""): issues.append("originality-or-rights-boundary-missing")
        rows.append({"id": data.get("id", f"question-english-performance-2-iv-14-{i}"), "status": "pass" if not issues else "fail", "issues": issues})
    schools = {institutions[u] for u in urls if u in institutions}
    passed = sum(row["status"] == "pass" for row in rows)
    summary = {"status": "pass" if passed == 10 and len(schools) >= 3 else "blocked", "unitId": "english-performance-2-iv-14", "reviewScope": "first-pass source and item contracts; not teacher/expert review or release approval", "questionCount": 10, "passedQuestions": passed, "sourceInstitutions": sorted(schools), "schoolCountMinimumMet": len(schools) >= 3, "draftRequired": True, "questions": rows, "catalogMissingUrls": sorted(url for url in urls if url not in institutions), "sourceCache": "pending; public PDF source files were read online, local copies not yet verified", "terraSecondPass": "cancelled by user; not run"}
    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("status", "questionCount", "passedQuestions", "sourceInstitutions", "catalogMissingUrls")}, ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
