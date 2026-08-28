"""替換國文 1-Ⅳ-2 聲情與表達技巧模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-1-iv-2.json").read_text())["source"]["url"]
ITEMS = [
    ("廣播員放慢速度並加重『請先確認出口位置』，最可能是要達成什麼效果？", ["凸顯安全重點，讓聽者注意必要行動", "表示廣播員忘記內容", "讓所有資訊變得不重要", "只為展示聲音大小"], "A", "放慢與重音把注意力集中到安全提醒，提示聽者應採取的行動。", "easy", "重音與速度"),
    ("同學音量降低、停頓後說『我其實有點擔心』。從聲情判斷，哪項最合理？", ["語氣透露不安，內容可能需要被傾聽與關心", "語氣表示他非常確定且毫不在意", "停頓表示他正在朗讀標題", "音量降低必然表示他在開玩笑"], "A", "音量降低與停頓配合『擔心』的詞語，顯示情緒不安，但仍應透過回應確認。", "medium", "情緒線索"),
    ("同一句『你今天來得真早』用明顯上揚的語調說出，最可能表示什麼？", ["帶有疑問或需要確認的語氣", "一定是在宣讀正式公告", "表示說話者正在列舉三項資料", "表示句子沒有任何語意"], "A", "上揚語調常提示疑問或確認；仍需結合情境，不能只由語調推定所有意思。", "medium", "語調"),
    ("回應同學意見時先說『我理解你擔心時間不足』，再提出另一方案，主要展現什麼？", ["先同理對方，再以清楚理由回應", "用禮貌語句掩飾完全不聽", "避免任何人表達不同意見", "表示不需要說明自己的方案"], "A", "先確認對方的情緒與理由，再提出方案，有助於尊重對話並維持討論焦點。", "easy", "回應技巧"),
    ("公告說『請於週五 17 時前完成登記，逾期不受理』。聽者最應優先記下什麼？", ["截止日期時間與逾期後果", "公告者的聲音高低", "自己對其他活動的回憶", "與登記無關的背景音樂"], "A", "截止時間與逾期後果會直接影響行動，是公告的核心資訊。", "easy", "公告聆聽"),
    ("演講者用『首先、其次、最後』介紹三個步驟，聽者可如何利用這些詞？", ["辨認內容順序並整理三個層次", "判斷演講者的年齡", "推論所有步驟同時發生", "忽略後面出現的具體內容"], "A", "順序詞是聽者整理篇章結構的線索，可協助掌握步驟先後。", "easy", "順序詞"),
    ("對方講解操作方法太快，哪種回應最有效？", ["請對方放慢並重複關鍵步驟，自己再重述確認", "假裝全部聽懂而直接操作", "打斷後改談無關話題", "只說『好』但不確認內容"], "A", "請求重複並用自己的話確認，可降低漏聽步驟造成的錯誤。", "medium", "澄清回應"),
    ("演講者在結尾反覆說『我們可以做到』，若前文提出具體行動，重複最可能有何作用？", ["強化信心與行動號召", "表示前文的證據全部無效", "讓聽者忘記演講主題", "只為增加沒有意義的字數"], "A", "結合具體行動時，重複句可強化情緒與鼓勵，形成行動號召。", "medium", "重複與說服"),
    ("人物回答『這件事嘛……我再想想』，語氣和停頓最可能暗示什麼？", ["尚未決定或有所猶豫", "已經明確答應且沒有疑慮", "正在宣布確定的時間表", "完全沒有回應問題"], "A", "拖長語氣與停頓常透露猶豫，但仍應結合前後對話確認人物真正立場。", "medium", "停頓與態度"),
    ("辨識一段口語表達技巧時，哪種依據最完整？", ["綜合詞語內容、音量速度、語調停頓與對話情境", "只看最後一個字", "只依說話者的外表猜測", "只計算句子長度"], "A", "聲情判讀需把語言內容、聲音特徵與情境一起考量，單一線索不足以作結論。", "hard", "綜合判讀"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-1-iv-2-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究聲情、聆聽與口語表達判讀題型（{locator}）；課綱 1-Ⅳ-2：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
