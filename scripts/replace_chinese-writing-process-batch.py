"""替換國文 6-Ⅳ-2 寫作流程模板題為段落組織判讀題。"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E5%9C%8B%E6%96%87.pdf"
CURRICULUM = json.loads((ROOT / "curriculum/chinese/performance-6-iv-2.json").read_text())["source"]["url"]
ITEMS = [
    ("題目要求介紹一次校外學習經驗，還要說明自己的收穫。下列哪項最符合審題結果？", ["確認文章須同時包含經驗事件與收穫反思", "只寫景物即可，不必提到學習", "只列出同行者姓名即可", "只抄寫題目，不需安排內容"], "A", "審題要抓出寫作對象、內容任務與限制；此題同時要求經驗和反思。", "easy", "審題"),
    ("以『我學會等待』為題寫作時，最適合作為中心思想的是哪一項？", ["透過一件具體事件說明等待帶來的體會", "把所有發生過的事情都不加選擇地列出", "只描寫天氣，完全不提等待", "只寫一句口號，不提供事件或感受"], "A", "立意需回應題目並形成可發展的核心觀點，具體事件能支撐等待的體會。", "medium", "立意"),
    ("文章主旨是『合作能解決困難』，下列哪項材料最適合取用？", ["小組分工修好校園展示板，並說明合作如何克服問題", "與主旨無關的美食價格清單", "只記錄某天的雲朵形狀", "另一篇文章的作者簡介"], "A", "取材要能直接支持主旨，分工修理並解決問題可呈現合作的作用。", "easy", "取材"),
    ("若要把『問題出現—尋找方法—完成改變』寫成三段文章，最適合的組織方式是什麼？", ["依事件發展順序安排開頭、發展與結尾", "把結尾放在最前且不提供任何線索", "每段各寫不同主題，避免互相連接", "只保留中間方法，刪除問題與結果"], "A", "依事件先後組織，可讓讀者理解問題如何導向方法與結果。", "easy", "組織"),
    ("寫給校長的建議信中，哪一句最適合放在提出請求的段落？", ["敬請您參考上述資料，評估於午休時段增設飲水設備", "喂，快點照我說的做，不然就算了", "我昨天看到一朵很大的雲，所以校長應該同意", "這件事跟前文無關，先談另一部電影"], "A", "正式書信需依對象調整語氣，並清楚提出請求與依據。", "medium", "遣詞"),
    ("初稿每段都在描述校園景色，卻沒有回應『一次挫折帶給我的改變』。修訂時最應先做什麼？", ["刪減無關景物，補入挫折事件與改變的關聯", "再增加更多無關的景物描寫", "把題目改成校園風景，不必檢查要求", "只改變字體大小，不調整內容"], "A", "文章偏離題旨時，應先回到題目要求調整材料與主旨關係。", "medium", "修訂主旨"),
    ("段落甲寫『因此我們決定分組調查』，下一段卻直接寫『調查結果顯示……』。若中間缺少說明，最適合補充什麼？", ["交代分組調查的目的、方法或執行過程", "加入與調查無關的童年回憶", "重複寫一次『因此』而不補資訊", "刪除調查結果讓文章停止"], "A", "補上目的、方法或過程，讀者才知道結論如何由前文的行動產生。", "hard", "段落銜接"),
    ("完成作文後，哪一組檢查順序最能提升文章品質？", ["先看是否切合題旨，再查結構銜接，最後修正字詞標點", "先改封面顏色，再決定文章是否離題", "只數每段字數，不看語意", "先刪除所有標點，再檢查主旨"], "A", "先確認內容方向，再處理篇章與語句細節，能避免只修表面而忽略離題。", "medium", "修訂順序"),
    ("一段材料很精彩，但只能用來支持『旅行中的新發現』，不能支持題目要求的『如何面對失敗』。最適合如何處理？", ["刪除、改寫或另放到能支持題旨的位置", "因為精彩就原封不動放入任何段落", "把題目要求刪掉以配合材料", "把材料獨立成與文章無關的結尾"], "A", "材料是否精彩仍須服從題旨；與題目無關就應調整或捨棄。", "medium", "材料取捨"),
    ("下列哪個寫作流程最完整？", ["審題立意取材組織遣詞成文，再檢查與修訂", "先寫結尾，再隨機貼上材料，不必檢查", "只列大綱，不寫正文也不修改", "先選華麗詞語，再猜測題目要求"], "A", "完整流程包含理解題目、確立中心、選材、組織、遣詞成文與修訂檢查。", "easy", "整體流程"),
]

def main() -> None:
    for i, (prompt, options, _, explanation, difficulty, locator) in enumerate(ITEMS, 1):
        path = ROOT / "questions/chinese" / f"question-chinese-performance-6-iv-2-{i}.json"
        data = json.loads(path.read_text())
        shift = i % 4
        data["prompt"] = prompt
        data["options"] = [{"id": chr(65+j), "text": t} for j, t in enumerate(options[shift:] + options[:shift])]
        data["difficulty"] = difficulty
        data["answer"] = {"value": chr(65 + ((4 - shift) % 4)), "explanation": explanation}
        data["provenance"] = {"origin": "original", "license": "All rights reserved", "sourceUrl": SOURCE,
            "sourceLocator": f"鹽埕國中 114 學年度下學期第一次段考三年級國文科公開試題卷；研究寫作流程與篇章判讀題型（{locator}）；課綱 6-Ⅳ-2：{CURRICULUM}。本題為獨立改編，非原題重製。",
            "authoringNote": "Safe adaptation; no source wording, options, passage, figure, or answer reproduced. Requires second-pass AI content review."}
        data["reviewStatus"] = "draft"
        data["updatedAt"] = "2026-08-28"
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
