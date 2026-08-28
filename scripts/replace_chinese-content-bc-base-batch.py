"""替換國文 Bc 基礎說明文題，避免舊題標籤與泛用題混用。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHOOL = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CAP = "https://www.grow22.com/download/114/114_cp/01_114P_Chinese.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%A8%8B%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"
ITEMS = [
    ("校刊介紹校園老樹，先說明樹齡與位置，再列出樹醫檢查結果。若要判斷文章是否有充分根據，最應查看什麼？", ["資料來源、觀察方法與數值是否交代清楚", "標題是否使用最大的字", "文章是否每句都押韻", "作者是否只使用第一人稱"], "A", "說明性文章的可信度要看資料來源、方法與數值，而非版面或押韻。", "hard", "證據與方法", SCHOOL),
    ("一篇文章說明校園午餐，先介紹『剩食率』的意思，再以三週紀錄說明變化。這樣安排的主要作用是什麼？", ["先建立概念，再用資料呈現變化", "把紀錄變成虛構故事", "避免讀者知道文章主題", "只增加文章的情緒色彩"], "A", "先定義術語可避免誤解，再用連續紀錄支持對變化的說明。", "medium", "定義與資料", SCHOOL),
    ("某報告寫『本校 80 位受訪者中有 48 位支持增設遮雨棚』。下列哪個結論沒有超出資料？", ["受訪者中有 60% 表示支持", "全市學生都支持增設遮雨棚", "所有家長都反對現有設計", "增設後一定不會再淋雨"], "A", "48÷80=60%，這只描述受訪樣本，不能推論全市或預測必然結果。", "medium", "樣本與比例", SCHOOL),
    ("說明文指出『午後西曬使教室較熱』，但沒有提供不同時段或教室位置的測量。讀者最合理的判斷是什麼？", ["這是待補充測量的可能解釋，尚不足以下定論", "只要句子通順就已證明因果", "沒有測量就能確定所有教室都相同", "應把可能原因改成必然結果"], "A", "缺少比較條件與測量資料時，只能視為可能解釋，不能直接斷定因果。", "hard", "因果限制", SCHOOL),
    ("文章比較紙本與電子閱讀，若想讓比較公平，哪種寫法最適當？", ["用相同面向比較，例如攜帶、查找與保存，再分別說明差異", "只列紙本優點，電子閱讀只寫缺點", "只比較兩者的名稱長短", "先判定一方較好，再刪除相反資料"], "A", "以相同面向呈現雙方資料，才能降低偏重並看出真正差異。", "medium", "比較說明", CAP),
    ("表格顯示某社區三個月份回收量為 120、150、135 公斤。若要描述趨勢，何者最精確？", ["先增加後減少，第三月仍比第一月多 15 公斤", "三個月持續增加", "三個月完全沒有變化", "第三月比第一月少 15 公斤"], "A", "120→150 增加，150→135 減少；135−120=15，因此第三月仍高於第一月。", "hard", "趨勢與差值", CAP),
    ("文章以『例如』引入『圖書館每週五舉辦交換書活動』。這個例子最主要的功能是什麼？", ["把較抽象的推廣做法具體呈現", "表示只有星期五能閱讀", "證明所有學校都採用同一活動", "取代全文的主旨"], "A", "具體例子能讓讀者理解抽象的推廣做法，但不能擴大成所有學校的情況。", "easy", "舉例說明", CAP),
    ("文章最後提出『因此，學校可先試辦一個月，再依紀錄調整』。若要判斷這個建議是否合理，應檢查什麼？", ["前文的問題、證據是否能支持試辦與評估的步驟", "建議句是否比正文長", "作者是否使用很多感嘆號", "試辦方案是否完全不需紀錄"], "A", "建議要與問題和證據相連，且試辦與紀錄提供了可檢驗、可調整的步驟。", "hard", "主張與方案", CAP),
    ("某圖表的縱軸以 50 為起點，兩組數值 52 與 56 的柱高差異看來很大。閱讀時最應如何處理？", ["回到實際數值與刻度，避免只依視覺高度判斷", "把 50 當成零計算差距", "認定柱高差距就是數值差距的十倍", "忽略縱軸並猜測趨勢"], "A", "縱軸不從零開始可能放大視覺差異，應以刻度和實際數值判讀。", "hard", "圖表刻度", CAP),
    ("說明文的結尾寫『上述資料只記錄一個班級，後續仍需擴大調查』。這句話主要展現什麼？", ["承認資料範圍限制，避免把局部結果當成普遍結論", "否定前文所有觀察", "表示資料完全沒有價值", "把說明文改成故事結局"], "A", "交代樣本限制能讓結論範圍更精確，也不等於否定已取得的資料。", "medium", "結論範圍", CAP),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator, source) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-content-bc-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": source,
            "sourceLocator": f"公開國中教育會考／公立國中段考的說明文與資料判讀能力方向（{locator}）；另以國語文課綱核對：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; removed old year labels and did not reproduce source wording, options, passage, figure, or answer. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
