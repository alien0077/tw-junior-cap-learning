"""替換國文 2-Ⅳ-5 報告評論演說與論辯模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%95%99%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%等%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"

CURRICULUM = "https://www.naer.edu.tw/upload/1/16/doc/806/%E5%8D%81%E4%BA%8C%E5%B9%B4%E5%9C%8B%E6%B0%91%E5%9F%BA%E6%9C%AC%E6%教%E8%82%B2%E8%AA%B2%E7%B6%B1%E8%A6%81%E5%9C%8B%E6%B0%91%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%9A%A8%E6%99%AE%E9%80%9A%E5%9E%8B%E9%AB%98%E7%B4%9A%E4%B8%AD%E7%AD%89%E5%AD%B8%E6%A0%A1(%E8%AA%9E%E6%96%87%E9%A0%98%E5%9F%9F%E2%94%80%E5%9C%8B%E8%AA%9E%E6%96%87).pdf"
CURRICULUM = "https://www.naer.edu.tw/"
ITEMS = [
    ("準備『校園午餐剩食』報告時，哪項資料最適合放在主張後作為證據？", ["連續四週記錄的每日廚餘重量", "報告者覺得午餐很難吃", "網路留言中一個未署名的句子", "與午餐無關的天氣傳聞"], "A", "連續且可查核的重量紀錄能直接支持剩食量的主張。", "easy", "報告證據選擇"),
    ("演說開頭先描述同學每天找不到安靜自習座位，再提出『延長圖書館開放』的主張。這樣安排有何作用？", ["由具體問題引出主題，吸引聽眾注意", "先公布所有結論而不說明背景", "讓聽眾無法知道演說主題", "以個人座位取代公共議題"], "A", "先呈現具體問題能建立情境，再自然引出後續主張。", "medium", "演說開場組織"),
    ("評論一篇『手機有助學習』的文章時，哪項做法最符合評論要求？", ["指出文章主張，並檢查所用例子是否足以支持主張", "只依作者名氣決定文章好壞", "只挑一句話批評而不看全文", "用自己的喜好取代文章證據"], "A", "評論需掌握主張並檢查理由與證據，而非只看作者或個人喜好。", "medium", "評論與證據"),
    ("辯論對方主張『所有作業都應改成線上』，你發現對方只提供一個班級的經驗。最適合如何回應？", ["指出樣本有限，並請對方補充不同班級或更多資料", "直接說對方永遠不可能正確", "改談自己喜歡的科目", "不聽理由便重複口號"], "A", "指出資料代表性限制並要求補充證據，是理性的論辯回應。", "hard", "論辯資料限制"),
    ("三分鐘報告只能使用一張投影片時，哪種設計最能幫助聽眾掌握重點？", ["放主旨、三項關鍵資料與一句結論", "貼上整篇逐字稿並縮小字體", "放十張互不相關的圖片", "只放報告者姓名"], "A", "有限版面應保留主旨、核心資料與結論，避免資訊過量。", "easy", "報告資訊取捨"),
    ("演說者引用統計圖表後，下一步最適合做什麼？", ["說明圖表中的關鍵變化如何支持自己的主張", "只念出圖表標題便跳過解釋", "把所有數字改成感嘆句", "宣稱圖表能證明任何結論"], "A", "需把資料與主張的關係說清楚，不能只展示圖表或過度延伸。", "medium", "圖表與主張"),
    ("辯論時對方提出反例，最合適的回應是什麼？", ["先重述反例，再說明它是否改變原主張及理由", "假裝沒有聽見反例", "只攻擊對方的個性", "立刻改變立場卻不解釋"], "A", "重述並分析反例與主張的關係，才能形成有理由的回應。", "medium", "反例處理"),
    ("報告介紹校園節電方案，先說明現況，再比較兩種方案的成本與效果，最後提出選擇。這種結構的優點是什麼？", ["讓問題、比較依據與結論彼此連貫", "只呈現方案名稱而不提供依據", "把結論藏起來避免檢查", "用情緒取代成本與效果"], "A", "先交代問題，再以共同面向比較，最後提出結論，推理鏈完整。", "medium", "報告推理結構"),
    ("評論同學的演說時，下列哪項回饋最具體且有助改進？", ["開頭的問題情境清楚，但第二項資料應標明來源", "內容很棒，加油就好", "我就是不喜歡這個主題", "你講得很爛，沒有任何理由"], "A", "回饋指出具體優點與可修正處，且能對應演說內容與資料來源。", "easy", "評論回饋"),
    ("演說結尾說『因此，請從本週少用一個一次性杯子開始，並在下週記錄改變。』這句主要具有什麼功能？", ["重申行動主張並提出可執行的呼籲", "新增與主題無關的人物", "只交代演說者的出生地", "否定前文所有證據"], "A", "結尾回扣主張並提出具體行動，能讓聽眾知道可如何回應。", "easy", "演說結尾與呼籲"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-2-iv-5-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究報告、評論、演說與論辯能力方向（{locator}）；另以官方語文領域課綱核對 2-Ⅳ-5（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
