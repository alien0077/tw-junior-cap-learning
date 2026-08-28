"""替換國文 6-Ⅳ-3 仿寫改寫模板題為實際語句判讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-3.json").read_text())["source"]["url"]
ITEMS = [
    ("句子『閱讀讓人看見更大的世界』的結構是『動作＋使人＋結果』。下列哪句最適合仿寫？", ["旅行讓人認識不同的生活方式", "旅行很有趣，大家都喜歡", "因為下雨，所以帶傘", "請把書放回原位"], "A", "第一句以動作為主語，透過『讓人』連接所產生的結果；選項 A 保留相同結構。", "medium", "仿寫結構"),
    ("將『校園裡有許多樹，夏天可以遮蔭』改寫成較精確的說明句，何者最恰當？", ["校園樹木可在夏季提供遮蔭，改善部分區域的日照感受", "校園樹木一定能讓所有地方全年涼爽", "樹木很漂亮，所以所有問題都能解決", "夏天、校園、樹木、遮蔭"], "A", "改寫保留原意並避免把局部作用誇大為全年、所有地點都有效。", "medium", "說明改寫"),
    ("『春風吹過田野，花朵輕輕點頭』若要保留擬人效果，哪句仿寫最適合？", ["夕陽收起餘暉，山村慢慢入睡", "夕陽的溫度是攝氏二十度", "研究人員測量夕陽高度", "山村位於河流北方"], "A", "『花朵點頭』把人的動作賦予花朵；選項 A 也把『收起、入睡』等人的動作寫給自然景物。", "easy", "擬人仿寫"),
    ("仿寫『只要願意練習，就能逐漸進步』時，哪句保留相同的條件關係？", ["只要先核對資料，就能減少誤判", "雖然下雨，但是活動照常", "因為停電，所以課程延期", "不但完成作業，而且整理書桌"], "A", "原句是『只要……就……』的充分條件關係，選項 A 保留相同句型與邏輯。", "easy", "關聯句型"),
    ("把記敘文改寫成第一人稱時，若要維持原故事情節，最先應確認什麼？", ["事件先後、人物關係與關鍵行動是否仍一致", "每個角色都改成自己的同學", "把結局先刪除再猜測", "只替換所有名詞，不理會事件"], "A", "改變敘述角度不等於改變事件；先核對情節與人物關係，才能避免改寫失真。", "medium", "敘事改寫"),
    ("下列哪種改寫方式最不恰當？", ["只替換少數詞語，卻保留原文整段句序與特殊表達", "保留核心意思，重新安排句子與例子", "依讀者年齡調整詞語難度", "改寫後核對是否仍回答原題"], "A", "只換少數詞語而保留原文結構與特殊表達，既可能失去改寫意義，也有近似重製的風險。", "hard", "改寫界線"),
    ("仿寫公共服務標語時，哪個步驟最能兼顧原句功能與自己的表達？", ["先辨認原句的對象、目的與句型，再用新的情境重新寫出", "逐字替換兩個名詞就直接發布", "只模仿字數，不管訊息是否清楚", "完全照抄原標語並刪去來源"], "A", "安全仿寫要理解原句的溝通功能，再重新設計語境與文字，而非逐字替換。", "hard", "標語仿寫"),
    ("將口語句『這部電影真的很好看』改寫為較正式的書面語，何者最恰當？", ["這部電影情節完整，值得觀賞", "這部電影超讚到不行", "這部電影真的好看欸", "這部電影看了就知道，讚啦"], "A", "選項 A 改用較精確、正式的詞語表達評價，符合書面語情境。", "easy", "語體改寫"),
    ("完成仿寫後，哪種檢查最能確認沒有只模仿表面形式？", ["比較核心意思、句型功能與新情境是否一致，再檢查語句通順", "只比較每句字數是否完全相同", "只看是否使用相同標點", "只問自己喜不喜歡字體"], "A", "好的仿寫同時檢查功能、意思、情境與語句，不是只追求表面字數或標點相同。", "hard", "仿寫檢核"),
    ("原句『資料越完整，判斷越可靠』要改寫成校園閱讀情境，哪句最能保留比較程度關係？", ["證據越充分，報告的結論越有根據", "證據很充分，大家都去操場", "因為證據充分，所以報告昨天完成", "證據和報告都放在桌上"], "A", "原句以『越……越……』表達程度同步變化，選項 A 保留此關係並換成報告情境。", "medium", "句型改寫"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究仿寫、改寫、語體與句型判讀題型（{locator}）；課綱 6-Ⅳ-3：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
