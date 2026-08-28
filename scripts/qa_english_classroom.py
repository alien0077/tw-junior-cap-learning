#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
key = "content-ac-iv-2"
lid = f"lesson-english-{key}"
lp = ROOT / "lessons/english" / f"{lid}.json"
lesson = json.loads(lp.read_text(encoding="utf-8"))
lesson.update({"title": "Ac-Ⅳ-2：常見教室用語", "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26"})
lesson["content"] = {"summary": "理解並在課堂情境中使用常見英文指令、請求與回應。", "sections": [
    {"heading": "學習目標", "body": "能理解 Open your book、Listen carefully、May I come in? 等教室用語並做適當回應。"},
    {"heading": "學習流程", "body": "先辨認指令或請求，再判斷說話者意圖，最後用完整情境選擇回應。"},
    {"heading": "常見錯誤", "body": "把祈使句誤當問題，或忽略 May I、Please 等禮貌表達。"}
]}
lesson["studyHighlights"] = ["辨認指令與請求。", "注意禮貌語氣。", "用課堂情境回應。"]
lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
items = [
    ("'Open your book' asks students to ___.", "open the book", "close the book", "leave the room", "write a letter"),
    ("'Listen carefully' means ___.", "pay attention", "run outside", "sleep", "draw a map"),
    ("'Raise your hand' asks students to ___.", "put a hand up", "open a door", "sit on the floor", "turn off a light"),
    ("'Work in pairs' means work with ___.", "one partner", "the whole city", "no one", "a dictionary only"),
    ("A polite way to ask permission to enter is ___.", "May I come in?", "Close the door!", "I am leaving.", "You come in."),
    ("A suitable reply to 'May I borrow your pen?' is ___.", "Sure, here you are.", "I am a pen.", "Close your book.", "No, I am reading yesterday."),
    ("'Please be quiet' asks students to ___.", "stop making noise", "speak louder", "run", "eat"),
    ("'Turn to page ten' asks students to ___.", "go to page ten", "close page ten", "write ten books", "leave at ten"),
    ("A suitable reply to 'Could you repeat that?' is ___.", "Of course.", "I am a chair.", "Open the window yesterday.", "No page."),
    ("'Hand in your homework' means ___.", "give the homework to the teacher", "take it home", "tear it up", "start a game")
]
for i, (prompt, answer, b, c, d) in enumerate(items, 1):
    qp = ROOT / "questions/english" / f"question-english-{key}-{i}.json"
    q = json.loads(qp.read_text(encoding="utf-8"))
    q.update({"prompt": prompt, "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26",
              "options": [{"id": "A", "text": answer}, {"id": "B", "text": b}, {"id": "C", "text": c}, {"id": "D", "text": d}],
              "answer": {"value": "A", "explanation": f"依教室用語的語意與情境，正確解讀為：{answer}。"}})
    qp.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
m = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))
for row in m["rows"]:
    if row.get("lessonId") == lid:
        row.update({"contentStatus": "content-reviewed", "reviewStatus": "content-reviewed"})
(ROOT / "data/m4-coverage-matrix.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(lid)
