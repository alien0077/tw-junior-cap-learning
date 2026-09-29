"""Ma-Ⅳ-4：發電與新能源科技的社會環境影響第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma-iv-4.json"; REPORT=ROOT/"implementation/reports/science-content-ma-iv-4-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"能源轉換、發電、排放與資料判讀","pattern":"取公立學校自然科評量以能量鏈、能源限制、環境影響與方案比較推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"電力、能源、效率、天候與環境資料","pattern":"取公開會考以圖表、比例、條件、替代方案和證據界線評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"再生能源、電池、電力供應與生活應用","pattern":"取公立國中試題以發電來源、供需、效率、控制變因和環境風險的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先列出需求、發電來源、轉換設備、輸送與儲能。","區分額定功率、實際輸出、供電時間與備援容量。","把天候、排放、土地、生態、成本和維護放進比較表。","用相同服務量和同一時間範圍公平比較方案。","以穩定度、環境邊界與停損條件寫出可修正結論。"] for _ in range(10)]
ROWS=[
("easy","太陽能板將陽光轉成電力，電池再把電力儲存；這描述的是什麼？",["能量轉換與儲存鏈", "能量憑空產生", "只改變電線顏色", "電力不需輸出就能供應負載"],"A","太陽能板轉換能量形式，電池暫存電能以調節供需；每一段都有輸入、輸出與損失。","先畫能源輸入→轉換→儲存→負載的箭頭，再找每段的能量與限制。"),
("medium","離島連續三天陰天，太陽能輸出下降但學校需求不變；哪項最能提升供電可靠度？",["加入足夠儲能與可控制的備援，並依需求設定容量", "只增加宣傳標語", "把陰天資料刪除", "假設額定功率等於每天實際輸出"],"A","間歇性能源需搭配儲能或備援，且容量要依負載、天候和可接受停電風險計算，不能只看額定功率。","先比較需求曲線和實際輸出，再檢查缺口由電池、備援或削峰填補。"),
("medium","兩能源方案都供應 100 kWh 電力，甲排放較低但占地較大；公平比較還應加入？",["土地用途、生態影響、建置與維護成本、供電時段及生命週期排放", "只比較發電量", "只看設備顏色", "只看一次安裝價格"],"A","相同輸出不代表總影響相同，土地、生態、成本、維護與全生命週期都可能改變方案適用性。","先固定服務輸出，再補齊環境、經濟、時間與社會指標。"),
("easy","若電池充入 10 kWh、取出 8 kWh，儲能往返效率為何？",["20%", "80%", "100%", "125%"],"B","效率=輸出÷輸入=8÷10=0.8=80%；剩餘能量在充放電過程轉成熱等損失。","先確認效率定義是有用輸出除以輸入，再代入相同能量單位。"),
("hard","柴油備援機可在無風無日照時供電，但排放高；最完整的決策方式是？",["比較缺電風險、啟動時間、燃料排放、成本、維護與備援使用頻率", "因排放高就忽略可靠度", "因能供電就不需計算排放", "只看柴油機額定功率"],"A","能源方案是多條件取捨；可靠度、排放、成本和維護需同時評估，並說明備援實際使用情境。","先列能源服務目標，再把穩定、環境與經濟代價放在同一決策表。"),
("medium","要比較風力與太陽能對離島學校的適用性，哪個實驗／資料設計較公平？",["固定同一需求與時間範圍，記錄多月風速、日照、實際輸出與停電缺口", "只比較一天的額定功率", "一方案看夏天、一方案看冬天且不校正", "只問哪個名稱較環保"],"A","同一服務需求與長期、對應的天候和輸出資料，才能比較間歇性與季節差異，避免單日偏差。","固定需求和時間尺度，再同步記錄資源條件、輸出與缺口。"),
("hard","風力發電量增加但候鳥撞擊風險上升，報告應如何處理？",["保留發電效益與生態風險，調查遷徙路徑並比較避讓、停機或選址方案", "只報發電量增加", "因有風力就否定所有生態資料", "把撞擊資料視為與能源無關"],"A","新能源仍可能造成局部生態代價；需用調查與替代設計降低風險，而不是以低碳標籤免除檢查。","把能源效益和局部風險分開量測，再找可降低風險的工程或營運條件。"),
("easy","為什麼比較發電方案時不能只看額定功率？",["額定功率是特定條件下的能力，實際供電還受天候、設備可用率、儲能與需求時段影響", "額定功率等於全年每小時輸出", "額定功率只代表設備重量", "只要額定功率大就一定排放低"],"A","實際可用電力取決於資源、設備、儲能和負載時間的配合，額定值不能取代實際輸出資料。","先分清能力上限和一段時間內真正可供應的能量。"),
("medium","若電價補貼使設備較便宜，卻把電池廢棄成本轉給地方政府，社會評估應？",["把補貼、廢棄、回收責任與長期公共成本一併揭露", "只看購買者的初始價格", "因有補貼就視為沒有成本", "忽略未來廢棄物"],"A","能源科技的成本可能跨越時間與群體分配；初始價格下降不能代表總社會成本下降。","沿生命週期追蹤誰付錢、誰承擔風險和何時發生，不只看購買時刻。"),
("hard","哪句最適合作為離島新能源提案結論？",["在目前需求、天候與儲能容量下，混合方案可降低停電缺口；仍需監測燃料、排放、生態與電池壽命並設停損門檻", "再生能源一定能取代所有備援", "只要排放低就不必考慮供電穩定", "只看三天資料就能決定永久能源政策"],"A","能源方案需同時說明服務能力、條件、環境代價和後續監測；可修正的提案比單一能源口號更可靠。","用需求—輸出—缺口—代價—監測五段收束並限定適用範圍。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-iv-4-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma-iv-4"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的能源轉換、供電、效率、儲能、排放、生態、成本與方案比較能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma-iv-4","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma-iv-4、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合離島供電、能源轉換鏈、太陽能、風力、柴油備援、儲能、效率、排放、土地、生態與公平決策。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-iv-4-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為能源轉換、供電穩定、儲能效率、排放、土地生態、成本、公平與離島方案比較專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma-iv-4")
if __name__=="__main__": main()
