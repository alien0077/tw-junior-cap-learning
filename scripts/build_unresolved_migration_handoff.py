#!/usr/bin/env python3
"""Explain every question migration item that lacks a unique target unit."""
from __future__ import annotations

import collections
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    lines = ["# M4 無唯一 targetUnitId 題目阻塞清單", "", "這是由目前 migration manifest 與 KG 逐題交叉產生的 blocker。每筆題目都保留原始 lesson／question；請外部 ChatGPT 依課綱語意決定 target，不能因為題數門檻而強行歸類。", ""]
    total = 0
    for subject in ("chinese", "english", "math", "science", "social"):
        manifest = json.loads((ROOT / "migrations" / f"{subject}-question-migration-pilot.json").read_text())
        unresolved = [item for item in manifest["items"] if item.get("targetUnitId") is None]
        if not unresolved:
            continue
        kg = {}
        for path in (ROOT / "knowledge" / subject).glob("*.json"):
            for node in json.loads(path.read_text()).get("nodes", []):
                kg[node["id"]] = node
        grouped = collections.defaultdict(list)
        for item in unresolved:
            qpath = next(ROOT.rglob(f"{item['questionId']}.json"))
            q = json.loads(qpath.read_text())
            lesson = json.loads((ROOT / "lessons" / subject / f"{item['sourceLessonId']}.json").read_text())
            ids = tuple(sorted(set(q.get("knowledgeIds", [])) | set(lesson.get("knowledgeIds", []))))
            grouped[ids].append(item)
        lines += [f"## {subject}（{len(unresolved)} 題；{len(grouped)} 種 KG 組合）", ""]
        for ids, items in sorted(grouped.items(), key=lambda pair: (-len(pair[1]), pair[0])):
            labels = [f"{kg.get(i, {}).get('label', kg.get(i, {}).get('title', 'KG missing'))} ({i})" for i in ids]
            lines.append(f"### {len(items)} 題｜" + "、".join(labels))
            lines.append("")
            lines.append("- 目前判定：`blocked`（沒有唯一 teachable unit）")
            lines.append("- 題目：")
            for item in sorted(items, key=lambda x: x["questionId"]):
                lines.append(f"  - `{item['questionId']}`；lesson=`{item['sourceLessonId']}`")
            lines.append("")
        total += len(unresolved)
    lines += ["## 外部 ChatGPT 回傳要求", "", "請對每個 KG 組合或逐題回傳：targetUnitId、decision（assign／split／classification-only／blocked）、理由、官方 curriculum code、公開 sourceUrl、sourceLocator（PDF 頁碼／章節），以及是否需要重寫題目。", "", f"合計無唯一 targetUnitId：{total} 題。"]
    (ROOT / "docs/M4_UNRESOLVED_MIGRATION_HANDOFF.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote unresolved migration handoff: {total} questions")


if __name__ == "__main__":
    main()
