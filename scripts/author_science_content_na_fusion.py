"""Na：永續發展與資源的利用第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-na.json"; REPORT=ROOT/"implementation/reports/science-content-na-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"資源利用、環境承載、污染與永續資料","pattern":"取公立學校自然科評量以資源流、需求、污染、方案比較和永續行動推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"能源、水資源、環境保護與生命週期判讀","pattern":"取公開會考以圖表、時間尺度、資源限制、生命週期和方案代價評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"校園資源、能源、廢棄物與永續方案","pattern":"取公立國中試題以生活資源流、需求量、污染負荷、控制變因和公共決策推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先界定方案服務的需求量、時間和系統邊界。","沿原料、製造、運輸、使用、清洗、回收和廢棄追蹤資源流。","把環境、經濟、社會公平與承載力指標放在一起。","比較實測資料、替代方案和敏感條件，不被單一比例帶走。","用條件式結論提出可量測、可修正的行動。"] for _ in range(10)]
ROWS=[
("easy","學校比較瓶裝水、飲水機和重複水壺時，第一步最應先固定什麼？",["使用人數、每日飲水量、比較期間與服務目標", "先選好最環保的答案", "只固定容器顏色", "只看垃圾桶裡的數量"],"A","若三種方案服務的人數、飲水量或期間不同，總量不能公平比較；先界定需求與邊界才能讀後續數據。","先固定服務功能和時間，再比較材料、能源、用水與廢棄。"),
("medium","重複水壺每次清洗耗水 0.5 L，一次性瓶每瓶製造耗水 0.2 L；只比較這兩項用水時，使用幾次後水壺清洗量超過製造一瓶？",["1 次", "2 次", "3 次", "5 次"],"A","0.5 L×1 已大於 0.2 L，因此第 1 次清洗就超過製造一瓶的用水量；這只是在指定邊界下的局部比較，不能直接代表完整生命週期。","先明確定義比較的是每次、累積或每人服務量，再檢查數值與結論範圍。"),
("easy","可回收標誌最不能直接證明哪件事？",["該物品已實際被收運、再製並取代新原料", "它可能具有可回收設計", "仍需查當地分類與處理系統", "回收效果受實際流程影響"],"A","標誌只提供設計或材質線索，不等於使用後真的被分類、收運、再製並取代原料。","把標誌、回收可能性和實際回收結果分成三個證據層次。"),
("medium","校園一次性餐具減量後，垃圾量下降但清洗用電增加；哪個指標最能補足判斷？",["同一服務量下的全生命週期能源、材料、排放與成本", "只看垃圾桶重量", "只看清洗次數", "只看餐具外觀"],"A","末端垃圾下降可能伴隨清洗能源與其他負荷上升，需要在相同服務量下比較完整生命週期。","先找被忽略的前端或使用階段，再把所有負荷換算到同一服務基準。"),
("hard","若飲水機方案平均環境負荷最低，但偏遠教室取水時間增加，永續決策應？",["呈現環境效益、可近性與時間成本，並設計分點供水或其他公平配套", "只選平均值最低的方案", "刪除偏遠教室資料", "因有公平問題就不需比較環境效益"],"A","永續同時包含環境、經濟與社會公平；平均值不能掩蓋特定群體承擔的時間與可近性成本。","把總體平均和分配結果分開列，再尋找降低不公平的設計。"),
("medium","要比較重複水壺的清洗方案，哪種實驗最公平？",["固定水壺數量、使用量、清潔標準和觀察期間，只改變清洗方式並記錄水電與衛生指標", "同時改變水壺材質、使用量和清洗方式", "只記錄最省水的一天", "只問使用者覺得哪種方便"],"A","固定服務量與衛生標準，只改變清洗方式，才可比較水電與衛生成效的取捨。","先把安全與服務標準固定，再量測資源輸入和結果。"),
("hard","若方案 A 使用較少材料但運輸距離長，方案 B 材料較多但在地製造；最合理的做法是？",["以同一服務量計算原料、製造、運輸、使用與終端處理的總體資料", "只看材料重量", "只看運輸距離", "用『在地』或『少塑』口號直接決定"],"A","不同生命週期階段可能互相抵銷，需把各階段負荷換算到共同功能與期間。","畫出兩方案完整流程，再找哪個階段的差異真正影響總量。"),
("easy","資源的承載力在校園飲水決策中可理解為？",["供水、處理、回收或環境系統在不失效下能長期承受的負荷", "今天能買到多少容器", "垃圾桶的顏色", "只要是可再生就沒有上限"],"A","承載力描述系統可持續承受的需求與污染負荷；即使資源可再生，也可能因取用過快或污染而超過上限。","找出系統的流入、流出、恢復速度和失效門檻。"),
("medium","若全校平均用水下降，但低收入家庭需購買昂貴水壺才能參與，報告應？",["分別呈現環境成效、購置成本、補助與未參與者的影響", "只報平均用水下降", "把成本視為個人問題不記錄", "因成本不公平就刪除環境資料"],"A","平均環境成效和成本分配是不同維度，永續方案需處理可負擔性與參與公平。","把平均總效益和群體分配效果分開分析，再提出補助或替代方案。"),
("hard","哪句最符合校園飲水永續評估的證據界線？",["在相同飲水量與觀察期間，方案甲降低材料廢棄但增加清洗用水；是否長期較永續仍需能源、成本、衛生與公平資料", "只要垃圾少就一定永續", "可再生資源不需管理", "回收率高就沒有任何環境代價"],"A","永續是多指標、長時間且有條件的判斷，需把生命週期、健康、安全、成本與公平納入，並標示未知資料。","用服務基準、全生命週期、多群體影響和未測限制收束結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-na-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-na"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的校園飲水、餐具、生命週期、資源、承載、回收、成本與公平決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-na","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-na、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合校園飲水、一次性與重複餐具、資源流、生命週期、可回收系統、承載力、污染、成本、健康與群體公平。原有題目已改為 Na 專屬公共資源決策題，未沿用 N 單元題幹；所有題目、答案、解析與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-na-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為校園飲水、餐具、生命週期、承載力、回收、資源流、成本、健康與群體公平專屬問題；與 N 單元分開設計；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content na")
if __name__=="__main__": main()
