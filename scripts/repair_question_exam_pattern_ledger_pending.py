#!/usr/bin/env python3
"""Remove one known unverified school-index citation from pending questions.

The ledger's remaining 344 rows all contain the same Bihua index citation,
which explicitly says the item/page has not been checked. Preserve all other
already-recorded refs. Six English root items have no other recorded ref, so
replace that index citation with verified public-school exam item mappings.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "implementation/reports/question-exam-pattern-ledger.json"
BAD_URL = "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw"

BHIHUA_INDEX = "https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw"
YICHANG_112_1 = (
    "https://www.ycjh.hlc.edu.tw/modules/tad_uploader/index.php?cat_sn=417&cfsn=2640"
    "&name=112-1-%E7%AC%AC1%E6%AC%A1%E6%AE%B5%E8%80%838%E5%B9%B4%E7%B4%9A%E8%8B%B1%E8%AA%9E%E7%A7%91%E9%A1%8C%E7%9B%AE-%E5%B4%94%E5%AE%8F%E4%BC%8A.pdf&op=dlfile"
)
GUOCHANG_110_2 = (
    "https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E8%8B%B1%E8%AA%9E%E5%8D%B7.pdf"
)
DAWAN_113_2 = (
    "https://www.dwm.kh.edu.tw/upload/344/104_64184/113%E5%AD%B8%E5%B9%B4%E5%BA%A6%E7%AC%AC%E4%BA%8C%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%8B%B1%E6%96%87%E4%BA%8C%E5%B9%B4%E7%B4%9A%E8%A9%A6%E9%A1%8C.pdf"
)

MAPPINGS = {
    "question-english-root-a-05": {
        "url": BHIHUA_INDEX,
        "title": "新北市立碧華國中114學年度第2學期第3次定期評量七年級英語試題卷.pdf",
        "year": "114-2",
        "locator": "PDF第2頁第23題：以 last week 語境選擇 cried 過去式；本題另設全新句子，僅借鑑過去時間詞與動詞形式判讀。",
        "pattern": "past-time marker and verb-form selection",
        "basis": "本地快取試卷標題、SHA-256與第2頁第23題原卷定位已由 Bihua paper audit 留存；題目只取過去時間詞與動詞形式辨識能力。",
        "paper": "114學年度第2學期第3次定期評量七年級英語科",
    },
    "question-english-root-b-05": {
        "url": YICHANG_112_1,
        "title": "花蓮縣宜昌國中112學年度第1學期第1次段考八年級英語試題卷.pdf",
        "year": "112-1",
        "locator": "PDF第4頁第19題：以 last week 語境辨認 studied 過去式；本題另設全新句子，僅借鑑時間標記與時態判讀。",
        "pattern": "past-time marker and verb-form selection",
        "basis": "公開原卷第4頁第19題測量 last week 與過去式動詞一致；本題句子、主詞及動詞均重新設計。",
        "paper": "112學年度第1學期第1次段考八年級英語科",
    },
    "question-english-root-a-08": {
        "url": YICHANG_112_1,
        "title": "花蓮縣宜昌國中112學年度第1學期第1次段考八年級英語試題卷.pdf",
        "year": "112-1",
        "locator": "PDF第2頁第7題：依對話情境選擇合適回應；本題另創請求與承諾寄送時程情境。",
        "pattern": "context-appropriate conversational response",
        "basis": "公開原卷第2頁第7題以對話情境選擇合適回應；本題用新請求、不同回應與寄送時程重新命題。",
        "paper": "112學年度第1學期第1次段考八年級英語科",
    },
    "question-english-root-b-08": {
        "url": BHIHUA_INDEX,
        "title": "新北市立碧華國中114學年度第2學期第3次定期評量七年級英語試題卷.pdf",
        "year": "114-2",
        "locator": "PDF第1頁第18題：依問句選出交代未到訪原因的對話回應；本題另創請求與承諾寄送時程情境。",
        "pattern": "context-appropriate conversational response",
        "basis": "本地快取試卷標題、SHA-256與第1頁第18題已由 Bihua paper audit 留存；只借鑑問答語用匹配，不使用原句或選項。",
        "paper": "114學年度第2學期第3次定期評量七年級英語科",
    },
    "question-english-root-a-11": {
        "url": GUOCHANG_110_2,
        "title": "高雄市立國昌國中110學年度第2學期第3次段考一年級英語科試題.pdf",
        "year": "110-2",
        "locator": "PDF第6頁第43題：綜合人物上課、補習及家庭行程，判斷可預約牙醫的時段；本題改為依天候備案讀取活動時間表。",
        "pattern": "schedule constraints and feasible-time inference",
        "basis": "官方公開原卷第6頁第43題以多項時間限制排除不可行時段；本題另創 rain/outdoor 兩方案，不複製原卷資料。",
        "paper": "110學年度第2學期第3次段考一年級英語科",
    },
    "question-english-root-b-11": {
        "url": DAWAN_113_2,
        "title": "高雄市立大灣國中113學年度第2學期第1次段考二年級英文試題.pdf",
        "year": "113-2",
        "locator": "PDF第1頁第8題：由對話判斷說話者是否同意對方；本題另創以尊重方式提出不同意見並邀請比較方案。",
        "pattern": "recognizing disagreement and appropriate response in dialogue",
        "basis": "校方公開原卷第1頁第8題測量對話中的不同意立場；本題另寫具建設性的異議表達，不複製聽力或選項。",
        "paper": "113學年度第2學期第1次段考二年級英語科",
    },
}


def ref(question: dict, spec: dict) -> dict:
    return {
        "url": spec["url"],
        "title": spec["title"],
        "year": spec["year"],
        "subject": "english",
        "locator": spec["locator"],
        "observedPattern": spec["basis"],
        "reuseDecision": "pattern-only",
        "status": "recorded",
        "locatorLevel": "item",
    }


def main() -> None:
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    pending = [q for q in data["questions"] if q.get("status") == "pending-source-record"]
    if len(pending) != 344:
        raise SystemExit(f"Refusing unexpected ledger state: pending={len(pending)}, expected=344")

    changed = []
    removed_with_other_evidence = []
    replaced_without_other_evidence = []
    for row in pending:
        path = ROOT / row["path"]
        question = json.loads(path.read_text(encoding="utf-8"))
        refs = question.get("examPatternRefs", [])
        bad_refs = [r for r in refs if r.get("url") == BAD_URL and r.get("status") != "recorded"]
        if len(bad_refs) != 1 or len(bad_refs) != sum(
            1 for r in refs if r.get("status") != "recorded"
        ):
            raise SystemExit(f"Refusing unexpected pending refs in {row['path']}")
        retained = [r for r in refs if r.get("url") != BAD_URL]
        if retained and all(r.get("status") == "recorded" for r in retained):
            question["examPatternRefs"] = retained
            removed_with_other_evidence.append(question["id"])
        else:
            spec = MAPPINGS.get(question.get("id"))
            if not spec or retained:
                raise SystemExit(f"No exact replacement mapping for {question['id']}")
            replacement = ref(question, spec)
            question["examPatternRefs"] = [replacement]
            question["provenance"]["sourceUrl"] = spec["url"]
            question["provenance"]["sourceLocator"] = (
                f"{spec['paper']}；{spec['locator']} 僅作 pattern-only 改寫，未複製原題、選項或答案。"
            )
            question["provenance"]["authoringNote"] = (
                "依官方課綱、KG與可追溯公立學校公開英文試題能力方向獨立編寫；"
                "題幹、選項、答案與解說均為原創，待後續題目內容／版權 gate。"
            )
            question["updatedAt"] = "2026-09-27"
            replaced_without_other_evidence.append({
                "questionId": question["id"],
                "lessonId": question.get("lessonId"),
                "schoolPaper": spec["paper"],
                "url": spec["url"],
                "locator": spec["locator"],
                "matchBasis": spec["basis"],
                "sha256": {
                    "question-english-root-a-05": "aa1b9993655f3d0dbae61707b6efeb6eb832e8ae3a2af92cab53202ca1a4f289",
                    "question-english-root-b-08": "aa1b9993655f3d0dbae61707b6efeb6eb832e8ae3a2af92cab53202ca1a4f289",
                }.get(question["id"]),
            })
        path.write_text(json.dumps(question, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        changed.append(question["id"])

    if len(removed_with_other_evidence) != 338 or len(replaced_without_other_evidence) != 6:
        raise SystemExit(
            f"Unexpected change split: removed={len(removed_with_other_evidence)}, "
            f"replaced={len(replaced_without_other_evidence)}"
        )

    report = {
        "reviewedAt": "2026-09-27",
        "status": "pending-reference-remediation-applied-validation-required",
        "scope": "Only the 344 rows then marked pending-source-record in question-exam-pattern-ledger.json.",
        "invalidReference": {
            "url": BAD_URL,
            "reason": "Official exam index only; each entry explicitly said subject attachment/page/item had not been checked, so it is not evidence of a question pattern.",
        },
        "removedInvalidReferenceWithOtherRecordedEvidence": {
            "count": len(removed_with_other_evidence),
            "questionIds": removed_with_other_evidence,
            "decision": "Retained all existing recorded public-school exam pattern references; removed only the non-evidence index citation.",
        },
        "replacementItemMappings": replaced_without_other_evidence,
        "changedQuestionCount": len(changed),
        "contentReviewBoundary": "This repairs source-ledger records only; it does not mark question content/answer/copyright review complete or promote any question from draft.",
    }
    out = ROOT / "implementation/reports/question-exam-pattern-ledger-pending-344-remediation.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "changed": len(changed),
        "invalidRefsRemovedWithOtherRecordedEvidence": len(removed_with_other_evidence),
        "exactItemRefsAdded": len(replaced_without_other_evidence),
        "report": str(out.relative_to(ROOT)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
