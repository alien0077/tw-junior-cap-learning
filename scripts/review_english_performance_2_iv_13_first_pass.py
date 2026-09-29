#!/usr/bin/env python3
"""First-pass contract review for English performance unit 2-IV-13."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTION_DIR = ROOT / "questions/english"
REPORT = ROOT / "implementation/reports/english-performance-2-iv-13-first-pass-review.json"
EXPECTED = ["B", "B", "A", "C", "D", "B", "C", "B", "A", "C"]
EXPECTED_URLS = {
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf",
    "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2671&name=112-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%8C%A2%E5%AE%8F%E5%81%89.pdf&op=dlfile",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E4%BA%8C%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf",
    "https://school.tc.edu.tw/open-message/193521/get-file/61f258cb9b96df7136093939.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_5.pdf",
    "https://school.tc.edu.tw/open-message/193521/get-file/61f259ce3fa2fc1d7e423fab.pdf",
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-2%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf",
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-3%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf",
}
EXPECTED_SOURCE_HINTS = {
    1: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf", "克漏字對話第21題"),
    2: ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2671&name=112-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%8C%A2%E5%AE%8F%E5%81%89.pdf&op=dlfile", "聽力基本問答第9題"),
    3: ("https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2671&name=112-1-%E7%AC%AC2%E6%AC%A1%E6%AE%B5%E8%80%839%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE%E8%88%87%E7%AD%94%E6%A1%88-%E9%8C%A2%E5%AE%8F%E5%81%89.pdf&op=dlfile", "手寫題第2題"),
    4: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E4%BA%8C%E8%8B%B1%E6%96%87%E6%AE%B5%E8%80%83%E8%A9%A6%E9%A1%8C.pdf", "單題第6題"),
    5: ("https://school.tc.edu.tw/open-message/193521/get-file/61f258cb9b96df7136093939.pdf", "聽力言談理解第7題"),
    6: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%8B%B1%E8%AA%9E%E7%A7%91_5.pdf", "單題第3題"),
    7: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/1-%E8%8B%B1%E6%96%87.pdf", "克漏字對話第24題"),
    8: ("https://school.tc.edu.tw/open-message/193521/get-file/61f259ce3fa2fc1d7e423fab.pdf", "單題第33題"),
    9: ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C-2%E5%B9%B4%E7%B4%9A%E8%8B%B1%E6%96%87-%E8%A9%A6%E9%A1%8C.pdf", "閱讀對話第26題"),
    10: ("https://www.dwm.kh.edu.tw/upload/344/104_64184/106-2-3%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf", "對話選擇第39題"),
}


def main() -> int:
    rows = []
    for index, answer in enumerate(EXPECTED, 1):
        path = QUESTION_DIR / f"question-english-performance-2-iv-13-{index}.json"
        issues: list[str] = []
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        if not data:
            issues.append("missing-question")
        else:
            if data.get("id") != f"question-english-performance-2-iv-13-{index}":
                issues.append("stable-id-mismatch")
            if data.get("lessonId") != "lesson-english-performance-2-iv-13":
                issues.append("lesson-mismatch")
            if data.get("knowledgeIds") != ["kg-english-performance-2-iv-13"]:
                issues.append("knowledge-id-mismatch")
            if data.get("reviewStatus") != "draft":
                issues.append("must-remain-draft")
            if data.get("answer", {}).get("value") != answer:
                issues.append("answer-key-mismatch")
            options = data.get("options", [])
            if len(options) != 4 or len({o.get("id") for o in options}) != 4:
                issues.append("option-count-or-id-error")
            elif len({o.get("text", "").strip() for o in options}) != 4:
                issues.append("duplicate-options")
            if len(data.get("solutionSteps", [])) != 5:
                issues.append("solution-must-have-five-steps")
            if any(len(step.strip()) < 12 for step in data.get("solutionSteps", [])):
                issues.append("solution-step-too-short")
            if len(data.get("answer", {}).get("explanation", "").strip()) < 35:
                issues.append("explanation-too-short")
            ref_list = data.get("examPatternRefs", [])
            prov = data.get("provenance", {})
            if len(ref_list) != 1:
                issues.append("requires-one-item-level-source")
            else:
                ref = ref_list[0]
                expected_url, locator_hint = EXPECTED_SOURCE_HINTS[index]
                if ref.get("url") not in EXPECTED_URLS or ref.get("url") != prov.get("sourceUrl") or ref.get("url") != expected_url:
                    issues.append("source-url-unverified-or-mismatch")
                if ref.get("locatorLevel") != "item" or not re.search(r"第\s*\d+\s*題", ref.get("locator", "")):
                    issues.append("source-locator-not-item-specific")
                if locator_hint not in ref.get("locator", ""):
                    issues.append("source-item-locator-mismatch")
                if ref.get("reuseDecision") != "pattern-only" or ref.get("status") != "recorded":
                    issues.append("source-policy-status-error")
                if ref.get("subject") != "english":
                    issues.append("source-subject-mismatch")
            if prov.get("origin") != "original" or "未複製" not in prov.get("authoringNote", ""):
                issues.append("originality-or-rights-boundary-missing")
            if not data.get("solutionStrategy", "").strip():
                issues.append("missing-solution-strategy")
        rows.append({"id": data.get("id", f"question-english-performance-2-iv-13-{index}"), "path": str(path.relative_to(ROOT)), "answerExpected": answer, "status": "pass" if not issues else "fail", "issues": issues})

    urls = {json.loads(p.read_text(encoding="utf-8"))["provenance"]["sourceUrl"] for p in QUESTION_DIR.glob("question-english-performance-2-iv-13-*.json")}
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
    source_by_url = {source["url"]: source.get("institution", "") for source in catalog.get("sources", [])}
    catalog_missing = sorted(url for url in urls if url not in source_by_url)
    schools = {source_by_url[url] for url in urls if url in source_by_url}
    if catalog_missing:
        rows.append({"id": "source-catalog", "status": "fail", "issues": ["catalog-url-missing"] + catalog_missing})
    passed = sum(row["status"] == "pass" for row in rows[:10])
    summary = {"status": "pass" if passed == 10 and len(schools) >= 3 and not catalog_missing else "blocked", "unitId": "english-performance-2-iv-13", "reviewScope": "first-pass item contracts; not teacher/expert review or release approval", "questionCount": 10, "passedQuestions": passed, "sourceInstitutions": sorted(schools), "schoolCountMinimumMet": len(schools) >= 3, "draftRequired": True, "questions": rows, "catalogMissingUrls": catalog_missing, "sourceCache": "pending; official public PDF files were read online, local copies not yet verified"}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("status", "questionCount", "passedQuestions", "schoolCountMinimumMet", "catalogMissingUrls")}, ensure_ascii=False))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
