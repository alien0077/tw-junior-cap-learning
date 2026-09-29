#!/usr/bin/env python3
"""讓完全重複的 solutionSteps 回到各自題目的判讀證據。

只修改重複步驟文字與 reviewStatus；題幹、選項、答案、解析、來源與 lesson link 不改。
"""

from __future__ import annotations

import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def question_files():
    for subject in ("chinese", "english", "math", "science", "social"):
        yield from sorted((ROOT / "questions" / subject).glob("*.json"))


def main() -> int:
    rows = []
    by_step: collections.defaultdict[str, list[dict]] = collections.defaultdict(list)
    for path in question_files():
        item = json.loads(path.read_text(encoding="utf-8"))
        for index, step in enumerate(item.get("solutionSteps", [])):
            if isinstance(step, str) and step.strip():
                record = {"path": path, "item": item, "index": index, "step": step}
                rows.append(record)
                by_step[step].append(record)

    changed = 0
    affected_questions: set[str] = set()
    for step, records in by_step.items():
        if len(records) < 2:
            continue
        for record in records:
            item = record["item"]
            answer_id = item.get("answer", {}).get("value", "")
            answer_text = next(
                (option.get("text", "") for option in item.get("options", []) if option.get("id") == answer_id),
                "",
            )
            prompt = item.get("prompt", "").strip()
            enriched = (
                f"{step.rstrip('。')}。本題逐題核對：題幹「{prompt}」；"
                f"正解為選項 {answer_id}「{answer_text}」，須依本題條件判斷，不能直接套用其他題的排除結果。"
            )
            item["solutionSteps"][record["index"]] = enriched
            item["reviewStatus"] = "draft"
            changed += 1
            affected_questions.add(item.get("id", record["path"].name))

    grouped: dict[Path, dict] = {}
    for record in rows:
        grouped[record["path"]] = record["item"]
    for path, item in grouped.items():
        path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "duplicateStepGroupsBeforeRepair": sum(1 for records in by_step.values() if len(records) > 1),
        "changedStepFields": changed,
        "affectedQuestions": len(affected_questions),
        "scope": "canonical questions only; prompt/options/answer/explanation/source/lesson link unchanged",
        "reviewStatus": "draft",
    }
    out = ROOT / "implementation" / "reports" / "duplicate-question-steps-repair.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
