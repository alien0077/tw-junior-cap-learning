"""替換國文 6-Ⅳ-6 數位編輯與分享模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-6.json").read_text())["source"]["url"]
ITEMS = [
    ("用簡報介紹校園閱讀調查時，哪項設計最能幫助觀眾掌握重點？", ["每頁只呈現一個重點，搭配標題、必要數據與簡短說明", "把完整訪談逐字稿縮成最小字體放滿每頁", "只放背景圖片，不標示調查範圍", "每頁使用不同結論，讓觀眾自行猜測"], "A", "簡報需分層呈現訊息；保留重點、必要數據與範圍，才能兼顧可讀性與證據。", "easy", "簡報層次"),
    ("在文章中加入一張統計圖前，最應先確認什麼？", ["圖表資料與文字主張一致，且標示來源、單位與範圍", "圖片解析度越高就一定正確", "只要顏色鮮豔，不必標示數值", "把圖表標題改成與資料無關的口號"], "A", "圖文整合需核對資料與主張，並提供來源、單位及範圍，避免誤導。", "hard", "圖文核對"),
    ("發布校刊文章前，哪項編輯工作不可省略？", ["核對錯字、標點、連結、圖片權限與個人資料", "只確認封面顏色是否漂亮", "刪除所有不同意見", "不讀全文就直接發布"], "A", "發布前要同時檢查文字品質、連結、素材權利與個資風險。", "hard", "發布前檢查"),
    ("製作影片介紹『校園減塑』的心得時，哪項安排最能支持觀點？", ["用觀察紀錄或前後數據說明改變，再清楚標示資料來源", "只加入快速轉場與音效，不交代證據", "把未查證的網路留言當成統計結果", "只朗讀標題，刪除所有限制"], "A", "觀點需由可核對的觀察或數據支持，並揭露來源與限制。", "medium", "影片證據"),
    ("共同編輯線上報告時，哪種做法最能維持內容一致？", ["先約定標題層級、用詞與資料版本，並記錄修改者和日期", "每個人自行更換術語，不留下紀錄", "只由最後開檔的人憑印象合併", "刪除所有版本以免看見差異"], "A", "共同編輯需要一致的格式與資料版本，修改紀錄也能追蹤內容變化。", "medium", "共同編輯"),
    ("圖文作品加入標題與小標，主要有什麼功能？", ["提示主題與內容層次，幫助讀者快速定位資訊", "讓所有段落看起來完全相同", "取代正文中的證據", "表示標題下的資料一定正確"], "A", "標題與小標提供導覽與層次，不能取代正文證據，也不能保證資料正確。", "easy", "標題層次"),
    ("把同學的作品分享到社群平台前，哪項做法最負責任？", ["先取得同意，確認個資與素材權利，並清楚標示作者與來源", "為了增加瀏覽量公開所有姓名與聯絡方式", "把別人的作品改名成自己的", "只要是同學作品就不需詢問"], "A", "分享涉及同意、個資、著作權與署名，不能因熟識或公開平台而省略確認。", "hard", "負責任分享"),
    ("讀者留言指出文章中的年份可能有誤，編輯最適合如何處理？", ["回查原始資料，確認後更正並註明修訂內容", "立即刪除留言並維持原文", "因為留言者不是作者就完全不查", "把年份改成讀者猜測的數字"], "A", "指出疑點後應回查來源；若有錯誤就更正並留下修訂說明。", "medium", "錯誤更正"),
    ("將長篇研究報告改成三分鐘短影片時，最需要保留什麼？", ["研究問題、主要證據、結論與必要的限制說明", "所有附錄的每一行文字", "只保留最吸引人的片段而刪除證據", "把研究限制改成肯定宣稱"], "A", "縮短形式可以刪減細節，但不能刪除問題、證據、結論與影響判斷的限制。", "hard", "長文轉短片"),
    ("數位作品完成後，哪項檢核最能證明它適合公開分享？", ["內容可讀、資料可追溯、連結可用，且已處理個資與素材授權", "檔案容量最大且動畫最多", "只確認自己看得懂，不管讀者", "只要成功上傳就代表內容正確"], "A", "公開作品要同時通過內容、來源、功能、個資與授權檢查，上傳成功不等於內容可靠。", "hard", "分享前 QA"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-6-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究數位編輯、圖文表達與發布判讀題型（{locator}）；課綱 6-Ⅳ-6：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
