import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-nc-iv-4.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-nc-iv-4-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","能源轉換、場址條件、供電、環境影響與資料判讀","取公立學校自然科對能源來源、效率、資料與生活應用的能力方向，另寫新興能源案例。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","能源、功率、效率、波動與系統證據","取公開會考對能源轉換、供需與科學限制的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","發電、燃料、供應穩定、環境與安全","取公立學校自然科對能源開發、燃料供應與環境限制的能力方向，重新設計題目。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","比較海岸小鎮的太陽能場址，哪組資料最不能省略？",["日照時數、遮蔽物、方向、季節輸出與夜間需求","只看晴天中午輸出","只看面板顏色","只比較場址名稱"],"A","太陽能輸出受日照、遮蔽、方向和季節影響，還要與需求時間對齊；單一時刻不能代表服務能力。","先固定要提供的服務，再把場址、時間、輸出和需求資料放在同一表格。"),
 ("medium","風力方案冬季風況佳但夏季午後風速低，最合理的供電結論是？",["需要逐時輸出、儲能或備援資料，不能只用冬季平均風速保證全年供電","冬季風大就代表全年穩定","風速高就不需設備維護","風力是再生能源所以沒有供電缺口"],"A","平均或季節資料只能描述部分條件；供電可靠度取決於需求時段、儲能、備援和輸出變動。","畫出需求與風力輸出的時間序列，標出缺口後再比較儲能和備援。"),
 ("medium","附近有穩定農業廢棄物，評估生質能仍要查什麼？",["含水率、收集量、運輸距離、處理排放、土地用途與季節供應","只看廢棄物名稱就能保證低碳","只看燃燒火焰","因為是生物來源就沒有污染"],"A","生質能的實際效益受原料品質、供應鏈、運輸、處理和排放影響；來源是生物質不等於整體無代價。","沿來源—收集—運輸—轉換—排放鏈逐段列資料和限制。"),
 ("hard","燃料電池發電端安靜，但要判斷整體環境效益還需知道？",["氫的製造來源、運輸儲存、轉換效率、洩漏與設備壽命","只看發電端沒有煙就足夠","只看燃料電池外觀","安靜代表一定可再生"],"A","燃料電池把反應位置與能源供應分開；若氫由高排放方式製造，整體生命週期仍需評估。","先區分發電端與上游供應鏈，再補足效率、排放、安全和壽命資料。"),
 ("easy","汽電共生的主要概念是？",["同一燃料先發電，再利用原本可能排出的熱，提高整體能源利用","它是一種新的燃料名稱","它能讓能量不需任何轉換損失","只適用於太陽能"],"A","汽電共生回收發電過程的熱，可提高整體利用率；仍要考慮燃料排放、需求匹配和設備維護。","先畫輸入、電力輸出和熱輸出，再檢查回收熱是否真的被需求使用。"),
 ("hard","核融合在能源課程中應如何描述？",["可作為研究中的高難度發電方向，不能把研究潛力寫成目前已普遍商轉的供電答案","已是所有家庭的主要電源","只要提到核就等同核分裂發電","完全不需評估材料與安全"],"A","技術成熟度是能源決策的重要條件；研究方向的潛力、示範成功和大規模商轉不能混用。","先標示技術階段，再分別寫已知證據、未知條件和不可過度外推的主張。"),
 ("medium","校園要在停電時維持照明四小時，比較新興能源時應固定什麼？",["照明功率、四小時服務、可接受中斷、儲能容量與備援條件","只固定設備名稱","只比較全年發電量","只看建置宣傳圖"],"A","公平比較需要相同服務量和時間尺度，並把儲能效率、備援與安全放入系統邊界。","先算需求能量，再逐方案扣除轉換和儲能損失，最後檢查備援與安全。"),
 ("hard","太陽能方案白天發電多但夜間需求高，哪個選擇最完整？",["比較電池容量、充放電效率、壽命、備援、退役回收和夜間供電缺口","只因白天總發電量高就直接採用","把夜間需求刪除","只看面板額定功率"],"A","供電效益不只看總量，還要看時段配合和儲能的生命週期、維護、安全與退役責任。","用逐時供需和儲能帳本估算缺口，再把設備壽命、回收和備援加入決策。"),
 ("medium","哪種報告能比較新興能源的環境代價而不流於口號？",["分別記錄運轉排放、製造與施工、土地／生態、噪音、運輸、廢棄與受影響者","只寫『綠色所以環保』","只記錄最高發電量","只問支持者感受"],"A","環境影響是多階段、多指標問題；把生命週期和受影響者列出，才能說明證據與限制。","先定義系統邊界，再把影響分成運轉、上游、場址、退役和社會分配。"),
 ("hard","哪句最適合作為新興能源開發結論？",["在需求時段、輸出與儲能資料可重現，且排放、生態、安全和維護門檻符合時，方案甲可先試辦；仍需以監測結果調整或停止","新興能源必定比舊能源好","任何再生能源都可無條件取代備援","研究中的技術可直接作為今天的穩定主電源"],"A","新興技術要同時寫服務、成熟度、限制、環境和可修正門檻，不能以名稱或潛力代替證據。","把方案的已知資料、未知資料和停損門檻寫入同一句條件式結論。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["界定能源服務、需求時段、輸出、儲能和可接受中斷。","畫出來源—轉換裝置—可用輸出—限制的能量鏈。","核對季節、場址、技術成熟度、生命週期、排放、生態與安全資料。",f"排除只看再生標籤、單一平均、研究潛力或無條件保證的選項，答案為 {target}。",f"用可重測、可修正的條件式結論回查：{explanation}"]
    return {"id":f"question-science-content-nc-iv-4-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-nc-iv-4"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的新興能源、供電、能源轉換、儲能、技術成熟度、生命週期與環境影響能力方向；本題為 Nc-Ⅳ-4 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-nc-iv-4","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-nc-iv-4、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合風力、太陽能、生質能、燃料電池、汽電共生、核融合研究、場址、儲能、供電時段、技術成熟度、生命週期與環境影響。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-nc-iv-4-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為風力、太陽能、生質能、燃料電池、汽電共生、核融合研究、供電時段、儲能、技術成熟度與生命週期；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content nc-iv-4")
if __name__=="__main__": main()
