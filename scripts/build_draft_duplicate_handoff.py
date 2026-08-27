#!/usr/bin/env python3
"""Expand duplicate draft prompts into a traceable ChatGPT handoff."""
from __future__ import annotations

import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    target_by_question = {}
    for path in (ROOT / "migrations").glob("*-question-migration-pilot.json"):
        manifest = json.loads(path.read_text())
        for item in manifest.get("items", []):
            target_by_question[item["questionId"]] = item.get("targetUnitId")
    groups = collections.defaultdict(list)
    for path in (ROOT / "questions").glob("*/*.json"):
        q = json.loads(path.read_text())
        if q.get("reviewStatus") == "draft":
            groups[(q["subject"], q.get("prompt", ""))].append(q)
    duplicate_groups = [(key, values) for key, values in groups.items() if len(values) > 1]
    duplicate_groups.sort(key=lambda item: (-len(item[1]), item[0][0], item[0][1]))
    no_target = collections.Counter()
    for _, values in duplicate_groups:
        for question in values:
            if target_by_question.get(question["id"]) is None:
                no_target[question["subject"]] += 1
    lines = [
        "# M4 Draft 重複題幹逐題核驗清單",
        "",
        "此文件由 repo 內 draft question 自動產生，只代表同科題幹文字完全相同；不代表題目必然錯誤。請逐群判斷是否為模板複製、合理的同概念變體，或需要重寫。",
        "",
        f"重複題幹群組：{len(duplicate_groups)}；涉及 draft 題目：{sum(len(v) for _, v in duplicate_groups)}。",
        "",
        "其中 targetUnitId 尚未唯一決定的 draft 題目：" + "、".join(f"{subject} {count} 題" for subject, count in sorted(no_target.items())) + "。這些不可因 parentId 缺少就強行遷移。",
        "",
        "## 回傳格式",
        "",
        "請對每個群組回傳 `keep`、`rewrite` 或 `blocked`，並說明依據；若 rewrite，請逐題提供新的題幹／選項／答案／解析與來源。不要只因文字相同就自動刪題。",
        "",
    ]
    for index, ((subject, prompt), questions) in enumerate(duplicate_groups, 1):
        lines.append(f"## G-{index:04d}｜{subject}｜{len(questions)} 題")
        lines.append("")
        lines.append(f"- 題幹：{prompt}")
        lines.append("- 建議判定：pending-review")
        lines.append("- 題目：")
        for q in sorted(questions, key=lambda item: item["id"]):
            lines.append(f"  - `{q['id']}`；lesson=`{q['lessonId']}`；targetUnitId=`{target_by_question.get(q['id'])}`；difficulty=`{q.get('difficulty')}`")
        lines.append("")
    (ROOT / "docs/M4_DRAFT_DUPLICATE_QUESTION_HANDOFF.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(duplicate_groups)} groups / {sum(len(v) for _, v in duplicate_groups)} questions")


if __name__ == "__main__":
    main()
