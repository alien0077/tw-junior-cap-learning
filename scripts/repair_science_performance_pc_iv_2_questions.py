import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","探究表達、圖表與證據能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","資料整理、溝通與受眾能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","科學論證、限制與責任表達能力方向")]
DATA=[
("audience","同一份河川資料給居民和研究小組閱讀，最合理的做法是？",["依受眾調整詞彙與形式，但保留相同證據、來源、單位與限制","給居民看就刪除所有不利結果","給研究小組只放漂亮圖片","不同受眾使用不同答案"],"A","A 允許溝通形式不同，但證據責任不能因受眾而改變。"),
("graph","植物高度比較圖表至少應標示哪些項目？",["標題、座標、單位、時間、樣本數、變異與資料來源","只要顏色和大標題","只畫平均線不寫單位","只放最高值"],"A","A 讓讀者能重建比較、理解變異並追查資料。"),
("claim-evidence","哪項最能把結論和資料連接起來？",["主張後指出對應數據、比較方法、推理與限制","只說結果支持我","把標題寫得更肯定","只列一串數字不解釋"],"A","A 形成主張—證據—推理—限制的完整鏈結。"),
("format","要呈現河川污染隨月份的變化，哪種形式最合適？",["有時間軸、單位、圖例和來源的折線圖，並配文字說明限制","只用一張最嚴重時的照片","用口號取代數值","把月份順序打亂增加設計感"],"A","A 圖表形式與變化問題對齊，同時保留查證資訊。"),
("accessibility","噪音海報只用紅綠色區分高低，最需要補什麼？",["數值、文字標籤、圖例、單位與替代文字，避免只靠顏色理解","更多漸層顏色","把字縮小塞入更多資料","刪除圖表改成口號"],"A","A 同時改善可及性與證據閱讀，不讓色覺或設備差異阻斷理解。"),
("uncertainty","口頭報告要如何負責任地表達一次測量結果？",["說明條件、樣本、變異與限制，不把一次觀察說成普遍定律","用更有自信的語氣掩蓋限制","刪掉不確定性避免追問","只報告最好的數字"],"A","A 保留不確定性，讓口頭形式仍符合證據界線。"),
("source","探究成果中的資料來源應如何呈現？",["標示來源、日期、資料範圍與必要的取得方式，讓讀者能追查","只寫網路上找到的","只列最有名的作者","來源不重要因為是自己的圖"],"A","A 讓原始資料和轉製圖表可追溯，避免無法核對。"),
("model","用模型解釋河川水流時，報告還應說明什麼？",["模型假設、適用範圍、忽略因素與它能支持的推論","只展示最逼真的畫面","宣稱模型就是現實","刪除模型不符合的觀察"],"A","A 讓讀者知道模型用途和限制，不把表現形式當成真實本身。"),
("feedback","同學看不懂圖表時，最有用的修正方式是？",["詢問卡住的位置，補上標題、單位、圖例或文字說明，再請讀者重看","只責怪讀者不夠專心","加入更多顏色","把資料全部刪掉"],"A","A 把回饋轉成可檢查的表達改善，而不是把理解責任推給讀者。"),
("completeness","什麼情況才可稱為完整的探究成果表達？",["問題、方法、資料、分析、結論、限制、來源與受眾形式彼此對齊","投影片頁數最多","把所有原始資料無分類貼上","只留下最後答案"],"A","A 完整是證據鏈和溝通條件對齊，不是資料或頁數越多越好。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常以資料整理、圖表、證據、結論、受眾與限制要求表達探究成果；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出科學表達核心「{topic}」。","列出受眾、目的、問題、資料、形式、來源、限制與可及性要求。",f"逐項比對哪個選項讓讀者能理解並查證；正確答案是 {ans}。",f"核對理由：{exp}","最後檢查形式是否掩蓋變異、刪除限制或讓讀者無法追查，必要時提出修正。"]
 return {"id":f"question-science-performance-pc-iv-2-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-pc-iv-2"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究多形式表達、圖表、證據與責任溝通能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-pc-iv-2","examPatternRefs":refs,"solutionStrategy":"先確認受眾和目的，再檢查形式是否保留問題、資料、單位、來源、限制、推理與可及性。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-pc-iv-2-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
