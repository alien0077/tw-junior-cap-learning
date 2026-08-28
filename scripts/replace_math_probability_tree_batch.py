#!/usr/bin/env python3
"""Replace the generic probability-tree questions with recomputable items."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON_ID = "lesson-math-performance-d-iv-2"
KG_ID = "kg-math-performance-d-iv-2"
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E6%95%B8%E5%AD%B8.pdf"
CAP_SOURCE = "https://www.grow22.com/download/114/114_cp/03_114P_Math.pdf"

items = [
    ("公平硬幣連續投擲兩次，恰好出現一次正面的機率為何？", ["1/2", "1/4", "3/4", "1/3"], "四條等可能路徑 HH、HT、TH、TT 中，恰有一次正面的 HT、TH 共 2 條，所以機率為 2/4＝1/2。"),
    ("衣櫃有 3 件上衣，其中 1 件紅色；另有 2 件長褲。各選 1 件上衣和 1 件長褲，選到紅色上衣的機率為何？", ["1/3", "1/5", "1/2", "2/3"], "上衣的選擇在 3 件中等可能，紅色上衣有 1 件；長褲種類不影響此事件，因此機率為 1/3。"),
    ("袋中有 3 顆紅球、2 顆藍球，不放回連取 2 顆，兩顆皆為紅球的機率為何？", ["3/10", "1/5", "1/2", "2/5"], "第一顆紅球機率為 3/5；取出紅球後剩 2 紅、4 球，第二顆紅球機率為 2/4；乘積為 3/10。"),
    ("先擲公平骰子一次，再擲公平硬幣一次，骰子出現偶數且硬幣出現正面的機率為何？", ["1/4", "1/6", "1/3", "1/2"], "骰子為偶數的機率是 3/6＝1/2，硬幣正面是 1/2；兩階段獨立，路徑機率為 1/2×1/2＝1/4。"),
    ("下雨機率為 0.3；下雨時公車遲到機率為 0.6，不下雨時遲到機率為 0.2。公車遲到的機率為何？", ["0.32", "0.18", "0.20", "0.80"], "沿兩條遲到路徑相加：0.3×0.6＋0.7×0.2＝0.18＋0.14＝0.32。"),
    ("等機率選擇甲、乙兩盒中的一盒；甲盒有 3 顆綠球、1 顆黃球，乙盒有 1 顆綠球、3 顆黃球。抽到綠球的機率為何？", ["1/2", "3/4", "1/4", "2/3"], "選甲盒抽到綠球的路徑為 1/2×3/4，選乙盒為 1/2×1/4；相加為 3/8＋1/8＝1/2。"),
    ("從卡片 1、2、3、4 中不放回抽取 2 張，兩張卡片號碼和為奇數的機率為何？", ["2/3", "1/2", "1/3", "3/4"], "總共有 4×3＝12 個有序結果；要成為奇數須一奇一偶，有 2×2×2＝8 個結果，機率為 8/12＝2/3。"),
    ("某產品第一次檢驗合格機率為 0.4；第一次合格後第二次合格機率為 0.5。若第一次不合格，第二次合格機率為 0.2，兩次都合格的機率為何？", ["0.20", "0.50", "0.28", "0.40"], "兩次都合格只有「第一次合格、第二次合格」這條路徑，機率為 0.4×0.5＝0.20。"),
    ("從 4 位同學中等機率選 1 位，再從 3 本書中等機率選 1 本。選到指定同學且指定書的機率為何？", ["1/12", "1/7", "1/4", "1/3"], "選到指定同學的機率為 1/4，選到指定書的機率為 1/3；兩階段獨立，乘積為 1/12。"),
    ("公平骰子連續擲兩次，至少有一次擲出 6 的機率為何？", ["11/36", "1/6", "10/36", "25/36"], "先算補事件：兩次都不是 6 的機率為 5/6×5/6＝25/36；所以至少一次 6 為 1－25/36＝11/36。"),
]
target_indices = [3, 2, 1, 0, 3, 2, 1, 0, 3, 2]
for i, (prompt, options, explanation) in enumerate(items, start=1):
    target = target_indices[i - 1]
    shift = (4 - target) % 4
    rotated = options[shift:] + options[:shift]
    data = {
        "id": f"question-math-performance-d-iv-2-{i}",
        "subject": "math",
        "type": "single-choice",
        "prompt": prompt,
        "options": [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)],
        "knowledgeIds": [KG_ID],
        "difficulty": ("easy", "medium", "hard")[(i - 1) % 3],
        "answer": {"value": chr(65 + target), "explanation": explanation},
        "provenance": {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": "高雄市立鹽埕國民中學 114 學年度第二學期第一次段考數學科；參考樹狀圖、兩階段試驗、條件機率、不放回抽取與補事件題型；另參考 114 年國中教育會考數學科；本題使用全新數值、情境與選項，非原題重製。",
            "authoringNote": "機率單元實質改寫；已依路徑或樣本空間重新計算答案與解析，未重製公開試題文字、圖表或選項；待第二輪 AI 內容複核。",
        },
        "reviewStatus": "draft",
        "updatedAt": "2026-08-28",
        "lessonId": LESSON_ID,
    }
    (ROOT / f"questions/math/question-math-performance-d-iv-2-{i}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"replaced {len(items)} probability-tree questions")
