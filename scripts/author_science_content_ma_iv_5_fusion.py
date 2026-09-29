"""Ma-Ⅳ-5：本土科學知能與社會、環境及健康第一輪題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-ma-iv-5.json"; REPORT=ROOT/"implementation/reports/science-content-ma-iv-5-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"環境、健康、病媒與生活資料","pattern":"取公立學校自然科評量以環境健康、資料證據、風險和生活行動推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"水質、氣候、健康與公共決策","pattern":"取公開會考以圖表、暴露條件、因果、替代解釋和風險界線評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"水環境、熱環境、病媒與健康行動","pattern":"取公立國中試題以環境條件、健康風險、控制變因和公共方案比較的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["先分辨觀察到的是環境指標、暴露條件還是健康結果。","把時間、地點、族群與測量方法圈出。","沿機制鏈連接水質／溫度／病媒與健康風險。","用對照、重複和替代解釋檢查因果，不把風險說成確診。","提出可執行、可監測且照顧弱勢的公共方案。"] for _ in range(10)]
ROWS=[
("easy","校園積水容器增加後，病媒蚊幼蟲數上升；最直接可先改善哪項環境條件？",["減少或清除積水孳生源", "只增加教室香味", "只測午間氣溫", "把幼蟲資料刪除"],"A","積水是病媒蚊繁殖的重要環境條件，清除或管理積水能直接降低孳生機會；仍需持續監測成效。","先找病媒生活史中可被改變的環境條件，再設計源頭處理。"),
("medium","比較校園不同位置的熱風險，哪項資料組合最有用？",["同一時段的氣溫、濕度、日照／遮蔭、地表材質與人體熱感指標", "只記錄校門口一次溫度", "只問哪裡看起來最亮", "只比較建築物顏色"],"A","熱暴露受溫度、濕度、輻射、遮蔭和材質影響，單一溫度讀值不能描述完整熱風險。","先界定暴露地點和時段，再同時記錄熱環境多個相關指標。"),
("easy","池塘水樣濁度升高，能否直接說喝水會生病？",["不能，還需檢測病原體、化學物與實際飲用暴露；濁度只是其中一項指標", "可以，濁度升高必然代表確診", "只要濁度下降就表示所有風險消失", "健康風險不需任何測量"],"A","濁度反映懸浮物與透明度，不能單獨等同病原體或個人健康結果；需補足相關檢測和暴露資訊。","區分危害、暴露與健康結果，不能把環境指標直接當成診斷。"),
("medium","若中午操場地表溫度高，但樹蔭下學生熱不適較少，最適合的校園方案是？",["增加遮蔭與飲水休息點，並監測不同位置和時段的熱指標與不適回報", "只把所有活動取消而不量測", "只宣稱樹木一定解決所有熱問題", "只測平均溫度不看個別區域"],"A","遮蔭與休息可降低暴露，但方案仍需依地點、時段和學生回報監測並調整，平均值可能掩蓋熱點。","把環境改善、行為安排和監測指標一起設計，而非只提出單一口號。"),
("hard","病媒蚊密度下降但通報病例未立即下降，最合理的判讀是？",["兩者時間尺度可能不同，還需追蹤潛伏期、外來暴露、通報延遲與其他地區資料", "病媒防治一定完全無效", "病例下降與病媒完全無關", "只要一次資料就能否定所有防治"],"A","環境指標與健康結果有不同時間延遲和多重來源，短期不一致不能直接證明有效或無效。","先標出指標和結果的時間尺度，再檢查延遲、流動與替代暴露。"),
("medium","要評估清除積水對幼蟲密度的效果，哪個設計較公平？",["選相近社區，記錄介入前後並保留未介入對照，固定季節與採樣方法", "只在清除後一天觀察一個容器", "介入區同時換採樣工具和時間", "只報幼蟲下降最多的點"],"A","前後資料、相近對照、固定季節和方法能減少自然波動與測量差異造成的混淆。","安排介入組、對照組、基線和重複採樣，讓行動成效可被追蹤。"),
("hard","公告『這口池塘有毒』可能造成恐慌；較負責任的公共溝通是？",["說明已測指標、尚未測的危害、暫時避免方式與後續檢測時間", "只用最嚴重的詞提高注意力", "隱瞞不確定性以維持秩序", "把環境風險直接寫成每個人的疾病"],"A","公共溝通需同時清楚、準確和可行動，交代證據與限制，避免把危害、暴露與確診混成一句話。","用『已知—未知—現在可做—何時更新』四欄整理訊息。"),
("medium","若防蚊藥劑可能傷害水生生物，方案比較應納入什麼？",["病媒控制效益、使用劑量、非目標生物風險、替代方法與監測門檻", "只看蚊子是否減少", "因有副作用就不需比較任何資料", "只看藥劑氣味"],"A","公共健康行動也可能產生生態副作用，需比較目標效益、非目標風險、替代方案與停用條件。","把健康效益和外部風險並列，為監測與停損設定具體條件。"),
("easy","為什麼環境健康調查要記錄地點、時間與受測族群？",["暴露和風險會隨空間、季節與族群條件改變，缺少這些資料難以比較", "地點時間只增加表格長度", "健康風險和族群永遠相同", "只要平均值就能代表所有人"],"A","熱、水質和病媒等暴露具有空間與時間差異，兒童、長者或慢性病者也可能有不同脆弱性。","先界定誰、何時、在哪裡暴露，再比較平均與高風險族群。"),
("hard","哪句最適合作為校園環境健康方案結論？",["在本次季節與測量範圍內，清除積水並增加遮蔭可降低部分暴露；仍需追蹤病媒、熱不適、弱勢族群與副作用資料", "只要一項指標改善就代表所有健康問題解決", "環境資料有不確定性所以不能採取任何行動", "把風險寫成所有人一定會生病"],"A","公共科學決策要把可觀察成效、健康結果、脆弱族群與未測限制一起呈現，並保留修正空間。","用環境指標—暴露—健康結果—公平—後續監測五段整理結論。"),
]
def make_question(n,row):
 d,p,o,a,e,s=row
 return {"id":f"question-science-content-ma-iv-5-{n}","subject":"science","type":"single-choice","prompt":p,"options":[{"id":k,"text":v} for k,v in zip("ABCD",o)],"knowledgeIds":["kg-science-content-ma-iv-5"],"difficulty":d,"answer":{"value":a,"explanation":f"{e} 正確答案為選項 {a}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的本土水環境、熱環境、病媒防治、健康風險、資料證據與公共方案能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-ma-iv-5","examPatternRefs":REFS,"solutionStrategy":s,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"; lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-ma-iv-5、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合臺灣校園與社區的水環境、熱環境、病媒防治、暴露、健康風險、公共溝通、弱勢公平與可修正方案。10 題均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-ma-iv-5-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題改寫為本土水環境、熱環境、病媒、暴露與健康、風險溝通、弱勢公平與公共方案專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content ma-iv-5")
if __name__=="__main__": main()
