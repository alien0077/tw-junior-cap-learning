"""替換國文 4-Ⅳ-5 書法行款布局行氣風格模板題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-4-iv-5.json").read_text())["source"]["url"]

ITEMS = [
    ("欣賞直式書法作品時，『行款』主要要觀察什麼？", ["文字排列的行列、方向與字距行距", "紙張的購買價格", "作者的出生年份", "展場燈光的顏色"], "A", "行款關注文字如何分行、排列，以及字距與行距等章法安排。", "easy", "行款概念"),
    ("一幅作品每一行的字距雖不完全相同，卻能自然連貫、視線順暢。這種效果最接近什麼？", ["行氣流動", "字義相反", "部首改變", "標點增加"], "A", "行與行、字與字之間形成連貫的視覺節奏，可稱為行氣流動。", "medium", "行氣觀察"),
    ("比較兩幅內容相同的書法作品時，哪項做法最能看出布局差異？", ["比較每行長短、留白位置與整體重心", "只比較墨汁品牌", "只看作品尺寸而不看字", "只依作者名氣判定"], "A", "布局可由行長、留白與整體重心觀察，不能只看外在或名氣。", "medium", "布局比較"),
    ("書法作品左側留出較寬空白，右側文字較集中。評論時最適合如何描述？", ["留白分布影響整體視覺重心與章法", "空白代表作者漏寫內容", "只要有空白就表示作品未完成", "留白與書法布局完全無關"], "A", "留白會影響視覺重心與章法，應放在整體布局中分析。", "medium", "留白與重心"),
    ("若作品每行起筆位置大致整齊、行距穩定，最可能帶來什麼閱讀效果？", ["視線容易沿行閱讀，整體秩序較清楚", "每個字的字義都會改變", "讀者一定無法辨認文字", "作品必然屬於同一位作者"], "A", "整齊的起筆與穩定行距有助閱讀與章法秩序，但不能據此推定作者。", "easy", "行距與閱讀"),
    ("作品甲筆畫厚重、字距緊密；作品乙筆畫輕快、留白較多。若不考慮作者資料，最合理的比較是什麼？", ["兩者呈現不同的筆勢與章法風格", "甲一定比乙具有更高藝術價值", "乙一定是草書，甲一定是楷書", "只要留白多就沒有章法"], "A", "可依可觀察的筆勢、字距與留白比較風格，不能把視覺差異直接等同價值或書體。", "hard", "風格比較限制"),
    ("觀察一幅橫幅作品時，哪項證據最能支持『行氣由左至右逐漸舒展』的評析？", ["各行字距與留白逐步增加，且視線連貫", "作品使用了昂貴的裝框", "作者曾獲得比賽獎項", "標題使用了四個字"], "A", "逐步增加的字距與留白是直接可觀察的章法證據，能支持行氣評析。", "medium", "評析證據"),
    ("若某作品單字結構端正，但行與行高低差異很大，最精確的說法是什麼？", ["單字結構穩定，但行款或整體布局仍可調整", "單字端正就代表所有章法都完美", "高低差異表示每個字都寫錯", "只能用作品年代解釋差異"], "A", "應區分單字結構與行款布局，才能做出具體而不過度的評價。", "medium", "局部與整體評析"),
    ("欣賞書法風格時，哪項資料最能讓評析更有依據？", ["指出筆畫、結構、行氣與布局等可觀察特徵", "只說『很有氣勢』而不舉例", "只查作品售價", "只看作者的社群追蹤人數"], "A", "以可觀察特徵說明風格，評析才可檢驗，不會流於空泛印象。", "easy", "風格評析"),
    ("臨寫作品後要檢查行款是否接近範本，哪種方法最適當？", ["對照行列方向、字距、行距、留白與重心", "只比較自己用了幾分鐘", "只看單一字是否漂亮", "把所有空白補滿再比較"], "A", "行款是整體安排，需同時對照方向、間距、留白與重心，而非只看單字。", "easy", "行款檢核"),
]

def main() -> None:
    for i, (prompt, options, _answer, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions" / "chinese" / f"question-chinese-performance-4-iv-5-{i}.json"
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
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究書法行款、布局、行氣與風格欣賞能力方向（{locator}）；另以官方語文領域課綱核對 4-Ⅳ-5（{CURRICULUM}）。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
