"""替換國文 Bc-Ⅳ-1 邏輯客觀理性說明模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

ITEMS = [
    ("校刊要說明一週午餐剩食量，哪種寫法最客觀？", ["記錄每日重量並註明統計期間", "大家都覺得剩食非常嚴重", "午餐一定是全校最浪費的地方", "我相信這個問題無法改善"], "A", "提供可查核的數據與期間，比使用無法驗證的感受或絕對判斷更客觀。", "easy", "客觀資料與範圍"),
    ("調查 100 位學生，62 位支持增設遮雨棚。下列何者是較嚴謹的敘述？", ["在本次受訪者中，62% 表示支持", "全校學生都支持增設遮雨棚", "增設遮雨棚一定能解決所有問題", "反對者沒有任何合理理由"], "A", "62% 只代表本次 100 位受訪者，不能擴大推論為全校或保證解決所有問題。", "medium", "統計資料的合理推論"),
    ("文章寫「午後氣溫升高，操場使用人數在三天內下降」。若要說明兩者關係，最應補充什麼？", ["更多日期與測量資料，避免只由三天判定因果", "作者的個人喜好", "與操場無關的故事", "把下降改寫成永遠不會使用"], "A", "三天觀察只能顯示可能關聯，還需要更多資料才能支持因果解釋。", "hard", "因果證據與限制"),
    ("說明校園噪音時，哪一句最符合客觀、理性的語氣？", ["測量顯示午休時教室外平均音量為 68 分貝", "午休時吵得讓人快要崩潰", "那些同學根本沒有公德心", "這是全校最糟糕的現象"], "A", "句子提供測量時間、對象與數值，不加入未經證明的情緒或人格評斷。", "easy", "客觀措辭"),
    ("某文比較兩種讀書方法，只列出方法甲的優點，沒有說明方法乙的資料。這樣的說明主要缺少什麼？", ["對兩種方法採用一致且完整的比較資料", "更多誇張形容詞", "作者的情緒宣告", "與主題無關的背景故事"], "A", "只呈現一方資料無法形成公平比較，應以一致標準補足另一方資訊。", "medium", "比較資料完整性"),
    ("若要解釋『雨後路面積水』，哪個推理最完整？", ["先指出排水孔堵塞，再以現場觀察說明水流受阻", "只說這是運氣不好", "只說所有道路都一定積水", "只引用居民的情緒反應"], "A", "把可能原因與可觀察證據連結，推理比單純感想或絕對化敘述完整。", "medium", "原因與證據"),
    ("下列哪項最適合作為『圖書館延長開放後借閱增加』的支持證據？", ["比較延長前後相同期間的借閱紀錄", "館員覺得新規定很棒", "一位同學說他以後可能會借書", "把借閱增加改寫成全國第一"], "A", "相同期間的前後紀錄可直接檢驗變化，其他選項不是資料或超出證據範圍。", "medium", "可查證證據"),
    ("報告指出『受訪的 30 人中有 18 人選擇步行』，下列哪個結論不超出資料？", ["這 30 位受訪者中，60% 選擇步行", "全市居民都偏好步行", "步行必定比所有交通方式安全", "所有學生明年都會改走路"], "A", "18÷30=60%，且結論明確限定在 30 位受訪者內。", "easy", "資料範圍與結論"),
    ("閱讀一份主張『植物放音樂會長得更快』的文章時，哪種做法最理性？", ["檢查實驗組、對照組、測量期間與數據", "只因標題有趣就接受結論", "只看作者是否有名", "把一次觀察當成適用所有植物"], "A", "檢查研究設計與資料，才能判斷主張是否有足夠證據。", "hard", "理性判讀研究主張"),
    ("撰寫校園節電說明的結尾時，哪一句最適當？", ["依據本月與上月電表紀錄，教室用電下降 8%，仍需持續觀察", "節電措施已百分之百成功且永遠有效", "不必看數據，大家都知道結果", "反對節電的人都不在乎環境"], "A", "引用數據並保留持續觀察的限制，符合客觀與理性說明。", "medium", "結論的證據與限制"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-content-bc-iv-1-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        options = options[shift:] + options[:shift]
        answer = chr(65 + ((4 - shift) % 4))
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": text} for j, text in enumerate(options)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": answer, "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究邏輯、客觀、理性說明能力方向（{locator}）；另以官方語文領域課綱核對 Bc-Ⅳ-1（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
