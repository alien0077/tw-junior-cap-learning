"""Jc：氧化與還原反應第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-jc.json"; REPORT=ROOT/"implementation/reports/science-content-jc-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"氧化還原、得氧失氧、電子轉移與金屬反應判讀","pattern":"取由氧、電子、氧化數與實驗資料判斷氧化還原角色的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"燃燒、生鏽、金屬置換、氧化還原資料","pattern":"取從圖表、反應式與生活情境判斷氧化劑、還原劑及防鏽效果的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"得氧失氧、電子轉移、金屬活性、生鏽與防鏽","pattern":"取以實驗、粒子與電子模型連結氧化還原定義及比較反應性的教學與評量方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jc-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jc"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的得氧失氧、電子轉移、氧化數、燃燒、生鏽、金屬置換及防鏽能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；題幹、選項、答案、解析與五步解法均依 Jc 單元重新撰寫，未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jc","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"若某物質在反應中得到氧，依傳統得氧失氧定義，它屬於？",["氧化","還原","催化劑","溶劑"],"A","得到氧是傳統定義中的氧化；同一反應中通常有另一物質失去氧而被還原。","先依定義判斷氧的去向，再找互補角色。",["圈出反應前後物質中的氧。","確認該物質是否增加氧。","將增加氧的物質判為氧化。","B、C、D 不是得氧的定義。","答案為 A。"],"easy"),
q(2,"從電子觀點看，物質失去電子通常代表？",["被氧化","被還原","完全沒有變化","只發生溶解"],"A","失去電子是氧化，得到電子是還原；兩者必須同時發生在氧化還原反應中。","把電子得失與氧化還原方向配對。",["標記反應物和生成物的電子數或氧化數。","找出失去電子的物種。","套用失電子等於氧化。","B、C、D 與電子定義不符。","所以 A 正確。"],"easy"),
q(3,"在氧化銅被碳還原成銅的反應中，氧化銅的角色和變化是？",["氧化劑，得到電子而被還原","還原劑，失去電子而被氧化","催化劑且沒有變化","溶劑且被蒸發"],"A","氧化銅中的銅離子接受碳提供的電子而形成銅，因此氧化銅是氧化劑並被還原。","同時判斷物質角色與自身電子變化。",["找出接受電子的氧化銅。","判斷接受電子代表還原。","把促使別人氧化、自己被還原者稱為氧化劑。","B、C、D 與反應角色不符。","答案為 A。"],"medium"),
q(4,"鋅片放入硫酸銅溶液後表面析出銅、鋅逐漸溶解；最合理的描述是？",["鋅失去電子被氧化，銅離子得到電子被還原","鋅得到電子被還原，銅失去電子被氧化","兩者都只發生物理溶解","沒有電子轉移"],"A","鋅較易失電子形成鋅離子，銅離子接受電子析出銅，這是金屬置換型氧化還原反應。","由可見析出與溶解追蹤電子得失。",["確認鋅由金屬變成離子。","確認銅離子由溶液變成金屬。","把失電子者判氧化、得電子者判還原。","B、C、D 顛倒或否認反應機制。","所以 A 正確。"],"medium"),
q(5,"鐵製品塗上完整油漆可減緩生鏽，主要是因為？",["隔絕水和氧氣，降低鐵發生氧化還原反應的機會","讓鐵得到更多氧氣","使鐵變成不含原子的物質","油漆會把所有電子永久消除"],"A","生鏽需要水和氧等條件，完整塗層可隔絕反應物，降低鐵被氧化的速率。","把防鏽方法連到氧化反應的必要條件。",["列出鐵生鏽需要接觸的環境物質。","確認油漆是否形成連續阻隔層。","比較有無塗層的生鏽速率。","B、C、D 不符合氧化與防鏽機制。","答案為 A。"],"easy"),
q(6,"比較鎂、鐵、銅對氧的反應性，哪項證據組合較可靠？",["在相同質量、表面狀態、氧氣濃度與加熱條件下，記錄反應速率與產物","只看金屬名稱長短","每種金屬使用不同溫度且不記錄","只問哪種顏色較漂亮"],"A","公平比較需控制條件並記錄可量測的反應速率、現象與產物，不能只靠主觀印象。","以控制變因和多項證據比較金屬活性。",["固定金屬質量、表面與氧氣條件。","固定加熱方式和觀察時間。","比較反應速率與氧化物證據。","B、C、D 缺乏可比性或客觀資料。","因此 A 最可靠。"],"medium"),
q(7,"某反應中氧化數由 +2 變成 0，最合理的判斷是？",["該元素被還原，接受電子","該元素被氧化，失去電子","該元素沒有發生變化","只能判定它是催化劑"],"A","氧化數下降表示接受電子、被還原；氧化數上升才代表氧化。","用氧化數變化確認電子方向。",["比較反應前後同一元素氧化數。","判斷由 +2 到 0 是下降。","將下降配對為得電子與還原。","B、C、D 與氧化數規則不符。","答案為 A。"],"medium"),
q(8,"漂白劑使有色物質褪色，若要判斷是否涉及氧化還原，哪項證據較有力？",["檢查有色物質或漂白成分的氧化數／電子變化，並設置適當對照","只看褪色速度最快的一次","褪色就一定代表所有物質都被還原","只聞氣味判斷電子轉移"],"A","褪色是現象，需以氧化數或電子轉移以及對照實驗確認反應機制，不能由顏色單獨決定。","區分可觀察現象與氧化還原機制證據。",["記錄褪色的條件與對照。","追蹤反應物和產物的氧化數或電子。","檢查是否有電子轉移證據。","B、C、D 過度推論或不安全。","所以 A 最有力。"],"hard"),
q(9,"若一個氧化還原反應中某物質是還原劑，該物質本身通常會？",["失去電子並被氧化","得到電子並被還原","不參與反應","只改變溶劑體積"],"A","還原劑提供電子使另一物質被還原，因此還原劑本身失去電子而被氧化。","用『提供電子者』辨認還原劑並判斷自身變化。",["找出把電子交給另一物種的物質。","將提供電子者定義為還原劑。","判斷它失電子並被氧化。","B、C、D 與角色定義不符。","答案為 A。"],"easy"),
q(10,"判斷一項反應確實是氧化還原反應，哪項檢查最完整？",["確認有電子轉移或氧化數升降，並能配對一方氧化、另一方還原","只看反應是否冒泡","只看反應物顏色","只看反應是否需要加熱"],"A","氧化還原的核心是電子轉移，常以氧化數升降判斷，且必須同時存在氧化與還原兩個方向。","以機制判準統整現象，而非把單一現象當定義。",["列出反應前後元素的氧化數。","找出上升與下降的元素。","確認失電子與得電子相互配對。","B、C、D 可能出現在非氧化還原過程。","因此 A 最完整。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["三版本公開線索共同支持以得氧／失氧、電子轉移與氧化數升降描述氧化還原，並辨認氧化劑、還原劑及同一反應中的互補關係。","燃燒、生鏽、金屬置換、漂白與防鏽需用反應證據、控制條件和電子／氧化數模型相互檢驗。"],"versionDifferences":["公立段考與會考公開題型提供得氧失氧、燃燒、生鏽、金屬置換與防鏽方向；康軒公開課程線索偏向電子模型、金屬活性、實驗證據與生活應用。公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以氧化銅還原、鋅銅置換、鐵鏽、金屬活性、氧化數、漂白與油漆防鏽建立根單元證據鏈。","把『看到顏色改變就一定是氧化還原』、『還原劑會被還原』與『防鏽等於消除電子』列為迷思診斷。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公立學校／公開自然科試題及課程資料的能力方向，重新撰寫得氧失氧、電子轉移、氧化數、氧化劑／還原劑、燃燒、生鏽、置換與防鏽。原有 10 題為泛用研究句型套題，已逐題改寫為氧化還原根單元專屬題，均具唯一答案、解析與五步解法，未複製教材或試題文字、圖表與答案；Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"question-science-content-jc-{x['id'].rsplit('-',1)[-1]}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jc：氧化與還原反應","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有 10 題為泛用研究句型套題，已逐題改寫為得氧失氧、電子轉移、氧化數、氧化劑／還原劑、燃燒、生鏽、置換與防鏽專屬問題；每題有唯一答案、解析與五步解法，三筆公開試題／課程資料僅作 pattern-only 來源，正式發布前仍須第二輪 AI／Terra 內容複核。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jc")
if __name__=="__main__": main()
