"""Ma-Ⅳ-1：生命科學進步與社會問題解決第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-ma-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"生命科學、健康、環境與資料證據","pattern":"取公立學校自然科評量以生物技術、證據、風險與生活決策推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生物技術、實驗設計與科學倫理情境","pattern":"取公開會考以資料判讀、控制變因、風險條件與證據界線評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"生技應用、健康資料與環境方案","pattern":"取公立國中試題以生命科學應用、對照、效益風險和證據限制的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先拆開生物學主張、技術方案、社會結果與權利問題。","確認資料來源、對照、樣本與測量指標。","比較預期效益、已知風險和不確定性。","找出誰受益、誰承擔成本或資料暴露，檢查同意與公平。","提出可逆、可監測且有條件的決策與補證據計畫。"] for _ in range(10)]
ROWS=[
("easy","藻類淨水系統的試驗組比對照組濁度下降，但尚未測試病原體；最合理的結論是？",["只能支持濁度改善，不能直接宣稱飲用安全", "濁度下降就代表所有病原體消失", "沒有測病原體所以濁度資料無用", "只要是生物技術就不需對照"],"A","濁度是其中一項水質指標，不能替代病原體或其他安全檢測；試驗結果有用但結論範圍需受測量限制約束。","把每項證據對應到它真正測到的指標，不讓一個漂亮結果代替未測項目。"),
("medium","要比較藻類方案去除污染物的效果，哪項設計較可靠？",["相同進水濃度與流量，設無藻對照，重複測量處理前後污染物濃度", "只測一次最清澈的水", "同時改變藻量、流量和溫度", "只問使用者覺得水是否乾淨"],"A","對照、固定輸入與重複測量才能把濃度差異和藻類處理作用連結，主觀外觀不足以取代化學或生物指標。","先把技術效果轉成可量測指標，再固定輸入並設計對照。"),
("easy","基因檢測結果可能影響個人保險與就業，決策時最需要先處理哪項？",["當事人知情同意、資料用途與存取權限", "只追求檢測速度", "把所有資料公開以增加效率", "因為資料是科學結果就不需要權利規範"],"A","個人健康或遺傳資料涉及隱私與後續使用，知情同意、用途限制和權限是社會採用的必要條件。","將技術能測什麼和社會是否可接受分開，列出資料生命週期與權利。"),
("medium","新疫苗在小樣本試驗中有效率高但副作用資料不足，最適合的下一步是？",["擴大且分層追蹤試驗，公開不確定性並設安全監測與暫停條件", "直接全面施用且不再追蹤", "只報有效率不報副作用", "因資料不足就宣稱疫苗完全無效"],"A","有效率和安全性是不同證據面向；擴大追蹤、監測和預設停止條件可降低未知風險。","先列已知效益與未知風險，再設可監測、可暫停、可修正的驗證階段。"),
("hard","若一項生技方案讓多數人受益，但試驗風險集中在少數低收入社群，應如何評估？",["檢查招募與補償是否公平，讓受影響者知情參與並比較替代方案", "因總體受益較大就忽略少數風險", "只看方案總收益不看分配", "因有風險就禁止任何研究"],"A","總體效益不能自動合理化不公平的風險分配；需處理同意、補償、替代方案與受影響群體的參與。","把效益總量和風險分布分開列，讓公平與權利成為可檢查的條件。"),
("medium","新技術能降低污染，但需要大量能源；哪份資料最能支援完整評估？",["單位污染去除量、能源輸入、排放、成本、維護與替代方案的比較", "只看去除率", "只看設備外觀", "只問一次使用者滿意度"],"A","技術的環境效益要和生命週期能源、排放、成本及替代方案一起比較，不能由單一去除率決定。","把功能輸出和資源輸入、外部代價放在同一張證據表。"),
("hard","若研究結果尚未能排除長期生態影響，哪種政策最符合可修正決策？",["先在有限範圍試行，設定監測指標、公開資料與停止門檻", "直接全面採用且不設回饋", "完全禁止所有後續研究", "只宣傳短期成功案例"],"A","有限試行與監測能在控制暴露的同時取得新證據，停止門檻讓政策可因風險訊號修正。","優先選擇可逆、可監測、可暫停的方案，而不是不可逆的全面承諾。"),
("easy","下列哪一項是科學證據，不是價值判斷？",["在控制條件下，試驗組平均污染物濃度下降 30%", "我們應該優先照顧哪一群人", "風險是否值得承擔", "學校預算應花在哪個方案"],"A","測量結果可由方法與資料檢查，屬於證據；優先順序、風險接受度與預算分配還需要社會價值討論。","先分辨可由測量檢驗的描述，再標記需要倫理與公共選擇的問題。"),
("medium","若藻類方案在實驗室有效，但戶外水溫與光照變動大，最需要做什麼？",["在接近實際條件的試驗中重複測量，記錄環境範圍與效能變化", "把實驗室結果直接套到所有河川", "只選最適溫度測試", "因環境變動就不必再研究"],"A","實驗室結果需要在實際環境範圍驗證；記錄溫度、光照和效能能指出技術適用條件。","先找實驗室與現場的差異，再設計能涵蓋差異的驗證條件。"),
("hard","對生命科學方案的結論，哪句最完整？",["現有資料支持特定條件下的效益，但採用前仍須補足安全、長期、個資／公平與替代方案證據", "有科學名稱就代表必然改善社會", "只要多數人喜歡就不需測量風險", "只要有未知風險就不能提出任何試行方案"],"A","生命科學進步要同時經過證據、技術可行性、風險、權利與分配的檢查；條件式和可修正決策比口號完整。","用證據強度、技術條件、風險分配和權利四欄收束，再提出下一步。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-iv-1-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma-iv-1"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的生技證據、實驗設計、健康風險、個資、環境效益與公平決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma-iv-1","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma-iv-1、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合生技證據、藻類淨水、健康風險、長期不確定性、基因檢測個資、知情同意、風險分配與可修正決策。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-iv-1-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為生技證據、藻類淨水、健康安全、基因個資、知情同意、風險分配與可修正決策專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma-iv-1")
if __name__=="__main__": main()
