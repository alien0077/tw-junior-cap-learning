import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","測量、變因與證據能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","觀察、方法與資料判讀能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","實驗設計、誤差與結論界線能力方向")]
DATA=[
 ("operational definition","研究紙橋承重時，哪項定義最適合讓不同小組比較？",["以第一次橋面明顯下陷前所承受的砝碼總質量記錄","看起來很穩就記高分","只寫成功或失敗","由組長決定哪次最好"],"A","A 指定可觀察失效現象、數值和停止條件，能由不同小組依同一標準記錄。"),
 ("unit","下列哪項最能避免冷卻測量的數字失去意義？",["記錄溫度時同時寫攝氏度、讀值時間與器材型號","只寫 32，不寫單位","把不同單位的數字直接平均","把小數位增加到十位"],"A","A 保留單位、時間和器材資訊；無單位或任意增加小數都不能提高測量意義。"),
 ("procedure","要比較兩杯熱水的冷卻速度，哪項程序最公平？",["固定水量、容器、起始溫度與位置，每兩分鐘讀值一次","一杯放窗邊，另一杯放桌內並自由讀值","先看結果再決定讀幾次","只挑下降最多的一段"],"A","A 固定可能影響冷卻的條件並統一讀值時間，才能將差異與比較因素連結。"),
 ("parallax","讀取量筒液面時，哪個做法最能減少視線造成的差異？",["眼睛與液面同高，依同一刻度規則讀取並記錄單位","從上方俯視比較容易","每人從自己習慣的角度讀","只保留看起來順眼的數字"],"A","A 統一視線與讀值規則，能降低視差；不同角度會讓同一液面產生不同讀值。"),
 ("repeat","紙橋每種設計要重複測量的主要理由是什麼？",["觀察偶然差異並比較典型表現，而不是只依一次結果","保證結果完全沒有誤差","讓表格看起來更大","可以不記錄失效條件"],"A","A 能估計偶然波動，但不能保證零誤差，也不能取代清楚的失效定義與原始紀錄。"),
 ("raw data","測量中途溫度計曾離開水中，最適當的紀錄方式是？",["保留原始讀值並標註異常與時間，不把缺值補成理想曲線","刪掉整組資料且不說原因","補一個符合趨勢的數字","只留下最後平均值"],"A","A 保留可追溯性並誠實揭露異常；補造或隱藏資料會破壞證據。"),
 ("resolution","溫度計最小刻度為 1°C，哪項結論較恰當？",["報告讀值的解析度限制，不宣稱能分辨 0.1°C 的差異","把 23 寫成 23.000°C 就能更準","所有小差異都確定是真實變化","刻度不重要，只看趨勢"],"A","A 讓結論符合器材能力；增加小數位不會創造不存在的解析度。"),
 ("method difference","兩組量影子長度結果不同，第一個應檢查什麼？",["比較兩組的起點、方向、時間、單位與遮蔽物，再判斷是否是方法差異","立刻宣稱其中一組造假","只採用較大的數字","刪除兩組不一致的結果"],"A","A 先查方法與環境條件，才能區分現象差異和測量程序差異。"),
 ("safety","使用重物測紙橋時，哪項做法符合方法與安全共同標準？",["逐步加重、保持手腳避開下方並記錄失效時刻","一次堆到最高以節省時間","為了數據爬到桌上加重","橋塌後仍繼續加重不管碎片"],"A","A 同時處理可重複加重、失效紀錄與人員安全；探究不能凌駕安全界線。"),
 ("conclusion","同一紙橋只測一次承重 420 克，哪項結論不超過證據？",["在這次測試條件下記錄到 420 克，仍需重複測試才能比較穩定表現","所有同型紙橋都一定承重 420 克","紙橋永遠比木橋強","420 克證明設計沒有任何限制"],"A","A 限定本次條件並承認需要重複；單次結果不能無限推廣。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常要求以觀察、測量、方法、資料與誤差界線判讀探究設計；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出本題的測量核心「{topic}」。","列出對象、操作型定義、單位、器材、時間、控制條件與安全限制。",f"逐項比對程序是否能產生可重複資料；正確答案是 {ans}。",f"核對理由：{exp}","最後檢查結論是否受器材解析度、異常、重複次數與樣本範圍限制。"]
 return {"id":f"question-science-performance-an-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-an-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究測量、方法與證據能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-an-iv-1","examPatternRefs":refs,"solutionStrategy":"先把模糊觀察轉成共同定義，再檢查單位、器材、程序、重複、異常、安全與結論範圍。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-an-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
