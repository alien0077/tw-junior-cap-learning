#!/usr/bin/env python3
"""Audit M4 draft content for QA prioritization; does not change content status."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
by_subject = collections.defaultdict(lambda: {"lessons": 0, "questions": 0, "duplicate_prompts": 0, "generic_options": 0, "interactive_missing": 0, "generic_lessons": 0, "cap_source": 0, "curriculum_source": 0})
prompts = collections.defaultdict(list)
for path in (ROOT / "questions").glob("*/*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("reviewStatus") != "draft":
        continue
    subject = data["subject"]
    by_subject[subject]["questions"] += 1
    source_url = data.get("provenance", {}).get("sourceUrl", "")
    if "cap.rcpet.edu.tw" in source_url:
        by_subject[subject]["cap_source"] += 1
    elif "stv.naer.edu.tw" in source_url:
        by_subject[subject]["curriculum_source"] += 1
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
    summary = data.get("content", {}).get("summary", "")
    if summary.startswith("依據「") and summary.endswith("整理核心概念、證據與應用。"):
        by_subject[subject]["generic_lessons"] += 1
    if subject in {"math", "science"} and len(data.get("interactive", {}).get("steps", [])) < 3:
        by_subject[subject]["interactive_missing"] += 1
lines = ["# M4 Draft QA 稽核報告", "", "此報告只用於排序內容 QA，不會將 draft 升級為 content-reviewed。重複題幹以同科同文字計算，可能反映相同課綱概念，仍需人工核對。", "", "| 科目 | draft lessons | 通用模板 lesson | draft questions | 重複題幹題數 | 模板選項題數 | 缺互動 lesson | CAP 來源題數 | 課綱來源題數 |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for subject in ("chinese", "english", "math", "science", "social"):
    row = by_subject[subject]
    lines.append(f"| {subject} | {row['lessons']} | {row['generic_lessons']} | {row['questions']} | {row['duplicate_prompts']} | {row['generic_options']} | {row['interactive_missing']} | {row['cap_source']} | {row['curriculum_source']} |")
lines += ["", "## 來源與狀態說明", "", "- `通用模板 lesson` 代表摘要仍為批次固定句型，必須先完成單元級內容重寫與核對。", "- 所有 draft 題目仍維持 `reviewStatus=draft`；來源 URL 僅表示課綱／會考範圍定位，不表示題目已通過學科審閱。", "- CAP 來源為教育部國中教育會考官方範圍頁；其餘為國家教育研究院課程綱要頁。", "- 目前沒有任何 draft lesson 因此報告而自動升級狀態。"]
(ROOT / "docs/M4_DRAFT_QA_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("wrote docs/M4_DRAFT_QA_REPORT.md")
