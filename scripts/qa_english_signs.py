#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
key = "content-ac-iv-1"
lid = f"lesson-english-{key}"
lp = ROOT / "lessons/english" / f"{lid}.json"
lesson = json.loads(lp.read_text(encoding="utf-8"))
lesson.update({"title": "Ac-Ⅳ-1：簡易英文標示", "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26"})
lesson["content"] = {"summary": "理解公共場所常見英文標示，依關鍵字判斷方向、規則與禁止事項。", "sections": [
    {"heading": "學習目標", "body": "能讀懂 Exit、Entrance、No Smoking、Keep Quiet 等簡易標示，並依語意採取適當行動。"},
    {"heading": "學習流程", "body": "先辨認核心名詞或否定詞，再判斷標示的對象與行動，最後用場所情境核對。"},
    {"heading": "常見錯誤", "body": "忽略 No 等否定詞，或把 Entrance 與 Exit 的方向混淆。"}
]}
lesson["studyHighlights"] = ["先找標示關鍵字。", "注意否定與方向。", "用場所情境核對。"]
lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
items = [
    ("Exit means ___.", "a way out", "a way in", "a place to eat", "a place to sleep"),
    ("Entrance means ___.", "a way in", "a way out", "a warning", "a ticket"),
    ("No Smoking tells people ___.", "not to smoke", "to smoke", "to run", "to sit"),
    ("Keep Quiet asks people to ___.", "be quiet", "shout", "sing loudly", "leave immediately"),
    ("A sign says 'Wet Floor.' You should ___.", "walk carefully", "run", "touch the floor", "turn off the lights"),
    ("'Push' tells you to ___.", "push the door", "pull the door", "lock the door", "paint the door"),
    ("'Pull' tells you to ___.", "pull the door", "push the door", "break the door", "ignore the door"),
    ("'No Parking' means you must not ___.", "park there", "walk there", "read there", "wait there"),
    ("At a 'Restroom' sign, you can find ___.", "a toilet", "a library", "a bank", "a kitchen"),
    ("'Emergency Exit' is used when people need to ___.", "leave safely", "buy food", "watch a movie", "borrow a book")
]
for i, (prompt, answer, b, c, d) in enumerate(items, 1):
    qp = ROOT / "questions/english" / f"question-english-{key}-{i}.json"
    q = json.loads(qp.read_text(encoding="utf-8"))
    q.update({"prompt": prompt, "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26",
              "options": [{"id": "A", "text": answer}, {"id": "B", "text": b}, {"id": "C", "text": c}, {"id": "D", "text": d}],
              "answer": {"value": "A", "explanation": f"依公共標示的英文語意，正確解讀為：{answer}。"}})
    qp.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
m = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))
for row in m["rows"]:
    if row.get("lessonId") == lid:
        row.update({"contentStatus": "content-reviewed", "reviewStatus": "content-reviewed"})
(ROOT / "data/m4-coverage-matrix.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(lid)
