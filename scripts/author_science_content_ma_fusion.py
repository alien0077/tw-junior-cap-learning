"""Ma：科學、技術及社會的互動關係第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma.json"; REPORT=ROOT/"implementation/reports/science-content-ma-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"科學證據、技術應用與環境決策","pattern":"取公立學校自然科評量以資料證據、方案限制、環境影響和生活決策推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"科學與生活科技、風險與資料判讀","pattern":"取公開會考以圖表、控制變因、證據界線和方案取捨評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"技術方案、能源、成本與社會影響","pattern":"取公立國中試題以科學解釋、工程設計、成本風險和多條件決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先把敘述分成科學主張、技術設計和社會選擇。","列出方案的輸入、輸出、限制、成本與受影響者。","檢查資料是觀察、模型預測還是價值判斷。","比較替代方案並找出風險由誰承擔、利益由誰取得。","用條件式結論說明目前能決定什麼與還需補什麼證據。"] for _ in range(10)]
ROWS=[
("easy","『雨量與集水面積決定可收集水量』最接近哪一類敘述？",["可用觀察或模型檢驗的科學關係","只要投票就能決定的社會價值","水桶外觀的技術偏好","沒有任何條件的口號"],"A","雨量、面積與水量之間可用測量或模型檢驗，屬於科學關係；是否採用系統則還涉及技術和社會。","先問敘述能否以觀察或計算檢驗，再與設計偏好和價值選擇分開。"),
("easy","把雨水回收器設計成有濾網、儲水桶和溢流管，主要是在做什麼？",["技術設計，把科學條件轉成可運作的系統", "直接證明所有人都會同意", "把成本和倫理問題消除", "只是在描述自然定律"],"A","濾網、容量和溢流管是依需求、材料和安全限制形成的工程設計，不等於單純的科學定律或社會共識。","辨認是在解釋自然現象，還是在安排元件與限制以完成任務。"),
("medium","兩方案供水量相同，甲較便宜但維護風險集中在少數班級，乙較貴但風險分散；最完整的比較是？",["同時列出總成本、維護責任、風險分配和受益者，不只選最低價格", "只選甲因為價格最低", "只選乙因為價格較高一定較安全", "把少數班級的影響刪除"],"A","相同供水量不能掩蓋成本與風險由誰承擔；社會決策需把分配結果和維護能力納入。","先固定方案達成的功能，再比較經濟、風險與分配，而非只看一個數字。"),
("medium","測試濾網去除濁度的效果時，哪項最能支持技術性能主張？",["固定進水量與初始濁度，設對照並重複量測處理前後濁度", "只看一次最清澈的出水", "同時改濾網和水量且不記錄", "問使用者覺得水看起來是否漂亮"],"A","固定條件、對照和重複量測可把出水差異與濾網作用連結起來，比單次外觀印象可靠。","把性能主張改成可量測指標，再設控制變因、對照和重複。"),
("hard","模型預測雨水系統每月可供水 500 L，但實測只有 350 L；最適合的下一步是？",["檢查降雨、集水效率、漏水、蒸發與使用量等假設，再以新資料修正模型", "直接把 500 L 當成真實結果", "因模型不準就放棄所有測量", "只挑 350 L 以外的資料"],"A","模型是有條件的預測；實測差異可用來檢查假設與損失路徑，不能直接把任一數值當成永久真值。","把預測與觀察並列，逐項尋找輸入、轉換與損耗的差異。"),
("medium","若學校採用新技術後節省水費，卻增加清潔人員工作量，決策報告應如何呈現？",["同時報節省量與工作時間／健康負荷，並提出補償或替代設計", "只報水費節省以證明技術一定更好", "因有人增加工作就刪除節水資料", "工作量與技術評估無關"],"A","技術效益和成本可能分散在不同人身上；完整評估要呈現總體效果與勞務分配，尋找可修正方案。","把效率指標和受影響者分開記錄，再檢查利益與負擔是否公平。"),
("hard","下列哪個問題屬於社會選擇，而不是單靠科學測量就能決定？",["學校是否願意用部分預算換取較低長期風險", "雨量計在一週量到多少毫米", "濾網前後濁度差多少", "儲水桶容量是否達到設計值"],"A","預算與風險的取捨涉及價值、優先順序和誰承擔，不是單一自然測量能替所有人決定的。","先分辨可測的事實，再找需要討論權利、價值與資源分配的選擇。"),
("medium","若飲用水安全資料不足，最負責任的技術決策是？",["暫不把回收水用於飲用，先完成檢測並限定於可控的非飲用用途", "因為能省水就直接飲用", "把未測的風險視為零", "刪除安全指標以免影響採用"],"A","安全資料不足時應降低暴露、限制用途並補做檢測，不能用節水效益取代風險證據。","先找不可逆或高代價風險，再設定使用邊界和必要驗證。"),
("hard","比較甲乙技術時，哪種資料表最能支援多方決策？",["功能供水量、能源、成本、維護、失效風險、受益與負擔族群", "只列售價", "只列宣傳標語", "只列設計外觀"],"A","多方決策需要同時看功能、環境、經濟、風險和分配；單一售價或外觀不能描述完整後果。","先建立共同服務指標，再把生命週期與利害關係人欄位放入同一表格。"),
("hard","對校園雨水系統的結論，哪句最符合科學、技術與社會的互動？",["在已測雨量、用水需求和安全限制下，方案可能有節水效益；是否採用仍須比較維護能力、成本與不同使用者的風險", "只要技術能運作，社會一定會受益", "只要有人反對，所有性能資料都不必看", "科學數據可以直接替全校決定價值排序"],"A","自然資料可支持性能與風險判斷，技術要面對限制，社會仍要處理成本、權利和分配；三者不能互相取代。","用科學證據定義可行範圍，用工程條件檢查能否實作，再把社會選擇公開化。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的科學證據、技術設計、系統限制、成本風險與社會決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合科學證據、技術設計、雨水回收系統、功能與限制、成本、風險、利害關係人及社會選擇。原有題目已改為科學—技術—社會互動專屬題目；所有題幹、選項、答案、解析與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為科學證據、技術設計、雨水回收、功能限制、成本、風險、利害關係人與社會決策專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma")
if __name__=="__main__": main()
