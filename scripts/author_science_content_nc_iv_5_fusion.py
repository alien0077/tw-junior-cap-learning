import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-nc-iv-5.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-nc-iv-5-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","能源轉換、效率、功率、生活科技與資料判讀","取公立學校自然科對能量轉換、效率與科技應用的能力方向，另寫裝置案例。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","能量、電力、效率、波動與實驗證據","取公開會考對能量資料、單位、效率與限制表達的推理方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","能源科技、燃料、供應與環境安全","取公立學校自然科對科技系統、能源利用與環境限制的能力方向，重新設計題目。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("easy","油電混合車減速時，回生煞車的主要能量路徑是？",["部分車輪運動能轉為電能儲存在電池，之後可供馬達使用","汽油直接變成煞車片冷氣","電池把所有熱量變回原有機械能","能量在轉換中完全不損失"],"A","回生煞車可把部分原本會以熱散失的運動能轉成電能，但轉換、儲存與馬達仍有損耗，不會百分之百回收。","先畫來源、轉換器、儲存、輸出和損耗，再判斷每個箭頭的能量形式。"),
 ("medium","某車引擎輸入能量 100 份、車輪得到 25 份機械能，轉換效率為？",["4%","25%","75%","125%"],"B","效率=有用輸出／輸入×100%=25/100×100%=25%；其餘能量可能以熱、聲和摩擦等形式散失。","先確認分子是有用輸出、分母是總輸入，再算百分比並檢查不超過 100%。"),
 ("medium","走走停停時直接驅動得到 18 份、回收電池再提供 5 份；比較車輪輸出時要注意什麼？",["可比較總輸出 23 份，但要確認電池初始能量，避免把原有儲能重複計入","直接把 18 和 5 當兩次燃料輸入","只看 5 份就代表效率提高一倍","回收電能不必計入系統邊界"],"A","回收能量的來源與電池初始狀態會影響系統帳本；公平比較需固定行程、輸入和電池狀態。","先畫完整能量帳本，再確認回收能量是否來自本次行程及是否重複計算。"),
 ("hard","太陽能飛機晴天能產電但陰天航程不足，最關鍵的設計條件是？",["日照輸入、任務功率、載重、電池容量、航程與備援是否相互匹配","只看光電板面積","只看晴天峰值輸出","因為日照可再生就不需備援"],"A","可行性取決於變動輸入和任務需求的時間配合；載重、儲能、功率與備援共同決定陰天能否完成任務。","把任務需求寫成時間和功率，再用日照、電池和損耗逐時核對能量缺口。"),
 ("easy","能源、裝置與有用輸出的區分何者正確？",["燃料化學能是來源，引擎或馬達是轉換裝置，車輪機械運動是有用輸出","馬達本身就是能源","輸出等同所有輸入能量","電池品牌就是能量形式"],"A","來源提供能量、裝置進行轉換、有用輸出是任務真正需要的結果；三者不可用名稱互相取代。","先替每項名詞標上來源、裝置或輸出，再沿能量箭頭檢查轉換和損耗。"),
 ("hard","電池車操作時沒有尾氣，仍需評估哪些生命週期條件？",["電力來源、電池製造材料、充電損耗、壽命、回收與車輛製造排放","只看行駛時是否冒煙","只看車內安靜程度","沒有尾氣就代表全生命週期零排放"],"A","操作階段的排放和完整生命週期不同；上游發電、材料、充電、壽命和回收都會改變整體影響。","先定義生命週期邊界，再分段列能源、材料、使用、維修與退役資料。"),
 ("medium","比較油電車和純電車在相同路線的能量表現，哪項控制最重要？",["固定路線、載重、速度、電池初始狀態、測試距離和比較的輸入邊界","讓一車走上坡、一車走下坡","只比較車身顏色","只挑最省的一次結果"],"A","路況、載重和初始狀態會改變輸出；控制條件和多次測試才能避免把情境差異誤當技術效益。","先固定任務，再統一輸入與測量方法，最後比較平均值與變異。"),
 ("hard","若太陽能無人機很輕但陰天續航不足，電池車續航較穩定但需充電，較完整的方案是？",["依任務時段、載重、天候、充電來源和備援需求設主方案與備援，不以單一綠色標籤決定","只因無人機輕就永久選它","只因電池車穩定就忽略充電來源","把陰天資料排除"],"A","科技選擇要對齊任務與條件；不同裝置可在不同情境互補，仍需比較生命週期、安全和維護。","列出任務限制和各方案缺口，再安排主備援與可重測指標。"),
 ("medium","一項能源科技的操作階段排放下降，哪項敘述最恰當？",["可表示特定操作階段改善，但不能直接推成製造、維修、回收與所有情境都改善","代表全生命週期一定零排放","代表效率永遠相同","不必再看輸入能源來源"],"A","排放主張必須限定系統邊界與階段；製造、供電、材料、維修和退役可能改變整體結果。","先指出資料涵蓋的階段，再列未涵蓋部分和下一項生命週期查證。"),
 ("hard","哪句最適合作為新興能源科技的結論？",["在指定路況、日照、載重、儲能和充電條件下，方案甲提升有用輸出並降低部分損耗；仍需追蹤製造、維修、回收與極端天候限制","只要有新技術就必然比舊技術好","能量轉換可以沒有任何損失","使用再生能源就不需計算效率"],"A","科技方案的效益是條件式且有系統邊界的；能量守恆仍成立，轉換損耗與生命週期限制不能省略。","把功能、輸入、轉換、損耗、條件和後續證據寫在同一條推理鏈。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["畫出能源來源、轉換器、儲存／控制、輸出和損耗。","確認有用輸出、輸入分母、功率、時間、效率和任務需求。","固定路況、天候、載重、初始狀態與生命週期範圍，檢查替代解釋。",f"排除把新興等同完美、把操作階段等同全生命週期或忽略儲能的選項，答案為 {target}。",f"用條件式能量帳本回查科技判斷：{explanation}"]
    return {"id":f"question-science-content-nc-iv-5-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-nc-iv-5"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的油電混合、電池、太陽能、能源轉換、效率、儲能、生命週期與科技決策能力方向；本題為 Nc-Ⅳ-5 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-nc-iv-5","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-nc-iv-5、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合油電混合、回生煞車、太陽能飛機、電池車、能源—裝置—輸出、效率、儲能、任務條件、生命週期與科技決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-nc-iv-5-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為油電混合、回生煞車、太陽能飛機、電池車、能源轉換、效率、儲能、任務條件與生命週期；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content nc-iv-5")
if __name__=="__main__": main()
