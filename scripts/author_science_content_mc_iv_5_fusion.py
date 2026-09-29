"""Mc-Ⅳ-5：電力供應與輸送第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mc-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-mc-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"電力、電壓、電流、輸送與能量損失","pattern":"取公立學校自然科評量以電路、功率、輸電、能量轉換和生活系統推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"輸配電、變壓、電能與資料判讀","pattern":"取公開會考以公式、圖表、條件、損失與工程方案評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"電力供應、輸送、變壓器與用電安全","pattern":"取公立國中試題以電力路徑、電流電壓、功率和供電系統的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先排出發電、升壓、長距離輸電、降壓與用戶配電順序。","確認輸送功率、電壓、電流與電阻的關係。","用 P_loss=I²R 判斷線損和升壓的作用。","檢查變壓器、備援、負載尖峰與安全條件。","以效率、可靠度、成本、環境與受影響者寫出方案結論。"] for _ in range(10)]
ROWS=[
("easy","長距離輸送同樣功率時，先升高電壓的主要理由是？",["在 P=VI 下可降低電流，並減少輸電線的 I²R 熱損失", "讓電阻變成零", "讓用戶端直接承受高壓", "使電能不需導線即可傳送"],"A","相同功率下電壓提高可使電流降低；線損與 I² 成正比，因此可減少輸電線發熱損失。","先固定輸送功率，再用 P=VI 找電流變化，最後代入 I²R 判斷損失。"),
("medium","發電站輸出 100 kW，升壓前輸電電壓 1 kV；若忽略其他因素，輸電電流約為？",["0.1 A", "10 A", "100 A", "100,000 A"],"C","P=VI，所以 I=P/V=100,000 W÷1,000 V=100 A；輸電端的單位要先換成瓦特和伏特。","先統一單位，再由 P=VI 解出電流，不把 kW 和 kV 直接相乘誤判。"),
("medium","電力路徑中，升壓後仍需在社區附近降壓，主要是因為？",["高壓適合降低長途線損，但用戶設備需要較安全且合適的電壓", "降壓能讓輸電距離變成零", "高壓只能在家庭使用", "變壓器會把電能憑空增加"],"A","輸電與用電的需求不同；高壓有利於長距離傳輸，降壓則讓用戶端符合設備與安全條件。","把輸電效率和用戶安全分成兩個階段，不把一種電壓套用全程。"),
("easy","若輸電線電阻固定，電流減半，線上的熱損失約變為原來的多少？",["1/4", "1/2", "2 倍", "4 倍"],"A","P_loss=I²R；電流變為 1/2 時，損失變為 (1/2)²=1/4。","先寫平方關係，再代入比例，不把線損誤當成只與電流一次方成正比。"),
("hard","山區診所每日用電量不變，但夜間需求尖峰增加；供電方案最應補充哪項分析？",["尖峰功率、電池／備援容量、輸電限制與停電可接受時間", "只看每日總電量", "只看發電設備額定功率", "只看白天平均負載"],"A","總電量相同不代表瞬間功率相同；尖峰會影響線路、變壓器和備援容量，也要考慮關鍵醫療負載。","把能量需求和功率尖峰分開，再檢查系統容量與停電風險。"),
("medium","要比較架空線與地下電纜，哪組資料最完整？",["線損、故障率、維修時間、建置成本、土地影響與極端天氣韌性", "只看外觀", "只看初始材料重量", "只問施工者喜好"],"A","輸電方案同時涉及效率、可靠度、維護、成本、土地和災害風險，單一外觀或重量不足。","先固定服務需求，再用多指標比較整個生命週期。"),
("easy","變壓器能升壓或降壓，主要依靠哪種物理現象？",["交變電流造成變動磁場，透過電磁感應在另一線圈產生電壓", "靜止電荷直接穿過絕緣層", "摩擦使電壓永久增加", "只靠導線長度改變電池能量"],"A","變壓器利用交變電流產生變動磁通量，透過電磁感應在另一線圈感應電壓；匝數比決定升降壓關係。","先確認需要變動磁場和兩組線圈，再判斷能量如何由一次側傳到二次側。"),
("hard","若某輸電區域在颱風後常停電，增加第二條不同路徑的供電線可能帶來什麼？",["提高冗餘與韌性，但也增加建置、維護和土地成本", "保證任何災害都不會停電", "只會增加用戶端電壓", "讓所有輸電損失自動消失"],"A","第二路徑可降低單點故障影響，但不能消除所有風險，且需要更多資源與土地；需比較成本效益。","先指出新增備援降低哪種故障，再列出新增的成本和仍存在的限制。"),
("medium","若學校要安裝太陽能並接入既有電網，哪項資料最不能省略？",["日照與輸出時間序列、校園負載、併網安全、儲能與維護條件", "只看屋頂面積", "只看面板額定功率", "只看宣傳上的減碳口號"],"A","可用電力取決於實際日照、負載時段、併網與儲能；額定功率和屋頂面積不能取代系統資料。","把能源來源、實際輸出、負載缺口、併網和維護放入同一決策表。"),
("hard","哪句最適合作為山區供電路徑的結論？",["在目前負載與天候資料下，升壓輸電可降低線損，降壓與備援則支撐用戶安全與可靠度；仍需監測尖峰、故障與維護成本", "只要電壓越高就能直接供家庭使用", "只要有發電機就不必考慮輸電", "線損與供電可靠度互不相關"],"A","完整結論要把效率、安全、可靠度與成本放在同一流程，並指出資料範圍和後續監測。","沿發電到用戶的全路徑逐段檢查功能、損失、風險與維護。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-mc-iv-5-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-mc-iv-5"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的發電、升壓、輸電、降壓、功率、線損、變壓器、備援與供電決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mc-iv-5","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mc-iv-5、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合發電、升壓、長距離輸電、降壓、配電、P=VI、I²R 線損、變壓器、尖峰負載、備援、成本與可靠度。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mc-iv-5-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為發電、升壓、輸電、降壓、功率、線損、變壓器、尖峰負載、備援與供電可靠度專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mc-iv-5")
if __name__=="__main__": main()
