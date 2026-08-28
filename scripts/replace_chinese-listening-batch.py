"""替換國文 1-Ⅳ-1 聆聽記錄歸納模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-1-iv-1.json").read_text())["source"]["url"]
ITEMS = [
    ("同學說『最近報告很多，我擔心來不及完成』。哪個回應最符合同理聆聽？", ["你似乎因為期限接近而感到焦慮，我們可以一起整理進度", "這有什麼好擔心的，大家都一樣", "你不要再說了，直接把報告給我", "我也有自己的事，所以不必聽你說"], "A", "先理解並重述對方的情緒，再提出協助方向，較能表現同理聆聽。", "easy", "同理回應"),
    ("聽完校園講座後整理筆記，哪種方式最能掌握重點？", ["分出主題、主要觀點、關鍵證據與行動建議", "逐字記下每個語助詞，不分辨重點", "只記講者姓名，不記內容", "只寫自己想談的另一個主題"], "A", "把訊息依主題、觀點、證據與建議整理，能比逐字抄錄更有效掌握結構。", "medium", "筆記重點"),
    ("聽者不確定對方說『下週再討論』是指哪一天時，最適當的做法是什麼？", ["請對方具體確認日期與時間", "自行猜一個日期並當成共識", "完全不記錄，等對方再次提醒", "直接把討論取消"], "A", "遇到關鍵資訊不明確時應澄清確認，不能以猜測代替對方的意思。", "easy", "澄清提問"),
    ("小組討論中，同學提出不同方案。哪種聆聽行為最能促進共同理解？", ["先整理對方的理由，再指出自己同意或疑問的部分", "對方一開口就打斷並否定", "只等待輪到自己發言，不聽內容", "把不同意見改寫成自己的主張"], "A", "重述理由並清楚回應，可確認是否正確理解，也能讓討論建立在共同資訊上。", "medium", "討論聆聽"),
    ("聆聽新聞報導時，哪項筆記最可能是核心訊息？", ["事件發生地點、主要變化、涉及對象與報導來源", "主播的衣服顏色", "自己對其他新聞的回憶", "每個停頓的秒數"], "A", "核心筆記應保留事件的關鍵事實、對象、變化與來源，排除與內容無關的細節。", "medium", "新聞聆聽"),
    ("聽取『先關閉電源，再拔除插頭，最後檢查指示燈』的操作說明，哪種記錄最有助於事後執行？", ["依先後順序列出三個步驟，並標出不可省略的安全提醒", "只記下『使用設備』四個字", "把三個步驟任意重新排列", "只記錄說明者的姓名"], "A", "操作說明的重點是步驟順序與安全條件，記錄時應保留兩者。", "easy", "操作聆聽"),
    ("對方提出與自己不同的意見時，哪種態度最合宜？", ["先聽完並確認其理由，再提出有根據的回應", "因為不同意就說對方一定錯", "只挑一句話攻擊，不理會整體理由", "假裝同意，事後散播未經確認的內容"], "A", "尊重不同意見不等於接受所有主張，而是先理解理由，再以證據回應。", "medium", "不同意見"),
    ("歸納訪談內容時，哪個做法最能避免曲解受訪者？", ["區分原話與自己的摘要，回看上下文並請受訪者確認", "只挑最符合自己想法的一句", "把疑問改寫成肯定答案", "刪除所有與主題不一致的回答"], "A", "區分引用與摘要、檢查上下文並回訪確認，能降低斷章取義的風險。", "hard", "訪談歸納"),
    ("聽完校方說明後要轉述給同學，哪項內容應優先保留？", ["決策內容、適用對象、時間地點與需要採取的行動", "說明者喝水的次數", "自己尚未查證的猜測", "與公告無關的個人評論"], "A", "轉述應保留能讓同學正確理解並行動的核心資訊，避免混入猜測。", "medium", "轉述"),
    ("完成聆聽筆記後，哪種檢查最能提升準確度？", ["對照錄音或原說明，確認數字、否定詞、先後順序與說話者立場", "只看筆記是否寫滿整頁", "只修改字體顏色，不回查內容", "把不確定的地方直接補成自己猜的答案"], "A", "數字、否定詞、順序與立場容易影響意思，應回查原始聆聽材料而非猜測補寫。", "hard", "聆聽檢核"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-1-iv-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究聆聽、記錄、歸納與口語理解題型（{locator}）；課綱 1-Ⅳ-1：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
