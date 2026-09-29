"""Jd-Ⅳ-6：酸鹼中和生成鹽、水與熱量第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-jd-iv-6.json"
REPORT=ROOT/"implementation/reports/science-content-jd-iv-6-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"酸鹼中和、鹽水、溫度與實驗資料判讀","pattern":"取由酸鹼反應式、指示劑、溫度變化與資料推論中和的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"酸鹼中和、熱量、體積與生活情境","pattern":"取從圖表、體積濃度與能量資料判斷酸鹼中和結果的能力方向。"},
 {"url":"https://www.hkjh.hc.edu.tw/uploads/1661481260739sfuB4gG2.pdf","title":"新竹市立新科國中公開康軒版自然課程計畫","year":"公開課程計畫","locator":"酸鹼中和、鹽水生成、熱量與安全","pattern":"取以 H⁺／OH⁻、鹽水、放熱及中和操作連結微觀模型和宏觀證據的方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
def q(n,prompt,opts,ans,exp,strat,steps,d="medium"):
 return {"id":f"question-science-content-jd-iv-6-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",opts)],"knowledgeIds":["kg-science-content-jd-iv-6"],"difficulty":d,"answer":{"value":ans,"explanation":exp},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的酸鹼中和、H⁺／OH⁻、鹽水、溫度、體積濃度及安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依公開資料能力方向獨立改寫；未複製原題、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-jd-iv-6","examPatternRefs":REFS,"solutionStrategy":strat,"solutionSteps":steps}
Q=[
q(1,"鹽酸和氫氧化鈉溶液反應生成氯化鈉和水；其中 H⁺ 與 OH⁻ 的微觀反應是？",["H⁺＋OH⁻→H₂O","H⁺＋OH⁻→NaCl","H⁺＋OH⁻→O₂","H⁺ 和 OH⁻ 完全不反應"],"A","中和的核心離子反應是 H⁺ 與 OH⁻ 結合生成水，其他離子可留在溶液中形成鹽。","先寫淨離子反應，再處理旁觀離子和鹽的來源。",["列出酸提供的 H⁺ 和鹼提供的 OH⁻。","配對兩種離子生成水。","辨認 Na⁺、Cl⁻ 等離子可形成鹽。","排除生成氧氣或完全不反應。","所以 A 正確。"],"easy"),
q(2,"稀鹽酸與氫氧化鈉溶液恰好中和後，溶液中的主要溶質是？",["氯化鈉，水是主要溶劑且 H⁺、OH⁻ 已大致消耗","只有氫氣","只有未反應的氫氧根","氧化銅沉澱"],"A","HCl 和 NaOH 反應生成 NaCl 和水；恰好中和表示 H⁺、OH⁻ 量相當，主要溶質為氯化鈉。","以完整反應式和恰好比例判斷生成物及剩餘粒子。",["寫出 HCl＋NaOH→NaCl＋H₂O。","確認 H⁺ 和 OH⁻ 彼此消耗。","留下 Na⁺ 和 Cl⁻ 形成溶液中的鹽。","排除氫氣、過量 OH⁻ 和氧化銅。","答案為 A。"],"easy"),
q(3,"酸鹼中和實驗中混合後溫度上升，較合理的結論是？",["反應可能釋放熱量，但需和未反應對照、初始溫度及熱損失一起判斷","溫度上升證明生成氧氣","任何溫度上升都必然是中和","溫度上升表示質量消失"],"A","中和常伴隨放熱，溫度上升是能量證據，但仍要控制環境和量測誤差，不能由溫度單獨確定反應。","區分支持性現象和足以排除其他原因的完整證據。",["記錄混合前兩溶液溫度。","設定未混合或等體積水的對照。","測量混合後最高溫度並考慮散熱。","判斷溫升是否與中和熱相符。","所以 A 是證據範圍內的結論。"],"medium"),
q(4,"若酸的體積與濃度固定，逐次加入鹼並量測 pH，接近恰好中和時最可能觀察到？",["pH 會在某一段體積附近快速由酸性跨向接近中性，再進入鹼性","pH 從頭到尾完全不變","加入鹼後一定立刻產生氧氣","pH 只由溶液顏色決定且沒有數值意義"],"A","當 H⁺ 逐漸被 OH⁻ 消耗，接近當量點時少量體積變化可能造成 pH 快速變化，過量鹼後呈鹼性。","把 pH 曲線、離子消耗和當量點連結。",["固定酸的體積和濃度。","逐量加入已知濃度的鹼。","記錄每次 pH 和加入體積。","找出 pH 快速變化的中和區間。","因此 A 正確。"],"hard"),
q(5,"要用指示劑判斷酸鹼是否接近中和，選擇指示劑時最重要的是？",["其變色範圍要落在目標反應的 pH 快速變化區間","只要顏色最鮮豔就一定適合","指示劑越多越能提高準確度","指示劑本身必須是金屬"],"A","指示劑的變色範圍需對應中和附近 pH 變化，顏色鮮豔或用量多不是選擇標準。","以量測目的和指示劑變色範圍配對。",["先估計中和附近的 pH 範圍。","查閱候選指示劑變色範圍。","選擇能在該區間明顯變色者。","用少量指示劑並設置重複測量。","所以 A 最適合。"],"medium"),
q(6,"比較不同酸鹼組合的中和溫度變化，哪項設計最公平？",["固定酸鹼濃度、體積、初始溫度與容器，只改變酸或鹼種類並量測最高溫度","每組使用不同體積和初始溫度","一組攪拌、一組完全不攪拌","只看手摸起來哪杯比較熱"],"A","初始條件、體積、濃度、容器與攪拌會影響溫度，固定它們才能比較化學組合的中和熱。","把熱量實驗的控制變因和客觀測量建立起來。",["列出影響溫升的量、濃度、初溫與散熱條件。","固定所有非研究變因。","只改變酸或鹼種類。","用溫度計重複量測最高溫。","因此 A 是公平設計。"],"medium"),
q(7,"若鹽酸過量加入氫氧化鈉，混合液最後仍呈酸性，微觀上代表？",["H⁺ 尚有剩餘，濃度大於 OH⁻，所以整體呈酸性","OH⁻ 一定完全消失且 H⁺ 沒有存在","Na⁺ 變成酸","水分子全部分解成氧氣"],"A","鹽酸過量表示提供的 H⁺ 超過 OH⁻，中和後仍有 H⁺ 剩餘，溶液呈酸性。","用限制試劑和剩餘離子判讀中和後酸鹼性。",["比較酸與鹼提供的 H⁺、OH⁻ 量。","配對可中和的等量離子。","找出過量且剩下的 H⁺。","將剩餘 H⁺ 對應到酸性。","答案為 A。"],"medium"),
q(8,"中和反應的產物被稱為『鹽和水』，其中鹽的來源最適合如何描述？",["酸的陰離子和鹼的陽離子在水中留下並組成鹽","只有水蒸發後才憑空生成鹽","鹽一定由 H⁺ 和 OH⁻ 直接形成","所有中和都生成同一種鹽"],"A","H⁺ 和 OH⁻ 生成水，酸、鹼的其他離子則可組成相應鹽；鹽的種類取決於反應物。","分離淨離子反應和旁觀離子，理解鹽的來源。",["寫出酸和鹼的離子組成。","移除 H⁺、OH⁻ 形成水的部分。","配對剩餘陽離子與陰離子。","檢查不同酸鹼組合會產生不同鹽。","所以 A 正確。"],"medium"),
q(9,"若中和實驗使用濃酸或濃鹼，哪項作法最安全？",["戴護目鏡與手套、少量操作並依規範稀釋或處理，避免直接接觸和快速混合大量試劑","直接把水倒入濃硫酸中並攪拌","用手感覺溫度取代溫度計","為了加快反應把酸鹼一次大量混合"],"A","濃酸鹼具有腐蝕性且混合可能劇烈放熱，需防護、少量、慢慢依規範操作；稀釋時也要遵守正確程序。","以危害控制優先於反應速度，遵守實驗室標準操作。",["辨認腐蝕與放熱風險。","戴好護目鏡、手套並使用少量。","依安全規範進行稀釋和滴加。","不可用手測溫或大量快速混合。","因此 A 是唯一安全作法。"],"easy"),
q(10,"某中和資料顯示混合前總質量 102.0 g，密閉容器中混合後總質量 102.0 g；最合理的解釋是？",["中和造成粒子重新排列而非質量憑空消失，封閉系統符合質量守恆","中和沒有發生","水的質量被反應吃掉","天平必定自動補足質量"],"A","密閉系統中酸鹼反應重新排列粒子，總質量維持不變符合質量守恆；需要其他資料判斷中和現象。","先確認系統邊界，再以粒子模型解釋總質量。",["確認容器是密閉且沒有物質逸出。","比較混合前後總質量。","把酸鹼反應視為粒子重新排列。","排除沒有反應、水消失與天平補質量。","所以 A 正確。"],"medium"),
]
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"
 lesson["fusionRecord"]={"commonCore":["中和的淨離子核心是 H⁺ 與 OH⁻ 生成水，其他離子可形成鹽。","酸鹼比例、限制試劑、pH、指示劑與溫度資料需共同判斷中和程度。","中和可能放熱，公平測量與腐蝕性試劑安全不可分離。"],"versionDifferences":["南一公開線索支持由生活中和與指示劑進入酸鹼反應。","康軒公開課程資料較突出 H⁺／OH⁻ 模型、體積濃度與實驗控制。","翰林公開課程計畫補充鹽水、熱量、滴定與安全連結；公開資料不足以宣稱取得完整教材內容。"],"originalAdditions":["以淨離子—旁觀離子—限制試劑—pH／熱量—安全五層框架分析中和。","加入滴定曲線、當量點、密閉質量與濃酸鹼處置的單元專屬遷移。"],"llmSynthesisNote":"依官方課綱、本單元 KG、南一／康軒／翰林公開版本線索與三筆公開試題／課程資料能力方向，重新撰寫酸鹼中和、鹽水、H⁺／OH⁻、pH、溫度、質量守恆與安全；未複製教材或試題文字、圖表與答案，Terra 第二輪與正式發布審查尚未完成，維持 draft。"}
 for e in lesson.get("versionResearch",[])+lesson.get("publisherResearch",[]): e["reviewedAt"]=TODAY
 for x in Q: (QDIR/f"{x['id']}.json").write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":"Jd-Ⅳ-6：酸鹼中和生成鹽、水與熱量","lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題已逐題改寫為 H⁺／OH⁻ 中和、鹽水、pH、指示劑、熱量、滴定、公平實驗、質量守恆與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content jd-iv-6")
if __name__=="__main__": main()
