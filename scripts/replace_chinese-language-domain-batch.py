"""替換國語文領域導覽單元的通用題，改為公開段考能力情境。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/official-curriculum-index.json").read_text())["source"]["url"]
ITEMS = [
    ("班級公告寫『週五前繳交閱讀紀錄，逾期請向導師說明』。若要判斷公告的溝通目的，何者最恰當？", ["清楚傳達期限、行動與例外處理", "描寫校園午後景色", "介紹一位虛構人物", "營造懸疑氣氛"], "A", "公告以期限、應做的行動及逾期處理為核心，目的在讓讀者採取正確行動。", "easy", "實用文本"),
    ("讀一則新聞時，標題說『全校都喜歡新午餐』，正文只調查 25 位學生。讀者最應保持哪種態度？", ["檢查樣本與『全校』結論是否相符", "直接接受標題的全稱判斷", "只看標題即可不讀正文", "把 25 人當成全國學生"], "A", "調查對象只有 25 人，不能直接支持『全校』的概括結論，需檢查證據範圍。", "hard", "閱讀與判斷"),
    ("下列哪一句最適合用在向校長提出改善圖書館建議的開頭？", ["我們根據借閱紀錄與同學意見，提出延長開館時間的建議", "我今天心情很好，所以任何方案都可以", "聽說有人說過，這件事一定如此", "先不說問題，請大家猜猜看"], "A", "正式建議需先交代資料依據與主張，讀者才能理解提案的出發點。", "medium", "表達與溝通"),
    ("詩句寫『落日貼近山脊，歸鳥收起喧聲』。若要分析其寫作效果，最應注意什麼？", ["景物與聲音共同營造的氣氛", "詩句中每個字的筆畫數", "作者座號與紙張大小", "把景物全部改成議論"], "A", "落日、山脊與收起喧聲的意象共同形成安靜的畫面與氣氛。", "medium", "文學欣賞"),
    ("小組討論是否設置校園雨具架，一位同學提出使用數據，另一位提出安全疑慮。最好的回應是什麼？", ["先重述兩項理由，再指出需要補充的資料", "只支持最先發言的人", "打斷對方並改談別的主題", "因為意見不同就停止討論"], "A", "良好溝通要理解不同主張，並找出可查證或需補充的資料。", "medium", "討論與聆聽"),
    ("查到網路文章主張『某飲料能提升記憶力』，卻沒有作者、日期或研究資料。下一步最適合做什麼？", ["查找作者、研究依據與其他可信來源交叉比對", "直接轉傳給全班", "因為語氣肯定就視為事實", "只依留言數量判定正確"], "A", "缺少作者、日期與研究依據時，應補查來源並交叉驗證，而非只看語氣或人氣。", "hard", "媒體識讀"),
    ("把『雨天路滑，請減速慢行』改寫成給低年級學生看的提醒，哪一項最合適？", ["下雨時地面會滑，請放慢腳步，小心走路", "雨天路滑，故相關交通安全之抽象概念須被重視", "所有人都必須立即停止一切活動", "路面狀況與行走安全完全沒有關係"], "A", "依受眾調整詞語與句型，保留原因和具體行動，較容易理解與執行。", "medium", "受眾與表達"),
    ("一篇說明文使用表格列出三個月份的回收量，並在文末提出減少垃圾的建議。讀者應如何閱讀？", ["先讀表格的標題、單位與數值，再判斷建議是否有資料支持", "只看文末建議，不必理解表格", "把表格數字當成故事人物", "只比較欄位顏色"], "A", "先確認圖表資訊，再檢查建議是否由資料合理推得，才能完整理解文本。", "hard", "圖文整合"),
    ("修改作文時發現段落順序是『提出結果、補充原因、再介紹問題』。最優先的修訂方向是什麼？", ["重新安排段落或補上銜接，使問題、原因與結果關係清楚", "只把所有句子加粗", "刪除所有標點符號", "加入與主題無關的對話"], "A", "調整篇章順序與銜接，能讓讀者理解問題、原因和結果的邏輯。", "medium", "寫作修改"),
    ("小組完成專題後，哪種成果最能同時展現理解、表達與反思？", ["用自己的話整理資料、說明證據，並指出結論的限制", "只貼上搜尋結果，不標示來源", "只背誦標題而不解釋內容", "只展示版面顏色，不回答問題"], "A", "能整理資料、說明證據並揭露限制，才同時展現理解、表達與批判反思。", "hard", "綜合表現"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-language-arts-domain-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究語文領域常見閱讀、表達與資料判讀題型（{locator}）；官方課綱索引：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
