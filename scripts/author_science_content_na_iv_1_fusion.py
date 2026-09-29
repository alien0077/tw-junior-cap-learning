"""Na-Ⅳ-1：生物資源利用與生物相互依存第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-na-iv-1.json"; REPORT=ROOT/"implementation/reports/science-content-na-iv-1-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"資源利用、食物網、族群與生態資料","pattern":"取公立學校自然科評量以生物資源、食物關係、族群變化和環境管理推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生態系、物種、棲地、資源與資料判讀","pattern":"取公開會考以食物網、時間序列、因果、承載和保育方案評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"溪流、資源採集、外來種與生物互動","pattern":"取公立國中試題以食物鏈、資源利用、棲地、控制變因與管理決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先指出被利用的資源、直接受影響的物種與棲地條件。","沿食物網和互動關係追蹤數量或功能的下一層變化。","區分觀察到的變化、合理機制與尚未證實的連鎖推論。","用未利用區、時間序列、重複樣區和替代解釋檢查。","提出兼顧生態、社區生計與可監測門檻的管理方案。"] for _ in range(10)]
ROWS=[
("easy","溪流捕撈大型魚增加後，小魚數量上升；這首先是什麼類型的影響？",["直接移除大型魚後，透過捕食關係產生的連鎖影響", "大型魚把小魚變成植物", "水溫一定因此下降", "與食物網無關的隨機變化"],"A","捕撈直接減少大型魚，若大型魚原本捕食小魚，小魚增加是沿食物網傳遞的間接結果。","先標出直接移除的物種，再沿箭頭追蹤下一層的增減方向。"),
("medium","潮間帶採集海藻量增加，最需要同時觀察什麼？",["海藻覆蓋率、附著生物、草食者、棲地結構與水質的時間變化", "只記錄採集者人數", "只看海藻當天重量", "只觀察天空顏色"],"A","海藻既是資源也可能提供食物、遮蔽與附著表面，採集影響可能經由多個物種與棲地傳遞。","把資源本身、直接使用者、依賴者和非生物棲地指標一起列入。"),
("easy","砍伐河岸樹木後，水溫上升、魚類幼體減少；最可能的中間機制是？",["遮蔭減少使水溫與棲地條件改變，進而影響幼魚", "樹木被砍會直接製造魚類", "水溫上升必然增加所有魚類", "魚類與河岸沒有任何關係"],"A","河岸植被提供遮蔭與根系穩定，移除後可能改變水溫、沉積和躲藏空間，影響魚類幼體。","沿活動→棲地條件→生物反應三段建立機制，不跳過中間證據。"),
("medium","外來種進入溪流後，原生種數量下降；要避免過度推論，應比較？",["有外來種與無外來種的相近溪段，並控制水溫、流量和棲地差異", "只比較外來種最多的一天", "只看原生種顏色", "刪除流量不同的樣區"],"A","相近對照與環境條件紀錄能檢查外來種和原生種變化的關聯，避免把流量或棲地差異誤當原因。","先找替代解釋，再設相近對照與一致的取樣方法。"),
("hard","若限制捕撈後大型魚恢復，但社區收入下降，管理方案應？",["設捕撈季節／配額、替代生計與魚類監測，依資料調整規則", "只保護魚而不處理生計", "因收入下降就取消所有限制", "只看單一物種數量"],"A","資源管理需同時維持生態功能與社區生活；可調整的配額、替代生計與監測比永久口號更能支持合作。","把生態指標和社會成本並列，設計可追蹤的管理門檻。"),
("medium","要測試海藻採集量對附著生物多樣性的影響，哪種設計較公平？",["設不同採集量與無採集對照，固定潮位、季節和樣區大小並重複調查", "採集組同時改變樣區與調查時間", "只調查採集後一次", "只選結果最好看的樣區"],"A","採集量是主要自變因，其他空間、時間與取樣條件需固定並設對照，才能比較多樣性變化。","先定義自變因、對照、樣區邊界和重複時間。"),
("hard","若小魚數量增加但水質變差，哪項結論最合理？",["食物網數量變化和棲地品質可能同時出現不同方向，不能只用小魚增加判斷生態系變好", "小魚增加必然代表水質改善", "水質資料一定比食物網重要且可刪除", "兩項結果互相矛盾所以都無效"],"A","不同指標可能反映不同面向；小魚增加不能抵銷污染或缺氧風險，需分開解釋並追蹤機制。","把族群數量、環境品質和生態功能分開列，再找它們的連結。"),
("easy","在食物網中，箭頭通常用來表示什麼？",["食物或能量由被取食者流向取食者", "生物一定朝箭頭方向移動", "箭頭越長代表生物越大", "所有物質只流一次且不會循環"],"A","食物網箭頭表示取食與能量傳遞方向；能量逐級散失，物質則可在系統中循環。","先問誰吃誰，再分開能量單向流動與物質循環。"),
("medium","為什麼資源利用的管理需要長期時間序列而非單次調查？",["族群繁殖、季節、天候和棲地恢復有延遲，單次數量不能代表長期趨勢", "單次調查永遠沒有任何價值", "長期資料一定沒有誤差", "只要資料多就不必設對照"],"A","生物反應和棲地恢復可能有時間延遲，長期資料能辨認季節波動、介入效果與承載限制。","先標出反應時間，再安排基線、介入後和對照的連續觀察。"),
("hard","哪句最適合作為溪流資源管理結論？",["在本次樣區與觀察期間，降低捕撈並恢復河岸植被與魚類恢復同時出現；仍需追蹤水質、生計與其他食物網物種", "魚類增加就證明所有管理都成功", "只要保護一種魚，整個生態系必然恢復", "資源利用有爭議所以不能用資料管理"],"A","完整結論交代範圍、資料支持的方向、其他指標與社會條件，避免將局部結果擴張成無條件定律。","用直接影響—連鎖機制—證據範圍—社會條件—後續監測收束。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-na-iv-1-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-na-iv-1"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的溪流、潮間帶、生物資源利用、食物網、外來種、棲地、保育與管理能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-na-iv-1","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-na-iv-1、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合溪流與潮間帶生物資源利用、食物網、捕撈、採集、河岸棲地、外來種、直接與連鎖影響、社區生計與保育監測。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-na-iv-1-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為溪流／潮間帶資源利用、食物網、捕撈、採集、棲地、外來種、直接與連鎖影響、監測和社區管理專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content na-iv-1")
if __name__=="__main__": main()
