import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","證據、模型與推理能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","資料比較、預測與限制能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","探究解釋、證據強度與結論界線能力方向")]
DATA=[
("evidence strength","哪項證據最能提高對某解釋的信心？",["不同地點以相同方法重複觀察，結果相近且能提出可檢驗預測","只找到一篇支持文章","只挑符合預期的資料","由權威口頭保證正確"],"A","A 同時具備重複、方法一致、跨地點與可檢驗預測，證據比單一聲稱更強。"),
("model boundary","紙板影子模型在室內有效，搬到有散射光的戶外出現落差，最恰當的說法是？",["先保留模型在原條件下的用途，再加入散射光與地面條件檢查限制","模型完全沒有價值","一次落差證明所有影子模型都錯","刪除戶外資料"],"A","A 既保留原模型可解釋的範圍，也把新背景納入修正，不把局部落差過度推廣。"),
("forecast","天氣預報因加入新雷達資料而改變，應如何理解？",["新資料可能改善預測或縮小適用範圍，不代表舊預報的所有依據都失效","預報改變代表科學只是意見","最新預報不需查證一定正確","昨天的觀測必然全錯"],"A","A 區分模型改進、範圍限制和全盤否定，符合科學知識可修正但非任意改換。"),
("parameter","疾病傳播模型在接觸率不同時產生不同曲線，首先應檢查什麼？",["接觸率假設、資料來源、時間範圍與模型適用條件","只選病例數較高的曲線","把所有參數固定成最樂觀值","不看資料直接選最新的模型"],"A","A 檢查參數與背景，才能知道差異是條件改變、資料品質或模型結構造成。"),
("provisional","下列哪句最能表達有條件的科學結論？",["在本次樣本與測量條件下，資料支持 X；仍需更多時段檢查 Y","X 永遠在任何地方成立","目前不知道所以任何說法都一樣","X 看起來合理，不必交代證據"],"A","A 清楚寫出證據、樣本與未知，既不誇大也不把未知等同任意意見。"),
("new evidence","新測量結果與舊模型不一致時，哪個順序較合理？",["先查定義、器材、樣本與條件，再比較模型假設與資料，最後決定是否修正","直接宣布舊知識錯誤","刪掉新結果以維持一致","只看哪個說法較受歡迎"],"A","A 先排除方法與背景差異，再以證據判斷模型是否需要調整。"),
("stable scope","『科學知識會修正』不應被解讀為什麼？",["所有說法都同樣可靠，想改就改","證據較充分的結論可在明確條件下長期有效","模型永遠不能使用","新證據不重要"],"A","A 是錯誤解讀；可修正性不會消除證據品質、方法與適用範圍的差異。"),
("model use","模型最主要的科學用途是什麼？",["在明確假設下提出可比較、可檢查的預測或解釋","取代所有實際觀察","產生看似精確但不能驗證的數字","保證未來一定照模型發生"],"A","A 指出模型能連結假設與預測並接受檢查；模型不是現實本身，也不保證絕對準確。"),
("revision","新模型較能解釋大尺度資料時，對舊模型如何處理最合適？",["檢查舊模型在哪些小範圍仍有效，再說明新模型增加的條件","把舊模型所有結果全部刪除","只因新名稱就全盤接受","拒絕比較兩者證據"],"A","A 以適用範圍連結新舊模型，呈現知識累積與修正，而非簡化成全對或全錯。"),
("communication","向同學說明一個尚未確定的科學解釋時，應包含什麼？",["支持證據、假設、目前限制、適用範圍與可檢驗的下一步","只說答案不說資料","用『大家都這樣說』代替證據","把不確定性刪掉避免誤會"],"A","A 讓聽者知道信心從何而來、哪些仍未知以及如何檢查，符合負責任的科學溝通。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以證據、模型、資料比較、預測與結論界線要求推理；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出本題的科學知識判讀核心「{topic}」。","列出證據來源、方法品質、模型假設、適用條件與結論範圍。",f"逐項比對哪個選項符合證據與模型判準；正確答案是 {ans}。",f"核對理由：{exp}","最後回查是否把可修正誤當任意意見，或把一次資料過度推廣；必要時寫出下一個可檢驗觀察。"]
 return {"id":f"question-science-performance-an-iv-2-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-an-iv-2"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究證據、模型、預測與修正能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-an-iv-2","examPatternRefs":refs,"solutionStrategy":"先分辨觀察、模型、解釋與預測，再檢查證據強度、假設、適用條件、新資料與結論界線。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-an-iv-2-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
