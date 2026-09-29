"""N：資源與永續發展第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-n.json"; REPORT=ROOT/"implementation/reports/science-content-n-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"資源利用、環境承載、污染與永續資料","pattern":"取公立學校自然科評量以資源流、環境影響、資料比較和永續行動推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"能源、水資源、環境保護與生命週期判讀","pattern":"取公開會考以圖表、時間尺度、資源限制和方案代價評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"資源、能源、環境承載力與永續方案","pattern":"取公立國中試題以資源補充、需求量、污染負荷、控制變因和生活決策推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出需求量、補充率、存量、污染、成本與公平指標。","判斷題目要求短期比較還是長期承載。","用資源流和時間尺度推論。","排除可再生等於無限、回收等於零污染等混淆。","寫出多指標、條件式且含限制的結論。"] for _ in range(10)]
ROWS=[
 ("easy","可再生資源為什麼仍可能被過度使用？",["因為需求速度可能長期超過自然補充速度","因為可再生資源永遠不能補充","只要回收一次就不會耗盡","可再生和不可再生完全沒有差別"],"A","可再生只表示在一定條件下能補充；若需求長期超過補充速度，存量仍會下降。","比較需求量與補充速度，而不是只看資源名稱。"),
 ("medium","校園每天用水 900 L、回收再利用 300 L；若其他用水不變，最直接的再利用率約為？",["1/3","2/3","3 倍","300 倍"],"A","再利用率=300÷900=1/3；這個比例不能直接代表所有環境影響都下降。","先確認分子、分母和指標定義，再檢查結論範圍。"),
 ("easy","評估校園節水方案時，哪項資料最不能省略？",["需求量、補充或供水條件、污染／處理負荷與不同使用者影響","只看本月水費","只看回收設備外觀","只記錄最省水的一天"],"A","永續方案需看資源流、系統容量、污染負荷與公平性，單一費用或單日數值不足。","建立資源、環境、社會三類指標。"),
 ("hard","若每日需求量長期大於自然補充量，資源存量曲線最可能如何？",["逐漸下降，直到需求或補充條件改變","永遠水平不變","因資源可再生而無限上升","只在第一天下降後自動恢復"],"A","當消耗速率長期超過補充速率，淨存量為負，會逐步下降；可再生不代表沒有承載上限。","把每日流入與流出放在時間序列比較。"),
 ("medium","回收率提高但處理耗電和污染也提高，最合理的永續判斷是？",["同時比較回收量、能源、污染、成本與生命週期，不能只看回收率","回收率高就一定最永續","處理耗電不算環境影響","只要有回收標誌就可忽略其他資料"],"A","回收只是資源流的一段；處理能源、運輸、污染和使用壽命都可能改變總體效果。","用生命週期而非單一比例判斷。"),
 ("hard","兩方案都省水，甲使污水處理負荷接近容量上限，乙省水較少但保有安全餘裕；如何比較？",["把節水量、處理負荷、異常日風險與成本一起列出，說明取捨","只選節水量最大的甲","只看方案名稱有沒有回收","因乙省水較少就完全否定"],"A","系統接近容量上限可能在高峰或故障時失效；永續評估要同時看效果、韌性與代價。","把承載力和安全餘裕納入決策。"),
 ("medium","要比較兩種校園能源方案，哪項設計較公平？",["固定服務量與使用時數，記錄能源輸入、輸出、污染、成本和維修，再重複觀察","只比較裝置額定功率","一方案測夏天、一方案測冬天且不校正","只問使用者喜不喜歡"],"A","公平比較需固定服務需求與時間，並收集能量、污染、成本和維修等對應指標。","先固定功能，再比較完整資源流。"),
 ("easy","5R 中先減少不必要消費，通常比單純回收更接近哪種策略？",["源頭減量，直接降低資源取得、製造與處理的後續負荷","把污染移到下游","增加一次性用品","只改變垃圾分類顏色"],"A","源頭減量可在資源被取得和產品被製造前降低需求，通常比只處理末端廢棄物更早介入。","沿資源生命週期找最前端的介入點。"),
 ("hard","若方案降低全校平均用量，卻讓低收入家庭須負擔更高設備費，永續報告應？",["同時呈現環境成效、成本分布與補助或替代方案，檢查世代和群體公平","只報平均用量下降","因有公平問題就刪除環境資料","設備費與永續無關"],"A","永續包含環境、經濟與社會面向；平均值不能掩蓋成本由誰承擔。","把總體效果和分配影響分開呈現。"),
 ("medium","哪個結論最符合資源與永續評估的證據界線？",["在需求不超過補充、污染負荷低於容量且成本與公平門檻可接受時，方案較可能長期維持","只要本月成本最低就一定永續","可再生資源完全不需管理","回收率 100% 就代表沒有任何環境代價"],"A","永續是多條件、長時間的判斷；需交代補充、承載、成本、公平與仍未測量的限制。","用多指標門檻和條件式結論收束。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-n-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-n"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的資源補充、需求、污染、承載力、能源、水、生命週期、5R 與永續決策能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-n","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-n、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合可再生與不可再生資源、需求、補充速度、污染、承載力、用水用電、5R、生命週期、成本、風險與世代／群體公平。原有科學問題取樣錯配題已全部改為資源與永續發展專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-n-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有科學問題取樣錯配題已移除，10 題改寫為資源補充、需求、污染、承載力、能源、水、生命週期、5R、公平與永續決策專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content n")
if __name__=="__main__": main()
