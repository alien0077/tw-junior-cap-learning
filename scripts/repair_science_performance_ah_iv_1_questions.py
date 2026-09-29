import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","科學報導、資料與證據能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","圖表、來源與因果判讀能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","查證、方法與結論界線能力方向")]
DATA=[
("claim","看到『研究顯示產品七天有效』時，第一步最適合做什麼？",["找原始研究並確認對象、比較組、結果、時間與方法","只看標題和轉發數","只相信廣告中的專家照片","直接把效果推論到所有人"],"A","A 把宣稱拆回可查證的研究設計；標題、轉發數或照片不能代替樣本和對照。"),
("source","下列哪項最能評估科學報導的來源品質？",["查作者、原始資料、研究日期、方法、同行檢視與利益關係","看文章用了多少驚嘆號","看網站是否有華麗版面","看留言區是否一致支持"],"A","A 同時檢查可追溯性、方法與可能偏差，較不會被形式或聲量誤導。"),
("causation","冰淇淋銷量和溺水事件同時上升，最恰當的判斷是？",["可能受炎熱天氣共同影響，不能只因同時上升就宣稱冰淇淋造成溺水","已證明冰淇淋造成溺水","兩者一定完全無關","只要畫成兩條線就能證明因果"],"A","A 區分相關和因果，需檢查共同因素、時間、研究設計與其他證據。"),
("chart","圖表縱軸只從 29°C 畫到 30°C，兩條線看起來差距很大，讀者應先做什麼？",["查完整座標、單位、實際差值、時間與樣本數","直接用斜率說暴增十倍","只看顏色鮮豔的線","把圖形大小當成測量值"],"A","A 先回到數值和背景，避免截斷座標放大視覺差異。"),
("sample","一篇報導以 8 位志願者的結果宣稱所有青少年都會受益，主要問題是？",["樣本少且代表性與外推範圍不足，不能直接推及所有青少年","人數越少越能代表所有人","只要結果漂亮就不需樣本","志願者一定不能做研究"],"A","A 指出樣本量、選樣與外推限制；小樣本不是必然無效，但不能無條件廣推。"),
("video","網路影片顯示磁鐵旁植物長得較快，但沒有控制組和完整方法，最恰當的說法是？",["它是值得查證的線索，尚不足以單獨證明磁鐵造成生長差異","影片看得到就已證明因果","因為是影片所以永遠不能研究","直接把結果推廣到所有植物"],"A","A 保留線索價值並守住因果證據界線，下一步需控制條件、重複與記錄。"),
("authority","專家說法與原始資料看似不一致時，應如何處理？",["查專家說法的適用條件、原始資料品質與是否其實回答不同問題","只因專家身分就刪除資料","只選與自己看法相同的一方","把兩者平均成一個答案"],"A","A 把權威和資料都放回方法、問題與範圍檢查，不用頭銜或偏好代替分析。"),
("interest","研究由產品公司資助，這代表什麼？",["是需要揭露並檢查研究設計、資料與是否有其他獨立研究的查核線索，不等於自動證明造假","只要有資助結果必然錯","有資助就不必讀方法","公司資助反而保證結果正確"],"A","A 正確處理利益關係：它提醒讀者查偏差，但不能單獨取代證據判定。"),
("counterevidence","看到一個反例與報導結論不同時，先做什麼？",["查反例的條件、測量、樣本與重複，再判斷是限制、誤差或真正矛盾","立即宣稱報導完全虛假","刪掉反例以維持結論","只看誰的追蹤者較多"],"A","A 先分析條件和資料品質，才可判斷反例如何影響原主張。"),
("conclusion","完整查核後仍只有一項小型研究，哪句結論較負責任？",["在該研究樣本與條件下觀察到可能效果，仍需更大或獨立研究確認","已證明對所有人有效","研究不大所以任何說法都一樣","權威報導因此不用補資料"],"A","A 限定樣本與條件並提出後續驗證，不誇大也不把未知等同任意。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以來源、圖表、樣本、因果、方法與證據界線要求判讀科學報導；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出科學報導查核核心「{topic}」。","把主張拆成來源、方法、樣本、比較、結果、時間、利益與限制。",f"逐項比對哪個選項最符合查證原則；正確答案是 {ans}。",f"核對理由：{exp}","最後檢查是否混淆相關與因果、權威與證據，並寫出需要的下一個查證行動。"]
 return {"id":f"question-science-performance-ah-iv-1-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-ah-iv-1"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究報導查核、資料判讀與證據能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-ah-iv-1","examPatternRefs":refs,"solutionStrategy":"先拆解主張，再查來源、方法、樣本、圖表、利益、因果與限制，最後提出可驗證的下一步。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-ah-iv-1-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
