import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","探究檢核、資料與改善能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","變因、異常、結論與再測能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","證據界線、資料品質與方法改善能力方向")]
DATA=[
("alignment","研究澆水量對葉片數的影響，卻只記錄植株高度，第一個問題是？",["指標與原問題不一致，資料不能直接回答葉片數問題","高度一定比葉片數更科學","只要圖表漂亮就能回答","把高度換算成葉片數即可"],"A","A 指出問題、指標和測量沒有對齊，不能靠換算或圖表外觀補足。"),
("raw data","測量中途漏記兩次，最適當的改善是？",["保留缺值與異常，補做相同條件測量並記錄補測原因","用平均值猜回缺失數字","刪掉整組資料不說明","只留下最符合趨勢的數字"],"A","A 保留可追溯性並用補測降低缺口，避免捏造或選擇性刪除。"),
("conclusion","兩地各測一次後寫『圖書館永遠比操場安靜』，主要問題是？",["樣本、時段與條件太窄，結論超出證據能支持的範圍","一次測量足以代表所有日子","永遠是科學常用的限定詞","地點比較不能做"],"A","A 限制樣本與推廣範圍，應改成條件式結論並增加重複觀察。"),
("method","兩組植物結果不同時，先查哪一項最有幫助？",["品種、初始狀態、光照、水量定義、時間、測量與重複","只查哪組的結論較漂亮","直接把兩組平均","刪除較小的結果"],"A","A 能定位背景和程序差異，才知道是現象、偶然波動或方法問題。"),
("improvement","哪項是可驗證的探究改善？",["固定測量時間並增加重複，預先寫出資料變異應如何改變","把答案改得更肯定","購買最貴器材但不改程序","刪除異常值讓平均變好"],"A","A 有明確程序改動、預期指標與再測方式，能檢查改善是否有效。"),
("control","隔熱杯比較時，一組量手感、一組量溫度，應如何改善？",["統一可操作的溫度指標、讀值時間、器材與重複程序","把手感分數直接當攝氏度","只採用最冷的一組","不必記錄單位"],"A","A 統一指標和程序，讓各組真的測量同一問題。"),
("error","溫度計未校正可能造成什麼問題？",["各次讀值可能有系統偏差，應先校正或記錄限制再解讀差異","只會讓資料看起來更精確","一定只影響一次讀值","只要增加小數位就能消除"],"A","A 說明系統偏差與校正必要性，小數位不能修復未校正器材。"),
("evidence boundary","一次觀察發現隔熱杯 A 較熱，哪個結論最恰當？",["在本次條件與測量下 A 讀值較高，仍需重複確認是否穩定","A 在所有環境一定最好","A 已證明沒有任何缺點","結果不同代表測量都錯"],"A","A 限定條件並保留重複需求，沒有把單次結果無限推廣。"),
("peer review","同儕審查探究紀錄時，哪項回饋最有用？",["指出資料支持與不足之處、最大缺口及一項可再測的改善","只說很棒不提證據","直接替作者改答案","只挑錯字不看方法"],"A","A 將回饋連到證據和可驗證改善，而非空泛稱讚或代寫結論。"),
("next test","改善後要如何判斷方法真的變好？",["預先指定資料完整度、重複穩定性或誤差降低的指標，再比較改善前後","只看報告頁數變多","只看結論更肯定","刪掉改善後不理想的資料"],"A","A 以預先指定指標比較改善前後，避免事後挑選成功證據。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以探究流程、資料品質、證據界線與方法改善要求學生檢核結果；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出探究檢核核心「{topic}」。","對照原問題、變因、指標、資料、程序、結論與限制。",f"逐項比對哪個選項真正能改善證據品質；正確答案是 {ans}。",f"核對理由：{exp}","最後寫出如何再測與哪個指標能證明改善有效，不能用重算或刪資料掩蓋缺口。"]
 return {"id":f"question-science-performance-pc-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-pc-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究探究檢核、資料、證據界線與改善能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-pc-iv-1","examPatternRefs":refs,"solutionStrategy":"先對齊問題與指標，再查原始資料、程序、異常、結論範圍與改善是否可驗證。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-pc-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
