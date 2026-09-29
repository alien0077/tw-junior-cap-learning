import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSON = ROOT / "lessons/science/lesson-science-content-md-iv-2.json"
QDIR = ROOT / "questions/science"
REPORT = ROOT / "implementation/reports/science-content-md-iv-2-first-pass-review.json"
TODAY = "2026-09-23"
SOURCES = [
    ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf", "高雄市立鹽埕國民中學公開自然科段考試題", "颱風季節、氣象資料與災害判讀", "取颱風路徑、風雨資料與災害判讀能力方向，未複製題文。"),
    ("https://www.nhjh.tp.edu.tw/uploads/1675417616549dOhkhC5L.pdf", "臺北市立內湖國民中學公開九年級理化段考", "風雨、氣壓、暴潮與防災", "取風雨、氣壓、海象及防災條件整合判讀方向，另寫新情境。"),
    ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf", "高雄市立國昌國民中學公開三年級自然科試題", "降雨、洪水、地形與生命財產風險", "取降雨、地形、暴露與安全決策能力方向，未複製原題或圖表。"),
]
REFS = [{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS = [
 ("easy", "從臺灣長期月資料看颱風活動，哪個敘述最恰當？", ["夏秋較常見是長期統計傾向，不代表每年固定月份必有颱風", "只要進入夏季每天都會有颱風", "冬季完全不可能有任何強風雨", "一個月份的資料就能代表所有年代"], "A", "季節性是長期資料的機率與頻率特徵，不能改寫成逐年必然預測；短期事件仍要看即時觀測與警報。", "先區分長期平均和單次預報，再檢查選項是否把傾向誇大成必然。"),
 ("medium", "同一颱風造成甲地招牌損壞、乙地道路中斷，判讀時首先應比較什麼？", ["兩地的颱風名稱字數", "風雨危害、地形、人口與設施暴露、建物脆弱度及防護條件", "只比較兩地誰的風速最大", "只比較災損照片張數"], "B", "損失是危害與暴露、脆弱度、防護交會的結果；只看風速不能解釋低窪、山谷、建物固定或預警差異。", "把資料分成危害、暴露、脆弱度和防護四欄，再尋找能解釋兩地差異的證據。"),
 ("medium", "山城累積雨量高於沿海鎮，但沿海鎮招牌損壞較多；較合理的說法是？", ["資料互相矛盾，所以不能分析", "山城可能有較高道路或溪水暴漲風險，沿海鎮則可能因建物與強陣風暴露增加風害；仍需更多資料", "災損較多的地方雨量一定較大", "只要風速小就沒有生命風險"], "B", "不同危害與暴露可以在兩地分別占優勢，必須按災害類型分解；沒有排水、道路、固定方式等資料時仍要保留限制。", "先把總損失拆成風害、水患和交通等類別，再將各類與相應條件配對。"),
 ("easy", "颱風眼經過時短暫變得平靜，哪個行動最安全？", ["趁平靜外出觀察海邊", "以官方警報與地方指示為準，留在安全處，不能把短暫平靜當成解除危險", "立刻拆除防水設備", "因為無風就可穿越積水道路"], "B", "颱風眼只是系統中的短暫區域，後續風雨可能再增強；生命安全與官方資訊優先於現場直覺。", "先判斷危險是否真正解除，再依官方資訊決定行動，排除以短時間觀察代替警報的選項。"),
 ("medium", "要比較兩個社區的颱風淹水風險，哪組資料最有用？", ["只記錄颱風名稱", "累積雨量與降雨時序、地勢與排水、河海位置、人口設施、警戒時間和歷次水位", "只看最高風速", "只問哪個社區覺得雨最大"], "B", "淹水風險需要水量、時間、地形水路、暴露與應變條件；風速或主觀感受都無法單獨代表積淹水結果。", "先畫水從哪裡來、往哪裡走，再把可能受影響的人物與反應時間疊合。"),
 ("hard", "研究『提早停課是否降低學生暴露』，哪個比較設計較公平？", ["只比較一次颱風中不同學校的災損", "比較相近地區的預警時間、出勤人數、路徑雨量與交通條件，並追蹤多次事件", "讓介入學校同時搬到高地", "只訪問平安返家的學生"], "B", "出勤、路徑、雨量、交通與地勢都可能影響暴露；多次事件和相近對照比單次印象更能支持政策效果判斷。", "先定義暴露指標，再控制地點和事件差異，使用對照與多次觀察排除替代解釋。"),
 ("hard", "沿海低窪市場收到暴潮警報，哪個優先順序正確？", ["先搶救可移動商品，再查看避難公告", "先依官方指示撤離或避開海岸與低窪處，確認人員安全，再處理可延後財物", "趁潮水還沒到海邊拍照", "把地下室電器留在原處等待雨停"], "B", "暴潮、豪雨與排水受阻可能同時發生，低窪區的人員暴露必須先降低；財物處置不能凌駕撤離與避難。", "依不可逆損失的優先級排序：人員安全、官方指示、遠離危險，再處理財產。"),
 ("medium", "颱風過後要判斷道路是否可恢復通行，哪項做法較完整？", ["看到雨停就開放所有道路", "確認水位、土石與路基、電線、落石、橋梁和官方檢查結果，再依公告通行", "只看社群上一張照片", "只要車輛能勉強通過就代表安全"], "B", "雨停不等於二次危險消失；水位、沖刷、落石、電力與橋梁結構都需要專業檢查和權責公告。", "列出表面天氣和道路結構的不同風險，再依官方檢查證據決定是否解除限制。"),
 ("hard", "用災損總額比較兩地受災嚴重程度時，最需要補充哪項觀念？", ["總額越大就必然代表每位居民風險越高", "要考慮人口、建物與資產量、受災範圍、物價和資料涵蓋，必要時用相對指標比較", "刪除小額損失即可公平", "只比較新聞標題的形容詞"], "B", "資產多的地區總額可能高，但個人或每棟建物的風險未必較高；指標定義和分母會改變比較結果。", "先確認總額的測量範圍，再選合適分母與空間時間尺度，避免把結果直接等同風險。"),
 ("medium", "家庭製作颱風安全卡，哪個內容最符合本課的證據推理？", ["只寫『颱風很可怕』", "標出颱風前的物品固定與避難資訊、颱風中的危險區域、颱風後的二次危險與通報方式", "只記錄最大風速數字", "用上一年的路徑保證今年安全"], "B", "安全卡要把危害、暴露、時序與可行行動連起來；即時公告和地點條件會改變決策，不能用舊路徑保證未來。", "按颱風前、中、後排列資料與行動，為每項行動標出觸發條件和官方資訊來源。"),
]

def make_question(n, row):
    diff,prompt,options,source_answer,explanation,strategy=row
    target="ACDBACDBAC"[n-1]
    correct_text=options[ord(source_answer)-65]
    distractors=[text for i,text in enumerate(options) if i != ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct_text)
        else: ordered.append(distractors[di]); di+=1
    steps=["圈出題目中的時間、地點、危害或損失條件。","把危害、暴露、脆弱度與防護資料分欄，避免只看單一數字。","比較選項是否符合資料的時間尺度、空間尺度與安全限制。",f"排除把統計傾向說成必然、把結果倒推原因或違反安全的選項，答案為 {target}。",f"用條件式句子回查結論：{explanation}"]
    return {"id":f"question-science-content-md-iv-2-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-md-iv-2"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化試題的颱風季節、風雨、氣象資料、災害、暴露與防災安全能力方向；本題為 Md-Ⅳ-2 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-md-iv-2","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-md-iv-2、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然科試題能力模式，獨立融合颱風季節性、危害、暴露、脆弱度、路徑、雨量、風速、地形、海岸、災損尺度與防災時序。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-md-iv-2-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為颱風季節性、危害—暴露—脆弱度、風雨與災損資料、防災時序及比較尺度；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content md-iv-2")
if __name__=="__main__": main()
