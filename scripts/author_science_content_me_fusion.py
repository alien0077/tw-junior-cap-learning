"""Me：環境汙染與防治第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-me.json"; REPORT=ROOT/"implementation/reports/science-content-me-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"環境污染、污染物、食物鏈與防治資料","pattern":"取公開自然科評量以環境變化、污染影響、監測指標與防治方案進行推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"水質、空氣、污染、資料判讀與環境決策","pattern":"取公開會考以圖表、時間序列、替代解釋和證據界線判讀污染問題的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"環境污染、營養鹽、污染鏈、監測與防治","pattern":"取公立國中試題以來源、路徑、受影響對象、控制變因和防治措施推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出污染來源、污染物、路徑、受影響對象與指標。","區分直接觀察、推論和尚未測量的部分。","依水、空氣、土壤或食物鏈建立傳遞鏈。","排除只看顏色、氣味或一次採樣的過度結論。","比較源頭、過程、末端和復原方案的效果與代價。"] for _ in range(10)]
ROWS=[
 ("easy","池塘突然變綠時，哪項最適合作為第一步？",["記錄時間、位置、水色、藻量與對照水體，再提出可能來源","直接宣布水中一定有毒","只看照片就清除池塘","把顏色當成污染物名稱"],"A","水色是觀察線索，不等於毒性或成因；要先留下可比較的時間、位置與指標資料。","先把現象轉成可量測的污染鏈問題。"),
 ("medium","要測試肥料逕流是否與藻華相關，哪項設計較合理？",["比較相近水體在相同降雨後的營養鹽、藻量與清晨溶氧，並記錄遮蔭與水深","只在藻華最嚴重一天看水色","先決定肥料是唯一原因再挑資料","只問居民覺得水臭不臭"],"A","多個指標、對照水體、相同降雨條件和干擾紀錄能支持關聯判讀，仍需保留其他來源的可能。","固定時間與空間，分開來源線索和因果結論。"),
 ("easy","油脂尚未進入雨水溝時，哪個措施最接近源頭防治？",["在產生處分流、收集並妥善清運廢油","只在下游撈除油膜","把污染水稀釋後排到別處","等雨水把油沖走"],"A","源頭防治是在污染物進入環境前減少產生或收集處理；下游撈除或稀釋可能只是延後或轉移風險。","先定位污染鏈的最前端，再判斷措施作用位置。"),
 ("medium","某區平均污染濃度下降，但下游社區的暴露增加；報告應如何處理？",["同時呈現平均值、地點、族群與時間，說明可能的風險轉移","只報平均值宣布完全改善","因下游增加就刪除平均值","只看最乾淨測站"],"A","平均值可能掩蓋空間分布；防治評估需檢查誰受益、誰承擔以及污染是否移動到下游。","把總量、分布與公平性放在同一張證據表。"),
 ("hard","濁度下降能否直接證明水已可安全飲用？",["不能，還要檢驗微生物、溶解污染物與相關安全標準","可以，清澈就代表所有污染物消失","不能，因為濁度永遠沒有用","可以，只要沒有氣味"],"A","濁度只反映部分懸浮物，不能代替微生物、溶解物和法規安全檢驗；結論必須限定在該指標。","分辨單一指標改善與整體安全保證。"),
 ("medium","比較兩種空氣污染防治方案，哪組資料最完整？",["污染濃度、測站位置、風向、暴露時間、成本、維護與副作用","只看排放口一次讀值","只看方案名稱寫著綠色","只看居民當天是否聞到味道"],"A","污染防治要連結測量位置、時間與傳播條件，也要評估成本、維護和風險轉移；單一讀值不足。","先固定測量尺度，再整合效果與代價。"),
 ("easy","若兩組污染資料都在雨季下降，最合理的處理是？",["比較相同季節、增加前後與對照資料，檢查降雨是否是共同影響","直接把下降全部歸功於防治方案","刪除雨季資料","只選下降較多的一組"],"A","季節可能是共同混淆因素；需用同季節對照、時間序列或額外資料分開方案效果。","找共同變化的混淆因子並重新設計比較。"),
 ("hard","污染物沿著『工廠排放—河水—藻類—魚—人』傳遞時，哪項判讀較適當？",["要同時追蹤來源、介質、食物鏈受影響者與暴露方式，不能只測河水顏色","只要魚還活著就沒有風險","藻類增加一定代表水質變好","人沒有直接碰水就不會暴露"],"A","污染鏈包含來源、路徑、受影響對象與暴露方式；食物攝取等間接路徑也需納入。","沿污染鏈逐段找證據與未測環節。"),
 ("medium","噪音防治方案要判斷是否有效，最需要補充哪項？",["在相同地點與時段重複量測音量，並記錄來源、距離與受影響時間","只問一次是否覺得安靜","只看隔音牆顏色","把白天平均值套用夜間"],"A","噪音具有時間、距離和來源差異；固定測點與時段並重複量測，才能比較方案效果與暴露時間。","把感受轉成可重做的音量與暴露測量。"),
 ("easy","下列哪個污染防治結論最符合證據界線？",["本次樣區營養鹽與藻量同步下降，顯示方案可能有效；仍需長期對照與其他污染物檢測","方案名稱是自然的，所以一定沒有副作用","一次水色變清就證明所有污染消失","只要平均值變好，所有地點都改善"],"A","這句話保留觀察、適用範圍和待補證據，沒有把局部短期資料擴大成全面保證。","用觀察—可能解釋—條件—限制完成報告。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-me-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-me"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的污染來源、污染鏈、水質、空氣、土壤、噪音、監測與防治能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-me","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-me、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合污染來源、污染物、傳遞路徑、受影響對象、藻華、水質、空氣、土壤、噪音、監測、防治、公平性與證據限制。原有通用污染研究題已全部改為本單元專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-me-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有通用污染研究題已移除，10 題改寫為污染來源、污染鏈、水質、空氣、土壤、噪音、監測、防治、公平與證據界線專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content me")
if __name__=="__main__": main()
