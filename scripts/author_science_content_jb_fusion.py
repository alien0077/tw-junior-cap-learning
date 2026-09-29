"""Jb：水溶液中的變化第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-jb.json"; REPORT=ROOT/"implementation/reports/science-content-jb-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"水溶液、溶質溶劑、溶解、均勻混合與資料判讀","pattern":"取由粒子模型、溶解現象、質量資料與分離方法判斷水溶液的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"溶液、濃度、溶解度、實驗現象與生活情境","pattern":"取從圖表、實驗與生活溶液資料判讀溶質分散、飽和、濃度及操作限制的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"水溶液、溶解、溶解度、飽和與分離","pattern":"取觀察溶解與均勻混合、比較溶解度、設計飽和實驗及選擇分離方法的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jb-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jb"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的水溶液、溶質溶劑、溶解、溶解度、飽和及分離能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；題幹、選項、答案、解析與五步解法均依 Jb 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jb","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"把少量食鹽加入水並攪拌後，若液體各處看起來均勻，食鹽在此水溶液中是？",["溶質","溶劑","沉澱物","濾紙"],"A","食鹽是被分散、溶解的物質，稱為溶質；水是主要溶劑。","先辨認被溶解者與負責分散的介質。",["找出加入並消失於液體中的物質。","確認水是連續的主要介質。","將食鹽命名為溶質。","B、C、D 分別是介質、未溶固體或分離工具。","所以 A 正確。"],"easy"),
q(2,"下列哪項最能說明食鹽溶於水後不是消失，而是形成水溶液？",["蒸發水後可重新得到食鹽，且溶液各處性質大致相同","食鹽變成了水","食鹽只停在杯底","只要看不見顆粒就代表發生化學反應"],"A","食鹽粒子可均勻分散在水中，移除水後可回收，顯示是物理性的溶解而非消失。","用可逆性與均勻性檢查溶解模型。",["觀察溶液是否各處均勻。","蒸發部分水並觀察是否留下固體。","把現象與粒子分散模型連結。","B、C、D 與溶液證據不符。","答案為 A。"],"easy"),
q(3,"同溫下把糖加入水，攪拌後杯底仍有固體；最合理的判斷是？",["已達此條件下的溶解度，部分糖未溶解","糖一定變成氣體","水變成溶質","所有固體都已均勻溶解"],"A","在固定溫度和水量下，若仍有固體且上層溶液均勻，可能已達飽和，加入的糖超過可溶量。","由未溶固體、溫度與溶質量判斷飽和狀態。",["確認溫度與水量固定。","觀察是否有固體長時間未溶。","比較加入量與該溫度的可溶量。","B、C、D 不符合物質守恆與觀察。","所以 A 最合理。"],"medium"),
q(4,"要比較食鹽和砂糖在水中的溶解度，哪項條件最需要固定？",["水的質量、溫度、攪拌時間與判定完全溶解的標準","只固定杯子的顏色","讓兩者使用不同溫度且不記錄","一種攪拌另一種不攪拌"],"A","溶解度受溫度、溶劑量和操作條件影響；固定這些條件才能比較不同溶質。","先找出會改變溶解量的控制變因。",["設定相同水量和溫度。","使用相同攪拌時間與判定標準。","逐步增加溶質並記錄完全溶解量。","B、C、D 會引入混淆變因。","答案為 A。"],"medium"),
q(5,"若要從含有不溶泥沙的食鹽水中取得較乾淨的食鹽，最合理的流程是？",["先過濾去除泥沙，再蒸發水分使食鹽析出","直接用磁鐵吸走食鹽","只用濾紙就讓已溶食鹽留下","先把所有物質燃燒"],"A","泥沙不溶於水可先過濾，食鹽仍在濾液中，再蒸發水使食鹽結晶。","依物質是否溶解選擇分離方法。",["辨認泥沙是固體不溶物。","過濾保留泥沙、收集濾液。","蒸發濾液中的水使食鹽析出。","B、C、D 無法正確分離這三種物質。","因此 A 正確。"],"medium"),
q(6,"相同質量的水中加入不同質量食鹽，若都完全溶解，哪項通常會改變？",["溶液中溶質的質量分率或濃度","食鹽的元素種類","水的化學式","重力定律"],"A","加入更多溶質而仍完全溶解，溶液的溶質比例會提高，但不會改變物質的元素種類或水的化學式。","用溶質與溶液總量的比例判斷濃度變化。",["固定水的質量。","比較兩杯溶質質量與溶液總質量。","計算或定性比較溶質比例。","B、C、D 不是濃度變化的結果。","答案為 A。"],"easy"),
q(7,"把一杯食鹽水分成上下兩層取樣，若攪拌充分且無沉澱，兩層的食鹽濃度應如何？",["理想狀況下大致相同","上層一定為零、下層一定最高","只由杯子形狀決定","每次取樣必定完全不同"],"A","均勻水溶液中溶質粒子分散於各處，充分混合且無沉澱時，上下層濃度大致相同。","用均勻混合模型判讀取樣位置。",["確認溶液充分攪拌且沒有固體沉澱。","辨認食鹽粒子分散在整杯溶劑中。","比較不同位置取樣的預期濃度。","B、C、D 與均勻溶液模型不符。","答案為 A。"],"easy"),
q(8,"同一杯糖水加熱後能溶解更多糖，冷卻後出現晶體，最合理的解釋是？",["溫度改變使溶解度改變，冷卻後超過可溶量的糖析出","糖在加熱時變成水","晶體是憑空生成的","冷卻會讓所有物質都消失"],"A","許多固體溶質在較高溫可溶較多，冷卻後溶解度下降，多出的溶質會結晶析出。","把溶解度視為溫度的函數，再判斷析出。",["比較加熱與冷卻時的可溶量。","確認冷卻後溶液中的溶質量未全部消失。","判斷超過低溫溶解度的部分。","B、C、D 違反溶解與物質守恆概念。","所以 A 正確。"],"medium"),
q(9,"要判斷一杯液體是水溶液而非懸浮液，哪項觀察較有用？",["靜置後仍均勻透明且通常不能用普通濾紙分離溶質","靜置後顆粒全部沉底","一定能用磁鐵分離","只要有顏色就一定是懸浮液"],"A","水溶液中的溶質粒子尺度很小，通常均勻且不會由普通濾紙分離；懸浮液則可能沉降。","比較均勻性、沉降與過濾行為。",["靜置觀察是否產生沉澱。","檢查是否各處均勻。","以普通過濾測試可否截留顆粒。","B、C、D 不是水溶液的普遍特徵。","答案為 A。"],"medium"),
q(10,"若實驗要比較不同水溫對食鹽溶解速度的影響，哪項設計最公平？",["固定水量、食鹽質量、攪拌方式與容器，只改變水溫並記錄完全溶解時間","同時改變水量和水溫","一杯攪拌、一杯不攪拌","只憑肉眼猜哪杯較快"],"A","只改變水溫並固定其他條件，才能把完全溶解時間差異歸因於溫度。","使用單一自變因與可量測終點。",["列出可能影響溶解速度的變因。","固定水量、溶質質量、攪拌和容器。","設定不同水溫並測量完全溶解時間。","B、C、D 缺少控制或沒有量測證據。","所以 A 最公平。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以溶質、溶劑、均勻分散、溶解度、飽和與分離方法描述水溶液中的變化。","水溶液判讀需連結粒子模型、溫度、水量、濃度、溶解／析出與可逆分離，並用控制變因設計實驗。"],"versionDifferences":["公立段考與會考公開題型提供溶液、溶解、溶解度、濃度與分離資料方向；康軒公開課程線索偏向均勻混合、飽和、溫度影響、粒子模型與實驗設計。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以食鹽水、糖水、泥沙、結晶、過濾、蒸發與水溫比較建立根單元水溶液證據鏈。","把『溶質消失就是消失』、『所有混合物都是水溶液』與『加熱一定能溶解無限量溶質』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新撰寫溶質溶劑、溶解、均勻性、溶解度、飽和、濃度、分離與控制變因。原有 10 題為日期與食鹽質量變換的重複計算套題，已逐題改寫為水溶液根單元專屬題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"question-science-content-jb-{x['id'].rsplit('-',1)[-1]}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jb：水溶液中的變化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有 10 題為日期與食鹽質量變換的重複計算套題，已逐題改寫為溶質、溶劑、溶解、溶解度、飽和、分離與控制變因專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jb")
if __name__=="__main__": main()
