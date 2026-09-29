import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://www.nhjh.tp.edu.tw/uploads/1660183128914WHF2n4Sp.pdf"
EXPECTED_ANSWERS = {1: "C", 2: "A", 3: "D", 4: "B", 5: "A", 6: "C", 7: "D", 8: "B", 9: "A", 10: "C"}
EXPECTED_SOURCE_ITEMS = {1: 40, 2: 42, 3: 39, 4: 42, 5: 39, 6: 41, 7: 40, 8: 42, 9: 41, 10: 39}
MATCH_BASIS = {
    39: "等土盆、等土壤與等量供水下操弄植物密度，再以流出水狀態檢驗水土保持效果。",
    40: "由根系固定土壤、葉片影響雨滴沖刷等作用解釋植物的水土保持機制。",
    41: "在山林開發與保育的情境下，將環境評估和降低破壞納入方案判斷。",
    42: "判讀植物對空氣品質與氣溫作用的主張及其證據界線。",
}


def main() -> int:
    failures = []
    rows = []
    all_steps: dict[str, str] = {}
    catalog = json.loads((ROOT / "implementation/reports/public-exam-source-catalog.json").read_text(encoding="utf-8"))
    catalog_urls = {source["url"] for source in catalog.get("sources", [])}

    for number, answer in EXPECTED_ANSWERS.items():
        path = ROOT / f"questions/science/question-science-content-db-iv-8-{number}.json"
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        issues = []
        if not data:
            issues.append("missing-question")
        else:
            options = data.get("options", [])
            option_ids = {option.get("id") for option in options}
            if data.get("answer", {}).get("value") != answer or answer not in option_ids:
                issues.append("answer-option-mismatch")
            if len(options) != 4 or len({option.get("text", "").strip() for option in options}) != 4:
                issues.append("options-not-four-unique")
            steps = data.get("solutionSteps", [])
            if len(steps) != 5 or any(len(step.strip()) < 20 for step in steps):
                issues.append("five-detailed-steps-required")
            for step in steps:
                if step in all_steps:
                    issues.append(f"reused-solution-step:{all_steps[step]}")
                else:
                    all_steps[step] = data["id"]
            if data.get("reviewStatus") != "draft":
                issues.append("must-remain-draft")
            refs = [ref for ref in data.get("examPatternRefs", []) if ref.get("url") == SOURCE_URL]
            expected_item = EXPECTED_SOURCE_ITEMS[number]
            if not refs or not any(
                ref.get("status") == "recorded"
                and ref.get("locatorLevel") == "item"
                and f"第{expected_item}題" in ref.get("locator", "")
                and ref.get("reuseDecision") == "pattern-only"
                for ref in refs
            ):
                issues.append("exact-public-exam-item-ref-required")
            if SOURCE_URL not in catalog_urls:
                issues.append("source-url-not-in-catalog")
            provenance = data.get("provenance", {})
            if provenance.get("sourceUrl") != SOURCE_URL or provenance.get("origin") != "original":
                issues.append("provenance-not-aligned")
            if len(data.get("solutionStrategy", "").strip()) < 25:
                issues.append("unit-specific-strategy-required")
            if "不重製原卷內容" not in provenance.get("authoringNote", ""):
                issues.append("originality-boundary-missing")

        if issues:
            failures.append({"id": data.get("id", path.name), "issues": issues})
        rows.append({
            "id": data.get("id", path.name),
            "examItem": f"printed page 4, question {EXPECTED_SOURCE_ITEMS[number]}",
            "matchBasis": MATCH_BASIS[EXPECTED_SOURCE_ITEMS[number]],
            "status": "pass" if not issues else "fail",
            "issues": issues,
        })

    report = {
        "unit": "Db-Ⅳ-8",
        "checked": len(rows),
        "passed": len(rows) - len(failures),
        "uniqueDetailedSolutionSteps": len(all_steps),
        "source": SOURCE_URL,
        "sourceInstitution": "臺北市立內湖國中",
        "sourceAcademicTerm": "110學年度第二學期第三次段考",
        "sourceItemMappings": rows,
        "failures": failures,
        "status": "pass" if not failures and len(rows) == 10 else "fail",
        "scopeBoundary": "首輪題目／答案／詳解與來源定位核查；題目維持 draft，不代表出版社融合、完整 lesson、版權或最終發布審查通過。",
    }
    report_path = ROOT / "implementation/reports/science-db-iv-8-first-pass-review.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("unit", "checked", "passed", "uniqueDetailedSolutionSteps", "status")}, ensure_ascii=False))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
