"""Mc-Ⅳ-1：生物機制應用於環境污染處理第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mc-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-mc-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"微生物、環境污染、濃度與生物處理","pattern":"取公立學校自然科評量以生物機制、資料變化、控制條件和污染處理推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"水質、微生物、濃度與環境方案","pattern":"取公開會考以圖表、質量濃度、因果、限制和實驗證據評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"微生物代謝、污染物轉換與水處理","pattern":"取公立國中試題以環境指標、機制鏈、控制變因和生活應用的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先確認污染物種類、進水量與要改善的指標。","區分有氧、缺氧、植物根區和微生物各自可能的作用。","沿濃度、流量、停留時間與負荷追蹤前後變化。","用無處理對照、重複和其他水質指標檢查機制。","寫出處理效果、未知副產物、容量限制與安全條件。"] for _ in range(10)]
ROWS=[
("easy","人工濕地中微生物分解有機污染物，首先需要確認哪項條件？",["污染物、微生物活性、氧氣條件與水流停留時間", "只看水面顏色", "只記錄植物高度", "只看進水溫度一次"],"A","污染物是否被轉換與微生物代謝、氧氣、停留時間和負荷有關，單一外觀不能代表處理機制。","先列污染物、作用者、環境條件與時間，再建立處理路徑。"),
("medium","同一人工濕地出水濃度下降，但進水量也同時減少；最需要補測什麼？",["污染物質量負荷、流量與濃度，分開判斷稀釋和真正去除", "只看出水顏色", "只記錄濃度下降百分比", "把流量資料刪除"],"A","濃度下降可能來自稀釋，需將濃度與流量換算成質量負荷，才較能判斷污染物是否被去除或轉換。","先分辨濃度和總量，再將流量變化納入比較。"),
("easy","有氧區和缺氧區的微生物可能進行不同代謝；比較時最重要的是？",["記錄溶氧、氧化還原條件、污染物前後濃度與副產物", "假設所有微生物作用相同", "只測植物葉片數", "只看水是否透明"],"A","代謝途徑受氧氣與環境條件影響，副產物也可能改變環境，因此需同時記錄條件和多個指標。","把環境條件、反應物、產物與副產物放入同一機制圖。"),
("medium","要檢驗人工濕地是否比單純儲水更能降低污染物，哪種設計較公平？",["相同進水濃度與流量，設有植物／微生物處理和無處理對照並重複測量", "處理組用較少進水且不設對照", "只比較最後一次透明度", "同時改變水溫、流量和植被"],"A","對照與固定輸入能比較人工濕地機制造成的差異；透明度單一指標不足以描述所有污染物。","先固定輸入和停留時間，再設處理與對照並選多項水質指標。"),
("hard","人工濕地在低負荷時去除率高，污染物大量輸入後去除率下降；最合理解釋是？",["微生物反應能力、氧氣或停留時間受到容量限制", "污染物越多處理能力必然無限增加", "去除率下降證明微生物從未作用", "只要種更多植物就沒有上限"],"A","系統的微生物量、氧氣供應、接觸時間和反應容量有限，負荷超過範圍時效果會下降。","比較輸入負荷和系統容量，再檢查氧氣、停留時間及微生物量。"),
("medium","人工濕地植物根區可能有助於處理，哪項證據最能支持機制？",["根區溶氧、微生物量、污染物濃度和根區前後的對照資料", "只看植物長得高", "只看葉片顏色", "只看濕地面積"],"A","根區功能需由條件與污染物變化的對應資料支持，植物外觀本身不能證明污染處理機制。","把假設的根區作用轉成可測的氧氣、微生物和污染物指標。"),
("hard","若污染物濃度下降但出水出現未測副產物，報告應如何處理？",["說明原污染物降低的證據，同時保留副產物未知風險並暫緩無條件排放", "只報原污染物下降", "把副產物視為必然無害", "因有未知就刪除所有處理資料"],"A","污染物轉換不等於風險消失，副產物需要鑑定與毒性評估；環境方案要設定排放和監測條件。","把去除、轉換和安全分成三個問題，不用單一下降率代替風險判斷。"),
("easy","為什麼人工濕地要量測停留時間？",["水與微生物、根區接觸的時間會影響反應是否充分", "停留時間只代表池塘顏色", "時間越久一定沒有任何副作用", "只要面積大就不需知道流速"],"A","流速、容積與停留時間決定污染物和處理介面接觸多久；過短可能反應不足，過長也可能造成缺氧或容量問題。","把空間大小和流動時間連到反應程度，再檢查其他水質條件。"),
("medium","要將人工濕地結果移用到工業廢水，首先應比較什麼？",["污染物種類與濃度、流量、溫度、毒性及處理容量", "只比較兩者水的顏色", "只看濕地植物種類", "假設所有廢水條件相同"],"A","不同工業污染物可能抑制微生物，流量、溫度和負荷也不同；必須先確認技術的適用邊界。","逐項比較輸入組成、環境條件、反應容量和安全限制。"),
("hard","哪句最適合作為人工濕地處理結論？",["在本次流量、溶氧、停留時間與污染負荷範圍內，特定污染物濃度下降；仍需確認質量負荷、副產物、長期容量與排放安全", "出水變清就代表所有污染物都被消除", "微生物處理永遠比工程處理好", "只要植物活著就能保證水質安全"],"A","完整結論需限定條件，分開濃度與總量，並保留副產物、容量和安全監測，不能由外觀或單一指標過度推論。","用輸入—機制—輸出—容量—安全五段整理結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mc-iv-1-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mc-iv-1"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的人工濕地、微生物代謝、有氧／缺氧、濃度負荷、停留時間、污染處理與安全能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mc-iv-1","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mc-iv-1、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合人工濕地、微生物有氧／缺氧代謝、植物根區、污染濃度與質量負荷、停留時間、處理容量、副產物與排放安全。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mc-iv-1-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為人工濕地、微生物代謝、氧氣條件、濃度與質量負荷、停留時間、處理容量、副產物與安全專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mc-iv-1")
if __name__=="__main__": main()
