#!/usr/bin/env python3
"""Build a source-backed, per-lesson QA queue for M4 draft content."""
from __future__ import annotations

import glob
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    curriculum = {}
    for filename in glob.glob(str(ROOT / "curriculum" / "**" / "*.json"), recursive=True):
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
        curriculum[data["id"]] = data
    kg_by_curriculum = {}
    kg = {}
    for filename in glob.glob(str(ROOT / "knowledge" / "**" / "foundational-graph.json")):
        for node in json.loads(Path(filename).read_text(encoding="utf-8")).get("nodes", []):
            kg[node["id"]] = node
            for curriculum_id in node.get("curriculumIds", []):
                kg_by_curriculum[curriculum_id] = node["id"]
    lessons = {}
    for filename in glob.glob(str(ROOT / "lessons" / "**" / "*.json"), recursive=True):
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
        lessons[data["id"]] = data
    questions = defaultdict(list)
    for filename in glob.glob(str(ROOT / "questions" / "**" / "*.json"), recursive=True):
        data = json.loads(Path(filename).read_text(encoding="utf-8"))
        questions[data["lessonId"]].append(data)
    rows = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))["rows"]
    draft_rows = [row for row in rows if row.get("reviewStatus") == "draft"]
    subject = Counter(row["subject"] for row in draft_rows)
    missing = Counter()
    output = [
        "# M4 Draft QA Queue",
        "",
        "本清單由 coverage matrix、curriculum、KG、lesson、question 交叉產生；僅供逐筆內容 QA，不改變任何 reviewStatus。",
        "",
        "| 科目 | draft rows | 缺 lesson | 缺 KG | 少於 10 題 | 缺來源 |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    stats = {}
    for name in ("chinese", "english", "math", "science", "social"):
        current = [row for row in draft_rows if row["subject"] == name]
        counters = Counter()
        for row in current:
            lesson = lessons.get(row.get("lessonId"))
            kg_id = (lesson or {}).get("knowledgeIds", [None])[0]
            if lesson is None:
                counters["lesson"] += 1
            if not kg_id or kg_id not in kg:
                counters["kg"] += 1
            if len(questions.get(row.get("lessonId"), [])) < 10:
                counters["questions"] += 1
            if not (lesson or {}).get("studyReferences"):
                counters["source"] += 1
        stats[name] = counters
        output.append(f"| {name} | {len(current)} | {counters['lesson']} | {counters['kg']} | {counters['questions']} | {counters['source']} |")
        missing.update(counters)
    output += [
        "",
        f"總計：{len(draft_rows)} draft rows；缺 lesson {missing['lesson']}、缺 KG {missing['kg']}、少於 10 題 {missing['questions']}、缺來源 {missing['source']}。",
        "",
        "## 逐筆核對欄位",
        "",
        "每筆應核對：課綱 title 與 source locator、lesson content 是否實質回答該 title、question 選項與答案是否正確、以及 KG endpoint 是否對應。自動通過僅代表欄位存在，不代表學科內容正確。",
    ]
    (ROOT / "docs/M4_DRAFT_QA_QUEUE.md").write_text("\n".join(output) + "\n", encoding="utf-8")
    print(f"draft rows={len(draft_rows)}; missing lesson={missing['lesson']}; missing KG={missing['kg']}; fewer questions={missing['questions']}; missing source={missing['source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
