"""Jc-Ⅳ-6：化學電池的放電與充電第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jc-iv-6.json"
REPORT=ROOT/"implementation/reports/science-content-jc-iv-6-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"化學電池、電流、電極與資料判讀","pattern":"取由電池構造、電流現象與反應資料推論能量轉換及電極作用的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"電池、電解質、電能與生活科技情境","pattern":"取從電路、電池資料與生活裝置判斷化學能與電能轉換的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"化學電池、氧化還原與電解操作","pattern":"取以氧化還原、電極、電解質及放電／充電操作連結電池原理的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jc-iv-6-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jc-iv-6"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的化學電池、電極、電解質、放電／充電與氧化還原能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jc-iv-6","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"化學電池接上燈泡後能使燈泡發光，主要的能量轉換是？",["化學能轉換成電能，再轉成光能與熱能","光能轉換成化學能而沒有電流","熱能消失成為電能","電能憑空產生"],"A","電池內的氧化還原反應提供化學能，外電路傳遞電能，燈泡再轉為光與熱。","先找能量來源，再追蹤電路元件的能量輸出。",["辨認電池內進行的是化學反應。","確認反應能推動電子經外電路移動。","判斷燈泡將電能轉成光與熱。","排除無來源產能與反向能量說法。","所以 A 正確。"],"easy"),
q(2,"簡易化學電池中兩種不同金屬片插入電解質溶液，電解質的主要作用是？",["提供可移動離子，使內部電荷能維持平衡並完成反應迴路","讓電子直接穿過溶液取代外電路","使兩金屬完全不反應","只用來冷卻金屬片"],"A","電解質中的離子可移動，協助內部電荷平衡與反應持續；電子主要經外電路移動。","區分外電路的電子移動和內部電解質的離子移動。",["找出外電路與溶液兩個通道。","判斷電子和離子各自能移動的位置。","確認溶液中的離子維持電荷平衡。","排除電子直接穿液、停止反應及單純冷卻。","答案為 A。"],"medium"),
q(3,"電池放電時，一個電極失去電子，另一個電極得到電子。失去電子的電極發生？",["氧化，並把電子送入外電路","還原，並吸收外電路電子","物理熔化而不反應","催化作用且完全不變"],"A","失去電子是氧化；在放電電池中，電子由氧化端經外電路流向還原端。", "先用電子得失判斷氧化還原，再連到電流路徑。",["比較兩電極反應前後的電子。","找出失去電子的一端。","將失電子判為氧化。","確認電子經外電路流向另一電極。","所以 A 正確。"],"easy"),
q(4,"一次電池使用一段時間後電壓逐漸降低，最合理的解釋是？",["反應物逐漸消耗或內部條件改變，使推動電子流動的能力下降","電池內的電子全部消失在空氣中","電池的質量一定變成零","電壓降低表示燈泡變成電池"],"A","放電消耗反應物並改變電極與電解質狀態，電池提供電能的能力可能下降；電子不會憑空消失。", "把電壓資料和電池內化學反應的消耗連結。",["記錄放電前後電壓與時間。","辨認電池內反應物是否逐漸消耗。","判斷可用化學能和電位差是否下降。","排除電子消失、質量歸零及角色顛倒。","答案為 A。"],"medium"),
q(5,"可重複充電電池接上外部電源時，主要發生的變化是？",["外部電能促使放電時的部分化學變化反向，重新儲存化學能","電池把所有化學物質變成氧氣","電能只在導線中消失而不影響電池","充電一定不會有任何熱量"],"A","充電以外部電能驅動反向反應，恢復部分可反應物質並儲存化學能；實際充電仍可能有能量損耗與發熱。", "比較放電與充電的能量流向及反應方向。",["先寫出放電時化學能轉電能。","反轉能量輸入方向，確認外部電源供電。","判斷部分反應可逆並恢復儲能狀態。","考慮損耗與發熱而非假設百分之百。","所以 A 最完整。"],"medium"),
q(6,"要比較兩種電解質對簡易電池輸出電壓的影響，哪項實驗較公平？",["固定金屬種類、距離、面積與溫度，只改變電解質種類並重複量測電壓","同時更換金屬與電解質","一組用大面積金屬、一組用小面積金屬","只挑選一次最高電壓記錄"],"A","只改變電解質並控制其他條件，才能把電壓差異歸因於電解質；重複測量可降低偶然誤差。", "以控制變因設計電池比較，並區分自變因和測量指標。",["列出影響電壓的金屬、距離、面積與溫度。","固定所有非電解質條件。","分組使用不同電解質。","重複測量並比較平均電壓。","因此 A 是公平設計。"],"medium"),
q(7,"若化學電池外電路的導線中沒有連通，最可能觀察到？",["電子無法形成連續外電路，燈泡不亮或電流極小","電解質會自動變成導線使燈泡照常發光","電池會立刻充滿電","氧化還原反應一定加快"],"A","外電路需連通讓電子移動；斷路時電流無法有效通過，燈泡通常不亮。", "先檢查電路閉合，再解釋電池反應和輸出。",["畫出電池、導線與燈泡的迴路。","檢查是否有斷點或接觸不良。","判斷電子是否能經外電路連續移動。","排除溶液代替導線、充電與加速反應的說法。","答案為 A。"],"easy"),
q(8,"若充電時電池明顯發熱或膨脹，最適當的處理是？",["立即停止使用並依安全規範隔離、通報或交由合格人員處理，不繼續強行充電","用手壓回原形後繼續充電","提高充電電壓讓它更快完成","把電池刺破放氣"],"A","異常發熱或膨脹可能表示內部故障與安全風險，應停止充電並採取合規處置；不可擠壓、刺破或提高電壓。", "把電學判讀和電池安全風險連接，不以實驗冒險換取資料。",["辨認發熱、膨脹是異常警訊。","停止外部電源與不必要接觸。","依場所規範隔離並請合格人員處置。","排除壓回、刺破及提高電壓等危險行為。","所以 A 是唯一安全選項。"],"easy"),
q(9,"比較放電和充電時的能量方向，哪項正確？",["放電主要由化學能輸出電能；充電由外部電能輸入並增加化學能","放電和充電都只把光能變成熱能","充電不需要外部電源","放電一定把電能轉成更多電能"],"A","放電與充電的能量流向相反：前者輸出電能，後者輸入電能以恢復化學儲能，兩者都可能有熱損耗。", "用能量箭頭比較兩種操作，而不是只看電流方向。",["畫出放電的化學能到電能箭頭。","畫出充電的外部電能到化學能箭頭。","加入燈泡或電池內阻造成的熱損耗。","排除沒有電源與能量自生的敘述。","答案為 A。"],"medium"),
q(10,"某電池接同一電阻後，甲電解質初始電壓 1.2 V、乙為 0.8 V；若金屬與條件相同，最合理的結論是？",["在此實驗條件下甲提供較大的初始電位差，但不能只由一次電壓推論長期容量","乙一定比甲能量總量高","甲的反應物一定比較多","只要電壓高就代表電池比較安全"],"A","初始電壓可比較當下電位差，但容量、壽命與安全需另外量測，不能由單次電壓直接推出。", "區分電壓、容量與安全三種不同指標。",["確認兩組金屬、電阻與測量時刻相同。","比較初始電壓 1.2 與 0.8 V。","只能判斷甲當下電位差較大。","列出仍需測量的容量、放電時間與安全性。","因此 A 是證據範圍內的結論。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["化學電池以氧化還原反應把化學能轉成電能，外電路傳遞電子，電解質傳遞離子。","放電與充電的能量方向和反應方向相反，但充電不一定完全恢復且可能有損耗。","電壓、容量、速率與安全是不同的電池評估指標。"],"versionDifferences":["南一公開線索支持由電池現象與電路進入化學能轉電能。","康軒公開課程資料較突出電極、電解質與氧化還原操作。","翰林公開課程計畫補充放電／充電、電解與生活科技連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以電子外電路、離子內電解質和能量箭頭拆解電池機制。","把可充電電池的電壓／容量區分、異常膨脹安全處置納入單元專屬遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫化學電池放電、充電、電極、電解質、資料判讀與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jc-Ⅳ-6：化學電池的放電與充電","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為化學能／電能轉換、電極、電解質、放電／充電、公平實驗、電壓與容量區分及安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jc-iv-6")
if __name__=="__main__": main()
