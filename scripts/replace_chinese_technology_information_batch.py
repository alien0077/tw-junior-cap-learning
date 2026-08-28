"""替換國文 2-Ⅳ-4 科技資訊與表達模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-2-iv-4.json").read_text())["source"]["url"]

ITEMS = [
    ("準備『校園用水』簡報時，看到一則沒有作者與日期的網路貼文，最適合如何處理？", ["先把它當線索，再以具名且可追溯來源查證", "直接當成正式統計資料", "只因轉發次數多就視為正確", "刪除所有其他資料避免比較"], "A", "無作者與日期的貼文可作線索，但須以可追溯來源查證，不能直接當正式資料。", "easy", "來源可信度"),
    ("兩個網站對同一項政策的數字不同，製作報告前最應先做什麼？", ["確認統計年度、對象、單位與原始資料來源是否相同", "挑數字較大的網站使用", "只看網頁版面較漂亮的網站", "把兩個數字平均後不說明原因"], "A", "統計年度、對象與單位不同可能造成差異，需先核對資料條件。", "medium", "交叉查證"),
    ("簡報要呈現四週垃圾量變化，哪種做法最能幫助觀眾理解趨勢？", ["用標示清楚的折線圖，附上期間、單位與資料來源", "只放一張沒有座標軸的圖片", "把最高值放大但刪除其他數值", "用大量動畫遮住數據"], "A", "折線圖適合呈現時間變化，且必須標示期間、單位與來源。", "easy", "圖表選擇與標示"),
    ("引用網路文章中的一段資料放入報告，哪種做法最適當？", ["改用自己的話整理，標示作者、標題、網址與查閱日期", "刪掉作者姓名讓版面更簡潔", "整段照貼但宣稱是自己調查", "只寫『網路資料』不提供連結"], "A", "改寫並完整標示來源，能讓讀者追溯資料，也避免誤認為自製內容。", "medium", "引用與來源標示"),
    ("為國小學生製作地震防災簡報時，哪項設計最合適？", ["用簡短句子、清楚圖示與可執行的避難步驟", "使用大量未解釋的專業術語", "每頁貼滿長段文字", "只放震度數字而不說明行動"], "A", "應依受眾調整詞語與呈現，並把資訊轉為可執行步驟。", "easy", "受眾與媒體設計"),
    ("某圖表縱軸從 95 開始，讓 100 與 105 的差異看起來很大。閱讀時最應注意什麼？", ["確認縱軸起點與刻度，避免視覺比例誇大差異", "只看圖形斜率不看刻度", "認定差距一定是五倍", "刪除所有數據只看顏色"], "A", "縱軸未從零開始可能放大視覺差異，必須讀清起點與刻度。", "hard", "圖表誤導判讀"),
    ("報告中使用自己拍攝的校園照片，若照片中可辨識同學的臉，最適合如何做？", ["取得同意或遮蔽可辨識資訊，再依規範使用", "因為自己拍攝就可任意公開", "只在照片旁寫自己的名字", "把照片來源全部刪除"], "A", "自己拍攝不等於可無限制公開，應尊重個資並取得同意或去識別化。", "medium", "影像使用與責任"),
    ("利用試算表整理訪談結果時，哪項做法最能提高可信度？", ["保留原始紀錄，註明分類規則並檢查加總是否一致", "只保留支持主張的回答", "修改數字讓圖表更整齊", "不記錄受訪人數與問題內容"], "A", "保留原始紀錄並說明處理規則，結果才可檢查與重現。", "medium", "資料整理透明度"),
    ("一則短影音宣稱『某飲品能讓所有人立刻變健康』，判讀時哪種做法最理性？", ["檢查宣稱的研究來源、樣本與是否使用絕對化語句", "只因影片觀看數高就相信", "只看背景音樂是否專業", "把個人見證當成所有人的證明"], "A", "研究來源、樣本與語句範圍會影響可信度，個人見證不能代表所有人。", "hard", "數位訊息判讀"),
    ("簡報最後列出『資料來源、製作限制與仍待查證的問題』，主要能產生什麼效果？", ["讓觀眾知道證據範圍，並能區分結論與推測", "讓報告看起來一定沒有錯", "避免觀眾檢查資料", "把所有責任轉給讀者"], "A", "揭露來源與限制能提高透明度，避免把推測誤當確定結論。", "medium", "科技表達的限制揭露"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-2-iv-4-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究科技資訊與表達能力方向（{locator}）；另以官方語文領域課綱核對 2-Ⅳ-4（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
