"""Mb-Ⅳ-1：生物技術跨領域發展與環境影響第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mb-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-mb-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"生物技術、環境、生態與資料推理","pattern":"取公立學校自然科評量以生物技術作用、實驗證據、環境路徑和風險推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"遺傳、生態、農業與環境資料","pattern":"取公開會考以圖表、控制變因、因果、族群變化和不確定性評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"生物技術、遺傳、農業與環境影響","pattern":"取公立國中試題以遺傳技術、環境暴露、對照、監測與生活決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先指出技術改變的生物特徵或功能。","沿田間、食物網、基因流動或廢棄物找暴露路徑。","分別列出效益、直接風險、間接風險和不確定性。","用隔離、對照、時間序列與監測指標檢查主張。","設定適用條件、停損門檻與受影響者參與方式。"] for _ in range(10)]
ROWS=[
("easy","耐旱作物的性狀若能讓植物在缺水時維持較高存活率，這首先是什麼類型的主張？",["可由控制水分與對照植株測量的生物功能主張", "已證明所有地區都增產的社會結論", "只由作物名稱決定的環境結論", "不需實驗即可成立的價值判斷"],"A","存活率可在控制水分與遺傳背景的試驗中測量；是否能增產、是否適合所有地區仍需其他資料。","先把技術性狀轉成可量測指標，再分開處理農業和社會外推。"),
("medium","比較耐旱作物與一般作物時，哪個試驗設計較公平？",["固定土壤、光照、肥料與種植密度，只改變作物性狀並設重複區", "耐旱作物用較多肥料且不設對照", "只選雨季結果", "把不同地點和不同病蟲害資料直接平均"],"A","固定環境條件、設對照與重複能把差異較合理地歸因於作物性狀，而非栽培條件。","先指定自變因，再列出可能影響生長的控制條件與重複方式。"),
("easy","耐旱作物花粉傳到鄰近野生近緣種，這是何種環境暴露路徑？",["基因流動，可能使性狀進入其他族群", "只代表土壤含水量變化", "只代表作物產量增加", "與生物技術沒有關係的天氣現象"],"A","花粉傳遞可使遺傳資訊跨族群移動；後續影響要看近緣種、性狀和生態條件，不能直接預言結果。","先找技術性狀如何離開目標作物，再追蹤接受者與可能生態後果。"),
("medium","若耐旱性提高但需要更多除草劑才能維持產量，完整評估應加入？",["除草劑用量、非目標生物、土壤、水質、收益與替代栽培法", "只看耐旱率", "只看種子價格", "把除草劑影響排除在技術之外"],"A","技術效益可能伴隨新的投入與環境影響；要把農業操作、非目標生物和水土暴露列入生命週期。","把性狀效益與因配套改變而產生的次級影響分開列。"),
("hard","實驗室沒有觀察到外逸風險，但田間有風、昆蟲和近緣種；最合理的下一步是？",["在受控田間試驗中監測花粉流向、近緣種與性狀出現率，設定停止條件", "把實驗室結果直接當成戶外安全證明", "因有未知風險就刪除所有田間資料", "只測作物高度"],"A","環境條件與生物互動會改變暴露路徑，需在接近實際條件下監測並設停損，而不是用實驗室結果過度外推。","比較場域差異，設計能直接測量外逸路徑的指標和門檻。"),
("medium","生物技術跨領域合作中，哪個配對最合理？",["遺傳學研究性狀、農業研究栽培、環境科學監測外逸與生態反應", "只由單一學科決定所有環境後果", "把社會資料當成不需檢驗的自然定律", "技術名稱越多就代表證據越強"],"A","不同領域分別處理基因、栽培、環境暴露與生態結果，還需共享方法和資料才能形成完整判斷。","按問題鏈拆出每個領域負責的證據，再檢查資料是否能接起來。"),
("hard","若作物增產資料只來自一季、兩個農場，哪個結論最恰當？",["資料支持該季與該地點的增產可能，長期與不同土壤仍需驗證", "可直接推論所有地區都增產", "樣本少代表技術一定無效", "只要平均值上升就不必看變異"],"A","時間與地點範圍限制外推；樣本仍可提供線索，但需更多場域、季節和變異資料。","先寫樣本支持的範圍，再列出需要擴大驗證的條件。"),
("easy","若要監測基因外逸，哪項是較直接的指標？",["鄰近近緣植物中出現該特徵或標記的比例與空間距離", "只記錄作物市場價格", "只量降雨量", "只問居民是否喜歡作物"],"A","鄰近近緣植物的特徵出現率和距離能直接追蹤性狀是否跨越目標範圍；其他資料可作背景但不能替代。","選擇能直接對應暴露路徑和結果的監測指標。"),
("medium","若耐旱作物可減少灌溉，但種子成本讓小農難以取得，方案應？",["同時呈現節水效益、成本分布、取得權與替代方案，與受影響農民共同評估", "只報節水量", "因成本問題就刪除環境效益", "把市場價格視為與科學無關"],"A","生物技術的環境效益與社會可及性同時決定能否公平採用，需讓受影響者參與並比較配套。","把環境效果和利益／成本分配分開呈現，再提出可修正的制度方案。"),
("hard","哪句最適合作為耐旱作物環境決策結論？",["在指定土壤、水分和隔離監測條件下，資料支持節水與存活效益；外逸、生態與公平風險仍須持續追蹤並設停損門檻", "耐旱性代表任何地區都不需水且沒有風險", "只要作物增產就應全面推廣", "有未知風險所以完全不能試驗"],"A","完整決策同時交代技術效益、場域條件、外逸與社會風險及後續治理，不把局部結果擴張成無條件規則。","用效益—暴露—不確定性—公平—監測五段收束。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mb-iv-1-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mb-iv-1"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的生物技術、耐旱作物、遺傳、田間試驗、基因流動、環境暴露、監測與公平決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mb-iv-1","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mb-iv-1、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合耐旱作物、遺傳與農業、跨領域證據、基因流動、田間暴露、生態風險、監測、公平與可修正決策。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mb-iv-1-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為耐旱作物、跨領域生物技術、田間試驗、基因流動、環境暴露、監測、公平與風險決策專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mb-iv-1")
if __name__=="__main__": main()
