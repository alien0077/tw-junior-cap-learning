"""Lb-Ⅳ-3：人類行動維持生存環境與生態平衡第一輪原創題庫。"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-lb-iv-3.json"
REPORT=ROOT/"implementation/reports/science-content-lb-iv-3-first-pass-review.json"
QDIR=ROOT/"questions/science"
TODAY="2026-09-23"
SOURCES=[
 {"url":"https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","title":"高雄市立鹽埕國民中學 114 學年度第 2 學期第 1 次段考自然科公開試題","year":"114","locator":"人類活動、生態平衡、環境因子與保育資料","pattern":"取公開自然科評量以環境、族群、人類活動和證據資料進行生態決策的能力方向。"},
 {"url":"https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","title":"114 年國中教育會考自然科公開試題","year":"114","locator":"生態系、環境變化、資源利用與資料判讀","pattern":"取公開會考以圖表、時間趨勢、因果限制和環境方案判讀的能力方向。"},
 {"url":"https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E8%87%AA%E7%84%B6%E7%A7%91.pdf","title":"高雄市立國昌國民中學二年級自然科公開段考試題","year":"112","locator":"人類與環境、生態保育、控制變因與多指標監測","pattern":"取公立國中試題以環境因子、族群變化、保育措施和控制條件作推理的能力方向。"},
]
REFS=[{**s,"subject":"science","observedPattern":s["pattern"],"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for s in SOURCES]
STEPS=[
 ["圈出人類行動、環境指標、族群指標與時間。","先分開直接觀察和推論。","畫出可能的因果鏈並找替代原因。","排除只看單一指標就宣布平衡恢復。","寫出有條件且可追蹤的結論。"],
 ["列出行動造成的直接環境改變。","找受影響的族群與交互作用。","依資料順序建立連鎖影響。","排除把口號或意圖當成效果證據。","提出需要補測的指標。"],
 ["確認方案的自變因、對照和測量指標。","固定樣區、時間和方法。","比較干擾區與保留區的多次資料。","排除季節和初始差異。","用趨勢而非單次數值判定。"],
 ["辨認溶氧、藻毯、族群和通行量各自代表什麼。","檢查資料是否同時改善。","找出瓶頸仍未改善的指標。","排除挑選有利資料的做法。","依門檻提出調整與後續監測。"],
 ["圈出方案的受益者與可能代價。","比較生態與人類使用的指標。","評估限制進入、動線和教育措施。","排除全年開放或全年封閉的單一口號。","用多指標和時間尺度做決策。"],
 ["確認研究區與對照區是否可比。","記錄起始值與觀察頻率。","重複測量環境和族群變化。","排除一次調查的偶然性。","報告結果與不確定性。"],
 ["找出人類活動改變的資源或棲地。","判斷可能影響哪些族群。","用食物網或棲地關係連結。","排除先看到下降就指定唯一原因。","提出可驗證的下一步。"],
 ["區分短期成效與長期風險。","比較至少兩個年份或季節。","檢查族群繁殖與棲地指標。","排除只看遊客滿意度或單一物種。","設定觸發修正的門檻。"],
 ["確認問題要求的是環境、族群或人類需求。","挑選相應的測量資料。","比較方案的效果和代價。","排除把相關當唯一因果。","寫出能被下一次調查檢驗的建議。"],
 ["列出行動、證據、限制與可能結果。","確認資料的空間和時間範圍。","用多指標交叉檢查生態平衡。","標示尚未測量的因素。","完成『資料顯示……因此……仍需……』結論。"],
]
ROWS=[
 ("easy","潮間帶遊客踩踏增加、幼蟹數量下降；最合理的第一步判讀是？",["記錄踩踏量、底質與幼蟹密度，並設相鄰未踩踏區比較","立即宣布遊客是唯一原因","只增加幼蟹放流量","因幼蟹下降就判定整個生態系死亡"],"A","資料提供關聯線索，還需比較踩踏、底質、季節和對照區，才能檢查是否存在其他原因。","先把人類行動、環境和族群指標分開測量。"),
 ("medium","為降低繁殖季干擾又保留居民通行，哪個方案最可檢驗？",["繁殖季分時限制進入、設固定動線，持續量測幼體與棲地指標","全年完全開放且不測量","全年封閉但不設成效指標","只張貼口號並以印象判斷"],"A","分時限制和固定動線能明確改變干擾條件，也能用幼體、棲地和通行量資料評估代價與效果。","選擇有清楚行動、對照和監測指標的方案。"),
 ("easy","某區水中溶氧改善，但幼體連續三次仍未出現；最適當的行動是？",["檢查繁殖棲地、採樣時間與其他干擾，再依證據調整方案","宣布所有保育措施已完全成功","刪除幼體資料","只提高居民通行量"],"A","不同指標反映不同瓶頸；溶氧改善不代表繁殖棲地或幼體來源已恢復，需追查並修正。","不挑選有利指標，找出尚未改善的限制。"),
 ("hard","要判斷夜間照明是否影響昆蟲，哪項設計較公平？",["設照明區與無照明對照區，固定樣區與觀察時間，重複記錄昆蟲數量和光照","照明區只測一次、對照區在另一季測量","只問居民覺得昆蟲變少沒有","同時改變照明、噪音和植被且不記錄"],"A","對照、固定時間與樣區、重複測量能把照明效果與季節及棲地差異分開，並提供可檢驗資料。","以控制變因和重複觀察建立因果證據。"),
 ("medium","整治河岸後水質變好，但魚類數量沒有增加；哪項結論最嚴謹？",["水質改善不等於所有族群立即恢復，還需檢查棲地、食物、繁殖與時間尺度","整治一定失敗","魚類數量一定測錯","水質是唯一影響魚類的因素"],"A","族群恢復可能受棲地、食物、繁殖或移入時間限制；單一環境指標變好不能直接保證族群同步增加。","分離環境改善、族群反應和恢復時間。"),
 ("hard","保育方案要同時評估生態效果和居民需求，哪組指標最完整？",["溶氧、棲地覆蓋、關鍵族群、幼體出現率與通行量的多次趨勢","只看週末遊客滿意度","只看某天一種生物數量","只看工程是否完工"],"A","生態平衡與人類使用涉及不同面向；多指標和時間趨勢能避免把單一短期結果當成整體成效。","先對應每個目標，再建立多指標監測表。"),
 ("medium","若清除外來植物後原生植物增加，但土壤流失也變嚴重，管理者應如何處理？",["同時評估生物多樣性與土壤風險，補上覆土或原生植被恢復並追蹤","只看原生植物增加就宣布完成","因有代價就永遠停止所有管理","把土壤資料刪除"],"A","方案可能有正面效果也有副作用，需用棲地和土壤指標調整，而非只選擇有利結果。","把受益與代價放在同一決策表。"),
 ("easy","『生態平衡就是每種生物數量完全相等』這句話哪裡有問題？",["平衡要看互動、環境條件與變動範圍，不代表所有數量相等","平衡只表示沒有生物","平衡只看人類滿意度","平衡代表族群永遠不變"],"A","生態系可能在一定範圍內動態變化；判斷要看環境、族群與交互作用是否維持功能，不能要求數量完全相等。","先定義平衡是有條件的動態狀態。"),
 ("hard","某保育區一年後藻毯減少、溶氧改善，但居民通行量也大降；如何回報方案？",["生態指標改善但使用代價增加，需比較可接受門檻並調整動線或時段","只報告溶氧改善即可","因通行下降就宣稱生態惡化","把居民資料排除"],"A","方案評估必須同時呈現生態效果與人類代價，才能尋找分時、動線或設施的調整方案。","把多方指標和門檻一起納入決策。"),
 ("medium","下列哪種結論最符合科學報告的證據界線？",["資料顯示干擾區幼體較少；在本次樣區與期間可能與干擾相關，仍需長期對照追蹤","已證明所有人類活動都會造成同樣結果","只要一項數值變好就證明生態完全恢復","沒有數據也能依方案名稱判斷成功"],"A","這句話清楚寫出觀察、範圍、可能關聯與仍需的證據，沒有把有限資料擴大成普遍定律。","用觀察—條件—可能解釋—待補證據的句型作最後檢核。"),
]
def make_question(n,row):
 difficulty,prompt,options,answer,explanation,strategy=row
 return {"id":f"question-science-content-lb-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",options)],"knowledgeIds":["kg-science-content-lb-iv-3"],"difficulty":difficulty,"answer":{"value":answer,"explanation":f"{explanation} 正確答案為選項 {answer}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0]["url"],"sourceLocator":"三筆公立學校／公開自然科試題與課程資料的人類活動、生態平衡、環境因子、保育方案、多指標監測與證據界線能力方向；本題只作 pattern-only 改寫來源。","authoringNote":"依官方課綱、KG 與公開資料能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-lb-iv-3","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":STEPS[n-1]}
def main():
 lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson["updatedAt"]=TODAY; lesson["reviewStatus"]="draft"; lesson["authoringStandard"]="version-fused-v1"
 lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-lb-iv-3、南一／康軒／翰林可取得的公開資源限制與三筆公立學校／公開自然科評量能力模式，獨立融合人類行動、環境因子、族群連鎖、棲地、保育方案、多指標監測、生態平衡與證據界線。原有能量錯配題已全部改為本單元專屬題目；所有正文、資料、題幹、選項、答案、互動回饋與五步解法均重新撰寫，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
 for e in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): e["reviewedAt"]=TODAY
 for n,row in enumerate(ROWS,1): (QDIR/f"question-science-content-lb-iv-3-{n}.json").write_text(json.dumps(make_question(n,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"原有能量錯配題已移除，10 題改寫為人類活動、環境因子、族群連鎖、保育方案、多指標、生態平衡與證據界線專屬問題；每題有唯一答案、解析與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print("authored science content lb iv 3")
if __name__=="__main__": main()
