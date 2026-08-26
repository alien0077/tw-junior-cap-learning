#!/usr/bin/env python3
"""Audit M4 draft content for QA prioritization; does not change content status."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
by_subject = collections.defaultdict(lambda: {"lessons": 0, "questions": 0, "duplicate_prompts": 0, "generic_options": 0, "interactive_missing": 0})
prompts = collections.defaultdict(list)
for path in (ROOT / "questions").glob("*/*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "draft":
        continue
    subject = data["subject"]
    by_subject[subject]["questions"] += 1
    prompts[(subject, data.get("prompt", ""))].append(path)
    if data.get("options", [])[1:3] == [{"id": "B", "text": "只記頁碼"}, {"id": "C", "text": "只背選項順序"}]:
        by_subject[subject]["generic_options"] += 1
for (subject, _), paths in prompts.items():
    if len(paths) > 1:
        by_subject[subject]["duplicate_prompts"] += len(paths)
for path in (ROOT / "lessons").glob("*/*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "draft":
        continue
    subject = data["subject"]
    by_subject[subject]["lessons"] += 1
    if subject in {"math", "science"} and len(data.get("interactive", {}).get("steps", [])) < 3:
        by_subject[subject]["interactive_missing"] += 1
lines = ["# M4 Draft QA 稽核報告", "", "此報告只用於排序內容 QA，不會將 draft 升級為 content-reviewed。", "", "| 科目 | draft lessons | draft questions | 重複題幹題數 | 模板選項題數 | 缺互動 lesson |", "|---|---:|---:|---:|---:|---:|"]
for subject in ("chinese", "english", "math", "science", "social"):
    row = by_subject[subject]
    lines.append(f"| {subject} | {row['lessons']} | {row['questions']} | {row['duplicate_prompts']} | {row['generic_options']} | {row['interactive_missing']} |")
(ROOT / "docs/M4_DRAFT_QA_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("wrote docs/M4_DRAFT_QA_REPORT.md")
