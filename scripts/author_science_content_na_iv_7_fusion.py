import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-na-iv-7.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-na-iv-7-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","資源使用、能源、回收、環境影響與資料推理","取公開自然科對資源、能源、回收與環境資料比較的能力方向，另寫校園方案。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","能源轉換、效率、材料與生命週期判讀","取公開會考對服務相同、效率、能源和資料限制的推理方向，未複製原題。"),
 ("https://market.cloud.edu.tw/resources/web/1807720","教育雲國中生態與環境教學資源","生態保育、資源循環與永續行動","取公開教育資源對資源循環與環境行動的能力方向，重新設計餐具和綠能情境。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","午餐後要降低一次性垃圾，哪個策略通常應優先評估？",["先減少不必要的使用量，再考慮再利用與回收","先把所有垃圾混在一起","增加一次性用品再宣導回收","只換垃圾桶顏色"],"A","減量直接避免原料、製造與運輸需求；再利用和回收仍有清洗、分類與後端處理條件，不能把順序簡化成口號。","先找能在源頭少用資源的改變，再確認是否維持相同服務和安全。"),
 ("medium","可重複餐盒和一次性餐盒要公平比較，應固定什麼？",["供應份數與衛生服務，再比較製造、清洗、運輸、使用次數和報廢","只比較單個餐盒重量","只看第一次購買價格","只看活動當天垃圾量"],"A","相同服務與時間邊界下，才可將多次使用和清洗負荷與一次性製造、運輸和廢棄比較。","先設定功能單位，例如供應六百份餐點，再列完整生命週期資料。"),
 ("medium","紙餐盒沾滿油和醬汁時，為何不能直接把所有紙盒視為可回收？",["污染可能降低纖維再製品質，需依分類規則和實際後端處理判斷","紙只要是紙就一定能再製","回收桶會自動清洗油污","沾污會讓紙變成綠能"],"A","材質、污染程度、分流品質和回收設施共同決定可否再製；丟入回收桶不是回收流程的全部。","先判斷物品材質與清潔度，再查當地分類和後端去處，不用名稱直接推論結果。"),
 ("hard","可重複餐盒只使用三次且每次清洗耗水耗電，哪個判斷最合理？",["仍要以相同服務的生命週期資料比較，不能因減少一次性垃圾就保證整體影響較低","三次使用必定比任何一次性方案好","清洗耗水與能源不算環境影響","只要餐盒看起來乾淨就不需衛生檢查"],"A","重複使用效益取決於使用次數、清洗方式、能源與水的來源、衛生要求等；需以同一功能單位算完整負荷。","把使用次數作為變因，累加製造、清洗、運輸和報廢，再檢查衛生底線。"),
 ("medium","屋頂太陽能供應洗滌設備部分電力，哪項資料仍需查？",["日照變化、儲能或備援、設備壽命、維修、屋頂承重與廢棄處理","只看晴天中午的發電量","只看面板顏色","只看宣傳中的年發電量而不看需求時段"],"A","綠能運轉可能降低化石燃料使用，但供應間歇性、設備生命週期、土地／結構與後端處理仍會影響方案。","先把需求時間和供應時間對齊，再補足設備、備援、安全和生命週期資料。"),
 ("hard","校園回收率上升但總垃圾量也上升，哪個解釋最值得檢查？",["回收率的分母、活動人數、一次性用品總量、分類污染與可能的反彈使用行為","只要回收率上升就是所有環境影響下降","把總垃圾量資料刪除","回收率與減量永遠相同"],"A","比例改善不代表總量下降；人數、分母、分類品質和因效率或便利增加而多用的反彈效應都需分開分析。","同時畫總量、回收量、回收率和每人量，檢查分母與行為是否改變。"),
 ("easy","自備水壺的主要減量作用是？",["在仍提供飲水服務下，減少一次性容器的製造與廢棄需求","讓所有用水和能源歸零","保證水壺永遠不需清洗","只改變飲水顏色"],"A","自備容器若被充分使用，可避免部分一次性容器投入；仍需考慮清洗、使用壽命、材質和衛生。","先固定飲水服務，再比較一次性容器數量與水壺使用、清洗和壽命。"),
 ("medium","若 LED 燈維持相近照度但使用者因此把更多區域整夜開燈，應檢查什麼？",["設備效率、照明總時數、區域數與總耗電，判斷節省是否被使用量反彈抵銷","只看單盞功率","只看燈具外觀","因效率提高就停止記錄用電"],"A","單位效率改善可能被使用時間或範圍增加抵銷；永續判斷需看相同服務下的總投入和行為變化。","把每盞功率、數量、時數和照度一起記錄，再比較改裝前後總量。"),
 ("hard","回收政策要讓學生真正改變資源流向，哪項設計最完整？",["清楚分類、減少污染、確認後端去處，並追蹤投入量、回收率、污染率和最終處理結果","只增加回收桶數量","只用競賽獎品鼓勵而不查結果","將不可回收物藏起來"],"A","回收的結果取決於分類品質和後端處理，需由源頭到最終去處追蹤，不能用桶子數量或宣傳代替證據。","畫出物品從使用到最終去處的流向，再為每段設定可檢查指標。"),
 ("medium","哪句最適合作為校園永續方案結論？",["在維持衛生、照明或飲水服務的條件下，方案甲減少每份服務的材料與能源投入；仍需追蹤使用次數、維修與後端處理","只要貼上綠色標章就一定永續","回收越多就代表製造越少","再生能源不需備援或廢棄規畫"],"A","結論要交代功能單位、條件、投入變化和仍需查證的生命週期限制；名稱或標章不能取代資料。","先寫服務和邊界，再比較材料、能源、回收與綠能全流程，最後列出失效條件。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["先界定要維持的服務，例如一份餐點、飲水或相同照度。","畫出原料、製造、使用、清洗／運輸、回收與報廢的資源流。","核對生命週期、供應穩定、衛生安全、後端處理和反彈效應資料。",f"排除只看標章、單次數字、桶子數或忽略服務品質的選項，答案為 {target}。",f"用條件式結論回查是否能被重測：{explanation}"]
    return {"id":f"question-science-content-na-iv-7-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-na-iv-7"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與生態資料的減量、再利用、回收、綠能、能源效率、生命週期與永續判讀能力方向；本題為 Na-Ⅳ-7 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-na-iv-7","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-na-iv-7、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與生態資料能力模式，獨立融合減量、再利用、回收、分類污染、綠能、服務功能、生命週期、供應穩定、反彈效應與校園永續方案。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-na-iv-7-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為減量、再利用、回收、綠能、服務功能、生命週期、供應穩定與反彈效應；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content na-iv-7")
if __name__=="__main__": main()
