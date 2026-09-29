#!/usr/bin/env python3
"""Repair three content lessons with evidence already present in the repo.

These are narrowly scoped metadata/research repairs.  The findings are
original summaries of the already recorded public source direction; no
publisher text, question, answer, or image is copied.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "implementation/reports/remaining-content-research-repair.json"


def load(subject: str, lesson_id: str) -> tuple[Path, dict]:
    for path in (ROOT / "lessons" / subject).glob("*.json"):
        item = json.loads(path.read_text(encoding="utf-8"))
        if item.get("id") == lesson_id:
            return path, item
    raise FileNotFoundError(lesson_id)


def main() -> None:
    changed = []

    path, item = load("chinese", "lesson-chinese-content-c")
    for record in item.get("versionResearch", []):
        if record.get("publisher") == "nani" and "http" not in record.get("sourceLocator", ""):
            record["sourceLocator"] = (
                "https://tutor.oneclass.com.tw/product/%E5%85%AB%E5%B9%B4%E7%B4%9A%E5%9C%8B%E8%AA%9E/；"
                + record["sourceLocator"]
            )
            changed.append({"lessonId": item["id"], "publisher": "nani", "change": "sourceLocator"})
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    path, item = load("english", "lesson-english-content-b-iv-8")
    item.setdefault("versionResearch", []).append(
        {
            "publisher": "nani",
            "edition": "南一國中英語公開期刊與閱讀資源",
            "sourceType": "public-web",
            "sourceLocator": "https://mag.nani.com.tw/?id1=2&id2=4；英語閱讀與教學周邊資源公開入口；未取得本單元受保護全文。",
            "reviewedAt": "2026-09-07",
            "findings": {
                "concepts": [
                    "引導式討論要先界定主題，再用問題、回應與追問逐步把個人意見轉成可理解的對話。",
                    "表達立場時需區分主張、理由與例證，並保留修正或追問的空間。",
                ],
                "representations": [
                    "以自編問題階梯、發言輪次卡、主張—理由—例證表和共識紀錄呈現討論進程。"
                ],
                "examplesOrEvidence": [
                    "公開入口可確認英語閱讀／教學資源的主題化組織；本課另寫校園午餐議題對話，要求學生用英文追問並整理不同立場。"
                ],
                "misconceptions": [
                    "把第一個想到的意見當成結論，或只說 I agree／I disagree 卻沒有理由與對話回應。"
                ],
                "assessmentEmphasis": [
                    "檢查學生能否提出與主題相關的問題、引用對話資訊、回應同伴並在新情境中重組理由。"
                ],
            },
            "licenseBoundary": "只研究南一公開入口的資源分類與教學方向；不複製或改寫教材、影音、題目、答案或圖片，本課全部材料原創。",
        }
    )
    changed.append({"lessonId": item["id"], "publisher": "nani", "change": "versionResearch"})
    path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result = {
        "updatedAt": "2026-09-07",
        "changedLessons": len({x["lessonId"] for x in changed}),
        "changedRecords": len(changed),
        "changes": changed,
        "statusRule": "reviewStatus and publisherEvidence remain unchanged",
    }
    REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
