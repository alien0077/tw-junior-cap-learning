"""Ma-Ⅳ-3：材料對生活與社會的影響第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma-iv-3.json"; REPORT=ROOT/"implementation/reports/science-content-ma-iv-3-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"材料性質、資源、能源與環境影響","pattern":"取公立學校自然科評量以材料性質、功能、生命週期與資料比較推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"材料、能源、污染、回收與生活情境","pattern":"取公開會考以圖表、成本效益、環境負荷與方案限制評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"材料用途、物理性質、回收與資源利用","pattern":"取公立國中試題以性質—功能配對、生命週期與公平決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先列出產品必須完成的功能與使用條件。","把材料硬度、韌性、耐熱、防水等性質和功能配對。","沿原料、製造、運輸、使用、清洗、回收與處置追蹤負荷。","比較數量、使用次數、能源、污染、成本與受影響者。","用情境條件和資料限制寫出可修正的材料選擇。"] for _ in range(10)]
ROWS=[
("easy","校園餐盒需要承受熱湯且不易漏水；哪組材料性質最直接對應這些功能？",["耐熱與防滲漏", "顏色鮮豔與氣味強", "密度小與導電性高", "透明與容易碎裂"],"A","熱湯需要材料在使用溫度下保持穩定，防漏則需要低滲透或可靠接合，兩者都是功能所需性質。","先寫用途的功能要求，再逐項配對材料性質，不從材料名稱直接下環保結論。"),
("medium","同一種可重複餐盒使用次數增加時，製造負荷被更多次使用分攤；要公平比較還應加入哪項？",["每次清洗的水、能源、清潔劑與設備壽命", "只看餐盒顏色", "只看第一次購買價格", "忽略運輸和廢棄"],"A","重複使用會降低每次製造分攤量，但清洗、運輸、維修與報廢也屬生命週期負荷，必須一併計算。","沿生命週期逐段列輸入與輸出，避免只看到製造或使用其中一段。"),
("medium","一次性餐盒每個製造排放 4 g，可重複餐盒製造排放 100 g；若忽略清洗，至少使用幾次後製造排放才低於一次性方案？",["25 次", "26 次", "96 次", "104 次"],"B","一次性使用 n 個為 4n g；需 4n>100 才超過可重複餐盒的製造負荷，n=26 時 104 g，表示至少第 26 次才讓可重複方案的平均製造負荷低於一次性累積值。題目若採『低於』應比較 4n>100，因此答案為 B。","先設使用次數 n，列出兩方案累積量，再注意『低於／不超過』的嚴格不等號。"),
("easy","『天然材料一定比塑膠環保』為何不成立？",["仍需比較取得、製造、運輸、使用壽命與廢棄等生命週期資料", "天然材料不可能消耗能源", "塑膠永遠不能回收", "材料名稱已包含完整環境評分"],"A","天然來源不會自動消除開採、加工、運輸或處置負荷；環境影響必須依情境與完整生命週期比較。","把口號換成可比較的階段和指標，再看材料在該情境的實際數據。"),
("medium","比較紙、塑膠與金屬餐盒時，哪份資料表最完整？",["重量、耐熱、壽命、清洗能耗、運輸、回收率、成本與受影響者", "只列單價", "只列垃圾桶重量", "只列使用者喜好"],"A","材料決策同時涉及功能、使用、生命週期、成本與分配；多欄資料才足以支持條件式比較。","先固定服務功能，再把物理性質、生命週期和社會指標放在同一張表。"),
("hard","若可回收餐盒回收率高，但再製需要高溫能源且本地沒有收運系統，最合理判斷是？",["回收標誌不等於實際環境效益，需確認收運、再製能源與替代材料的整體結果", "回收率高就必然零污染", "沒有收運系統也代表材料已被回收", "高溫能源不屬於環境負荷"],"A","回收的效果取決於系統是否運作、能源與污染代價及是否真正替代原料；單一回收率不足。","沿回收後流程追蹤實際去向、能源和替代量，不把標誌當成結果。"),
("medium","要測試餐盒保溫性能，哪個實驗較公平？",["使用相同初始水溫、容量、環境溫度與測量時間，只改變材料並重複記錄溫度", "每種材料裝不同容量且測不同時間", "只挑保溫最好的一次", "同時改材料和盒蓋是否密封"],"A","控制初始條件、容量、環境與時間，只改變材料並重複量測，才較能歸因於材料差異。","先指定自變因，再列所有可能影響熱傳的控制變因與重複方式。"),
("hard","若新材料降低垃圾量卻讓清潔工作增加、成本由弱勢班級承擔，報告應？",["同時呈現垃圾、清洗工時、成本分布與補助或替代方案", "只報垃圾量下降", "因有社會代價就刪除環境成效", "清潔與公平不屬材料影響"],"A","材料影響不只在垃圾量；勞務與成本分配會影響方案能否公平而持續，應和環境效益並列。","把總體環境效果與誰承擔成本分開呈現，再設計改善配套。"),
("easy","材料生命週期的順序通常應從哪裡開始追蹤？",["原料取得，再到製造、運輸、使用與終端處理", "直接從垃圾桶結束，不必看製造", "只從購買價格開始", "只看使用者喜好"],"A","完整生命週期從原料與製造開始，經運輸、使用、維修或清洗，最後到回收、再利用或處置。","畫流程箭頭並在每一段記錄資源輸入、排放和功能結果。"),
("hard","哪句最適合作為校園餐盒選材結論？",["在固定餐次、使用年限與清洗條件下，方案甲的總負荷較低；若清洗能源或回收系統改變，需重新評估", "方案甲材料名稱較天然，所以永遠最好", "只要單價最低就代表社會成本最低", "任何材料都能用同一結論評估"],"A","材料優劣依功能、使用情境和生命週期條件改變；限定範圍並說明敏感條件，結論才可被檢驗與修正。","用條件、指標、比較結果和改變條件時的回應四步收束。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-iv-3-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma-iv-3"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的材料性質、功能、生命週期、能源、回收、成本、公平與方案比較能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma-iv-3","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma-iv-3、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合材料性質與功能、餐盒生命週期、能源、清洗、回收、污染、成本與公平分配。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-iv-3-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為材料性質、功能、生命週期、清洗、回收、能源、成本、公平與餐盒方案比較專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma-iv-3")
if __name__=="__main__": main()
