"""以公立國中段考的文本判讀題型，替換 5-Ⅳ-3 泛用題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-5-iv-3.json").read_text())["source"]["url"]

ITEMS = [
    ("短文先交代校園老樹的現況，再列出樹醫檢查結果，最後提出維護方案。這種安排的主要作用是什麼？", ["由現況到證據再到方案，使說明脈絡清楚", "只為增加人物對話", "刻意隱藏文章主旨", "把不同事件任意拼接"], "A", "文章依現況、檢查證據與處理方案展開，讀者能循序理解問題與回應。", "medium", "篇章安排"),
    ("一段說明文字先界定『雨水回收』，接著比較住家與校園的使用方式。讀者最適合如何掌握內容？", ["先掌握定義，再比較兩種情境的異同", "只記住最後一句，不看前文", "把比較內容當成故事高潮", "只依標題猜測所有細節"], "A", "先理解核心概念，再依比較面向整理材料，才不會混淆兩種使用情境。", "easy", "定義與比較"),
    ("文章寫道：『第一次測量時，操場邊溫度較高；增加樹蔭後，第二次測量的差距縮小。』這段最主要的功能是什麼？", ["用前後資料支持改善措施可能有效", "只描寫操場的顏色", "證明所有地點溫度都相同", "表示作者完全沒有進行觀察"], "A", "前後測量資料提供可比較的證據，但只能支持此情境的改善效果，不能推論所有地點都相同。", "hard", "資料與證據"),
    ("短文以『雖然……但是……』連接兩句：雖然公車班次增加，但是尖峰時段仍然擁擠。這組關聯詞表達什麼關係？", ["轉折", "因果", "承接", "選擇"], "A", "前句提出班次增加的情況，後句指出仍擁擠的不同結果，形成轉折。", "easy", "語句關係"),
    ("故事先寫學生誤以為同學故意不回信，後來才知道對方住院。這種前後資訊安排最能造成什麼效果？", ["先保留疑問，再以新資訊修正讀者判斷", "讓人物永遠沒有任何改變", "把敘事改成沒有事件的目錄", "直接列出所有答案而不留線索"], "A", "後文補充原因，使讀者重新理解先前事件，形成資訊逐步揭露的效果。", "medium", "敘事資訊"),
    ("詩句『暮色收起喧鬧，窗前只剩一盞小燈』若要概括氣氛，何者最恰當？", ["安靜中帶有孤寂感", "熱鬧歡騰且人聲鼎沸", "緊張刺激的競賽場面", "歡迎賓客的正式場合"], "A", "『收起喧鬧』與『只剩一盞小燈』共同營造安靜、略顯孤寂的氛圍。", "easy", "意象與氣氛"),
    ("人物說『我沒事』，卻把未喝完的水杯握得很緊。若要推論人物心情，最可靠的依據是什麼？", ["對話和動作彼此對照的線索", "讀者自己的姓名", "故事印刷紙張的顏色", "與人物無關的標題字體"], "A", "表面語句與緊握水杯的動作不完全一致，需綜合兩種線索推論，而不能只看單一句話。", "hard", "人物描寫"),
    ("說明文先列出三項現象，再逐項解釋原因，最後提出可行作法。這種結構最適合幫助讀者做什麼？", ["把現象、原因與解決方向分層整理", "只注意作者的情緒而忽略資訊", "把三項現象改讀成三位人物", "避免讀者比較不同原因"], "A", "分層呈現能讓讀者知道『看到什麼、為什麼、怎麼做』，便於整理重點。", "medium", "說明結構"),
    ("兩篇文章都談閱讀習慣：甲文使用調查數據，乙文只描述作者個人經驗。若要比較可信度，第一步應做什麼？", ["確認兩篇文章的證據類型與適用範圍", "直接判定篇幅較長者一定正確", "只比較標題是否押韻", "因為主題相同就視為證據相同"], "A", "數據與個人經驗的證據性質不同，先辨認證據類型及可支持的範圍，才能公平比較。", "hard", "證據比較"),
    ("段落由『問題現象』跳到『因此我們應該……』，中間沒有說明理由。修改時最需要補上什麼？", ["連接現象與主張的理由或證據", "與主題無關的景物描寫", "更多重複的標題", "完全刪除原有問題"], "A", "補出理由或證據，讀者才看得出前面的現象如何支持後面的主張。", "medium", "篇章銜接"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-5-iv-3-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        rotated = options[shift:] + options[:shift]
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65 + j), "text": text} for j, text in enumerate(rotated)]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {
            "origin": "original",
            "license": "All rights reserved",
            "sourceUrl": SOURCE,
            "sourceLocator": f"高雄市立鹽埕國中 114 學年度下學期第一次段考三年級國文科試題卷；研究文本判讀與字音字形以外的閱讀題型（{locator}）；課綱 5-Ⅳ-3：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review.",
        }
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
