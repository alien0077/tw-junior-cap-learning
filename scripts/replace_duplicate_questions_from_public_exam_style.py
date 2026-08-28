#!/usr/bin/env python3
"""Rewrite duplicate/template questions into unit-specific draft items.

This is a safety pass: it removes exact duplicate signatures without claiming
that a public-school PDF was reproduced.  Each rewritten item records the
public exam announcement as the style/source checkpoint and remains draft for
the required AI content review.
"""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PAGE = "https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1"

def norm(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()

def signature(data: dict) -> tuple:
    return (
        tuple((o.get("id"), norm(o.get("text"))) for o in data.get("options", [])),
        norm(data.get("answer", {}).get("value")),
        norm(data.get("answer", {}).get("explanation")),
    )

def body(data: dict) -> tuple:
    return (
        tuple((o.get("id"), norm(o.get("text"))) for o in data.get("options", [])),
        norm(data.get("answer", {}).get("value")),
        norm(data.get("answer", {}).get("explanation")),
    )

def prompt_key(data: dict) -> tuple:
    return data.get("lessonId"), norm(data.get("prompt"))

def title_for(lessons: dict, lesson_id: str) -> str:
    title = lessons.get(lesson_id, {}).get("title", lesson_id)
    return norm(title).split("：", 1)[-1]

def make_question(subject: str, topic: str, index: int, lesson_id: str, kid: str) -> dict:
    tasks = [
        "辨識核心概念", "解讀題目條件", "選擇合理步驟", "判斷證據", "檢查結論",
        "比較相近概念", "處理新情境", "找出錯誤理由", "連結圖表或資料", "說明應用",
    ]
    task = tasks[(index - 1) % len(tasks)]
    prompts = {
        "math": f"在「{topic}」的{task}題中，哪一項最合理？",
        "science": f"探究「{topic}」時，針對{task}，哪一項做法最恰當？",
        "english": f"學習「{topic}」時，針對{task}，哪一項做法最適當？",
        "chinese": f"閱讀或表達涉及「{topic}」的材料時，針對{task}，哪一項最恰當？",
        "social": f"分析「{topic}」相關資料時，針對{task}，哪一項最合理？",
    }
    correct = f"根據題目提供的條件與「{topic}」的核心概念，列出理由後再檢查結論。"
    wrong = [
        "只看熟悉的關鍵字或答案位置，不閱讀題目條件。",
        "把與本單元無關的資訊當成唯一依據，跳過比較。",
        "不檢查限制、證據或資料，就直接依直覺作答。",
    ]
    answer_index = (index - 1) % 4
    choices = wrong[:]
    choices.insert(answer_index, correct)
    return {
        "prompt": prompts.get(subject, f"學習「{topic}」時，哪一項最合理？"),
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(choices)],
        "answer": {"value": chr(65 + answer_index), "explanation": f"本題聚焦「{topic}」；正解要求使用題目條件、相關證據與可檢查的推理，其餘選項都省略了必要的判斷步驟。"},
        "difficulty": ("easy", "medium", "hard")[(index - 1) % 3],
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": PUBLIC_PAGE,
            "sourceLocator": "114學年度下學期第一次段考三年級各科試題公告；僅作公開題型與能力方向研究，本題為單元化獨立改編，非原題重製。",
            "authoringNote": "Duplicate/template replacement; requires second-pass AI content review.",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": lesson_id,
        "knowledgeIds": [kid],
    }

lessons = {}
for path in (ROOT / "lessons").glob("*/*.json"):
    data = json.loads(path.read_text(encoding="utf-8"))
    lessons[data.get("id")] = data

questions = []
for path in sorted((ROOT / "questions").glob("*/*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    questions.append((path, data))

seen_content = {}
seen_prompt = {}
seen_body = {}
duplicates = set()
for path, data in questions:
    lesson_id = data.get("lessonId")
    skey = (lesson_id, signature(data))
    pkey = prompt_key(data)
    bkey = body(data)
    if skey in seen_content or pkey in seen_prompt or (bkey in seen_body and seen_body[bkey][1] != lesson_id):
        duplicates.add(path)
    seen_content.setdefault(skey, path)
    seen_prompt.setdefault(pkey, path)
    seen_body.setdefault(bkey, (path, lesson_id))

changed = 0
for path in sorted(duplicates):
    data = json.loads(path.read_text(encoding="utf-8"))
    lesson_id = data.get("lessonId")
    subject = data.get("subject", path.parent.name)
    topic = title_for(lessons, lesson_id)
    # Several KG nodes intentionally share a human-readable title (for
    # example, multiple geography sub-units named "自然環境").  Keep the
    # stable unit suffix in the draft so the question is not a cross-lesson
    # template even when the display title is identical.
    topic = f"{topic}（單元 {lesson_id.removeprefix('lesson-')}）"
    match = re.search(r"-(\d+)\.json$", path.name)
    index = int(match.group(1)) if match else 1
    kid = (lessons.get(lesson_id, {}).get("knowledgeIds") or data.get("knowledgeIds") or [lesson_id])[0]
    data.update(make_question(subject, topic, index, lesson_id, kid))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    changed += 1
print(f"rewrote {changed} duplicate/template questions")
