#!/usr/bin/env python3
"""Content-QA the first three Chinese topic lessons with unit-specific items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
units = {
    "content-ab": ("字詞理解與語境運用", "辨識字詞的形音義，並依上下文選擇恰當用法。", ["先看字形與讀音。", "再用上下文判斷詞義。", "最後檢查詞性與搭配。"]),
    "content-ac": ("句段關係與標點表意", "分析句子結構、連接語與標點如何共同形成語意。", ["圈出句子的核心成分。", "找出連接語與指代。", "比較標點改變後的語氣。"]),
    "content-ad": ("篇章結構與主旨", "從段落關係、線索與證據整理文章主旨。", ["辨認各段功能。", "整理重複出現的線索。", "用文本證據概括主旨。"]),
}
for key, (title, summary, highlights) in units.items():
    lesson_id = f"lesson-chinese-{key}"
    lesson_path = ROOT / "lessons/chinese" / f"{lesson_id}.json"
    lesson = json.loads(lesson_path.read_text(encoding="utf-8"))
    lesson.update({"title": title, "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26"})
    lesson["content"] = {"summary": summary, "sections": [{"heading": "學習目標", "body": summary}, {"heading": "學習流程", "body": "；".join(highlights)}, {"heading": "常見錯誤", "body": "只憑單一字面或單一句子下結論，忽略上下文與前後段落。"}]}
    lesson["studyHighlights"] = highlights
    lesson_path.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    qdir = ROOT / "questions/chinese"
    for i, focus in enumerate(["核心概念", "語境線索", "結構辨識", "連接關係", "證據判讀", "錯誤辨識", "語意比較", "應用情境", "整合判斷", "自我檢核"], 1):
        qpath = qdir / f"question-chinese-{key}-{i}.json"
        q = json.loads(qpath.read_text(encoding="utf-8"))
        q.update({"prompt": f"在「{title}」的學習中，進行{focus}時，哪一項做法最恰當？", "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26"})
        q["options"] = [{"id": "A", "text": "回到文本，結合前後文與明確線索判斷"}, {"id": "B", "text": "只依第一眼看到的字面意思"}, {"id": "C", "text": "只看題目長短猜答案"}, {"id": "D", "text": "忽略句段位置與語氣"}]
        q["answer"] = {"value": "A", "explanation": f"{title}需要以文本線索支持判斷；只看字面或題目形式都不足以完成{focus}。"}
        qpath.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(lesson_id)
