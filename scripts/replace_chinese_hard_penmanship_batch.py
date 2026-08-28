"""替換國文 4-Ⅳ-6 正確美觀硬筆字模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-6.json").read_text())["source"]["url"]

ITEMS = [
    ("在方格紙上寫字時，若要讓字形穩定，最先應注意什麼？", ["主要筆畫的位置與整體重心", "每個字都寫到格線外", "只追求書寫速度", "把所有筆畫改成相同長度"], "A", "先掌握主要筆畫與重心，字形才不易偏斜或失去比例。", "easy", "字形重心"),
    ("寫左右結構的「明」字時，哪種做法最能維持整潔？", ["注意左右部件比例與中間空隙", "把右邊部件壓縮到幾乎看不見", "讓兩部件互相重疊", "只放大左邊部件而不看格線"], "A", "左右結構要兼顧部件比例與間距，才能清楚辨認並保持平衡。", "easy", "部件比例"),
    ("抄寫一段公告時，哪項安排最能幫助讀者閱讀？", ["字距與行距一致，段落和標題有明確區隔", "每行長短任意且不留空間", "把標題和正文寫成相同大小並連在一起", "為了省紙把字全部擠在同一行"], "A", "一致的字距、行距與層次能建立清楚的版面結構。", "easy", "字距行距"),
    ("若一個字的橫畫明顯向右上斜，與其他字的基準線不一致，最可能影響什麼？", ["整行的穩定感與閱讀整齊度", "字典中詞語的讀音", "紙張的吸墨速度", "文章的段落主旨"], "A", "基準線不穩會影響整行的視覺整齊與書寫穩定感，但不會改變詞語讀音。", "medium", "基準線與整齊"),
    ("下列哪種修改最能改善『字小、行距大、版面鬆散』的筆記？", ["適度放大字形並縮小過大的行距，保留必要留白", "把所有字寫到紙張邊緣", "刪除標題與標點", "把不同段落全部混成一行"], "A", "調整字形與行距、保留必要留白，可在可讀性與版面平衡間取得較好效果。", "medium", "版面調整"),
    ("寫「樹」這類筆畫較多的字時，哪個方法最適當？", ["依正確筆順分配部件空間，完成後檢查是否易辨認", "為了快速完成而任意省略關鍵筆畫", "把每一筆都寫到格線外", "只寫外框不寫內部結構"], "A", "依筆順安排部件並檢查完整結構，能兼顧正確與辨識度。", "medium", "複雜字書寫"),
    ("若同一段文字中有些字靠左、有些字靠右，最適合如何檢查？", ["對照基準線與格線，逐字調整位置與大小", "只改最後一個字", "把所有字塗黑重新開始", "只看筆的顏色是否一致"], "A", "對照基準線與格線才能找出位置、大小不一致的原因並修正。", "easy", "格線檢查"),
    ("硬筆字的『美觀』評量若要較公平，最應依據什麼？", ["筆畫清楚、結構穩定、大小與間距協調等可觀察標準", "書寫者的年齡與座號", "筆的價格越高越美觀", "只看紙張是否昂貴"], "A", "以筆畫、結構、大小與間距等可觀察標準評量，較不依賴主觀或無關資訊。", "medium", "書寫評量標準"),
    ("練習後想知道字形是否改善，哪種證據最有用？", ["用相同句子前後對照，檢查基準線、比例與間距", "只記錄今天寫了幾分鐘", "只比較筆記本封面", "詢問自己喜不喜歡這支筆"], "A", "相同材料的前後對照能直接觀察字形、比例與間距是否進步。", "easy", "前後對照"),
    ("抄寫正式通知時，哪項做法最能兼顧正確與美觀？", ["先核對文字與標點，再以穩定筆畫、適當大小和間距抄寫", "只追求速度而不回看錯字", "把標點全部省略以節省空間", "只模仿字形外觀，不確認內容"], "A", "先確認內容正確，再控制筆畫、大小與間距，才能兼顧文字正確與版面美觀。", "medium", "書寫流程"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-6-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究正確美觀硬筆字能力方向（{locator}）；另以官方語文領域課綱核對 4-Ⅳ-6（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
