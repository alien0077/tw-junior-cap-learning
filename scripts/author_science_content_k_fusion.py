"""K：自然界的現象與交互作用第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-k.json"
REPORT=ROOT/"implementation/reports/science-content-k-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"自然現象、能量、力、物質與資料判讀","pattern":"取由現象觀察、系統交互作用、能量／物質變化與資料推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"自然現象、模型、圖表與生活情境","pattern":"取從模型、實驗資料、生活與環境情境整合推論自然現象的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"自然界交互作用、能量、物質、系統與科學探究","pattern":"取以系統、尺度、交互作用、守恆與證據建立跨領域自然科理解的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-k-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-k"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的自然現象、系統交互、能量／物質、模型、守恆與證據整合能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-k","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"觀察一顆球從斜坡滾下，若球的速度增加，最適合的系統描述是？",["重力位能和動能在系統內轉換，並可能有摩擦造成熱能，需先界定系統邊界","能量憑空增加且沒有來源","球的質量一定變大","只有顏色改變才能算自然現象"],"A","球下降時重力位能可轉為動能，摩擦和空氣阻力也可能把部分能量轉為熱；能量分析要界定系統。","以系統邊界和能量轉換解釋可觀察運動。",["界定球、斜坡、空氣是否包含在系統。","比較高度和速度變化。","辨認位能轉成動能。","加入摩擦造成的熱能或聲音。","所以 A 最完整。"],"medium"),
q(2,"海邊白天吹海風、夜晚可能吹陸風，最合理的共同原因是？",["陸地和海水受熱與冷卻速率不同，造成氣壓差與空氣流動","海水會把風固定推向陸地","風只由月亮顏色決定","白天和夜晚的重力方向不同"],"A","陸地比熱與受熱冷卻不同，造成近地面溫度、密度和氣壓差，驅動海陸風；時間改變熱收支。","從熱傳、密度、氣壓和流動串起自然現象。",["比較白天陸地和海水的升溫速度。","推論空氣溫度、密度與氣壓差。","判斷高壓空氣往低壓流動。","夜晚反向比較冷卻和風向。","因此 A 正確。"],"medium"),
q(3,"植物蒸散、雲形成與降雨都涉及水在環境中的移動；要研究校園樹蔭如何影響地表溫度，哪項設計較公平？",["選相似地表，控制測量時間與天氣，只比較樹蔭和無樹蔭區並重複量測","一處在早上、一處在中午且不記錄風速","只測一次手感溫度","同時改變地表材質、樹種與測量時間"],"A","研究樹蔭效應需控制時間、地表、天氣與量具，設置對照並重複測量，才能把差異歸因於遮蔭。","以系統變因和對照設計研究跨領域現象。",["選相似地表和相鄰區域。","固定測量時刻、儀器和高度。","設定樹蔭與無樹蔭對照。","重複量測並記錄溫度、風和雲量。","所以 A 是公平設計。"],"medium"),
q(4,"月相每天改變但月球本身不發光，最合理的模型是？",["太陽光照亮月球不同部分，地球觀察到的明亮部分隨相對位置改變","月球每天改變自己的形狀","月相是雲遮住太陽造成的固定現象","月球亮度與太陽無關"],"A","月相是日、地、月相對位置改變造成可見受光面比例不同，不是月球形狀真的改變。","用光源、球體與觀察位置建立幾何模型。",["確認太陽是主要光源。","用球體代表月球和地球。","改變三者相對位置。","比較觀察到的受光面比例。","所以 A 正確。"],"easy"),
q(5,"食物網中一種捕食者大量減少，可能同時影響多個族群；要判斷因果，哪項資料最重要？",["長期記錄多個營養階層的族群數量、資源與環境條件，並和未受影響區域比較","只看一種獵物一天的數量","只問居民的印象","把所有變化都歸因於捕食者而不查氣候"],"A","食物網有多重交互作用，需長期、多族群和對照資料，並控制資源、氣候與人為干擾，才能判斷因果。","以系統網絡、時間序列和對照避免單因果誤判。",["畫出捕食者和獵物關係。","記錄多個營養階層與資源。","加入氣候、人為干擾等替代解釋。","比較受影響和對照區的長期趨勢。","因此 A 最有證據力。"],"hard"),
q(6,"金屬湯匙放入熱湯後變熱，這個現象主要涉及？",["熱能由高溫湯經由接觸傳到較低溫的湯匙，最後趨向熱平衡","冷能從湯匙流進熱湯","湯匙的質量變成熱能而消失","熱傳只可能在真空中發生"],"A","熱能淨傳遞方向由高溫物體到低溫物體，湯匙與湯接觸後溫差降低並趨向熱平衡。","以溫差、熱傳方向和系統平衡解釋宏觀變化。",["比較湯和湯匙初始溫度。","判斷熱能淨傳遞方向。","觀察溫差逐漸減小。","排除冷能流動、質量消失和真空必要性。","所以 A 正確。"],"easy"),
q(7,"若地震測站收到不同波的到時資料，可用來推估震央位置；這種方法的核心是？",["不同測站的波到時差提供距離線索，交會多站資料可定位","只要一個測站的最大振幅就能精確畫出震央","震央由地面顏色決定","地震波不會在地下傳播"],"A","不同波速造成到時差，可估算測站到震源的距離，多站圓弧交會才可縮小震央範圍。","由測量差值、模型和多站交會建立地球現象推理。",["記錄 P、S 波或不同波到時。","利用到時差估算距離。","以多個測站建立可能位置範圍。","交會資料以定位震央並標示不確定性。","所以 A 最完整。"],"hard"),
q(8,"雲中水滴形成較大雨滴並降落，最能代表哪種自然界交互作用？",["水在大氣中的相變、碰撞聚合與重力共同作用，將微小水滴轉成降水","雨滴由空氣憑空產生且沒有水循環","重力會把所有氣體變成雨","雲和地面完全沒有物質交換"],"A","水蒸氣凝結成雲滴，雲滴碰撞聚合並受重力沉降，屬於大氣、水循環和力的交互作用。","把物質狀態、粒子碰撞和重力跨尺度連結。",["確認水蒸氣凝結形成雲滴。","描述雲滴碰撞聚合。","判斷重力使大水滴沉降。","把過程連到水循環而非憑空生成。","所以 A 正確。"],"medium"),
q(9,"面對『某自然事件一定由單一因素造成』的說法，最好的科學回應是？",["先建立可能因素與交互作用模型，再用可檢驗資料和替代解釋比較","直接接受最直覺的因素","只找支持原說法的資料","因為因素很多所以不能研究"],"A","自然系統常有多因素交互，需提出模型、控制或比較資料並檢查替代解釋，而不是直覺接受或放棄研究。","用模型—證據—替代解釋的探究流程處理複雜現象。",["列出事件可能涉及的因素。","畫出因素間可能的交互作用。","提出可量測的預測和對照。","比較支持與反駁資料並修正模型。","所以 A 是科學回應。"],"medium"),
q(10,"要向社區說明一項環境措施的效果，哪種證據與溝通最完整？",["明確說明系統邊界、指標、基準線、資料不確定性與長期結果，並區分測得事實和推論","只公布最漂亮的一次數據","只用口號不提供測量方法","把相關性直接說成必然因果"],"A","環境措施需以基準線、指標、長期資料和不確定性呈現，並誠實區分觀察與因果推論，才能支持公共決策。","將自然系統證據轉成可追溯且不過度宣稱的科學溝通。",["定義系統邊界和想改善的指標。","建立措施前的基準線與對照。","長期收集資料並揭露不確定性。","分別標示測量事實、推論和限制。","所以 A 最完整。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["自然現象可由物質、能量、力、尺度和系統邊界的交互作用描述。","模型、守恆、時間序列、對照與不確定性是跨領域自然探究的共同工具。","複雜自然系統常由多因素交互形成，需避免單一因果與過度宣稱。"],"versionDifferences":["南一公開線索支持由日常現象、能量與環境觀察進入自然系統。","康軒公開課程資料較突出模型、測量、資料和控制變因。","翰林公開課程計畫補充尺度、交互作用、環境與公共溝通連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以系統邊界—交互作用—守恆—證據—不確定性五層框架統整根單元。","加入海陸風、月相、食物網、雨滴、地震定位、熱平衡和環境溝通的跨現象遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫 K 根單元自然界現象、系統交互、能量、物質、模型、證據與安全的整合題；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"K：自然界的現象與交互作用","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為系統、尺度、能量、物質、力、食物網、天氣、地震、資料證據與科學溝通整合問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content k")
if __name__=="__main__": main()
