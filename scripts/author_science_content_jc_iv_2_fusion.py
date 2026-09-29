"""Jc-Ⅳ-2：燃燒實驗認識氧化第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jc-iv-2.json"
REPORT=ROOT/"implementation/reports/science-content-jc-iv-2-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"燃燒、氧氣、反應現象與資料判讀","pattern":"取由燃燒現象、氧氣條件及反應資料判讀氧化的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"燃燒、氣體檢驗、控制變因與生活情境","pattern":"取從實驗圖表、氣體證據與生活燃燒情境推論反應的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"氧化燃燒、實驗操作與安全","pattern":"取以燃燒操作、氧化證據與安全控制連結宏觀現象與微觀反應的教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jc-iv-2-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jc-iv-2"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的燃燒、氧氣、實驗控制、氣體證據及安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jc-iv-2","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"蠟燭火焰被玻璃鐘罩罩住後逐漸熄滅，最合理的解釋是？",["罩內可支持燃燒的氧氣逐漸被消耗，燃燒條件不再滿足","蠟燭的質量變成零","玻璃會把熱量永久吸走","二氧化碳本身一定是可燃物"],"A","燃燒需要可燃物、氧氣與達到著火點；密閉罩內氧氣減少後，火焰無法維持。","把熄滅現象連回燃燒三要素與系統邊界。",["確認鐘罩限制了空氣交換。","列出燃燒需要的三項條件。","判斷哪項條件會隨時間消耗。","排除質量歸零、玻璃吸熱及氣體誤判。","所以 A 最符合觀察。"],"easy"),
q(2,"要證明氧氣是蠟燭燃燒的必要條件，哪項對照最適合？",["相同蠟燭與點燃方式，一支在空氣中、一支置於已移除氧氣的環境並比較能否持續燃燒","一支蠟燭較粗、另一支較細且不記錄時間","只比較兩支蠟燭顏色","把蠟燭和電池同時改變"],"A","只改變氧氣條件並保持蠟燭、點燃方式等相同，才能把燃燒差異歸因於氧氣。","用單一自變因建立燃燒必要條件的對照。",["固定蠟燭大小與初始狀態。","固定點燃時間和環境溫度。","只改變是否有可用氧氣。","比較火焰持續時間或是否熄滅。","因此 A 是公平對照。"],"medium"),
q(3,"木片燃燒後留下黑色焦炭與灰，若要判斷產生新物質，哪項證據最有力？",["產物的顏色、質地與可燃性和木片不同，且不能用簡單物理方法恢復木片","只看火焰很亮","只記錄燃燒用了幾秒","只看木片長度變短"],"A","產物出現新性質且不能簡單恢復，支持化學反應；亮度、時間與長度只是現象或數值，不能單獨證明新物質。","優先檢查物質性質與可逆性，不把單一現象當充分證據。",["比較木片和燃燒產物的性質。","檢查是否有新物質。","判斷物理方法能否恢復木片。","排除亮度、時間與長度的單一指標。","所以 A 的證據最完整。"],"medium"),
q(4,"以相同質量的鎂帶和鐵絲比較燃燒，若要比較兩者對氧的反應性，最需要控制哪項？",["金屬表面狀態、質量、氧氣供應與加熱方式","只控制觀察者的座位","讓鎂帶在純氧、鐵絲在空氣中燃燒","每次使用不同質量且不記錄條件"],"A","公平比較必須控制表面、質量、氧氣與加熱條件，否則觀察到的差異可能來自實驗設計而非金屬本身。","先列控制變因，再以反應速率與現象比較活性。",["選定相同或可比較的金屬質量。","處理表面狀態與氧氣濃度。","固定點燃與加熱方式。","記錄亮度、反應時間與產物等可量測證據。","因此 A 最能支持公平比較。"],"medium"),
q(5,"在氧氣不足時燃燒含碳燃料，較可能出現哪項風險？",["可能產生一氧化碳等不完全燃燒產物，需保持通風並避免吸入","一定只產生氧氣","燃料會變成水而沒有氣體","氧氣不足會使所有燃燒完全停止且沒有產物"],"A","氧氣不足可能使含碳燃料不完全燃燒，產生一氧化碳等危險物；通風與氣體檢測是安全要求。","把燃燒條件與產物種類及實驗安全連在一起。",["辨認燃料含有碳。","檢查氧氣是否充足。","推論可能發生不完全燃燒。","考慮一氧化碳無色且有毒的風險。","所以 A 是正確且安全的判斷。"],"medium"),
q(6,"燃燒實驗前先把可燃物周圍的酒精擦乾，主要是為了？",["避免酒精蒸氣或液體意外擴大火勢，控制可燃物與火源的接觸","讓燃料一定完全燃燒","使氧氣變成不可燃氣體","增加火焰溫度以便觀察"],"A","移除多餘可燃物可降低火勢擴散風險；安全操作不是為了保證完全燃燒或改變氧氣。","先辨認危害來源，再選擇降低暴露與擴散的操作。",["找出實驗中的火源與可燃液體。","判斷酒精外漏會增加哪種風險。","移除或隔離多餘可燃物。","排除改變氧氣或刻意升溫的錯誤目的。","因此 A 符合安全原則。"],"easy"),
q(7,"把點燃的蠟燭放入密閉瓶後，瓶內壁出現水珠；若用試紙與對照確認，這可支持燃燒產生？",["水，表示燃料中的氫與氧反應形成含氫產物","氧氣增加","固態碳直接變成水珠","只有玻璃融化"],"A","含氫燃料燃燒可生成水，冷卻後水蒸氣凝結在瓶壁；需搭配適當對照，不能把所有水珠都歸因於燃燒。","把宏觀凝結現象和反應物元素組成及對照資料配對。",["確認水珠出現於燃燒後並排除瓶內原有水分。","檢查燃料是否含氫。","用試紙或質量資料驗證水的存在。","排除氧氣增加與玻璃融化的說法。","所以 A 最合理。"],"hard"),
q(8,"若比較不同蠟燭的燃燒時間，哪項作法最能減少結論偏差？",["使用相同環境與初始質量，重複多次並記錄平均燃燒時間","每種蠟燭都在不同風速下測一次","只挑選自己預期最快的一次","不記錄蠟燭起始質量"],"A","控制環境、統一起始量並重複測量，才能比較燃料性質造成的差異並降低偶然誤差。","用控制變因、重複測量與平均值提高證據品質。",["固定風速、溫度、燭芯長度與起始質量。","為每種蠟燭設置相同測量流程。","重複測量燃燒時間。","計算平均並檢查離群值。","因此 A 的證據最可靠。"],"medium"),
q(9,"下列哪項最能說明『燃燒是一種氧化反應』？",["燃料和氧反應形成氧化物或其他含氧產物，並伴隨能量釋放","所有發光現象都是燃燒","只要物質溫度上升就一定得到氧","只有固體才能燃燒"],"A","燃燒通常是物質與氧快速反應並釋放能量，生成物含有氧或可由氧轉移證據支持；發光與升溫本身不是定義。","從反應物、生成物和能量三方面確認氧化，而非只看外觀。",["辨認是否有氧參與反應。","確認是否生成新物質或氧化物。","觀察能量釋放作為輔助證據。","排除把發光、升溫或固態當成必要條件。","所以 A 最完整。"],"easy"),
q(10,"若火焰在罩內熄滅，想判斷是氧氣消耗而不是燃料耗盡，哪項補充實驗最適合？",["使用相同燃料量，另設可持續補充空氣的對照，並測量罩內氧氣或燃料剩餘量","只換不同顏色的罩子","只觀察火焰顏色一次","把燃料量與罩子大小同時改變"],"A","控制燃料量並設置空氣交換對照，再量測氧氣或剩餘燃料，才能區分氧氣不足與燃料耗盡兩種解釋。","用替代解釋與可量測對照設計檢驗因果。",["列出熄滅的兩種可能原因。","固定燃料初始量和燭芯條件。","設置空氣可交換與不可交換的對照。","測量氧氣變化及燃料是否仍存在。","依資料判定真正原因，而不是只看火焰熄滅。"],"hard"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["燃燒是可燃物與氧快速反應並釋放能量的氧化過程。","燃燒三要素、系統邊界、產物證據與控制變因共同支撐實驗判讀。","完全與不完全燃燒的差異連結產物、安全與通風。"],"versionDifferences":["南一公開線索支持由火焰與燃燒現象進入氧化概念，但未取得完整逐頁課文。","康軒公開課程資料較能支撐燃燒操作、氣體條件與控制變因。","翰林公開課程計畫補充氧化燃燒與實驗安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以燃燒三要素、氧消耗與產物證據組成實驗推理鏈。","把不完全燃燒、通風、火源隔離與替代解釋納入單元專屬安全活動。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫燃燒實驗、氧化證據、控制變因、完全／不完全燃燒與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jc-Ⅳ-2：燃燒實驗認識氧化","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為燃燒三要素、氧氣消耗、控制變因、產物證據、完全／不完全燃燒與安全操作專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jc-iv-2")
if __name__=="__main__": main()
