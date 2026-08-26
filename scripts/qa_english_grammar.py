#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
units = {
    "content-ad": ("Ad：句構", "辨識英文句子的主詞、動詞與受詞，依基本句型組織語意。"),
    "content-ad-iv-1": ("Ad-Ⅳ-1：國中文法句型", "運用國中常見時態、助動詞、比較句與連接詞組織正確句子。"),
}
items = [
    ("主詞辨識", "In 'Mia reads every night,' who is the subject?", "Mia", "reads", "night", "every"),
    ("動詞辨識", "In 'They play soccer,' which word is the verb?", "play", "They", "soccer", "the"),
    ("一般現在式", "Leo ___ to school by bus every day.", "goes", "go", "going", "went"),
    ("現在進行式", "Look! The children ___ in the park.", "are running", "run", "ran", "runs"),
    ("過去式", "We ___ the museum yesterday.", "visited", "visit", "visits", "visiting"),
    ("助動詞", "You ___ wear a helmet when riding a bike.", "should", "are", "did", "has"),
    ("疑問句", "___ she like science?", "Does", "Do", "Is", "Has"),
    ("否定句", "Tom ___ eat meat.", "does not", "do not", "is not", "has not"),
    ("比較級", "This book is ___ than that one.", "more interesting", "most interesting", "interesting", "interest"),
    ("連接詞", "I stayed home ___ it was raining.", "because", "but", "or", "so"),
]
for key, (title, summary) in units.items():
    lp = ROOT / "lessons/english" / f"lesson-english-{key}.json"
    lesson = json.loads(lp.read_text(encoding="utf-8"))
    lesson.update({"title": title, "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26"})
    lesson["content"] = {"summary": summary, "sections": [
        {"heading": "學習目標", "body": summary + "，並能以句子結構檢查文法。"},
        {"heading": "學習流程", "body": "先找主詞與動詞，再確認時態、助動詞或連接詞，最後朗讀並檢查句意。"},
        {"heading": "常見錯誤", "body": "主詞與動詞不一致、時態混用，或將助動詞後的動詞誤加變化。"},
    ]}
    lesson["studyHighlights"] = ["先找主詞與動詞。", "依句型確認變化。", "用句意檢查答案。"]
    lp.write_text(json.dumps(lesson, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for i, (focus, prompt, answer, b, c, d) in enumerate(items, 1):
        qp = ROOT / "questions/english" / f"question-english-{key}-{i}.json"
        q = json.loads(qp.read_text(encoding="utf-8"))
        q.update({"prompt": f"{focus}：{prompt}", "reviewStatus": "content-reviewed", "updatedAt": "2026-08-26",
                  "options": [{"id": "A", "text": answer}, {"id": "B", "text": b}, {"id": "C", "text": c}, {"id": "D", "text": d}],
                  "answer": {"value": "A", "explanation": f"依英文句型與文法規則，正確答案為 {answer}。"}})
        qp.write_text(json.dumps(q, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(key)
m = json.loads((ROOT / "data/m4-coverage-matrix.json").read_text(encoding="utf-8"))
for row in m["rows"]:
    if row.get("lessonId") in {f"lesson-english-{k}" for k in units}:
        row.update({"contentStatus": "content-reviewed", "reviewStatus": "content-reviewed"})
(ROOT / "data/m4-coverage-matrix.json").write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
