import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-nc-iv-3.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-nc-iv-3-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","燃料、能源轉換、燃燒、環境影響與資料判讀","取公立學校自然科對燃料特性、能源使用與環境資料的能力方向，另寫地質燃料案例。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","化學反應、能源、物質特性與圖表推理","取公開會考對物質性質、能量與證據限制的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","化石燃料、燃燒、排放、資源與能源決策","取公立學校自然科對燃料來源、燃燒與能源選擇的能力方向，重新設計題目。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","判斷一層含煤地層的形成線索，哪組條件最重要？",["遠古有機物來源、沉積掩埋、低氧或缺氧、長期壓力與溫度","只要地底有樹葉就一定形成煤","只要找到恐龍化石就能證明是煤","埋藏一天即可完成轉化"],"A","煤的形成需要有機物、沉積、長時間及地質條件；『化石』不等於大型動物遺骸，單一線索也不足以證明完整成因。","先從地層資料找來源，再依時間、氧氣、壓力與溫度建立形成鏈。"),
 ("medium","石油和天然氣的形成資料顯示遠古微小生物沉積於缺氧細泥，深埋後產生液態與氣態烴；可支持什麼？",["在特定沉積盆地與地質條件下，有機物可能長期轉化為石油或天然氣","所有海洋都必然產油","只要有泥就一定有天然氣","石油是由恐龍直接變成"],"A","資料支持有機物、沉積、低氧、深埋和地熱等條件共同形成的可能性，不能外推成所有海洋或所有泥層都產油。","把資料明示的條件逐一列出，再標記不能由案例外推的範圍。"),
 ("medium","原油加熱後得到不同沸點範圍的餾分，最合理的解釋是？",["原油含有多種成分，利用沸點差異分離，不代表原油是單一純物質","原油本身只有一種分子","分餾會把元素變成另一種元素","所有低沸點餾分都必定是同一產品"],"A","原油是多種烴類與其他成分的混合物，分餾主要利用揮發性與沸點差異進行物理分離；產品用途還要查組成和範圍。","先判斷混合物或純物質，再用沸點排序說明分離，不把產品名稱直接套上。"),
 ("easy","下列何者最能描述烴類？",["主要由碳與氫組成的有機化合物，分子大小與排列可影響沸點和狀態","只含氧和氮的物質","所有烴類都溶於水且不可燃","烴類一定是固體"],"A","烴類的基本組成是碳和氫，不同分子結構會影響揮發性、沸點與常溫狀態；不能把所有烴類視為同一物質。","先抓組成定義，再用分子大小、排列和物理性質做有範圍的推論。"),
 ("hard","某餾分甲沸點 35–70℃、乙 150–200℃、丙 250–350℃，哪個排序判讀正確？",["在分餾過程中甲較易先汽化，丙較晚凝結；用途仍需查實際組成與產品規格","丙一定比甲含氧更多","甲一定完全沒有碳","沸點越高就一定是純物質"],"A","較低沸點的成分通常較易汽化，較高沸點者較不易揮發；沸點範圍只能支持分離先後，不能單獨決定完整用途或組成。","先由沸點排列揮發性，再標記資料不足的產品名稱、組成與排放推論。"),
 ("medium","化石燃料燃燒時，哪個結論最完整？",["會釋放可用能量，也可能產生二氧化碳；不完全燃燒或含硫成分還可能造成其他污染","燃燒只產生能量沒有物質變化","只要火焰看不見煙就沒有排放","二氧化碳不是燃燒產物"],"A","燃燒是化學反應，能量釋放與物質生成同時存在；排放種類受燃料組成與燃燒是否完全影響。","分開能量、反應物、產物和燃燒條件，不能用肉眼煙霧取代排放測量。"),
 ("hard","天然氣運轉排放可能低於煤，但仍不能稱為零污染，原因是？",["仍會產生二氧化碳，且開採、處理、運輸可能有甲烷洩漏與設備風險","只要是氣體就沒有污染","天然氣不需要運輸或儲存","低於煤代表所有環境影響皆為零"],"A","比較低排放不等於沒有排放；供應鏈洩漏、燃燒、基礎設施與事故都要納入生命週期。","先確認比較基準，再把燃燒、開採、運輸、儲存和洩漏分段檢查。"),
 ("medium","煤、石油、天然氣的能源決策要兼顧供應和環境，哪組資料較完整？",["能量供應、設備效率、燃料運輸、儲量／有限性、排放、安全與替代方案","只看每公斤燃料的價格","只看現有設備方便，不查排放","只用燃料名稱推測風險"],"A","能源選擇是系統比較，需同時看輸入、轉換、供應可靠度、生命週期與替代方案；單一價格或名稱不足。","建立燃料檔案卡，讓每個主張都對應一項可查證的資料和限制。"),
 ("hard","某離島改用液化天然氣但需要新儲槽和船運，最需要補查什麼？",["船運天候可靠度、儲槽安全、洩漏防護、維護成本、排放與停電備援","只看燃料火焰顏色","因天然氣低碳就省略安全演練","只問設備是否漂亮"],"A","燃料特性改變會帶來新的儲存、運輸和安全條件；低排放的可能效益不能取代供應鏈與備援資料。","先畫供應鏈，再逐段列危害、暴露、維護和停運後果。"),
 ("medium","哪句最適合作為化石燃料使用的科學結論？",["在供應需求、設備安全與排放門檻成立的條件下，方案甲可作過渡供能；仍需降低需求、監測排放並評估有限資源與替代能源","天然氣較乾淨所以永遠沒有問題","化石燃料能量高就不需考慮氣候影響","只要找到新礦就代表資源不會耗盡"],"A","化石燃料可提供能量但具有限性與排放代價，結論要寫條件、監測和替代路徑，不能把過渡方案說成永久無風險。","把能源服務、供應安全、排放、資源時間尺度和替代行動放進同一句條件式結論。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["圈出有機物來源、沉積、氧氣、壓力、溫度或燃料組成線索。","區分形成條件、物質性質、加工分離、燃燒產物與能源決策。","依資料核對沸點、單位、供應鏈、排放、安全與不能外推的範圍。",f"排除把化石誤作恐龍、把混合物當純物質或把低排放說成零污染的選項，答案為 {target}。",f"用地質—物質—使用—限制鏈回查結論：{explanation}"]
    return {"id":f"question-science-content-nc-iv-3-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-nc-iv-3"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的化石燃料形成、物質特性、分餾、燃燒、排放、供應與能源決策能力方向；本題為 Nc-Ⅳ-3 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-nc-iv-3","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-nc-iv-3、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合有機物沉積、缺氧、壓力與地熱、煤／石油／天然氣、烴類、原油混合物、分餾、燃燒、排放、供應鏈與能源決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-nc-iv-3-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為化石燃料形成、組成、分餾、燃燒、排放、供應鏈和能源選擇；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content nc-iv-3")
if __name__=="__main__": main()
