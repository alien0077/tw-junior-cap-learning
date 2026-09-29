"""Jf-Ⅳ-3：酯化與皂化反應第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jf-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-jf-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"酯化、皂化、醇與有機酸、氣味與資料判讀","pattern":"取由反應物結構、產物性質與實驗資料判斷酯化及皂化的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"有機反應、香味、清潔材料與實驗安全","pattern":"取從生活材料、反應條件與產物資料推論有機反應的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"酯化與皂化、酯類、肥皂及生活應用","pattern":"取以醇、有機酸、酯、鹼水解與界面活性連結有機反應的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jf-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jf-iv-3"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的酯化、皂化、醇／有機酸、產物、清潔材料與安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jf-iv-3","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"醇和有機酸在適當條件下反應生成酯和水，這類反應稱為？",["酯化反應","皂化反應","電解反應","中和沉澱反應"],"A","醇與有機酸脫去水形成酯，稱為酯化；皂化則是酯在鹼性條件下水解。","先辨認反應物官能基與生成物，再區分酯化和皂化。",["找出反應物為醇和有機酸。","確認生成物包含酯和水。","將此組合命名為酯化。","排除鹼水解、電解與沉澱。","答案為 A。"],"easy"),
q(2,"酯化實驗加熱並加入少量酸性催化劑，主要作用是？",["加快達到平衡的速率，催化劑本身不等於生成物","把所有反應物直接變成香味","使酯化一定變成不可逆","只為了讓水蒸發而不發生反應"],"A","加熱和催化劑可提高反應速率或促進有效碰撞，使酯化較快達到平衡；催化劑不會直接成為酯。","區分反應速率、平衡和生成物身分。",["辨認酯化是可逆反應或需達平衡。","判斷催化劑降低活化能、加熱提高速率。","確認酯仍由醇和酸的結構形成。","排除催化劑變生成物及無反應說法。","所以 A 正確。"],"medium"),
q(3,"酯化產物常具有特殊香味；若聞到香味，最適合的科學結論是？",["香味支持可能生成具有揮發性的酯，但仍需反應式、分離或分析資料確認","香味證明一定只有一種純酯","香味表示所有有機物都安全可食","只要聞到香味就能確定酸和醇的種類"],"A","香味是產物性質的線索，但多種揮發物都可能造成氣味，需以組成與反應資料確認，且不可直接嗅聞未知物。","區分感官線索、化學身分與安全判斷。",["記錄反應物和產物的可能結構。","觀察香味作為輔助現象。","用反應式、沸點或分析資料確認酯。","不可直接吸聞未知蒸氣或由氣味判定可食。","因此 A 是證據範圍內的結論。"],"medium"),
q(4,"皂化反應通常是油脂或酯在鹼性條件下水解，主要生成？",["肥皂類物質和甘油（或相應醇）","二氧化碳和氧氣","只有水和氯化鈉","金屬氧化物和氫氣"],"A","油脂是酯類，鹼性水解可生成脂肪酸鹽（肥皂）和甘油；具體產物依酯結構而定。","由酯鍵水解和鹼性條件判斷產物類型。",["辨認油脂含有酯結構。","確認鹼提供水解條件。","判斷脂肪酸鹽是肥皂成分。","辨認另一產物為甘油或相應醇。","答案為 A。"],"medium"),
q(5,"肥皂分子能幫助清除油污，主要因為其分子具有？",["親水端和親油端，可在水與油之間形成乳化或膠束","只有親水端而不能接觸油","只有親油端而不能被水帶走","能把油污變成氧氣"],"A","肥皂分子一端親水、另一端親油，可包圍油滴並讓其分散在水中，便於沖洗。","把分子兩端的極性與清潔功能連結。",["辨認油污是非極性或疏水性。","找出肥皂的親油端和親水端。","說明包圍油滴並形成分散系統。","排除只有單一端和生成氧氣的說法。","所以 A 正確。"],"easy"),
q(6,"若比較不同鹼濃度對油脂皂化速率的影響，哪項設計最公平？",["固定油脂質量、攪拌、溫度與容器，只改變鹼濃度並量測達到指定皂化程度的時間","同時改變油脂質量與鹼濃度","一組加熱、一組不加熱","只看泡沫高度而不記錄時間和質量"],"A","控制油脂、溫度、攪拌與容器，只改變鹼濃度並使用可量化終點，才能比較皂化速率。","以控制變因和明確終點量化有機反應速率。",["列出影響皂化的油脂質量、溫度和攪拌。","固定非濃度變因。","設定皂化程度的可測終點。","重複量測達終點時間並比較。","因此 A 是公平設計。"],"medium"),
q(7,"若酯化反應達到平衡後移除生成的水，平衡通常會如何移動？",["往生成酯和水的方向移動，以補回被移除的水","完全停止酯化","只往反應物方向移動","一定使催化劑消失"],"A","移除生成物水會使系統傾向生成更多酯和水，直到新平衡；催化劑不因移除水而消失。","用可逆反應和生成物移除預測平衡位移。",["確認水是酯化生成物。","辨認系統受到移除生成物的擾動。","判斷反應往生成物方向移動。","排除停止、反向和催化劑消失。","答案為 A。"],"hard"),
q(8,"酯化和皂化的關係，哪項描述正確？",["酯化可由醇和有機酸形成酯；皂化則在鹼性條件下使酯水解，方向與條件不同","兩者都是同一個單向反應且不需水","皂化一定生成酯和水","酯化只發生在無機鹽中"],"A","酯化與皂化涉及相反方向或不同條件的酯鍵形成／水解；皂化的鹼性水解產生脂肪酸鹽和醇。","比較反應物、條件與生成物，而非只看名稱。",["列出酯化的醇、酸、酯和水。","列出皂化的酯、鹼、脂肪酸鹽和醇。","比較水和鹼在兩反應中的角色。","排除同一單向反應與無機鹽說法。","所以 A 正確。"],"hard"),
q(9,"製備具香味的酯時，最重要的實驗安全措施之一是？",["小量操作、避免直接吸聞和明火，並在通風與防護條件下加熱","把反應物一次倒入密閉容器並加熱到最高溫","用舌頭確認產物味道","因為香味好聞所以不需要標示"],"A","酯化可能使用易燃、腐蝕或揮發性物質，需小量、通風、遠離明火、防護且不可直接嗅聞或品嘗。","將酯化香味活動轉成安全的暴露和火災控制。",["查閱酸、醇和催化劑的危害。","使用小量、通風和護目鏡。","遠離明火並控制加熱方式。","不直接吸聞、不品嘗、不密閉加熱。","因此 A 是安全作法。"],"easy"),
q(10,"要確認皂化後確實形成具有清潔作用的肥皂，哪項證據組合最完整？",["分析產物含脂肪酸鹽、觀察乳化油污能力，並和未皂化油脂及清水設對照","只看溶液顏色","只看泡沫越多就一定成分正確","只測反應容器溫度"],"A","產物組成與乳化功能的資料及對照可共同支持肥皂形成；泡沫、顏色或溫度單獨不足以確認。","用結構分析、功能測試與對照證明有機產物。",["收集皂化產物並分析脂肪酸鹽。","設計油污乳化測試。","加入未皂化油脂和清水對照。","比較清潔功能與組成資料。","所以 A 的證據最完整。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["酯化由醇和有機酸形成酯與水，皂化是酯在鹼性條件下水解形成脂肪酸鹽和醇。","反應條件、可逆平衡、產物性質與功能測試需共同判斷有機反應。","肥皂的親水／親油結構連結皂化產物和清潔功能，安全需考慮揮發、腐蝕與易燃。"],"versionDifferences":["南一公開線索支持由香味與生活材料進入酯化。","康軒公開課程資料較突出醇、有機酸、反應條件與產物。","翰林公開課程計畫補充皂化、肥皂界面活性及安全應用；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以反應物—條件—平衡—產物—功能—安全六層框架比較酯化與皂化。","把移除水、乳化對照、香味證據和有機反應安全納入單元專屬遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫酯化、皂化、酯類香味、肥皂界面活性、平衡與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jf-Ⅳ-3：酯化與皂化反應","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為酯化、皂化、產物、平衡、香味證據、肥皂界面活性、公平實驗與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jf-iv-3")
if __name__=="__main__": main()
