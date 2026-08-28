#!/usr/bin/env python3
"""Replace one linear-function lesson with independently adapted exam-style items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-math-linear-function-graph"
KID = "kg-math-content-f-8-2"
SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"
ANSWER = "https://www.grow22.com/download/114/114_cp/07_114P_Answer.pdf"

rows = [
    ("一次函數 y=2x-5 的圖形通過下列哪一點？", ["(0,5)", "(2,0)", "(3,1)", "(4,4)"], "C", "將各點代入 y=2x-5，(3,1) 使 1=6-5 成立。", "第6題坐標平面代入題型改編"),
    ("一次函數 y=-3x+7 的圖形與 y 軸交於哪一點？", ["(7,0)", "(0,7)", "(0,-3)", "(-3,0)"], "B", "與 y 軸交點的 x=0，代入得 y=7，因此交點為 (0,7)。", "第6題坐標與截距題型改編"),
    ("一條直線通過 (1,4) 與 (3,10)，其斜率為何？", ["2", "3", "4", "6"], "B", "斜率=(10-4)/(3-1)=6/2=3。", "第6題兩點與圖形題型改編"),
    ("一次函數 y=4x-9 的圖形與 x 軸交於何處？", ["(0,-9)", "(9,0)", "(9/4,0)", "(-9/4,0)"], "C", "與 x 軸交點的 y=0，4x-9=0，所以 x=9/4。", "第6題坐標軸截距題型改編"),
    ("函數 y=ax+2 的圖形通過 (3,-4)，則 a 為何？", ["-2", "-1", "2", "-6"], "A", "代入得 -4=3a+2，故 3a=-6，a=-2。", "第6題代入求參數題型改編"),
    ("一次函數圖形通過原點與 (2,6)，其函數式為何？", ["y=2x", "y=3x", "y=6x", "y=x+4"], "B", "斜率=(6-0)/(2-0)=3，且通過原點所以截距為 0，函數式為 y=3x。", "第6題兩點求函數式題型改編"),
    ("一次函數 y=-x+5 的 x 軸截距為何？", ["-5", "0", "1", "5"], "D", "與 x 軸交點 y=0，故 -x+5=0，x=5。", "第6題坐標軸截距題型改編"),
    ("當一次函數的 x 增加 2、y 減少 8 時，其斜率為何？", ["-4", "-2", "2", "4"], "A", "斜率=Δy/Δx=-8/2=-4。", "第6題變化量與斜率題型改編"),
    ("直線 y=3x+b 通過 (-1,7)，則 b 為何？", ["4", "7", "10", "-10"], "C", "代入 7=3(-1)+b，得 b=10。", "第6題代入求截距題型改編"),
    ("一次函數 y=2x+b 的圖形通過 (4,1)，則其 y 軸截距 b 為何？", ["-8", "-7", "7", "9"], "B", "代入 1=2(4)+b，得 b=1-8=-7。", "第6題代入求參數題型改編"),
]

answer_positions = ["B", "C", "D", "B", "C", "D", "B", "C", "D", "A"]
for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "math" / f"question-math-linear-function-graph-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    target = ord(answer_positions[index - 1]) - ord("A")
    options = options[1:target + 1] + options[:1] + options[target + 1:]
    answer = answer_positions[index - 1]
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE, "sourceLocator": f"114年國中教育會考數學科；{locator}；官方答案表：{ANSWER}；另參考高雄市立鹽埕國中公開數學段考之坐標與函數能力方向；獨立改編，非原題重製。"},
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} CAP-style linear-function questions")
