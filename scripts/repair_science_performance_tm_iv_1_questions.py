import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","模型、資料與預測能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","尺度、假設與探究應用能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","模型評估、證據與限制能力方向")]
DATA=[
("purpose","使用水循環圖前最重要的問題是？",["它要表示哪個流程、忽略哪些細節以及能回答什麼問題","哪張圖最像照片","箭頭長度就是真實流速","圖越複雜越正確"],"A","A 把模型放回目的與簡化條件，避免把圖解外觀當自然本身。"),
("scale","球棒模型顯示分子位置時，為何不能直接用它判斷真實大小？",["模型改變了尺度與比例，只保留特定結構關係","球棒一定沒有科學用途","分子不能被任何模型表示","只要顏色正確就代表大小正確"],"A","A 指出尺度簡化和模型用途的關係。"),
("assumption","肺部球囊模型最適合說明什麼？",["胸腔體積變化與氣體進出方向，不能代表所有微觀交換","肺泡全部化學反應","真實肺部完整比例","每種氣體的精確濃度"],"A","A 限定類比能支持的部分，避免把模型當完整機制。"),
("validation","模型預測和觀察不同時，第一步較適合做什麼？",["檢查輸入、參數、測量條件與模型假設，再決定修正範圍","刪除不符合的資料","宣布模型完全無用","只挑符合的案例"],"A","A 先分析差異來源，再依證據修正或縮小模型。"),
("moon","桌面月球模型無法同時保留大小和距離，最合理的做法是？",["說明選擇的比例與目的，標示被犧牲的尺度並用觀測日期檢查預測","假裝所有比例都真實","因為不完美就不用模型","只選看起來漂亮的擺法"],"A","A 讓尺度取捨透明，並用資料檢查模型仍能回答的問題。"),
("representation","要呈現水在各環境庫之間流動，哪種模型較合適？",["標示箭頭、庫存、轉移條件與時間的流程圖，再說明未呈現的細節","只放一張雲的照片","只列名詞不畫關係","用動畫速度代表真實時間"],"A","A 形式與流程問題對齊，同時標示變數與限制。"),
("parameter","疾病模型中的接觸率改變，預測曲線不同，應如何解讀？",["先說明參數與假設，再用實際資料比較哪種條件較符合","曲線最高的一定是真實未來","參數只是裝飾不能改","只看模型畫面不看資料"],"A","A 把參數和證據連結，避免將模擬結果當保證。"),
("counterexample","模型在小尺度有效，換到大尺度出現落差，最恰當的結論是？",["檢查尺度和省略因素，保留原範圍有效部分並修正外推限制","所有小尺度結果都錯","直接把大尺度資料刪掉","模型只要成功一次就能到處用"],"A","A 以適用範圍和證據處理落差，不全盤否定或過度外推。"),
("model quality","評估模型好不好，最重要的依據是？",["是否符合目的、假設透明、能提出可檢查預測且與資料比較","外觀是否逼真","名稱是否專業","投影片是否華麗"],"A","A 以用途、透明假設、預測和資料檢查模型品質。"),
("revision","模型不符合資料時，哪項做法最科學？",["保留原始資料，查方法與假設，提出修正版並說明新的適用範圍","修改資料使模型成立","直接換成最新模型不比較","宣布自然現象無法理解"],"A","A 讓模型修正可追溯、可檢驗並保留仍有效的部分。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以模型、尺度、假設、預測、資料與限制要求推理；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出模型判讀核心「{topic}」。","列出模型目的、尺度、假設、變數、預測、資料與適用範圍。",f"逐項比對哪個選項不超出模型能力；正確答案是 {ans}。",f"核對理由：{exp}","最後檢查是否把模型當自然本身，並寫出可用資料驗證或修正的下一步。"]
 return {"id":f"question-science-performance-tm-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-tm-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究模型、尺度、假設、預測與限制能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-tm-iv-1","examPatternRefs":refs,"solutionStrategy":"先確認模型目的與尺度，再檢查假設、預測、資料、限制與修正範圍。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-tm-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
