#!/usr/bin/env python3
"""Build a complete, handoff-ready list of all M4 items still in draft."""
import glob
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
matrix = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))
rows = [r for r in matrix["rows"] if r.get("reviewStatus") == "draft"]
lessons = {}
questions = Counter()
for filename in glob.glob(str(ROOT / "lessons" / "*" / "*.json")):
    data = json.loads(Path(filename).read_text(encoding="utf-8"))
    lessons[data["id"]] = data
for filename in glob.glob(str(ROOT / "questions" / "*" / "*.json")):
    data = json.loads(Path(filename).read_text(encoding="utf-8"))
    if data.get("reviewStatus") == "draft":
        questions[data.get("lessonId")] += 1

subject_names = {"chinese": "國文", "english": "英文", "math": "數學", "science": "自然", "social": "社會"}
lines = [
    "# M4 未完成項目清單（供 ChatGPT 協作）", "",
    "更新日期：2026-08-26", "",
    "本文件列出目前 coverage matrix 中所有 `draft` 項目，供外部 ChatGPT 尋找官方課綱、學校課程計畫、合法公開題源與核對方法。清單本身不代表內容正確。", "",
    "## 總覽", "",
    f"- Draft coverage rows：{len(rows)}",
    f"- Draft lessons：{sum(1 for x in lessons.values() if x.get('reviewStatus') == 'draft')}",
    f"- Draft questions：{sum(questions.values())}",
    "- 每個 draft row 已有 lesson、KG endpoint、至少 10 題與來源定位；缺口是單元級內容、答案與題目品質核對。", "",
    "## 請外部 ChatGPT 協助的工作", "",
    "1. 依每列的課綱代碼與官方 source locator，找出可公開核對的學習重點。",
    "2. 找南一、康軒、翰林及實際使用學校的公開課程計畫／目次；區分版本存在證據與逐章內容證據。",
    "3. 以合法公開或自編方式重寫 lesson 與 10 題 question；不要複製受著作權保護的課文、習題或題庫。",
    "4. 逐題驗證 options、answer.value、answer.explanation、KG endpoint、provenance；完成後才可將狀態升為 `content-reviewed`。", "",
    "## 欄位說明", "",
    "| 科目 | lesson ID | 課綱 title | KG IDs | draft 題數 | lesson 來源 | 模板警示 |", "|---|---|---|---|---:|---|---|",
]
for row in rows:
    lesson = lessons.get(row.get("lessonId"), {})
    refs = lesson.get("studyReferences", [])
    source = refs[-1] if refs else "（缺來源）"
    generic = "是" if lesson.get("content", {}).get("summary", "").startswith("依據「") else "否"
    lines.append("| {} | `{}` | {} | `{}` | {} | {} | {} |".format(
        subject_names.get(row.get("subject"), row.get("subject")), row.get("lessonId", ""),
        row.get("title", lesson.get("title", "")), ", ".join(lesson.get("knowledgeIds", [])),
        questions.get(row.get("lessonId"), 0), source, generic))

lines += ["", "## 使用限制", "", "- `draft` 是未完成狀態，不是錯誤標記；即使欄位完整，也不能視為教師／學科專家審閱。", "- `模板警示=是` 表示摘要仍是固定批次句型，應優先重寫；`否` 也仍須逐單元核對。", "- 版本／冊別 metadata 只能證明教材存在，不能直接證明 lesson 或 question 的內容正確。"]
(ROOT / "docs/M4_INCOMPLETE_ITEMS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {len(rows)} draft rows to docs/M4_INCOMPLETE_ITEMS.md")
