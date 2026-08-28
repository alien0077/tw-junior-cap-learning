"""替換國文 1-Ⅳ-3 聆聽邏輯模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-1-iv-3.json").read_text())["source"]["url"]
ITEMS = [
    ("聽到『教室午後很熱，因此我們調整窗簾與座位』，兩部分的關係是什麼？", ["前者說明原因或情況，後者提出因應做法", "前後兩句完全沒有關聯", "後者是前者的時間地點", "前者是後者的反面例子"], "A", "教室很熱是情況，調整窗簾與座位是因應做法；『因此』連接前因與後果或對策。", "easy", "因果與對策"),
    ("演講者說『因此』時，聽者要判斷後句是否合理，最應回想前句的哪項資訊？", ["前句提出的原因、證據或條件", "講者衣服的顏色", "背景音樂的節拍", "聽眾座位的排列"], "A", "『因此』表示推論或結果，必須回看前面的原因、證據或條件才能檢查連接是否合理。", "medium", "連接詞"),
    ("聽取兩種交通方案的優缺點時，哪種筆記最能支持後續選擇？", ["用相同面向分別記錄成本、時間、便利性與限制", "只記下自己先喜歡的方案", "只抄錄講者的開場問候", "把兩方案的資料混在同一欄"], "A", "用相同標準記錄雙方優缺點，才能進行有根據的比較與選擇。", "medium", "比較筆記"),
    ("聽到『雖然成本較高，但是使用壽命較長』，應辨識出哪種關係？", ["轉折：成本高的限制與壽命長的優點並存", "因果：成本高必然造成壽命長", "選擇：只能選成本或壽命其中一項", "承接：兩句只是重複同一意思"], "A", "『雖然……但是……』引出限制與相反方向的優點，屬於轉折，不等於必然因果。", "easy", "轉折"),
    ("講者先指出校園垃圾量增加，再引用一週稱重紀錄。這份紀錄在論述中主要扮演什麼角色？", ["提供支持現象的具體證據", "取代所有問題與結論", "表示講者的個人姓名", "證明其他學校也有完全相同數據"], "A", "一週紀錄可支持校園垃圾量的觀察，但不能自動推論其他學校也有相同數據。", "medium", "證據功能"),
    ("聽取解題示範時，哪項訊息最值得記錄？", ["題目條件、關鍵步驟與檢查答案的方法", "講者每次咳嗽的次數", "投影片背景的裝飾圖案", "與解題無關的聊天內容"], "A", "解題示範的可用資訊是條件、推理步驟與驗算方法，這些能支持之後獨立解題。", "easy", "解題聆聽"),
    ("聽到『雨水增加使河流水位上升』後，哪個問題最能檢查是否理解因果？", ["哪個現象是原因？若雨水減少，預期水位如何變化？", "講者使用了哪種麥克風？", "河流的名字有幾個字？", "這句話共有幾個標點？"], "A", "能指出原因與預期結果，才表示掌握因果關係，而不是只記住句子表面文字。", "medium", "因果理解"),
    ("聆聽辯論時，如何判斷一項理由是否有效？", ["檢查理由是否與主張相關，且有足夠、可信的證據支持", "只看發言者音量是否最大", "因為說得很快就視為有道理", "只計算發言次數"], "A", "理由的有效性取決於與主張的關聯及證據品質，不由音量、速度或次數決定。", "hard", "理由評估"),
    ("聽完『先調查漏水位置，再比較修繕方法，最後估算費用』，若要找出可行方法，第一步應做什麼？", ["先確認問題位置與成因，避免在資訊不足時選方案", "直接選費用最高的方案", "先宣布問題已經解決", "忽略調查結果只比較名稱"], "A", "先掌握問題與成因，才能依證據比較不同方法，避免未查證就決定。", "medium", "問題解決"),
    ("聽完一段包含主張、理由、例子與限制的說明後，要歸納其邏輯，哪種做法最完整？", ["分別標出主張、支持理由、具體例子與適用限制，再檢查彼此關係", "只抄最後一句當成全部內容", "只記住例子的細節而刪除主張", "把限制改寫成無條件的結論"], "A", "完整歸納要分辨不同功能的資訊，並保留限制，才能正確重建說明的邏輯。", "hard", "邏輯歸納"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-1-iv-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究聆聽邏輯、證據與問題解決判讀題型（{locator}）；課綱 1-Ⅳ-3：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
