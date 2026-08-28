#!/usr/bin/env python3
"""Replace one Chinese punctuation lesson with independently adapted items."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = "lesson-chinese-punctuation-effects"
KID = "kg-chinese-content-ac-iv-1"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"

rows = [
    ("下列句子空格依序填入標點，何者最恰當：「請先看清楚□再回答□不要急著猜□」", ["， 。 ，", "：；、", "、，。", "；：，"], "A", "冒號引出提醒內容，句末用句號，第二個分句間用逗號。", "第1題改編"),
    ("「你真的要現在出發□」句末應使用哪個標點才能表現詢問語氣？", ["。", "！", "？", "、"], "C", "句子是在詢問對方是否出發，應用問號。", "第1題改編"),
    ("「太好了□我們終於完成了□」兩個空格依序應填入什麼？", ["！。", "，！", "？、", "；，"], "B", "第一句感嘆後接下一分句，用逗號；全句感嘆結束用驚嘆號。", "第1題改編"),
    ("下列哪一項最適合用冒號引出後面的說明？", ["他只說了一件事：明天要提早集合。", "他只說了一件事，明天要提早集合。", "他只說了一件事；明天要提早集合。", "他只說了一件事、明天要提早集合。"], "A", "冒號可用在總說語後，引出後面的具體說明。", "第1題改編"),
    ("「書包裡有三樣東西□課本、筆記本和水壺。」空格應填哪個符號？", ["，", "：", "；", "？"], "B", "前句總說有三樣東西，後面列出內容，應用冒號。", "第1題改編"),
    ("下列哪一句使用分號最恰當？", ["下雨了；請帶傘。", "我喜歡閱讀；妹妹喜歡畫畫。", "他買了；三本書。", "請記得；準時到校。"], "B", "兩個分句各自完整且並列，適合以分號分隔。", "第1題改編"),
    ("「等等□你剛才說什麼□」兩個空格依序應填入什麼？", ["，？", "、。", "：！", "；、"], "A", "等等是句中停頓，後句是疑問，依序用逗號與問號。", "第1題改編"),
    ("下列哪一項的頓號使用正確？", ["我們準備了鉛筆、橡皮擦、尺。", "我們準備了鉛筆，橡皮擦，尺。", "我們準備了鉛筆；橡皮擦；尺。", "我們準備了鉛筆：橡皮擦：尺。"], "A", "列舉同類詞語時可用頓號分隔。", "第1題改編"),
    ("「我不是不想幫忙□只是今天已有安排。」空格最適合填入哪個符號？", ["，", "？", "！", "、"], "A", "前後是同一句中的轉折分句，使用逗號最自然。", "第1題改編"),
    ("下列哪一句用驚嘆號最能表現強烈情緒？", ["你今天幾點回家？", "請把窗戶關好。", "小心，前面有落石！", "桌上放著一本書。"], "C", "提醒危險且帶有強烈情緒，句末用驚嘆號。", "第1題改編"),
]

for index, (prompt, options, answer, explanation, locator) in enumerate(rows, 1):
    path = ROOT / "questions" / "chinese" / f"question-chinese-punctuation-effects-{index}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data.update({
        "prompt": prompt,
        "options": [{"id": chr(65 + i), "text": text} for i, text in enumerate(options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "knowledgeIds": [KID],
        "lessonId": LESSON,
        "provenance": {
            "origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度第 2 學期三年級第 1 次段考國文科；{locator}；獨立改編，非原題重製。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
    })
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"replaced {len(rows)} Chinese questions")
