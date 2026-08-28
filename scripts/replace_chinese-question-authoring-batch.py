"""替換國文 6-Ⅳ-5 題目創作模板為實際題目審查情境。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-5.json").read_text())["source"]["url"]
ITEMS = [
    ("要設計一道判讀校園公告的選擇題，最先應確認什麼？", ["題目只測量一個明確、符合單元的能力", "先決定哪個選項字數最長", "先把答案放在 A 再設計題幹", "先複製公開試卷的整題內容"], "A", "先確認測量目標與單元符合度，才能避免題目偏離學習內容或變成猜選項。", "medium", "命題目標"),
    ("設計『哪項結論符合表格資料』的題目時，錯誤選項最適合如何產生？", ["改變資料範圍、單位或推論程度，形成可由表格排除的干擾", "寫成完全無關且一眼就能排除的句子", "只把正確答案換個標點再當干擾", "讓兩個選項都完全符合資料"], "A", "好的干擾項應利用常見誤讀但能由題幹資料判定，且不能造成兩個正確答案。", "hard", "干擾項"),
    ("發表『校園應增設遮雨棚』的見解時，哪項內容最能使主張完整？", ["說明理由並提供調查或觀察資料作為支持", "只重複三次主張而不提供根據", "只寫自己的座號", "引用與校園無關的傳聞"], "A", "見解要有理由與可查證的證據，讀者才能評估主張是否合理。", "easy", "主張與證據"),
    ("準備發布一段改寫自公開段考題型的教材題目時，檢查來源最重要的目的為何？", ["確認研究脈絡可追溯，且沒有複製受保護的原題文字或選項", "讓題目看起來像原試卷以增加權威感", "把來源名稱刪掉以免讀者查證", "證明所有自編題都是官方原題"], "A", "來源紀錄要能追溯研究脈絡，同時遵守獨立改編與著作權界線。", "hard", "來源與授權"),
    ("一道題目同時要求讀者計算比例，又要求判斷修辭效果，但題幹沒有清楚區分任務。最可能造成什麼問題？", ["測量目標混雜，答錯時難以判斷真正的學習困難", "一定能更精確測量兩種能力", "只要選項夠長就能解決", "答案會自動變得唯一"], "A", "無關能力混在同一題會降低診斷性，無法知道錯誤源自計算還是修辭判讀。", "medium", "測量效度"),
    ("新題目請同學試答後，多數人選了同一個錯誤選項。下一步最適合先檢查什麼？", ["題幹是否有歧義、資料是否足夠，以及干擾項是否利用了誤讀", "直接把錯誤選項標成正確答案", "只增加題目字數", "刪除所有解析避免被發現"], "A", "試答結果是診斷訊號，應回頭檢查題幹清楚度、資料充分性與干擾項設計。", "hard", "試答修訂"),
    ("引用公開資料中的統計數字設計新題目時，哪種做法最適當？", ["標示資料來源與範圍，重新設計題幹和選項，不冒充原題", "只保留數字並宣稱題目是官方發布", "刪除來源讓讀者無法核對", "把原試卷截圖直接放進題庫"], "A", "引用資料需保留可追溯來源；題目與選項仍應獨立設計，不能冒充官方或直接重製。", "hard", "資料引用"),
    ("一題的題幹可同時支持選項 A 與 B。要修正唯一答案問題，最適合如何做？", ["補足限制或改寫選項，使只有一項完全符合題幹證據", "保留兩項正確並隨機指定答案", "刪除題幹中的所有條件", "把兩個選項合併成更長的模糊句"], "A", "唯一最佳答案需由題幹條件與選項文字共同保證，不能靠事後指定。", "medium", "唯一答案"),
    ("題目解析除了寫『答案是 C』，還應包含什麼？", ["指出判斷依據，並說明其他選項為何不符合", "只重複題目而不解釋", "加入題幹沒有的資料", "以『大家都知道』代替理由"], "A", "解析要呈現可核對的推理與選項排除理由，才能支持學習與後續 AI 審查。", "easy", "答案解析"),
    ("完成一批自編題目後，哪組 QA 最能符合本專案規則？", ["核對單元符合度、唯一答案、解析、來源界線、同課與跨課重複", "只計算題目數量，不看內容", "只確認 JSON 能開啟，不檢查答案", "只比較檔案大小，不查看題幹"], "A", "本專案的 AI 審查需同時涵蓋內容、答案、解析、來源與重複，結構通過不能取代內容判讀。", "hard", "綜合 QA"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-5-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究命題、資料引用與閱讀判讀題型（{locator}）；課綱 6-Ⅳ-5：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
