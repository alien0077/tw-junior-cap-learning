import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"questions/science"
SOURCES=[("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考","科學家、合作與證據能力方向"),("https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw","新北市立北投國民中學公開定期評量試題頁","探究分工、資料與方法能力方向"),("https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php","新北市立新埔國民中學公開段考試題頁","多元觀點、倫理與結論界線能力方向")]
DATA=[
("background","研究者背景最合理的作用是什麼？",["提供不同問題入口與觀察視角，再用共同方法檢查主張","直接決定答案正確與否","可用族群標籤代替資料","背景不同就不能合作"],"A","A 把背景視為問題視角來源，答案仍需透過可公開檢查的方法與資料建立。"),
("common practice","下列何者最能表現跨背景研究者共同的科學特質？",["公開方法、記錄資料、接受質疑並依證據修正","只相信最有名的人","把不同意見刪除","以直覺代替重複檢查"],"A","A 指向可追溯、可質疑和可修正的工作方式，不依賴名望或直覺。"),
("collaboration","城市熱島研究中，居民提供地點線索、測量組校正感測器、分析組比較材質，這表示什麼？",["不同貢獻可互補，但每項資料仍須標註方法與限制","只有分析組的工作算科學","合作後不必檢查資料","由人數最多的組決定結果"],"A","A 同時承認多角色貢獻與證據責任；合作不會免除方法檢核。"),
("conflict","跨實驗室結果不一致時，第一步較適合做什麼？",["比較定義、樣本、時間、單位、器材校正與程序","依職稱高低投票","刪除較不受歡迎的資料","只採用數字較大的結果"],"A","A 先尋找方法和背景差異，才能判斷是真實現象、偶然差異或程序不一致。"),
("stereotype","如何把『某類人天生比較會做科學』改成可研究且較公平的問題？",["不同教學資源是否影響學生使用同一測量程序的表現，並採公平取樣","哪一族群天生最聰明","直接相信刻板印象","不需要定義能力就比較"],"A","A 定義資源、程序、結果與取樣，避免把身分標籤當成固定能力。"),
("ethics","研究珊瑚礁時，哪項做法同時兼顧證據與責任？",["降低干擾、取得必要同意、記錄觀察限制並回饋受影響社群","為增加樣本任意搬動生物","隱藏不利資料以保護成果","只公布最漂亮的照片"],"A","A 將環境、社群與資料透明納入研究品質；成果不能以傷害或選擇性公開換取。"),
("contribution","若學生協助校正儀器卻未被列入貢獻紀錄，最適當的改進是？",["補記具體工作與責任，讓資料來源和研究貢獻可追溯","只列最有名的研究者","因為是學生就不必記錄","把所有人寫成同樣工作"],"A","A 透明記錄具體貢獻能追溯責任，也避免隱形勞動被忽略。"),
("evidence","在地居民指出魚群變少，研究團隊最適合如何使用這項知識？",["把它當作重要問題線索，再以固定地點、時間和計數方法檢查","直接當成已證明的因果結論","因為不是儀器資料就完全拒絕","只引用支持原想法的訪談"],"A","A 尊重在地觀察又不跳過共同方法，能把經驗轉成可檢查的研究設計。"),
("teamwork","小組成員對資料解讀不同時，哪種回應最符合共同科學特質？",["各自說明證據、方法與限制，必要時設計能區分解釋的重測","由聲音最大的人決定","把異議者排除","先決定結論再挑資料"],"A","A 讓分歧回到證據、方法和下一步測試，而非權力或排除。"),
("communication","向社區說明研究結果時，最完整的做法是？",["說明資料、方法、限制、受影響者與可行的回饋方式","只報告成功故事","用專業術語避免提問","隱藏不確定性讓居民安心"],"A","A 兼顧證據透明、限制與社群責任，讓受影響者能理解和回應。"),
]
def make(i,row):
 topic,prompt,choices,ans,exp=row
 refs=[{"url":u,"title":f"{t}；僅取能力方向，未複製原題、選項、圖表或答案。","year":"113-114","subject":"science","locator":loc,"observedPattern":"公開自然科評量常要求從觀察、合作、資料、方法、倫理與證據界線判讀科學工作；本題為獨立改寫。","reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc in SOURCES]
 steps=[f"讀題定位：圈出本題的科學工作核心「{topic}」。","分辨人物背景、合作分工、共同方法、證據品質與倫理責任。",f"逐項比對選項是否回到可檢查資料與公平程序；正確答案是 {ans}。",f"核對理由：{exp}","最後檢查是否把背景變成刻板印象、把權威代替證據，或忽略受影響者與資料限制。"]
 return {"id":f"question-science-performance-an-iv-3-{i}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":chr(65+j),"text":x} for j,x in enumerate(choices)],"knowledgeIds":["kg-science-performance-an-iv-3"],"difficulty":"medium","answer":{"value":ans,"explanation":exp+f" 正確答案：{ans}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三個公立國中公開自然科評量；僅研究科學家、合作、證據與倫理能力方向，不重製原題、選項、圖表或答案。","authoringNote":"依官方課綱 KG 與三個公立學校公開自然科評量來源能力方向獨立重寫；情境、選項、答案、解析與五步解題均為原創；待第二輪 AI/Terra 內容複核。"},"reviewStatus":"draft","updatedAt":"2026-09-21","lessonId":"lesson-science-performance-an-iv-3","examPatternRefs":refs,"solutionStrategy":"先分辨背景提供的視角與真正的證據，再檢查合作分工、方法透明、資料限制、倫理與社群責任。","solutionSteps":steps}
for i,row in enumerate(DATA,1): (OUT/f"question-science-performance-an-iv-3-{i}.json").write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"rewrote {len(DATA)} questions")
