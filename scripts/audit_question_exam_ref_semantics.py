#!/usr/bin/env python3
"""Flag study-plan/lesson-plan documents incorrectly labeled as exam patterns."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"
REPORT = ROOT / "implementation/reports/question-exam-ref-semantics.json"

# URLs confirmed to be lesson plans rather than exam papers. Keep this exact
# source-level list alongside the generic title/year guard below.
NON_EXAM_URLS = {
    "https://lgt.ntpc.edu.tw/TeachPlanFile_Upload/2022/plan/641_plan.pdf",
    "https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf",
}
NON_EXAM_TERMS = re.compile(r"課程計畫|教案|簡案|教學計畫|lesson\s*plan", re.IGNORECASE)

# First-party identity checks for index pages whose displayed institution or
# exam metadata has previously been misattributed in question-level records.
# Keep unresolved index-only references pending until an attached paper is
# inspected and a question-level locator is recorded.
SOURCE_IDENTITY_RULES = {
    "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw": {
        "institution_token": "碧華",
        "year": "114-2",
        "required_status": "pending-item-locator",
        "verified_item_mappings": {
            "question-science-content-jf-iv-2-4": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第2頁第14題",
            },
            "question-science-content-jf-iv-2-7": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第3頁第18題",
            },
            "question-science-content-jf-iv-2-8": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第3頁第23題",
            },
            "question-science-performance-tr-iv-1-1": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第5頁第33題",
            },
            "question-science-performance-tr-iv-1-7": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級理化試題卷.pdf」第5頁第33題",
            },
            "question-english-performance-3-iv-6-1": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第2頁第20題",
            },
            "question-english-performance-3-iv-6-3": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第1頁第13題",
            },
            "question-english-performance-3-iv-6-2": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第2頁第30題",
            },
            "question-english-performance-3-iv-6-8": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第2頁第21題",
            },
            "question-english-performance-3-iv-6-9": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第2頁第24題",
            },
            "question-english-content-b-iv-5-1": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第3頁第46題",
            },
            "question-english-content-b-iv-5-2": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第3頁第42題",
            },
            "question-english-content-b-iv-5-3": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第4頁第47題",
            },
            "question-english-content-b-iv-5-5": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第4頁第48題",
            },
            "question-english-content-b-iv-5-9": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第4頁第52題",
            },
            "question-english-content-b-iv-5-4": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第4頁第43題",
            },
            "question-english-content-b-iv-6-8": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級英語試題卷.pdf」第3頁第45題",
            },
            "question-english-content-b-iv-6-1": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第4頁第43題",
            },
            "question-english-content-b-iv-6-7": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第3頁第48題",
            },
            "question-english-content-b-iv-6-9": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第4頁第47題",
            },
            "question-english-content-b-iv-6-10": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第4頁第53題",
            },
            "question-english-content-b-iv-7-7": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-八年級英語試題卷.pdf」第1頁第8題",
            },
            "question-english-root-a-05": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "PDF第2頁第23題：以 last week 語境選擇 cried 過去式；本題另設全新句子，僅借鑑過去時間詞與動詞形式判讀。",
            },
            "question-english-root-b-08": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "PDF第1頁第18題：依問句選出交代未到訪原因的對話回應；本題另創請求與承諾寄送時程情境。",
            },
            "question-math-root-a-04": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第3頁第16題",
            },
            "question-math-root-a-05": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第1頁第2題",
            },
            "question-math-root-a-06": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第1頁第6題",
            },
            "question-math-root-a-07": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第1頁第7題",
            },
            "question-math-root-a-08": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第2頁第8題",
            },
            "question-math-root-a-09": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第2頁第9題",
            },
            "question-math-root-a-13": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第1頁第4題",
            },
            "question-math-root-a-14": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第2頁第14題",
            },
            "question-math-root-a-15": {
                "status": "recorded",
                "locatorLevel": "item",
                "locator": "校方附件「114-2-3-七年級數學試題卷.pdf」第1頁第3題",
            },
        },
    },
}


def main() -> int:
    flagged: list[dict[str, object]] = []
    files_scanned = 0
    refs_scanned = 0
    for path in sorted(QUESTIONS.rglob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        files_scanned += 1
        for index, ref in enumerate(data.get("examPatternRefs", [])):
            refs_scanned += 1
            title = str(ref.get("title", ""))
            year = str(ref.get("year", ""))
            url = str(ref.get("url", ""))
            reasons = []
            if url in NON_EXAM_URLS:
                reasons.append("confirmed-non-exam-source-url")
            if NON_EXAM_TERMS.search(title) or NON_EXAM_TERMS.search(year):
                reasons.append("title-or-year-identifies-teaching-plan")
            identity_rule = SOURCE_IDENTITY_RULES.get(url)
            if identity_rule:
                if identity_rule["institution_token"] not in title:
                    reasons.append("source-institution-mismatch")
                if year != identity_rule["year"]:
                    reasons.append("source-year-mismatch")
                verified_mapping = identity_rule.get("verified_item_mappings", {}).get(data.get("id"))
                if verified_mapping:
                    for key, expected in verified_mapping.items():
                        if ref.get(key) != expected:
                            reasons.append(f"verified-item-{key}-mismatch")
                else:
                    if ref.get("status") != identity_rule["required_status"]:
                        reasons.append("index-only-source-not-pending-item-locator")
                    if ref.get("locatorLevel") != "page":
                        reasons.append("index-page-locator-level-mismatch")
            if reasons:
                flagged.append({
                    "questionId": data.get("id", path.stem),
                    "path": str(path.relative_to(ROOT)),
                    "refIndex": index,
                    "url": url,
                    "title": title,
                    "year": year,
                    "reasons": reasons,
                })

    counts = Counter(item["url"] for item in flagged)
    report = {
        "status": "pass" if not flagged else "blocked",
        "filesScanned": files_scanned,
        "examPatternRefsScanned": refs_scanned,
        "flaggedQuestionRefs": len(flagged),
        "affectedQuestionFiles": len({item["path"] for item in flagged}),
        "countsByUrl": dict(sorted(counts.items())),
        "findings": flagged,
        "note": "A flagged teaching plan is not a public exam source; move it only to a semantically valid reference field and retain each question as draft until sufficient verified exam-pattern evidence exists.",
    }
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in (
        "status", "filesScanned", "examPatternRefsScanned", "flaggedQuestionRefs", "affectedQuestionFiles", "countsByUrl"
    )}, ensure_ascii=False))
    return 0 if not flagged else 1


if __name__ == "__main__":
    raise SystemExit(main())
