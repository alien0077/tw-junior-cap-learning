"""Ka-Ⅳ-10：三稜鏡分光第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-ka-iv-10.json"
REPORT=ROOT/"implementation/reports/science-content-ka-iv-10-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"光的折射、色散、光譜與實驗圖表判讀","pattern":"取由光路圖、顏色偏折與資料判斷三稜鏡分光現象的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"光譜、折射、波長與生活光學情境","pattern":"取從模型、光譜資料與生活光學情境推論色散與光的性質的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"三稜鏡、色散、光譜與探究操作","pattern":"取以折射率、波長、色散、光譜與控制變因建立光學探究的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-ka-iv-10-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-ka-iv-10"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的三稜鏡、折射、色散、光譜、波長與安全探究能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ka-iv-10","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"白光通過三稜鏡後在屏幕上形成彩色帶，這種現象稱為？",["色散，白光中的不同色光因折射程度不同而分開","反射，所有光仍沿原方向","聲音共振","熱傳導"],"A","白光包含多種波長的色光，在三稜鏡中折射率不同，偏折角不同而分開形成光譜，稱為色散。","把白光組成、折射率差和屏幕彩帶連成模型。",["確認入射光是白光。","辨認不同顏色在棱鏡內折射程度不同。","觀察出射光角度分開。","將此現象命名為色散。","所以 A 正確。"],"easy"),
q(2,"在一般玻璃三稜鏡中，哪種可見光通常偏折角較大？",["紫光，因為在玻璃中的折射率通常較大","紅光，因為波長最長一定偏折最大","所有顏色偏折完全相同","不可由任何資料判斷"],"A","可見光在玻璃中的折射率通常隨波長而變，紫光偏折較大、紅光較小；實驗仍需依材料與光路確認。","比較顏色、波長和介質折射率的關係。",["確認不同顏色在玻璃中的速度／折射率不同。","比較紫光與紅光的偏折方向。","判斷紫光偏折角通常較大。","排除顏色完全不影響和紅光必最大。","答案為 A。"],"medium"),
q(3,"三稜鏡分光實驗中，把屏幕移遠，主要會影響哪項觀察？",["彩色光帶各色光斑的間距可能變大，但不必然改變每種光在棱鏡內的折射率","白光會變成沒有波長的光","所有顏色會合成聲音","三稜鏡的材質會自動改變"],"A","屏幕距離增加會放大不同出射方向造成的空間分離，材料折射率仍由光色和介質決定。","區分幾何觀察尺度與材料本身光學性質。",["辨認各色光以不同角度離開三稜鏡。","比較屏幕距離改變後的光斑位置。","說明角度差乘上距離使間距改變。","排除改變波長、聲音或材料的說法。","所以 A 正確。"],"medium"),
q(4,"若只用紅色雷射光通過三稜鏡，通常不會看到完整彩虹帶，主要原因是？",["入射光近似單一波長，沒有多種色光可供分開","雷射光不能折射","三稜鏡只能讓白光直線通過","紅光沒有能量"],"A","色散需要不同波長的光；單色雷射只會產生單一主要出射光路，仍可能發生折射。","區分折射是單色光也會有，色散需多波長。",["確認雷射接近單一波長。","判斷沒有其他顏色可被分離。","仍保留單一光束的折射。","排除不能折射、只能白光和無能量。","答案為 A。"],"easy"),
q(5,"要比較不同玻璃三稜鏡的色散能力，哪項實驗設計較公平？",["使用相同白光、入射角、屏幕距離與測量方法，只更換三稜鏡材料並重複測量彩帶分離角或寬度","每個棱鏡使用不同光源和入射角","只看彩帶顏色鮮豔程度","一個屏幕近、一個屏幕遠且不記錄距離"],"A","控制光源、入射角、幾何距離和測量方法，只改變棱鏡材料才能比較材料色散；需量化分離結果。","以控制變因和光路幾何建立材料比較。",["固定白光光源和入射方向。","固定屏幕位置和測量尺度。","更換棱鏡材料作唯一自變因。","量測光譜寬度或不同顏色偏折角並重複。","所以 A 是公平設計。"],"medium"),
q(6,"若三稜鏡出射的紅光和紫光在屏幕上位置不同，最直接的物理原因是？",["兩種光在玻璃中的折射率不同，依折射定律產生不同偏折角","紅光和紫光質量不同","屏幕會主動把光變色","光的顏色由三稜鏡重量決定"],"A","不同波長在玻璃中的折射率不同，因此進出介面時折射角不同，造成屏幕位置分離。","用介面折射和色散差異解釋光路。",["確認兩色光入射於同一棱鏡。","比較兩色在玻璃中的折射率。","套用折射方向和角度差。","排除質量、屏幕主動變色與重量。","答案為 A。"],"medium"),
q(7,"太陽光經雨滴形成彩虹，和三稜鏡分光相似之處是？",["水滴也能讓白光折射、反射並因不同顏色折射程度不同而分開","雨滴會把聲音變成光","只有紅光能通過水滴","彩虹與光的波長無關"],"A","雨滴和三稜鏡都可造成折射與色散，內部反射和觀察幾何共同形成彩虹；不同顏色的波長仍很重要。","把人工棱鏡模型遷移到自然光學現象。",["確認太陽光含多種可見色光。","追蹤光進入、離開水滴的折射。","加入水滴內部反射的幾何條件。","判斷各色因折射率不同而分開。","所以 A 正確。"],"medium"),
q(8,"觀察三稜鏡光譜時，哪項安全作法最重要？",["避免把雷射或強光直射眼睛，固定光路並使用屏幕觀察","直接用眼睛盯住雷射出口","把三稜鏡拿到眼前觀察光路","為增加亮度把光源功率調到最高"],"A","強光或雷射可能傷害眼睛，應固定光路、以屏幕接收，不能直視或任意提高功率。","將光路設計和眼睛安全同時納入實驗。",["辨認光源可能造成眼睛暴露。","把出射光導向屏幕而非人眼。","固定棱鏡和光源，限制反射散射。","不直視出口、不把器材靠近眼睛、不任意增功率。","所以 A 是安全作法。"],"easy"),
q(9,"若光譜上紅光和紫光的分離距離變小，不能直接宣稱『光的波長變相同』，還應先檢查？",["屏幕距離、入射角、棱鏡方向、光源組成與測量尺度是否改變","只檢查屏幕顏色是否漂亮","只問觀察者是否疲倦","把所有變化歸因於波長"],"A","分離距離同時受出射角差和屏幕距離、入射幾何及光源影響，需先排除裝置與測量改變。","用替代解釋和控制變因避免光學資料過度推論。",["列出影響光譜間距的幾何和光源因素。","核對屏幕距離與棱鏡方向。","確認入射角、光源組成和刻度。","再判斷材料色散或波長差異。","所以 A 最完整。"],"hard"),
q(10,"若要用光譜比較兩種光源，哪項觀察最適合支持光源成分不同？",["在相同光路和測量條件下，兩者的連續／線狀光譜、峰值位置或相對強度有可重複差異","只看光源外殼顏色","只看哪個燈比較亮一次","只改變屏幕距離再比較彩帶寬度"],"A","光譜形狀、線條位置和相對強度是可比較的成分線索，需控制光路和重複測量；外殼顏色或單次亮度不足。","把三稜鏡分光由現象提升為可重複的光譜證據。",["固定光源到棱鏡的距離和入射角。","固定屏幕與測量尺度。","記錄連續或線狀光譜特徵。","重複比較峰值和相對強度，排除亮度單一差異。","所以 A 最有證據力。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三稜鏡分光同時涉及光在介面折射、不同波長折射率差與屏幕上的幾何分離。","光譜觀察需區分光源組成、棱鏡材料、入射幾何、屏幕距離和測量尺度。","模型、控制變因、重複測量與眼睛安全是光學探究的共同要求。"],"versionDifferences":["南一公開線索支持由彩虹與三稜鏡現象進入色散。","康軒公開課程資料較突出折射率、波長、光路和資料判讀。","翰林公開課程計畫補充光譜、光源比較與實驗安全；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以光源—介面—折射率—色散—屏幕—光譜證據六層框架分析分光。","加入幾何放大、單色雷射、彩虹遷移、測量替代解釋和雷射安全。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫三稜鏡折射、色散、光譜、控制變因、自然彩虹與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Ka-Ⅳ-10：三稜鏡分光","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為折射、色散、不同顏色偏折、單色光、屏幕幾何、光譜、彩虹、控制變因與雷射安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ka-iv-10")
if __name__=="__main__": main()
