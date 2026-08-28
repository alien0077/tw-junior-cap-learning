#!/usr/bin/env python3
"""Deterministic semantic-risk scan; reports only, never promotes review status."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
risks = collections.Counter()
examples = collections.defaultdict(list)

def flag(kind, path):
    risks[kind] += 1
    if len(examples[kind]) < 20:
        examples[kind].append(str(path.relative_to(ROOT)))

lessons = {}
for p in (ROOT / "lessons").glob("*/*.json"):
    d = json.loads(p.read_text())
    lessons[d["id"]] = d
    if d.get("reviewStatus") != "draft":
        continue
    if "草稿" in d.get("title", ""):
        flag("draft-marker-in-title", p)
    summary = d.get("content", {}).get("summary", "")
    if summary.startswith("依據「") and summary.endswith("整理核心概念、證據與應用。"):
        flag("generic-lesson-summary", p)
    if d.get("subject") in {"math", "science"} and len(d.get("interactive", {}).get("steps", [])) < 3:
        flag("math-science-interaction-missing", p)

prompt_groups = collections.defaultdict(list)
for p in (ROOT / "questions").glob("*/*.json"):
    d = json.loads(p.read_text())
    if d.get("reviewStatus") != "draft":
        continue
    prompt_groups[(d.get("subject"), d.get("lessonId"), d.get("prompt", ""))].append(p)
    opts = d.get("options", [])
    if len(opts) < 2:
        flag("question-fewer-than-2-options", p)
    if not d.get("answer", {}).get("value"):
        flag("question-missing-answer", p)
    if not d.get("answer", {}).get("explanation", "").strip():
        flag("question-missing-explanation", p)
for (_, _, _), paths in prompt_groups.items():
    if len(paths) > 1:
        for p in paths:
            flag("duplicate-prompt-within-lesson", p)

lines = ["# M4 Semantic Risk Report", "", "本報告由 deterministic scan 產生，只排序風險，不會自動升級任何 reviewStatus。", "", "| 風險 | 數量 |", "|---|---:|"]
for k, n in sorted(risks.items()):
    lines.append(f"| {k} | {n} |")
if not risks:
    lines.append("| 未發現結構性風險 | 0 |")
lines += ["", "## 範例檔案（每類最多 20 筆）", ""]
for k in sorted(examples):
    lines.append(f"### {k}")
    lines.extend(f"- `{x}`" for x in examples[k])
    lines.append("")
(ROOT / "docs/M4_SEMANTIC_QA_REPORT.md").write_text("\n".join(lines), encoding="utf-8")
print(f"wrote semantic risk report; risk categories={len(risks)} flags={sum(risks.values())}")
