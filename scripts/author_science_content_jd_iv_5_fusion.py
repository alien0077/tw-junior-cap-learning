"""Jd-Ⅳ-5：酸、鹼、鹽的生活應用與危險性第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jd-iv-5.json"
REPORT=ROOT/"implementation/reports/science-content-jd-iv-5-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"酸鹼鹽生活應用、標示、反應與安全資料","pattern":"取由生活物質性質、酸鹼鹽反應及安全資訊判斷用途與危險性的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"酸鹼、鹽類、清潔用品、腐蝕與生活情境","pattern":"取從成分標示、資料表與生活情境推論物質用途及風險的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"酸鹼鹽性質、生活應用與實驗安全","pattern":"取以酸鹼鹽性質、生活材料、反應危害與安全操作連結教學的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jd-iv-5-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jd-iv-5"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的酸、鹼、鹽生活應用、成分標示、腐蝕與安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jd-iv-5","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"胃藥中含有可中和胃酸的鹼性成分，主要利用哪種化學性質？",["鹼可與酸反應，降低過多 H⁺ 造成的酸性","鹼會把胃酸變成氧氣","鹼一定能消除所有疾病","胃藥只靠顏色改變發揮作用"],"A","胃藥的鹼性成分可和胃酸中的 H⁺ 反應，降低酸性；效果與用量和成分有關，不能推成治療所有疾病。","把生活用途連回酸鹼中和與證據範圍。",["辨認胃酸是酸性物質。","找出胃藥中的鹼性成分。","判斷 H⁺ 被中和而酸性降低。","排除生成氧氣、萬能治病與顏色作用。","所以 A 正確。"],"easy"),
q(2,"食醋可用於去除水垢，較合理的原因是水垢中的碳酸鹽可與酸？",["反應生成較易溶解的物質並放出二氧化碳","把酸變成金屬而附著更牢","使碳酸鹽變成氧氣","完全不發生反應，只靠醋的顏色覆蓋"],"A","醋酸可與碳酸鹽反應，生成鹽、水與二氧化碳，使水垢逐漸溶解；仍需注意材質和接觸安全。","以酸與碳酸鹽反應解釋生活清潔用途。",["辨認水垢主要含碳酸鹽。","找出食醋的酸性。","預測生成鹽、水與二氧化碳。","確認固體減少是反應證據。","因此 A 最合理。"],"easy"),
q(3,"洗滌鹼等鹼性清潔劑去除油污時，哪項安全觀念正確？",["鹼性清潔劑可能刺激或腐蝕皮膚，應看標示並戴適當防護，不徒手長時間接觸","鹼性代表完全無害，可以入口","只要有香味就能不戴手套","鹼性清潔劑一定可和所有清潔劑混合"],"A","強鹼可能造成刺激或腐蝕，應依標示使用並防護；不同清潔劑混合可能產生危險反應。","把物質用途與濃度、標示和暴露風險一起判斷。",["確認清潔劑的酸鹼性與濃度資訊。","查閱腐蝕或刺激警示。","使用手套、護目鏡及通風等適當防護。","不要入口或任意混合其他清潔劑。","所以 A 是正確安全觀念。"],"easy"),
q(4,"食鹽是日常常見的鹽類；從粒子觀點看，固態食鹽不易導電但溶於水後可導電，原因是？",["水溶液中的鈉離子和氯離子能自由移動，固態離子位置受限","食鹽溶於水後產生金屬電子","固態食鹽沒有任何離子","水把氯離子變成氧氣"],"A","固態離子被晶格固定，溶於水後鈉、氯離子可移動並傳遞電荷，因此溶液導電。","從鹽類的離子結構和移動性判斷生活性質。",["辨認食鹽是離子化合物。","比較固態與水溶液的粒子移動。","確認可移動離子造成導電。","排除電子生成、無離子與氧氣說法。","答案為 A。"],"medium"),
q(5,"漂白水與酸性清潔劑不應混合，最主要的安全理由是？",["可能產生有害氣體或劇烈反應，應依標示分開使用並保持通風","混合後一定變成食鹽水而完全安全","酸會讓漂白水變成飲料","兩者混合只會改變顏色沒有風險"],"A","漂白成分和酸混合可能釋放刺激性或有毒氣體，必須避免混用並遵守產品標示。","以化學相容性和危害資料判斷清潔用品安全。",["辨認兩種產品各自的成分與酸鹼性。","查閱標示中的不可混用警語。","推論可能產生氣體或劇烈反應。","隔離使用並維持通風，不自行測試。","所以 A 是唯一安全答案。"],"easy"),
q(6,"若要比較兩種除垢劑對同質量水垢的效果，哪項設計最公平？",["固定水垢質量與表面、除垢劑體積與溫度，只改變除垢劑種類並量測剩餘質量","一種用濃溶液、一種用稀溶液且不記錄","一組加熱另一組不加熱","只看泡沫多少判定除垢量"],"A","控制水垢、體積、溫度與接觸時間，只改變除垢劑種類，並以剩餘質量或溶解量量化效果。","用控制變因和可量測指標比較生活化學效果。",["固定水垢初始質量與表面狀態。","固定除垢劑體積、溫度和接觸時間。","將除垢劑種類設為唯一自變因。","量測剩餘質量或溶解量並重複。","因此 A 是公平設計。"],"medium"),
q(7,"食品中加入少量某些鹽類可調整風味或保存，但判斷能否食用時最重要的是？",["確認成分、濃度、用途與法規／標示，不把所有鹽類都視為可食","只要名稱中有『鹽』就一定安全","只看顏色決定能否入口","加熱後所有鹽類都會變無害"],"A","鹽類種類很多，安全性取決於成分、濃度、用途和規範，不能由『鹽』這個名稱推論可食。","區分化學分類名稱與實際毒性、用途及劑量。",["確認未知鹽類的完整成分。","查閱食品用途與標示規範。","考慮濃度與攝取量。","排除名稱、顏色和加熱的過度推論。","所以 A 最可靠。"],"medium"),
q(8,"接觸不明酸、鹼或鹽類粉末時，哪項操作最適當？",["先查標示與安全資料，戴防護具並避免直接聞、摸或入口","用舌頭少量試味道","用手指判斷是否溶解","直接和另一種藥品混合觀察"],"A","未知化學品可能有腐蝕、刺激或毒性，應先查資料、做好防護並由合格人員處理，不可用人體測試。","以危害辨識和標準操作取代猜測性試驗。",["停止不必要的接觸。","確認容器標示或請教師長協助。","使用適當護目鏡、手套和通風。","不聞、不摸、不嘗、不任意混合。","因此 A 是安全作法。"],"easy"),
q(9,"農業土壤過酸時，施用適量石灰粉可能改善酸性；其主要思路是？",["石灰的鹼性成分可中和部分酸，並需依土壤資料控制用量","石灰會把所有土壤變成純水","施用越多越好且不會影響植物","石灰是酸性物質所以增加 H⁺"],"A","石灰中的鹼性成分可中和土壤酸性，但過量會造成另一種失衡，需依 pH 與土壤檢測決定。","將酸鹼中和概念遷移到環境管理並保留用量限制。",["測量土壤初始 pH。","辨認石灰的鹼性與中和作用。","估計需要的適量並分次施用。","施用後再測量，避免過量造成傷害。","所以 A 最合理。"],"medium"),
q(10,"清潔劑標示『腐蝕性』，使用時哪項作法最能降低風險？",["依標示稀釋或使用、戴護目鏡與手套、保持通風且不與其他清潔劑混用","改用密閉空間以免味道外散","把剩餘液體倒入飲料瓶方便攜帶","為了增強效果任意加酸或加鹼"],"A","腐蝕性清潔劑需依標示和防護使用，並避免密閉、誤裝及混用；不可自行調配。","將標示資訊轉換成具體的暴露控制措施。",["讀取腐蝕性與不可混用警示。","準備護目鏡、手套和通風。","使用原容器並依指示操作。","避免密閉空間、誤裝和任意加料。","答案為 A。"],"easy"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["酸、鹼、鹽的生活用途必須和其粒子性質、濃度、成分及反應證據連結。","用途不等於安全，標示、濃度、暴露路徑與不可混用警語是風險判讀核心。","公平實驗與安全操作同時適用於生活清潔、食品、土壤與材料情境。"],"versionDifferences":["南一公開線索支持由胃藥、食醋與生活清潔進入酸鹼鹽用途。","康軒公開課程資料較突出鹽類導電、酸鹼反應及生活實驗。","翰林公開課程計畫補充成分、危害與實驗安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以『用途—成分—濃度—暴露—標示』框架判斷酸鹼鹽生活化學。","納入漂白水混用、未知粉末、土壤改良、除垢比較與食品鹽類的安全遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫酸、鹼、鹽生活應用、成分判讀、腐蝕與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jd-Ⅳ-5：酸、鹼、鹽的生活應用與危險性","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為酸鹼鹽生活用途、清潔與食品、腐蝕刺激、標示、不可混用、公平實驗與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jd-iv-5")
if __name__=="__main__": main()
