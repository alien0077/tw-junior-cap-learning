import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","知識、現象與數據推論能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","變因、機制與證據連結能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","替代解釋、資料判讀與結論界線能力方向")]
DATA=[
("observation","鞋底拉力不同時，第一步應如何連結知識？",["先描述拉力差，再檢查重量、角度、表面與摩擦概念","直接說粗糙一定造成差異","只看鞋底外觀顏色","把差異平均掉"],"A","A 先對齊資料與控制條件，再用摩擦概念提出推論。"),
("mechanism","完整的科學推論除了資料還需要什麼？",["相關概念提供的機制、適用條件、預測與限制","只需要專業名詞","只需要一個相關圖形","只需要更肯定的語氣"],"A","A 讓資料、知識、機制和可檢查預測連成推論鏈。"),
("plant","植物質量下降可能由多種因素造成，哪種研究設計較好？",["固定盆土、光照與時間，分別比較葉面積、風速、溫度與供水影響","只測一次質量就宣布蒸散","只選最熟悉的原因","把所有條件同時改變"],"A","A 保留替代解釋並用控制比較逐步定位原因。"),
("causation","兩變數一起增加時，哪項結論最負責任？",["先說明相關觀察，仍需控制條件和機制證據才能主張因果","一定是前者造成後者","兩者完全沒有關係","只要畫折線圖就證明因果"],"A","A 區分相關與因果，避免把共變化直接當機制證明。"),
("sound","兩條弦長度不同且基頻不同，如何提出可檢查推論？",["連結弦長與振動頻率，預測縮短弦長的方向並固定張力與材料","只說聲音變大","把任何變化叫共振","只看其中一次讀值"],"A","A 有概念連結、方向預測與控制條件。"),
("scale","同一概念換到不同材料時，推論應注意什麼？",["檢查材料、尺度、溫度與測量條件是否仍符合原本適用範圍","概念永遠不需調整","只要名稱相同就能直接外推","把新資料刪掉"],"A","A 讓推論尊重概念的條件和尺度限制。"),
("alternative","鞋底差異也可能來自重量不同，最有用的下一步是？",["固定重量並在相同表面與角度重測，再比較拉力","只重測最粗糙的鞋底","詢問誰覺得較滑","把重量差異藏起來"],"A","A 設計能區分鞋底和重量影響的控制測試。"),
("evidence","若植物只記錄質量，哪項推論不能直接成立？",["不能單憑質量下降判定唯一是蒸散，還需其他條件與指標","質量可以完全代表所有機制","蒸散永遠不需測量","所有植物都會同樣變化"],"A","A 說明單一指標不足以決定多個可能機制。"),
("conditional","下列哪句是較好的條件式結論？",["在相同重量、角度與表面下，本次粗糙鞋底所需拉力較大，仍需重複確認","粗糙鞋底在任何情況都摩擦最大","摩擦概念已證明所有結果","拉力不同所以知道全部原因"],"A","A 限定資料條件並保留重複與替代解釋。"),
("revision","實驗數據不符合原本推論時，最適合做什麼？",["檢查概念適用範圍、控制條件、測量與替代解釋，再修正推論","修改數據使概念成立","只保留支持推論的結果","宣布概念永遠錯誤"],"A","A 讓不符資料促成查證與修正，而非挑資料或全盤否定。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以知識、現象、數據、機制、變因與證據界線要求推論；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出推論核心「{topic}」。","分辨直接觀察、既有知識、機制、控制條件、替代解釋與結論範圍。",f"逐項比對哪個選項能由資料和知識共同支持；正確答案是 {ans}。",f"核對理由：{exp}","最後回查是否把相關當因果、把局部結果外推，並寫出能區分解釋的下一步。"]
 return {"id":f"question-science-performance-tr-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-tr-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究知識連結、現象、數據與推論能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-tr-iv-1","examPatternRefs":refs,"solutionStrategy":"先描述資料，再連結概念和機制，檢查控制條件、替代解釋、尺度與條件式結論。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-tr-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
