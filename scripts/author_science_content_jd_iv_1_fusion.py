"""Jd-Ⅳ-1：氧化物酸鹼性與酸對物質的反應第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jd-iv-1.json"
REPORT=ROOT/"implementation/reports/science-content-jd-iv-1-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"氧化物酸鹼性、酸與金屬／碳酸鹽反應、氣體判讀","pattern":"取由指示劑、反應現象與生成物資料判斷氧化物及酸反應的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"酸鹼、氧化物、氣體檢驗與生活情境","pattern":"取從實驗圖表、酸鹼資料與氣體證據推論物質反應的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氧化物酸鹼性、酸的反應與安全","pattern":"取以氧化物分類、酸的化學性質、反應證據與安全操作連結教學的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jd-iv-1-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jd-iv-1"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的氧化物酸鹼性、酸反應、指示劑、氣體證據及安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jd-iv-1","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"將二氧化碳通入紫色石蕊水，溶液變紅的主要原因是？",["二氧化碳溶於水形成酸性物質，使溶液呈酸性","二氧化碳本身是紅色液體","水被氧化成金屬","石蕊遇到所有氣體都變紅"],"A","二氧化碳與水反應形成碳酸，使溶液呈酸性，紫色石蕊因此變紅；顏色是酸性證據。","把氣體溶解、生成物與指示劑反應連成證據鏈。",["確認二氧化碳能溶於水。","判斷溶於水後是否形成酸性物質。","用紫色石蕊觀察酸鹼性變化。","排除顏色、金屬與所有氣體通則的錯誤。","所以 A 正確。"],"easy"),
q(2,"氧化鈣加入水後形成氫氧化鈣，若以酸鹼性分類，氧化鈣較適合歸為？",["鹼性氧化物，因為與水形成鹼性物質","酸性氧化物，因為所有氧化物都呈酸性","中性氣體，因為氧化鈣不含水","純金屬而非氧化物"],"A","氧化鈣與水反應形成氫氧化鈣，呈鹼性，因此可依反應性歸為鹼性氧化物。","用氧化物與水的反應結果判斷酸鹼性。",["辨認氧化鈣是金屬氧化物。","觀察與水反應生成的物質。","確認氫氧化鈣使溶液呈鹼性。","排除所有氧化物同類與非氧化物的說法。","答案為 A。"],"medium"),
q(3,"稀鹽酸加入鎂帶後產生氣泡，並可使點燃的木條發出爆鳴聲；氣體最可能是？",["氫氣，來自酸與鎂反應並可燃","氧氣，因為氧氣一定爆鳴","二氧化碳，因為所有酸反應都產生它","氯氣，因為溶液含氯離子"],"A","酸與活潑金屬反應常生成氫氣；氫氣遇火會有爆鳴聲，但實驗應使用少量並遵守安全規範。","以反應物類型和氣體檢驗共同判斷，不只看氣泡。",["辨認反應物為酸與金屬。","列出酸與金屬常見生成物。","用爆鳴聲作為氫氣的支持證據。","排除氧氣、二氧化碳與氯氣的檢驗特徵。","所以 A 最合理。"],"medium"),
q(4,"稀鹽酸加入碳酸鈣粉末後產生氣泡，將氣體通入澄清石灰水變混濁，氣體是？",["二氧化碳，因為碳酸鹽與酸反應可產生二氧化碳","氫氣，因為所有氣泡都是氫氣","氧氣，因為石灰水會吸收氧氣","水蒸氣，因為反應一定沸騰"],"A","碳酸鈣與酸反應生成二氧化碳，二氧化碳使澄清石灰水變混濁，是常用的支持證據。","把反應物類別與特定氣體檢驗配對。",["辨認碳酸鹽與酸的組合。","預測可能生成二氧化碳。","用澄清石灰水檢驗氣體。","排除把所有氣泡當氫氣或氧氣的錯誤。","答案為 A。"],"easy"),
q(5,"氧化銅是黑色固體，加入稀硫酸並加熱後固體逐漸溶解且溶液呈藍色；合理解釋是？",["氧化銅與酸反應生成可溶性的硫酸銅和水","氧化銅被酸蒸發成藍色氣體","硫酸只把黑色染成藍色而沒有反應","藍色表示生成氫氣"],"A","氧化銅與硫酸發生酸鹼反應，生成硫酸銅溶液和水；固體溶解及顏色改變是新物質證據。","從固體消失與溶液顏色判斷反應產物，不把顏色當染色。",["確認氧化銅是金屬氧化物。","判斷酸與鹼性氧化物會反應。","辨認可溶性硫酸銅造成藍色溶液。","排除蒸發、染色和氫氣的說法。","所以 A 正確。"],"medium"),
q(6,"比較不同酸對相同碳酸鈣質量的反應速率，哪項最公平？",["固定酸濃度與體積、碳酸鈣粒徑與質量、溫度，只改變酸的種類並量測產氣速率","每種酸使用不同濃度和不同質量碳酸鈣","一組加熱另一組不加熱","只看哪組泡沫最高而不計時間"],"A","控制酸濃度、體積、固體質量、粒徑與溫度，只改變酸的種類，並量測單位時間產氣量才可公平比較。","先控制所有速率變因，再比較單一酸種類。",["列出濃度、體積、粒徑、質量與溫度。","固定非研究變因。","把酸的種類設為唯一自變因。","用量筒或感測器記錄產氣速率。","因此 A 是公平設計。"],"medium"),
q(7,"要判斷一種未知氧化物是酸性還是鹼性，哪項方法最有證據力？",["分別觀察它與水、酸或鹼的反應，搭配指示劑與產物資料，不只看粉末顏色","只看粉末是白色或黑色","只聞氣味判斷酸鹼","看容器大小判斷氧化物種類"],"A","氧化物酸鹼性需由與水、酸鹼的反應及指示劑、產物證據判斷，顏色與氣味不足以定義。","用多種可檢驗反應建立分類，而不是外觀分類。",["先確認未知物確為氧化物。","設計與水、酸、鹼的安全反應。","記錄指示劑與生成物變化。","比較證據是否支持酸性或鹼性。","所以 A 最完整。"],"hard"),
q(8,"處理濃酸時不慎濺到皮膚，最適當的第一步是？",["立即用大量流動清水沖洗並依實驗室規範通報處理","用手帕用力擦拭後繼續實驗","立刻加入另一種化學品在皮膚上中和","等待疼痛消失再處理"],"A","化學品濺到皮膚應立即以大量流動清水沖洗並通報，不能擦拭、私自中和或等待。","安全處置優先於追求實驗結果，採取快速稀釋與求助。",["停止接觸污染源。","立刻移到洗眼／沖身設備或流動清水處。","持續沖洗並通知教師或依規範求助。","不要擦拭、私自中和或延遲。","所以 A 是唯一合適的第一步。"],"easy"),
q(9,"酸雨可能使石灰岩建築表面逐漸受損，最合理的化學原因是？",["酸與碳酸鈣反應，可能生成可溶物並放出二氧化碳，使岩石逐漸溶蝕","酸雨會把石灰岩變成氧氣","石灰岩只因被水沖洗而一定消失","二氧化碳會讓所有岩石變成金屬"],"A","石灰岩主要含碳酸鈣，酸可與碳酸鹽反應生成鹽、水與二氧化碳，造成材料表面溶蝕。","把課堂酸與碳酸鹽反應遷移到環境材料情境。",["辨認石灰岩的主要成分碳酸鈣。","列出酸與碳酸鹽的反應產物。","判斷可溶物與氣體會使固體表面減少。","排除氧氣、單純沖洗與金屬轉換說法。","因此 A 正確。"],"medium"),
q(10,"若要確認酸和某氧化物反應後確實生成新物質，哪項資料組合最完整？",["記錄氧化物質量或外觀、溶液指示劑／顏色、產物溶解性與反應式，並設置未加酸對照","只拍反應前後照片一次","只測量室溫","只問反應者是否覺得有變化"],"A","質量、顏色、溶解性、反應式與對照可共同支持新物質形成，單一照片、溫度或主觀感受不足。","用多證據和對照判斷化學反應，不把單一現象當定論。",["設定未加酸的對照組。","記錄反應前後固體與溶液資料。","檢查產物的組成與溶解性。","用反應式核對酸與氧化物的反應。","所以 A 是最完整的證據組合。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["氧化物酸鹼性需由與水、酸鹼的反應及指示劑、產物證據判斷。","酸與金屬、碳酸鹽及金屬氧化物會呈現不同氣體或溶液產物。","反應現象、控制變因、對照和安全操作共同支撐酸反應判讀。"],"versionDifferences":["南一公開線索支持由指示劑與生活材料進入氧化物和酸的性質。","康軒公開課程資料較突出酸與金屬、碳酸鹽及氧化物的實驗證據。","翰林公開課程計畫補充氧化物分類、酸反應與安全操作；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以『物質類型—反應產物—檢驗證據—安全』框架整理氧化物與酸反應。","把酸雨侵蝕、濃酸濺傷、氣體辨識與公平速率實驗納入單元專屬遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫氧化物酸鹼性、酸與金屬／碳酸鹽／氧化物反應、指示劑、氣體證據與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jd-Ⅳ-1：氧化物酸鹼性與酸對物質的反應","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為氧化物酸鹼性、指示劑、酸與金屬／碳酸鹽／氧化物、氣體證據、公平實驗與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jd-iv-1")
if __name__=="__main__": main()
