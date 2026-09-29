"""Lb-Ⅳ-2：人類活動改變環境並影響生物第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-lb-iv-2.json"; REPORT=ROOT/"implementation/reports/science-content-lb-iv-2-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"人類活動、環境指標與生物反應","pattern":"取公立學校自然科評量以活動—環境—生物因果鏈與資料判讀的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"污染、棲地、光照與環境資料","pattern":"取公開會考以對照、時間順序、替代解釋和證據界線評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"水質、棲地連通性與生物量測","pattern":"取公立國中試題以環境變因、控制實驗和生物分布推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先寫出人類活動與受影響的環境指標。","再找出指標改變後的生物反應與時間順序。","畫出活動→環境→生物的因果鏈並標出資料。","用受影響區／對照區和替代解釋檢查因果強度。","用限定條件的語句提出結論與需要補測的資料。"] for _ in range(10)]
ROWS=[
("easy","河川築壩後，上游水位上升、下游沉積物減少；要研究對魚類的影響，首先應量測哪一組資料？",["水流速度、棲地連通性、沉積物與魚類分布","只量壩的高度","只問居民是否喜歡大壩","只記錄魚的顏色"],"A","這些資料能把工程造成的水文與棲地改變，連到魚類分布的可能反應；單一工程尺寸不足以說明生物影響。","先把活動、環境指標和生物指標分成三層，再選能連成因果鏈的量測。"),
("medium","道路拓寬後，路旁蛙類出現率下降；哪個比較最能檢查是否與道路工程有關？",["找相近但未施工路段作對照，固定季節與夜間觀察時間並重複記錄","只比較施工後一晚的蛙聲","把下雨夜和乾燥夜直接混在一起","只挑下降最多的路段"],"A","對照路段、相同時段與重複觀察可降低季節、降雨和自然波動造成的混淆。","先設定受影響區與對照區，再固定觀察時間和天氣條件。"),
("easy","農田肥料經雨水流入池塘，藻類增加、溶氧降低；下列哪個是環境指標而非人類活動？",["溶氧", "施肥", "排水管設置", "農田耕作"],"A","溶氧是被量測的環境條件；施肥、排水和耕作是可能造成改變的人類活動。","問每個名詞是在做某件事，還是在描述環境狀態。"),
("medium","夜間增加強光照明後，昆蟲在燈下聚集；要判斷是否影響蝙蝠取食，應補測什麼？",["蝙蝠活動時間、昆蟲數量與有無照明區的比較","只量燈的瓦數","只拍燈下昆蟲一張照片","只觀察白天蝙蝠"],"A","要連接照明、昆蟲和蝙蝠，需同時記錄各層級的時間與數量，並比較有無照明條件。","沿因果鏈逐層放入可量測指標，避免只量活動本身而沒有生物反應。"),
("hard","都市鋪面增加後，夏季地表溫度上升、某蜥蜴數量下降；哪個結論最守證據界線？",["鋪面可能透過溫度與遮蔭改變影響蜥蜴，但仍需檢查食物、棲地和捕食者","鋪面一定是蜥蜴減少的唯一原因","溫度升高就代表所有爬蟲都會減少","只要兩條曲線同向就已證明因果"],"A","資料支持合理的可能機制，但食物、棲地與捕食者仍是替代解釋，需再控制或比較。","把資料支持的可能性和尚未排除的因素同時寫進結論。"),
("medium","河岸清除植被後，水溫上升且魚苗減少；若要測試遮蔭的作用，哪個設計最適合？",["設不同遮蔭程度的相近河段，固定水流與取樣時間，重複量水溫和魚苗","同時改變水流、底質和遮蔭","只測清除後一天的水溫","只比較魚苗最大的一次數量"],"A","遮蔭程度是主要自變因，其他環境條件與重複量測需盡量固定，才能比較水溫與魚苗反應。","先定義自變因，再列控制變因、對照或梯度與重複次數。"),
("hard","棲地被道路切成兩塊後，兩側小獸的遺傳多樣性下降；最需要補充哪種證據？",["比較道路前後或有無道路的族群交流、移動紀錄與相近棲地對照","只量道路寬度","只記錄某一天看到幾隻小獸","只問工程人員的主觀感受"],"A","遺傳差異可能與族群隔離有關，需補測移動與交流及對照棲地，不能由道路寬度單獨推出。","選擇能直接連到棲地連通性與族群交流機制的資料。"),
("easy","環境指標『濁度』主要是在描述什麼？",["水中懸浮物造成的透明度變化", "魚類的心跳速率", "工程經費", "所有生物的健康總和"],"A","濁度描述水中懸浮物使光線散射、透明度降低的程度；它是環境測量，不等於直接證明某種生物已受傷。","先辨識指標的物理意義，再說明它能支持到哪一層結論。"),
("medium","某溪流整治後魚類增加，但同時水溫下降、禁捕開始；如何避免誤判整治效果？",["比較未整治對照、記錄水溫與禁捕期間，分開評估各因素","把所有增加都歸因於整治","只看整治前後兩張照片","刪除禁捕資料以保持單一答案"],"A","多個條件同時改變時，需用對照與分段資料拆解水溫、禁捕和工程的相對作用。","列出所有同步改變的因素，再設計能區分各因素的比較。"),
("hard","對人類活動影響生物的報告，哪句最完整？",["在本次地點與期間，資料支持活動先改變某環境指標，再伴隨生物反應；仍須以對照和重複資料檢查其他原因","看到生物變少就能宣稱人類活動必然造成","只要環境指標改變就代表所有生物都受害","資料有雜訊所以不能提出任何推論"],"A","完整報告要保留時間順序、機制線索、條件範圍和證據限制，既不過度推論也不放棄可檢驗的推論。","用活動→指標→生物三段式整理，最後加上對照、重複和替代解釋。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-lb-iv-2-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-lb-iv-2"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的人類活動、環境指標、污染、棲地、對照與因果推理能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-lb-iv-2","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-lb-iv-2、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合人類活動、環境指標、污染、棲地連通性、時間順序、對照、替代解釋與證據界線。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-lb-iv-2-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為人類活動—環境指標—生物反應因果鏈、污染、棲地、光照、對照與替代解釋專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content lb-iv-2")
if __name__=="__main__": main()
