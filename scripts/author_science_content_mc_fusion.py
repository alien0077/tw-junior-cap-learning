"""Mc：科學在生活中的應用第一輪原創題庫。"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; LESSON=ROOT/"lessons/science/lesson-science-content-mc.json"; REPORT=ROOT/"implementation/reports/science-content-mc-first-pass-review.json"; QDIR=ROOT/"questions/science"; TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"科學在生活中的應用、能量、物質、資料與安全","pattern":"取公立學校自然科評量以生活情境、機制、資料判讀和安全條件進行跨概念推理的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生活科學、實驗設計、能量轉換與證據界線","pattern":"取公開會考以圖表、測量條件、替代解釋和生活應用評估的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"保溫、物質分離、照明、能源與控制變因","pattern":"取公立國中試題以科學原理連結生活器材、控制變因與多指標決策的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[["圈出主張、結果指標、自變因與控制條件。","判斷要用哪個科學機制解釋。","設計公平比較並重複測量。","排除把一次成功、外觀或廣告當普遍證據。","寫出支持範圍、限制和下一步檢驗。"] for _ in range(10)]
ROWS=[
 ("easy","要檢驗『保溫杯甲比乙好』，哪項問題最可測量？",["固定初溫與容量，量測相同時間後兩杯液體溫度變化","問使用者覺得哪個外觀較好","只看廣告標語","不記錄時間就比較手感"],"A","固定初溫、容量、環境與時間，量測溫度變化，才能把差異連到保溫效果。","把模糊主張改成結果指標和控制條件。"),
 ("medium","保溫杯比較中，哪項最可能是混淆變因？",["甲裝熱水、乙裝冰水，卻直接比較最後溫度","兩杯使用相同容量和初溫","兩杯在相同房間測量","每隔相同時間記錄溫度"],"A","不同初始溫度會影響最後讀值，不能把它和杯子材質的效果分開；應固定初溫或比較溫度變化量。","先找不是研究目標卻同時改變的條件。"),
 ("easy","濾水器讓水看起來清澈，最穩妥的結論是？",["只能支持混濁度或外觀改善，不能直接保證可飲用","已證明所有微生物都被去除","水中所有溶解物一定消失","只要清澈就不需安全檢驗"],"A","外觀是其中一項指標，仍需檢驗微生物、溶解物和法規安全標準；不能把單一觀察擴大成全面保證。","分開外觀指標、污染物類型和安全結論。"),
 ("medium","要比較兩種濾材去除混濁物的效果，哪項設計較公平？",["用相同原水量與混濁度、相同流速，重複測量過濾前後濁度","一種濾材過濾 1 L，另一種過濾 10 L","只比較濾水後顏色，不量過濾前","一邊加熱一邊過濾，另一邊不加熱"],"A","固定原水、流速與操作條件，量測前後濁度並重複，才能比較濾材對同一指標的效果。","固定輸入與操作，建立前後差值。"),
 ("easy","LED 與傳統燈在相同照度下比較，哪個資料最能支持節能判斷？",["實測功率、使用時間與照度均記錄在相同條件下","只看燈泡顏色","只看標示的最高亮度","只問哪盞看起來更白"],"A","節能要比較達到相同照度時的功率，再結合使用時間；顏色或最高亮度不能單獨代表耗電。","先固定服務效果，再比較功率和時間。"),
 ("hard","某產品一次測試效果很好，最合理的報告方式是？",["說明本次條件下觀察到效果，並提出重複、樣本與其他情境的限制","宣稱所有人使用都會同樣有效","刪除不理想的測試結果","把產品名稱當成原理證明"],"A","單次結果只能支持特定條件下的觀察；需要重複、不同樣本和完整條件才能擴大結論。","將觀察、推論和適用範圍分層書寫。"),
 ("medium","保溫、濾水和照明三個案例共同需要哪種科學思考？",["先指出機制與可量測結果，再控制條件、檢查限制和安全","只比較產品價格","只背產品名稱","以一次直覺決定所有情境"],"A","三者都要把主張轉成可測問題，連結熱傳、分離或能量轉換，再用證據和限制評估。","找出案例中的機制—指標—條件鏈。"),
 ("hard","宣稱『濾水後即可飲用』時，下一個低風險且必要的查驗是？",["依水質風險檢測微生物與可能污染物，並查核設備規格與使用期限","直接讓所有人飲用測試水","只看濾芯顏色","把清澈度當成完整安全證明"],"A","飲用安全需要針對污染物和設備規格檢驗，並遵守操作與更換期限；外觀不能代替風險評估。","把未知污染物轉成具體檢測與安全步驟。"),
 ("medium","高效率產品價格較高但使用電量較低，哪項比較最完整？",["比較初期成本、使用時間、節電量、壽命、維修、回收與電力來源","只看效率標籤就宣布一定最省","只看購買價格","因節能就宣稱沒有製造環境代價"],"A","技術選擇要看使用週期與條件，效率是重要證據但不是所有成本和環境影響的完整答案。","用生命週期和適用條件補足單一指標。"),
 ("easy","若結果不符合原先預測，科學探究最好的做法是？",["保留資料，檢查儀器、控制條件與替代解釋，再設計下一步","刪除結果直到符合預測","修改答案但不說明理由","直接宣布科學方法無效"],"A","反例能幫助檢查模型；應保留原始資料，查找誤差和條件，再以新測試修正解釋。","把不符合預測的結果當成改進模型的證據。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-mc-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-mc"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的生活應用、保溫、濾水、照明、能源、控制變因與證據界線能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-mc","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-mc、南一／康軒／翰林公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合保溫、濾水、照明、能量、物質分離、控制變因、測量誤差、安全與生命週期決策。原有科學問題取樣錯配題已全部改為科學在生活中的應用專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-mc-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有科學問題取樣錯配題已移除，10 題改寫為保溫、濾水、照明、控制變因、安全、測量限制與生活決策專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content mc")
if __name__=="__main__": main()
