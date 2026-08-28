#!/usr/bin/env python3
"""Replace two math lessons with independently adapted public-school exam items.

The source PDF and answer key were read separately.  The payload below changes
the numbers/context and records the source question locator; it does not copy
the source wording.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
SOURCE_NOTE = "高雄市立鹽埕國中 114 學年度第 2 學期第 1 次段考三年級數學科試題；題目頁／答案頁逐題核對後獨立改編，非原題重製。"

def q(prompt, options, answer, explanation, locator, lesson_id, kid):
    return {
        "prompt": prompt,
        "options": [{"id": k, "text": v} for k, v in zip("ABCD", options)],
        "answer": {"value": answer, "explanation": explanation},
        "difficulty": "medium",
        "provenance": {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
                        "sourceLocator": f"{SOURCE_NOTE} 來源題號：{locator}"},
        "reviewStatus": "draft", "updatedAt": "2026-08-28", "lessonId": lesson_id,
        "knowledgeIds": [kid],
    }

F = "lesson-math-content-f-9-2"
D = "lesson-math-content-d-9-3"
items = {
    F: [
        ("二次函數 y=2(x-3)^2-5 的頂點座標為何？", ["(3,-5)", "(-3,-5)", "(3,5)", "(-3,5)"], "A", "頂點式 y=a(x-h)^2+k 的頂點是 (h,k)，所以為 (3,-5)。", "第 3 題改編", "kg-math-content-f-9-2"),
        ("函數 y=-(x+2)^2+7 的圖形具有哪一項性質？", ["開口向上且有最小值", "開口向下且有最大值", "對稱軸為 x=2", "頂點為 (2,7)"], "B", "二次項係數為負，圖形開口向下；頂點為 (-2,7)，因此有最大值 7。", "第 3 題改編", "kg-math-content-f-9-2"),
        ("將 y=3(x-1)^2+4 的圖形向左平移 2 單位，新的頂點為何？", ["(-1,4)", "(1,2)", "(3,4)", "(1,6)"], "A", "向左 2 單位使頂點的 x 座標 1 變為 -1，y 座標不變。", "第 6 題改編", "kg-math-content-f-9-2"),
        ("二次函數 y=-2(x-4)^2+9 與 x 軸相交於幾個點？", ["0", "1", "2", "3"], "C", "令 y=0 得 (x-4)^2=9/2，有兩個相異實根，因此與 x 軸相交於 2 點。", "第 5 題改編", "kg-math-content-f-9-2"),
        ("若 y=a(x+1)^2-6 的圖形通過 (-1,-6) 與 (1,2)，a 為何？", ["1", "2", "4", "8"], "B", "代入 (1,2)：2=a(2)^2-6，得 4a=8，所以 a=2。", "第 9 題改編", "kg-math-content-f-9-2"),
        ("y=(x-2)^2-3 的圖形最低點為何？", ["(2,-3)", "(-2,-3)", "(2,3)", "(-2,3)"], "A", "平方項係數為正，最低點就是頂點 (2,-3)。", "第 3 題改編", "kg-math-content-f-9-2"),
        ("若二次函數 y=-(x-5)^2+1 的圖形向上平移 4 單位，頂點變為何？", ["(5,-3)", "(5,5)", "(1,5)", "(9,5)"], "B", "向上平移只改變 y 座標，頂點 (5,1) 變為 (5,5)。", "第 6 題改編", "kg-math-content-f-9-2"),
        ("二次函數 y=4x^2-8x+1 的對稱軸方程式為何？", ["x=-1", "x=1", "x=2", "x=4"], "B", "對稱軸 x=-b/(2a)=8/8=1。", "第 4 題改編", "kg-math-content-f-9-2"),
        ("若拋物線 y=a(x-2)^2+3 開口向上，a 必須符合哪項條件？", ["a<0", "a=0", "a>0", "a=3"], "C", "二次函數以頂點式表示時，a>0 代表開口向上。", "第 1 題改編", "kg-math-content-f-9-2"),
        ("函數 y=-(x+3)^2+2 的最大值為何？", ["-3", "2", "3", "-2"], "B", "開口向下，頂點為 (-3,2)，所以最大值是 2。", "第 3 題改編", "kg-math-content-f-9-2"),
    ],
    D: [
        ("公平骰子擲一次，出現大於 4 點的機率為何？", ["1/6", "1/3", "1/2", "2/3"], "B", "可能結果為 1 至 6，其中 5、6 共 2 個，機率為 2/6=1/3。", "第 14 題改編", "kg-math-content-d-9-3"),
        ("同時擲一枚公平硬幣與一顆公平骰子，出現反面且骰子為偶數的機率為何？", ["1/12", "1/6", "1/4", "1/2"], "C", "反面機率 1/2，偶數機率 3/6=1/2，獨立事件相乘得 1/4。", "第 18 題改編", "kg-math-content-d-9-3"),
        ("從 1 至 8 的八張卡片中任取一張，抽到 3 的倍數之機率為何？", ["1/8", "1/4", "3/8", "1/2"], "B", "3 的倍數為 3、6，共 2 張，機率 2/8=1/4。", "第 19 題改編", "kg-math-content-d-9-3"),
        ("袋中有 4 顆紅球與 6 顆藍球，任取 1 顆，取到紅球的機率為何？", ["2/5", "3/5", "1/2", "2/3"], "A", "總數 10 顆，紅球 4 顆，機率為 4/10=2/5。", "第 14 題改編", "kg-math-content-d-9-3"),
        ("從 1 至 5 任選一個整數，選到奇數的機率為何？", ["1/5", "2/5", "3/5", "4/5"], "C", "奇數 1、3、5 共 3 個，總共 5 個等可能結果，機率 3/5。", "第 14 題改編", "kg-math-content-d-9-3"),
        ("同時擲兩顆公平骰子，點數和為 7 的機率為何？", ["1/36", "1/12", "1/6", "1/3"], "C", "符合的有 (1,6) 至 (6,1) 共 6 種，總結果 36 種，機率 6/36=1/6。", "第 15 題改編", "kg-math-content-d-9-3"),
        ("從 1 至 10 中任取一數，取到質數的機率為何？", ["1/5", "2/5", "1/2", "3/5"], "B", "質數為 2、3、5、7，共 4 個，機率 4/10=2/5。", "第 19 題改編", "kg-math-content-d-9-3"),
        ("轉盤等分為 8 格，其中 3 格為綠色。轉一次停在綠色的機率為何？", ["3/8", "1/3", "5/8", "3/5"], "A", "8 格等可能，綠色 3 格，所以機率為 3/8。", "第 14 題改編", "kg-math-content-d-9-3"),
        ("從 1 至 6 任選一數，選到平方數的機率為何？", ["1/6", "1/3", "1/2", "2/3"], "B", "平方數為 1、4，共 2 個，機率為 2/6=1/3。", "第 19 題改編", "kg-math-content-d-9-3"),
        ("甲、乙各有 2 種飲料可選，任選一種組合，共有幾種等可能結果？", ["2", "3", "4", "6"], "C", "甲有 2 種、乙有 2 種，乘法原理得到 2×2=4 種。", "第 15 題改編", "kg-math-content-d-9-3"),
    ],
}

for lesson_id, rows in items.items():
    for index, (prompt, options, answer, explanation, locator, kid) in enumerate(rows, 1):
        path = next((p for p in (ROOT / "questions").glob("*/*.json") if json.loads(p.read_text()).get("id") == f"question-math-content-{lesson_id.removeprefix('lesson-math-content-')}-{index}"), None)
        if path is None:
            raise SystemExit(f"missing question file for {lesson_id} #{index}")
        data = json.loads(path.read_text())
        data.update(q(prompt, options, answer, explanation, locator, lesson_id, kid))
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print("replaced", sum(len(v) for v in items.values()), "questions")
