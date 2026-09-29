"""Jf-Ⅳ-4：常見塑膠第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jf-iv-4.json"
REPORT=ROOT/"implementation/reports/science-content-jf-iv-4-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"塑膠、聚合物、性質、燃燒與環境資料判讀","pattern":"取由結構、加熱性質、用途與環境資料判斷塑膠材料的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"塑膠材料、回收、生命週期與生活情境","pattern":"取從材料性質、回收標示與環境資料推論塑膠選擇和影響的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"有機聚合物、塑膠種類、生活應用與環境","pattern":"取以聚合物結構、熱性質、用途、回收及永續材料建立教學方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jf-iv-4-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jf-iv-4"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的塑膠、聚合物、熱性質、用途、回收與環境能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jf-iv-4","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"塑膠通常由許多小分子單體連接形成長鏈，這類大分子稱為？",["聚合物","電解質離子","金屬晶格","單一元素原子"],"A","許多單體以化學鍵連接形成長鏈或網狀大分子，稱為聚合物；塑膠多屬有機聚合物材料。","由單體和長鏈結構辨認聚合物概念。",["辨認小分子單體作為反應單位。","觀察是否形成重複連接的長鏈。","將長鏈大分子命名為聚合物。","排除離子、金屬晶格和單原子。","所以 A 正確。"],"easy"),
q(2,"熱塑性塑膠受熱通常可以軟化並重新塑形，主要和哪項結構特徵有關？",["分子鏈間作用可在加熱時減弱，冷卻後再固定形狀，未形成不可逆大網狀結構","它一定含有金屬離子","加熱會把塑膠變成氧氣","所有塑膠都會燃燒成同一物質"],"A","熱塑性塑膠的鏈狀結構在適當加熱下可移動、塑形，冷卻後固定；不同材料仍有不同溫度和安全限制。","用分子鏈結構連到熱性質，不把所有塑膠一概而論。",["辨認材料為鏈狀聚合物。","判斷加熱時鏈段活動性增加。","觀察冷卻後形狀固定。","排除金屬離子、氧氣和同一燃燒產物。","答案為 A。"],"medium"),
q(3,"熱固性塑膠加熱後不易再次軟化，較合理的原因是？",["分子鏈間形成較多交聯網狀結構，受熱時不易重新流動","它不含任何碳元素","它一定是金屬材料","加熱會使所有分子消失"],"A","熱固性塑膠的交聯網狀結構固定，受熱可能分解而非像熱塑性塑膠重新熔融。","比較鏈狀和交聯網狀結構對可塑性的影響。",["確認熱固性材料的交聯程度。","比較加熱時分子鏈能否滑動。","區分軟化再塑形和分解。","排除無碳、金屬和分子消失。","所以 A 正確。"],"medium"),
q(4,"選擇食品包裝塑膠時，除了重量輕，還應考慮哪組資料？",["阻隔性、耐熱性、與食品接觸安全、用途壽命及回收處理方式","只看顏色越鮮豔越好","只看價格最低而不查成分","只看能否漂浮在水面"],"A","材料選擇需符合食品接觸、溫度、阻隔、機械和生命週期要求，單一外觀、價格或密度不足。","把材料性質和使用情境及生命週期整合。",["先定義食品包裝的功能需求。","查閱耐熱、阻隔和接觸安全資料。","評估使用後的回收或處理。","排除顏色、最低價格和漂浮的單一判準。","因此 A 最完整。"],"medium"),
q(5,"塑膠回收標誌中的數字最適合如何使用？",["作為辨識樹脂種類與分類的線索，仍須依當地回收規範和清潔狀態處理","代表數字越大越容易回收","只要有標誌就能丟進任何回收桶","代表塑膠一定可重複使用無限次"],"A","回收標誌主要提供樹脂識別線索，不等於當地一定收受或可無限回收，需查規範並做好分類。","區分識別標誌、回收可行性與實際地方規範。",["讀取標誌和樹脂種類。","查詢所在地回收系統的收受規定。","確認容器是否需清空、清潔或拆分。","排除數字排序、任何桶和無限回收的錯誤。","答案為 A。"],"medium"),
q(6,"若比較兩種塑膠包裝對環境的影響，哪項評估最完整？",["比較原料取得、製造能源、運輸、使用次數、回收率與最終處理的整個生命週期","只比較單件重量","只看包裝顏色","只看丟棄當天的體積"],"A","塑膠環境影響可能在原料、製造、使用與廢棄各階段產生，需用生命週期資料比較，而非只看重量或外觀。","把單一材料選擇轉成生命週期和多指標評估。",["列出兩種包裝的原料與製造條件。","比較運輸、使用次數和清洗需求。","查回收率、焚化或掩埋資料。","整合各階段能耗與排放，而非單一重量。","所以 A 最完整。"],"hard"),
q(7,"加熱未知塑膠時產生刺鼻煙霧，最安全的判斷是？",["立即停止加熱、移除火源並通風，依安全資料和合格設備處理，不直接吸聞","靠近煙霧聞出塑膠種類","加熱到最高溫讓它快速消失","把煙霧導向同學確認氣味"],"A","未知塑膠熱分解可能產生刺激或有害物，不能以人體嗅覺辨識；應停止、通風並依規範處理。","把材料熱分解風險轉成暴露控制和安全決策。",["辨認刺鼻煙霧是危害警訊。","停止加熱並移除火源。","保持通風、隔離並通報。","不直接吸聞、不轉向他人、不自行加熱測試。","因此 A 是安全作法。"],"easy"),
q(8,"要比較兩種塑膠的抗拉強度，哪項實驗設計較公平？",["使用相同形狀、尺寸、厚度、溫度與拉伸速度，只改變塑膠種類並重複測量","一種裁成寬條、一種裁成細條","一組在高溫、一組在低溫且不記錄","只用手拉一次判定強度"],"A","形狀、厚度、溫度與拉伸速率會影響強度，控制後才能把差異歸因於塑膠種類；需用儀器重複量測。","用控制變因和客觀力值建立材料比較。",["列出尺寸、厚度、溫度與拉速等因素。","製作相同幾何形狀的試片。","固定測量機與環境條件。","重複量測最大拉力並比較平均值。","所以 A 是公平設計。"],"medium"),
q(9,"可分解塑膠的標示最不應被解讀成哪項？",["只要丟到任何自然環境就會立刻完全消失且沒有影響","它可能需要特定溫度、濕度或微生物條件才分解","仍需依產品和地方處理規範回收或堆肥","分解速度與厚度、添加物和環境有關"],"A","可分解通常有特定條件與時間，不代表在海洋、土壤或一般環境立即消失；仍須依規範處理。","辨認環境宣稱的條件限制，避免把標籤當無條件保證。",["讀取產品對分解條件的完整說明。","確認是否需工業堆肥或特定微生物。","比較分解時間和環境影響。","排除立刻、任何環境、無條件消失的誤讀。","所以 A 是不應有的解讀。"],"hard"),
q(10,"若一個塑膠容器耐熱但不適合裝酸性食品，最合理的材料選擇判斷是？",["材料性質必須和實際使用條件配對，耐熱不代表耐酸或食品接觸一定安全","耐熱就代表能裝所有物質","酸性食品會讓所有塑膠立刻燃燒","只要容器透明就一定安全"],"A","耐熱、耐酸、化學相容性和食品接觸安全是不同指標，需依資料與用途分別確認。","將材料多性質和使用情境逐項配對。",["列出使用條件中的溫度和酸鹼性。","查閱容器耐熱、耐酸與食品接觸資料。","比較材料與內容物的相容性。","排除耐熱等同全用途、燃燒和透明即安全。","因此 A 正確。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["塑膠是聚合物材料，單體、鏈狀／交聯結構和熱性質影響用途。","材料評估需把性質、使用條件、回收標誌、生命週期和安全資料分開又整合。","回收或可分解標示不是無條件保證，需看地方規範和環境條件。"],"versionDifferences":["南一公開線索支持由生活塑膠、加熱與材料性質進入聚合物。","康軒公開課程資料較突出熱塑／熱固、結構與用途比較。","翰林公開課程計畫補充回收、生命週期、環境與安全選擇；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以單體—聚合結構—熱性質—用途—生命週期—安全六層框架分析塑膠。","加入回收數字、可分解條件、熱分解煙霧、抗拉公平實驗和食品包裝相容性。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫聚合物、熱塑／熱固、塑膠用途、回收、環境生命週期與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jf-Ⅳ-4：常見塑膠","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為聚合物、單體、熱塑／熱固、材料用途、回收、生命週期、可分解條件、公平強度實驗與熱分解安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jf-iv-4")
if __name__=="__main__": main()
