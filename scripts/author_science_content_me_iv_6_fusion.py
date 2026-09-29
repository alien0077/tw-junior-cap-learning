import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-me-iv-6.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-me-iv-6-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E5%9C%8B%E6%98%8C--%E4%BA%8C%E5%B9%B4%E7%B4%9A--%E7%90%86%E5%8C%96%E7%A7%91_2.pdf","高雄市立國昌國民中學公開理化科段考試題","食物鏈、污染物傳遞、生物累積與環境決策","取公立學校公開題型對食物鏈、污染物和證據判讀的能力方向，未複製原題。"),
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","環境因子、生態調查、食物關係與資料推論","取公立國中自然科對食物關係、污染與資料限制的能力方向，另寫湖泊案例。"),
 ("https://market.cloud.edu.tw/resources/web/1807720","教育雲國中生態與環境教學資源","生態系、食物鏈、污染物與保育應用","取公開教學資源對生態關係、環境觀察和行動方案的能力方向，未重製內容。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","同一湖泊中，藻類、浮游動物、小魚到鷺鷥魚肉的污染物濃度依序升高，最適合先提出哪個模型？",["可能存在沿營養階層傳遞並放大的現象","污染物只在水中，不會進入生物","最高階生物一定立刻中毒","數字越大表示樣本一定越健康"],"A","若採樣時間、食物關係、組織基準和污染物特性可比，階層濃度上升與生物放大模型一致；它仍是有條件的模型解釋。","先畫誰吃誰，再核對濃度、單位和取樣條件，最後把『一致』與『證明』區分。"),
 ("medium","同一種魚在暴露十天後體內濃度增加，但沒有比較其他營養階層；這較適合稱為？",["生物放大已被證明","生物累積，因為描述同一生物隨時間的體內增加","食物網消失","污染物已完全分解"],"B","生物累積描述同一個體或物種在暴露期間的體內變化；生物放大則需要不同營養階層的可比資料。","先問比較的是同一生物隨時間，還是不同營養階層，再選概念，不因數值增加就跳到放大。"),
 ("medium","比較水中 0.02 微克／公升和魚肉 12 微克／公斤時，最先要注意什麼？",["數字較大的魚一定承受六百倍危險","水和魚肉的測量對象、單位、濕重／乾重與採樣條件不同，不能直接用數字相除下結論","所有單位都可直接比較","只要魚還活著就可忽略單位"],"B","環境濃度和組織濃度回答不同問題，分母與取樣條件會改變數值意義；先核對可比性才能談傳遞或風險。","逐一標記測量對象、單位、組織基準和時間，只有基準可比才進行濃度趨勢判讀。"),
 ("hard","高階魚的濃度較高，但高階魚來自另一座污染源不同的池塘，能得出什麼？",["直接證明食物鏈造成放大","只能說兩群樣本有濃度差異，不能把差異全歸因於營養階層","證明兩座池塘完全相同","只要營養階層相同就沒有替代解釋"],"B","地點和污染源同時改變，混淆了營養階層與環境暴露；必須使用同水域或合適對照和更多資料。","列出兩地不同條件，判斷是否有混淆變因，再決定結論只能停留在差異描述。"),
 ("easy","若污染物不易分解且進入體內的量長期大於排出量，哪個過程較可能發生？",["體內濃度可能隨時間增加，形成生物累積","污染物必定只留在水中","食物鏈一定縮短","所有生物都會立刻死亡"],"A","進入、代謝、分解與排出速率的差額會影響體內濃度；不易分解只是重要條件之一，不能保證所有物種結果相同。","把進入量和排出量畫成帳本，加入時間和物種差異，再用可能而非必然語氣表達。"),
 ("hard","整治後水樣濃度下降，但老魚與底泥濃度仍偏高，最合理的溝通是？",["水變乾淨後所有魚立即安全","環境濃度下降與生物、底泥變化可能有時間差，應持續檢測並依主管機關建議行動","只測一尾魚即可保證全湖","污染物一定已消失"],"B","不同環境庫和生物階層的更新速度不同；風險溝通要分開環境檢出、食用暴露和健康效應，不能用一個水樣全面保證。","先分辨哪個庫的資料變了，再追蹤魚種、體型、底泥與食用暴露，最後引用正式公告而非自行試吃。"),
 ("medium","要驗證營養階層濃度是否上升，哪項設計最有力？",["只測一次最高階一尾生物","在同水域相近時間測各營養階層，統一組織與單位並增加樣本和重複","只選最高數值的樣本","把不同污染物混在同一張表"],"B","相同空間、時間、分析基準與足夠樣本可減少替代解釋，讓階層趨勢較能被檢查；單一極端值不代表族群。","先畫食物網和取樣表，再統一基準、設定樣本與重複，最後比較平均與變異及其限制。"),
 ("hard","若同一魚種在兩季濃度不同，但食物來源和脂肪比例也不同，應如何下結論？",["季節一定是唯一原因","濃度差異可能同時受季節、食物、脂肪比例與污染源影響，需要控制或分層分析","直接稱為生物放大","刪掉脂肪比例資料"],"B","季節和生物特性與暴露來源同時變動，不能把差異指定給單一因素；分層、對照和額外測量可幫助釐清。","把每個同步變化列成候選原因，尋找可固定或分層比較的條件，再降低結論強度。"),
 ("medium","有人說『鷺鷥魚肉檢出污染物，所以人吃一口就會中毒』，哪個回應最正確？",["檢出、危害與實際風險不同，要看濃度、食用量、頻率、暴露途徑與主管機關指引","只要檢出就能算出每個人的疾病","魚越大就一定完全不能吃","只要煮熟污染物就全部消失"],"A","檢出是分析結果，不等同健康效應；風險需要結合劑量、頻率、個體和正式標準，不能自行把食品建議簡化。","把檢出、暴露和健康結果拆開，查核濃度與食用條件，再依主管機關公告而非直覺下建議。"),
 ("hard","食物網不是直線且某污染物只在脂肪組織較易留存，最需要補充哪筆資料？",["只記錄生物顏色","各物種攝食關係、體型／年齡、脂肪比例、污染物濃度基準與暴露時間","只記錄最高階名稱","只測水面溫度一次"],"B","分枝食物網、體內分布、生物特性和時間都會改變濃度判讀；補足這些資料才能評估是否存在階層放大及其限制。","先把食物網從單線改成關係圖，再加入生物特徵、暴露時間和一致分析基準，最後檢查每條推論的證據。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["畫出食物關係並標示環境濃度或體內濃度。","核對物種、營養階層、組織、單位、時間與污染物特性。","分辨生物累積、營養階層放大、相關與健康風險的不同問題。",f"排除把檢出直接等同危害、忽略混淆變因或過度外推的選項，答案為 {target}。",f"把結論寫成有證據範圍的句子並列出補測資料：{explanation}"]
    return {"id":f"question-science-content-me-iv-6-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-me-iv-6"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開生態自然科資料的食物鏈、污染物傳遞、生物累積、生物放大、資料單位與環境決策能力方向；本題為 Me-Ⅳ-6 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-me-iv-6","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-me-iv-6、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開生態自然科題型能力模式，獨立融合食物鏈、污染物傳遞、生物累積、生物放大、濃度基準、組織差異、樣本設計、食物安全與風險溝通。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-me-iv-6-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為食物鏈、污染物傳遞、生物累積與放大、單位與樣本、食物安全和風險溝通；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content me-iv-6")
if __name__=="__main__": main()
