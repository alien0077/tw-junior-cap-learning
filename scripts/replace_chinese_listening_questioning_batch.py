"""替換國文 2-Ⅳ-2 聽聞、提問與回饋模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

ITEMS = [
    ("同學說：「我覺得校園應增加遮蔭，但還沒調查哪裡最需要。」哪個追問最能幫助釐清方案？", ["你打算調查哪些地點，以及用什麼標準判斷需要程度？", "你是不是完全不喜歡陽光？", "大家一定都會同意你的想法吧？", "這和昨天的比賽有什麼關係？"], "A", "問題聚焦調查範圍與判準，能把模糊主張轉成可討論的方案。", "medium", "澄清主張與條件"),
    ("組員報告：「回收率上升了。」若你想知道證據，最適合如何提問？", ["請問比較的是哪段期間，回收率上升了多少？", "你為什麼總是說得不清楚？", "是不是所有人都做得很好？", "這個題目是不是很無聊？"], "A", "詢問期間與變化量能讓抽象的『上升』具體化並可核對。", "easy", "追問數據"),
    ("朋友說明旅行計畫後，你不確定集合時間。哪個回應最恰當？", ["我確認一下，我們是星期六上午八點在車站集合嗎？", "你講得太差了，重說一遍。", "反正到時候再看著辦。", "我直接猜一個時間就好。"], "A", "重述已理解的內容並提出確認問題，可避免因誤聽造成錯誤。", "easy", "重述與確認"),
    ("聽完同學的讀書方法分享，若想提供有用回饋，哪一項最具體？", ["你把每週目標寫清楚了；若再記錄實際完成量，會更容易檢查成效", "你的方法一定是全班最好的。", "我不喜歡讀書，所以沒有意見。", "大家照做就不會有問題。"], "A", "回饋同時指出具體優點與可改進處，且與分享內容直接相關。", "medium", "建設性回饋"),
    ("小組討論是否設置飲水機，一人說水質、一人說費用。主持人最適合怎麼做？", ["整理兩個面向，再請大家分別提出可查證的資料", "只讓聲音最大的人決定", "宣布其中一個面向不重要", "改談下次聚餐地點"], "A", "整理不同面向並要求資料，能維持討論焦點與邏輯。", "medium", "主持討論與聚焦"),
    ("同學說：「這部影片很有教育意義。」若要了解他的理由，哪個問題最適合？", ["影片中的哪個情節讓你這樣判斷？", "你是不是只是在跟著別人說？", "所有影片都有教育意義嗎？", "你看影片花了幾分鐘？"], "A", "要求指出具體情節，能讓對方說明判斷依據而非停留在評語。", "easy", "由評語追問依據"),
    ("你發現同學的發言與資料表不一致，哪種回應最能保持理性？", ["我看到表中五月數值較低，可以請你說明剛才結論使用哪一欄資料嗎？", "你根本沒有讀懂資料。", "我不管資料，先接受你的結論。", "把表格收起來不要再討論。"], "A", "指出具體差異並請對方說明資料欄位，避免直接攻擊個人。", "medium", "依資料澄清"),
    ("訪談長者時，對方回答較慢，哪種做法最符合良好聆聽？", ["耐心等待，必要時用簡短重述確認自己是否理解", "頻繁插話替對方完成句子", "只挑自己想聽的片段", "未確認內容就立刻公開"], "A", "等待並重述確認，能尊重受訪者也降低理解錯誤。", "easy", "訪談聆聽"),
    ("討論兩種校慶活動方案時，哪個問題最能促進比較？", ["兩方案的參與人數、成本與所需時間各是多少？", "哪個方案看起來比較酷？", "你是不是一定支持第一案？", "誰的想法最受歡迎？"], "A", "用共同面向詢問資料，才能形成有根據的方案比較。", "medium", "比較型提問"),
    ("回饋同學演講時，哪種順序最適當？", ["先說明一項具體優點，再提出一項可執行的改進建議", "先否定整場演講，再說自己沒有看內容", "只說很好，不指出任何依據", "把回饋改成與演講無關的故事"], "A", "具體優點加上可執行建議，能讓回饋尊重且有助修正。", "easy", "回饋順序"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-2-iv-2-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究聽聞、邏輯提問與回饋能力方向（{locator}）；另以官方語文領域課綱核對 2-Ⅳ-2（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
