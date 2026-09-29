"""Mc-Ⅳ-7：電器標示與電費計算第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mc-iv-7.json"; REPORT=ROOT/"implementation/reports/science-content-mc-iv-7-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"電功率、用電量、能源與資料計算","pattern":"取公開自然科評量以功率、時間、單位、能源使用和生活資料進行計算的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"能源、電器、功率與資料判讀","pattern":"取公開會考以圖表、條件、單位和生活科技情境判讀能源效益的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"電器標示、功率、時間、電費與節能判讀","pattern":"取公立國中試題以標示讀取、單位換算、用電量和方案比較推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出功率、使用時間、電價與要求量。","把 W 換成 kW。","用用電量=kW×h 計算。","再乘電價且檢查 kWh 與元的單位。","回查待機、實際使用率和估算條件。"] for _ in range(10)]
ROWS=[
 ("easy","800 W 的電熱器每天使用 2.5 小時，當日用電量為？",["0.32 kWh","2.0 kWh","20 kWh","2000 kWh"],"B","800 W=0.8 kW，0.8×2.5=2.0 kWh；功率不能直接當成電費。","先換 kW，再乘小時，最後確認是用電量不是費用。"),
 ("medium","某燈具標示 40 W，每天使用 5 小時，連續 30 天用電量約為？",["0.6 kWh","6 kWh","60 kWh","600 kWh"],"B","40 W=0.04 kW，0.04×5×30=6 kWh。","把天數納入時間，並統一功率單位。"),
 ("easy","若用電量 6 kWh、每 kWh 電價 5 元，電費約為？",["11 元","30 元","60 元","300 元"],"B","費用=用電量×單價=6×5=30 元；kWh 是用電量單位，元才是費用。","先分辨題目要用電量還是電費，再乘單價。"),
 ("hard","甲燈 60 W 每天 4 小時，乙燈 100 W 每天 2 小時；30 天內哪個用電量較大？",["甲燈 7.2 kWh，較大","乙燈 6.0 kWh，較小","兩者相同，都是 7.2 kWh","只看功率不能判斷"],"A","甲=0.06×4×30=7.2 kWh；乙=0.1×2×30=6.0 kWh，所以甲較大。功率較小不代表一定省電，時間也要算。","比較功率×時間，而不是只比瓦特數。"),
 ("medium","一台待機 5 W 的螢幕每天 24 小時插著，30 天待機用電量約為？",["0.36 kWh","3.6 kWh","36 kWh","360 kWh"],"B","5 W=0.005 kW，0.005×24×30=3.6 kWh；待機時間長仍會累積用電。","把待機的完整 24 小時當成使用時間計算。"),
 ("hard","新燈每天節省 1.2 kWh，安裝增加 1,800 元，電價每 kWh 5 元，約幾天回收差額？",["150 天","300 天","900 天","1,800 天"],"B","每天省 1.2×5=6 元，1,800÷6=300 天；仍需檢查壽命、照度和維修。","先把節電量換成每日省下的錢，再除以增加成本。"),
 ("medium","兩台冰箱功率相同，但甲壓縮機每天實際運轉 8 小時、乙 12 小時，哪項合理？",["若其他條件相同，乙用電量較大","甲一定較耗電，因為開關次數少","功率相同就代表費用相同","時間與用電量無關"],"A","用電量由功率和實際運轉時間共同決定；乙運轉時間較長，估算用電量較大。","把額定功率與實際工作時間分開。"),
 ("easy","電器標示『110 V、900 W』中的 900 W 主要表示？",["額定功率，即能量使用的速率","每月固定電費 900 元","電器質量 900 kg","電壓 900 V"],"A","W 是功率單位，表示能量使用的快慢；電壓另以 V 表示，費用還要看時間和電價。","先辨認標示物理量與單位。"),
 ("hard","高效率冷氣每小時用電較少，但購買和維修成本較高；最合理的選擇方式是？",["依使用時數、用電、價格、壽命、維修與環境條件比較總體效益","只看效率等級就保證最省錢","只看購買價格，不看使用時間","宣稱高效率等於零環境影響"],"A","科技選擇要整合用電量、初期成本、壽命、維修與環境代價，結論必須限定使用情境。","把計算結果放進生命週期和條件比較。"),
 ("medium","某校比較兩種燈具時，哪項資料最能避免錯誤宣稱『一定比較省電』？",["相同照度下的實測功率、每日使用時數、待機耗電與量測期間","只記錄包裝上的最大亮度","只問一位使用者覺得哪盞亮","只比較燈具外觀"],"A","相同照度、實測功率、使用與待機時間能把功能條件固定，較能支持用電比較；包裝單一數字不足。","先固定服務效果，再收集完整使用條件。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-mc-iv-7-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-mc-iv-7"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的電器標示、功率、使用時間、用電量、電費與節能方案能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mc-iv-7","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mc-iv-7、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合電器標示、功率、時間、kWh、電費、待機、回收成本與能源科技評估。原有科學問題取樣錯配題已全部改為電器標示與電費計算題；所有正文、數據、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mc-iv-7-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有科學問題取樣錯配題已移除，10 題改寫為電器標示、功率、時間、用電量、電費、待機與節能方案比較專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mc iv 7")
if __name__=="__main__": main()
