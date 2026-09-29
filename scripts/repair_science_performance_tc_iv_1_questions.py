import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","數據懷疑、資料與解釋能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","測量、異常與替代解釋能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","資訊查證、風險與結論界線能力方向")]
DATA=[
("observation","雨量表突然出現極端值，第一步最適合做什麼？",["確認單位、日期、位置、器材與附近資料，再列可能解釋","直接宣布一定故障","直接宣布一定是真暴雨","刪掉極端值讓平均好看"],"A","A 先描述與查條件，保留真實事件、器材問題或輸入錯誤等可能。"),
("sensor","兩支手機同時顯示不同室溫，最合理的查證是？",["比較位置、陽光、外殼、感測器與校正，再用標準工具重測","只相信較高的數字","把兩數平均當真值","把一支手機貼到另一支上"],"A","A 能區分環境、器材和校正造成的差異，不能由一次畫面決定原因。"),
("definition","食品標示寫『天然所以安全』，應先拆開哪些概念？",["天然的來源、成分與劑量，及安全的適用者、風險與研究證據","只查包裝顏色","只看消費者按讚數","把天然直接當安全"],"A","A 把模糊語句轉成可查證的成分、劑量、族群和證據問題。"),
("alternative","觀察到水池泡沫增加，哪項做法最符合合理懷疑？",["列出清潔劑、降雨攪動與藻類等解釋，再設計能區分它們的採樣","直接認定有人倒清潔劑","只找支持污染的照片","因為有三種解釋所以都是真的"],"A","A 讓替代解釋接受可比較查證，不把可能性當結論。"),
("missing metadata","圖表沒有單位和時間，最適當的判斷是？",["資料暫不足以支持強結論，先補查單位、期間、來源與測量方法","數字越大一定越嚴重","圖表有顏色就足夠","直接用自己的單位解讀"],"A","A 指出關鍵背景缺口，沒有單位和時間不能可靠比較。"),
("outlier","一筆數值遠離其他測量時，哪項處理最恰當？",["保留並檢查原始紀錄、器材、條件與重測，不可未查證就刪除","直接刪掉離群值","把它改成平均值","只用它證明新理論"],"A","A 先查異常來源與真實變異，再決定如何在結論中呈現。"),
("evidence","哪項資料最能區分兩個可能解釋？",["兩個解釋對結果預測不同，且能在相同條件下重複測量的資料","只找支持其中一個的文章","詢問哪個故事比較合理","用投票決定"],"A","A 資料必須能讓預測分開並可重做，才有判別力。"),
("risk","健康資訊只引用一個小型研究，負責任的說法是？",["在該研究樣本與條件下有初步結果，仍需更多資料確認風險與效果","已證明對所有人安全","因為研究小所以完全沒有價值","只要專家轉發就確定"],"A","A 同時承認線索和樣本限制，不把初步資料擴大。"),
("source","網路圖表標示『最新研究』但沒有原始連結，下一步是？",["查作者、日期、原始研究、資料定義與方法，再判斷能否引用","直接轉傳給同學","只看分享數","自行補一個來源"],"A","A 先恢復可追溯來源，避免用模糊權威語氣代替證據。"),
("conclusion","查證仍無法區分兩個解釋時，最恰當的結論是？",["說明目前資料不足、保留兩種可能，提出下一個能區分的觀察","選最符合直覺的解釋","把兩種解釋平均成一個","宣布科學無法回答任何問題"],"A","A 誠實表達不確定性並保留可檢驗的下一步。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以資料來源、異常、測量條件、替代解釋與結論界線要求合理懷疑；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出數據查核核心「{topic}」。","先分辨直接觀察、測量條件、解釋、風險與價值語句。",f"逐項比對哪個選項能提出可查證的合理懷疑；正確答案是 {ans}。",f"核對理由：{exp}","最後寫出仍缺少的資料、能區分解釋的下一步，以及目前結論不可超出的範圍。"]
 return {"id":f"question-science-performance-tc-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-tc-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究數據懷疑、資訊查證與替代解釋能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-tc-iv-1","examPatternRefs":refs,"solutionStrategy":"先描述資料與異常，再查來源條件、提出替代解釋，最後設計能區分解釋的重測與條件式結論。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-tc-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
