import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","探究策略、資料與思考能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","問題拆解、方法與證據能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","資料轉換、遷移與反思能力方向")]
DATA=[
("decompose","校園積水的大問題要如何開始？",["拆成位置、時間、降雨、排水與堵塞等可查的小問題","同時做所有測量不分主次","只拍一張照片就下結論","先選最熟悉的原因"],"A","A 把複雜問題拆成有資料和停止條件的小決定。"),
("stuck","探究卡住時最先做什麼？",["命名是資料缺失、變因太多、工具不合或概念不清，再選對應策略","只增加工作量","一直重複同一錯誤步驟","直接放棄所有問題"],"A","A 先診斷卡點，策略才能對準真正缺口。"),
("representation","冷卻表格看不出差異時，哪項做法合理？",["查時間與起始條件，再改畫時間—溫度圖或計算差值／速率","把數字四捨五入到產生差距","只挑最極端的一列","刪掉看不出差異的資料"],"A","A 用表示轉換改善判讀，不加工或挑選資料。"),
("monitor","研究過程中監控推理應問什麼？",["目前證據支持什麼、最大未知是什麼、下一步能改變哪個判斷","答案看起來像不像預期","報告頁數夠不夠","別人是否已經同意"],"A","A 把思考焦點放在證據、未知和下一步判準。"),
("ecology","鳥數每天不同，如何區分鳥的變動和觀察者影響？",["固定路線與時段重複觀察，記錄觀察者位置與天氣","隨意增加不同地點照片","直接宣布鳥變少","只用最清楚的一張照片"],"A","A 針對混淆因素設計可比較的重複觀察。"),
("stop","為小問題設定停止條件的作用是什麼？",["知道何時資料已足以回答該小問題，避免無限收集無關資料","保證答案一定正確","可以省略來源","讓所有問題同時結束"],"A","A 停止條件讓探究有焦點，也能說明仍有哪些未知。"),
("transfer","把冷卻研究策略遷移到生態觀察時，哪項不能直接照抄？",["要依新情境的對象、變因、資料、尺度與安全調整程序","保留背後比較和監測原理","重新定義指標和時間","檢查新情境限制"],"A","A 表面步驟需依新問題調整，遷移的是原理而非形式。"),
("evidence gap","哪項最能指出探究的最大證據缺口？",["說明哪個關鍵變因沒有測量、哪個來源不明或哪個比較條件未固定","只說資料太少","只說我不喜歡結果","把所有資料再印一次"],"A","A 將缺口具體化，才能設計有效下一步。"),
("strategy","若圖表無法回答原問題，最合理的策略是？",["回看指標與問題是否對齊，必要時重畫、補測或改寫問題","把標題改得更有信心","只增加顏色","刪除原問題"],"A","A 先檢查對齊關係，再用資料或表示調整，而非包裝問題。"),
("reflection","哪項最能表示探究策略真的遷移？",["在新情境保留原理，重新設定變因、資料、限制和安全，並說明為何改變步驟","完全複製原流程不解釋","只使用相同器材","把不同問題都叫同一名稱"],"A","A 有原理保留、情境調整和理由說明，才是可解釋的遷移。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以問題拆解、資料、方法、圖表、證據與遷移要求探究思考；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出探究思考核心「{topic}」。","列出問題、證據、卡點、表示、策略、停止條件與新情境限制。",f"逐項比對哪個選項有明確判準和可查證行動；正確答案是 {ans}。",f"核對理由：{exp}","最後說明如何監控下一步、保留原理並依新資料修正，不把忙碌或複製流程當成進展。"]
 return {"id":f"question-science-performance-t-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-t"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究探究策略、問題拆解、資料轉換與遷移能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-t","examPatternRefs":refs,"solutionStrategy":"先拆解問題並診斷卡點，再選資料、表示和策略，設定停止條件，最後檢查原理是否能遷移。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-t-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
