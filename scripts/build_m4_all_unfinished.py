#!/usr/bin/env python3
"""Build a line-by-line M4 unfinished-item handoff."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
names = {"chinese": "國文", "english": "英文", "math": "數學", "science": "自然", "social": "社會"}
matrix = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text())
lesson_by_id = {}
question_by_id = {}
for p in (ROOT / "lessons").glob("*/*.json"):
    d = json.loads(p.read_text()); lesson_by_id[d["id"]] = d
for p in (ROOT / "questions").glob("*/*.json"):
    d = json.loads(p.read_text()); question_by_id[d["id"]] = d
lines = ["# M4 未完成項目逐條清單", "", "更新日期：2026-08-26", "", "本文件逐條列出目前仍未完成或需外部判斷的項目。`draft`、`mapped`、`pending-review` 均不代表完成。", ""]
draft_rows = [r for r in matrix["rows"] if r.get("reviewStatus") == "draft"]
lines += ["## A. Draft lesson（逐條）", "", f"共 {len(draft_rows)} 筆。每筆需核對課綱內容、重寫通用模板並完成學科語意審核。", ""]
for i, r in enumerate(draft_rows, 1):
    lesson = lesson_by_id.get(r.get("lessonId"), {})
    lines.append(f"{i}. `{r.get('lessonId')}`｜{names.get(r.get('subject'), r.get('subject'))}｜{r.get('title', lesson.get('title',''))}｜status=draft｜需：內容、來源定位與語意審核")

draft_questions = [d for d in question_by_id.values() if d.get("reviewStatus") == "draft"]
lines += ["", "## B. Draft question（逐條）", "", f"共 {len(draft_questions)} 題。每題需核對選項、答案、解析、概念對齊與重複性。", ""]
for i, d in enumerate(sorted(draft_questions, key=lambda x: x["id"]), 1):
    lines.append(f"{i}. `{d['id']}`｜{names.get(d.get('subject'), d.get('subject'))}｜lesson=`{d.get('lessonId')}`｜status=draft｜需：逐題 QA")

unresolved = []
for p in (ROOT / "migrations").glob("*-question-migration-pilot.json"):
    d = json.loads(p.read_text())
    for item in d.get("items", []):
        if item.get("targetUnitId") is None:
            unresolved.append((d.get("subject"), item))
lines += ["", "## C. Migration unresolved（逐條）", "", f"共 {len(unresolved)} 題。需依 question/lesson 的 KG leaf 與語意決定 target；無法判斷須標記 blocked。", ""]
for i, (subject, item) in enumerate(sorted(unresolved, key=lambda x: x[1]["questionId"]), 1):
    lines.append(f"{i}. `{item['questionId']}`｜{names.get(subject, subject)}｜lesson=`{item['sourceLessonId']}`｜targetUnitId=null｜需：外部語意判斷")

units = []
for p in (ROOT / "canonical-units").glob("*/canonical-unit-*.json"):
    d = json.loads(p.read_text())
    if d.get("status") not in {"verified", "deprecated"}:
        units.append(d)
lines += ["", "## D. Canonical unit（逐條）", "", f"共 {len(units)} 個尚未 verified。需確認 official grouping、instructional cohesion、teachable 與 mapping relation。", ""]
for i, d in enumerate(sorted(units, key=lambda x: x["id"]), 1):
    lines.append(f"{i}. `{d['id']}`｜{names.get(d.get('subject'), d.get('subject'))}｜status={d.get('status')}｜teachable={d.get('teachable')}｜需：語意核驗")

lines += ["", "## E. 出版社章節來源（逐冊缺口）", "", "以下每冊都缺可公開固定定位的出版社正式逐章目次與逐碼 KG 對照：", ""]
for publisher, subjects, count in [("南一", "國文、英文、數學、自然、社會", 30), ("翰林非國文", "英文、數學、自然、社會", 24)]:
    for i in range(1, count + 1):
        lines.append(f"{i}. `{publisher}-{i:02d}`｜科目範圍：{subjects}｜需：出版社正式目次 URL、頁碼／章節定位、KG code；找不到則 blocked")

lines += ["", "## 外部回覆要求", "", "每條請回傳：`decision`、`targetUnitId`、`reason`、公開 `sourceUrl`、`sourceLocator`、必要的 `rewrite`、`confidence`。不得使用內部引用、搜尋摘要或猜測頁碼。", ""]
(ROOT / "docs/M4_ALL_UNFINISHED_ITEMS.md").write_text("\n".join(lines) + "\n")
print(f"wrote line-by-line handoff: lessons={len(draft_rows)} questions={len(draft_questions)} unresolved={len(unresolved)} units={len(units)}")
