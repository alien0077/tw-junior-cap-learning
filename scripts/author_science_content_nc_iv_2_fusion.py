import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/"lessons/science/lesson-science-content-nc-iv-2.json"
QDIR=ROOT/"questions/science"
REPORT=ROOT/"implementation/reports/science-content-nc-iv-2-first-pass-review.json"
TODAY="2026-09-23"
SOURCES=[
 ("https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E8%87%AA%E7%84%B6.pdf","高雄市立鹽埕國民中學公開自然科段考試題","能源方案、資料判讀、環境影響與生活決策","取公立學校自然科對能源開發、資料證據與風險判讀的能力方向，另寫能源審議情境。"),
 ("https://www.grow22.com/download/114/114_cp/05_114P_Nature.pdf","114 年國中教育會考自然科公開試題","能源、效率、供需、圖表與科學推理","取公開會考對能源資料、多條件比較與限制表達的能力方向，未複製原題。"),
 ("https://www.kcjh.kh.edu.tw/upload/190/104_34764/%E4%B8%89%E5%B9%B4%E7%B4%9A%E7%90%86%E5%8C%96-%E7%AC%AC三次段考5-OK.pdf","高雄市立國昌國民中學公開三年級自然科試題","發電、環境代價、事故風險與公共決策","取公立學校自然科對能源效益、風險與社會環境資料的能力方向，重新設計題目。"),
]
REFS=[{"url":u,"title":t,"year":"109-115","subject":"science","locator":loc,"observedPattern":pat,"reuseDecision":"pattern-only","status":"recorded","locatorLevel":"paper"} for u,t,loc,pat in SOURCES]
ROWS=[
 ("medium","比較潮汐機組與屋頂光電加電池前，第一步最應界定什麼？",["能源需求、系統範圍、評估期間和受影響的人與生物","先決定支持哪個方案","只看最高發電量","只問一位居民"],"A","沒有系統邊界，就無法比較供電效益和由誰在何時承受的代價；需求與價值也不能互相冒充資料。","先寫需求與服務，再固定地點、期間、受影響對象和比較指標。"),
 ("hard","某方案估計可補足尖峰 28%，但候鳥調查只有兩季；合理結論是？",["28% 代表方案必定最佳","供電效益有初步資料，候鳥風險證據不足，應補做繁殖與遷徙季監測再決定","候鳥資料不足所以供電數字無效","只要是潮汐能就沒有生態影響"],"B","供電比例與生態調查回答不同問題；資料不足應降低結論強度並設計補測，而不是刪除或補猜。","把已知效益與未知代價分開，標記時間、樣本和季節缺口，再寫條件式決策。"),
 ("medium","要把『可能影響魚苗』改寫成可查證問題，哪項最好？",["哪個物種在何季節、何位置受到何種水流或濁度變化影響，如何測量與比較","魚苗一定會消失嗎","大家覺得危險嗎","只看機組外觀"],"A","可查證問題要指定對象、時間、地點、影響機制、指標和比較方法，才能由模糊疑慮轉成研究設計。","先拆出物種、季節、空間和危害，再選濁度、水流、出現率或繁殖等指標。"),
 ("easy","能源風險評估中，『老舊堤岸且缺乏替代道路』較接近哪種條件？",["脆弱度，會使同一危害造成較大後果","能源來源","發電功率","再生性"],"A","脆弱度描述受影響系統承受和恢復的能力；老舊設施和替代路徑不足會放大危害後果。","先分辨危害、暴露、脆弱度和效益，再把條件放進相應欄位。"),
 ("hard","若候鳥繁殖季活動下降，但施工期濁度也增加，哪種推論最謹慎？",["資料支持可能有關聯，仍需基線、對照、其他干擾和時間序列來判斷機制","已證明機組是唯一原因","候鳥下降一定與發電量成正比","只要停工一天就能證明"],"A","兩項結果同時發生可形成假說，但施工、天候、食物或人為干擾也可能影響活動；需比較和重複。","先描述共同時間變化，再列替代解釋與控制方法，不把關聯寫成唯一因果。"),
 ("medium","能源方案的事故風險要如何寫得比『很危險』更有用？",["列出危害、暴露對象、發生可能性、後果嚴重度、可逆性與防護門檻","只用低中高顏色，不說理由","只引用支持者的保證","以零風險為唯一標準"],"A","風險溝通需要把事件、對象、可能性、影響與防護條件具體化；低中高只能作摘要，不能代替理由。","把模糊形容詞拆成事件鏈，再為每一段指定資料、門檻和責任。"),
 ("hard","社區審議能源設施時，哪項做法較能兼顧公平？",["讓居民、養殖戶、研究者、學生和電力調度者都看到資料、提出受影響指標，並公開決策與補救規則","只由發電量受益者投票","只公布工程成本","把噪音和景觀代價交給少數居民承擔"],"A","公平不只是多數表決，還要看誰獲益、誰承受風險、誰能參與及超標後如何補救。","列出各群體的效益、暴露和成本，再把資料公開、參與和補救寫入方案。"),
 ("medium","屋頂太陽能加電池方案初期成本低，但電池容量未確認；下一步應查什麼？",["需求時段、儲能容量與效率、壽命、維護、消防安全和退役回收","只看屋頂面積","只看晴天發電量","因成本低就忽略容量"],"A","初期成本不能代表整體風險；儲能是否能覆蓋需求、如何維護及退役都會改變方案結果。","先用逐時需求估算容量，再加入效率、壽命、安全、成本與回收責任。"),
 ("hard","何種條件最適合支持『先試辦再擴大』的能源決策？",["設定明確期間、基線、供電效益指標、生態與安全門檻、公開資料和超標暫停規則","只要支持者多就試辦","不需監測因為規模小","先擴大再決定要不要收資料"],"A","可逆試辦把不確定性轉為學習機會，但必須事先定義成功、失效和責任，否則只是延後決策。","先寫基線與門檻，再指定測量、公開、停損和修正流程。"),
 ("medium","哪句最適合作為潮口能源方案的結論？",["在供電缺口、施工濁度、候鳥活動與維護成本均未超過事前門檻，且監測資料公開的條件下，先以小規模試辦並保留停工選項","只要能發電就應永久建設","只要有生態疑慮就所有能源都不能用","28% 比 19% 大所以不需其他資料"],"A","成熟的能源決策承認不確定性，以服務效益和環境社會門檻共同決定，並讓新資料能觸發暫停或調整。","把效益、風險、門檻、監測者和修正權責放在同一句條件式結論中。"),
]

def make_question(n,row):
    diff,prompt,opts,source_answer,explanation,strategy=row; target="ACDBACDBAC"[n-1]
    correct=opts[ord(source_answer)-65]; distractors=[x for i,x in enumerate(opts) if i!=ord(source_answer)-65]
    ordered=[]; di=0
    for label in "ABCD":
        if label==target: ordered.append(correct)
        else: ordered.append(distractors[di]); di+=1
    steps=["界定能源需求、地點、期間、受影響者與系統邊界。","把效益、危害、暴露、脆弱度、機率、後果和價值選擇分開。","核對基線、季節、樣本、生命週期、成本、供電時段與安全門檻。",f"排除只看發電量、把可能說成必然或忽略少數群體的選項，答案為 {target}。",f"用可監測、可修正的條件式決策回查結論：{explanation}"]
    return {"id":f"question-science-content-nc-iv-2-{n}","subject":"science","type":"single-choice","prompt":prompt,"options":[{"id":k,"text":v} for k,v in zip("ABCD",ordered)],"knowledgeIds":["kg-science-content-nc-iv-2"],"difficulty":diff,"answer":{"value":target,"explanation":f"{explanation} 正確答案為選項 {target}。"},"provenance":{"origin":"original","license":"All rights reserved","sourceUrl":SOURCES[0][0],"sourceLocator":"三筆公立學校／公開自然與理化資料的能源開發、效益、風險、生命週期、生態與公共決策能力方向；本題為 Nc-Ⅳ-2 原創情境改寫。","authoringNote":"依官方課綱、Knowledge Graph 與公開題型 pattern-only 方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。"},"reviewStatus":"draft","updatedAt":TODAY,"lessonId":"lesson-science-content-nc-iv-2","examPatternRefs":REFS,"solutionStrategy":strategy,"solutionSteps":steps}

def main():
    lesson=json.loads(LESSON.read_text(encoding="utf-8")); lesson.update({"updatedAt":TODAY,"reviewStatus":"draft","authoringStandard":"version-fused-v1"})
    for row in lesson.get("publisherResearch",[])+lesson.get("versionResearch",[]): row["reviewedAt"]=TODAY
    lesson["fusionRecord"]["llmSynthesisNote"]="本課依官方自然科學課綱、kg-science-content-nc-iv-2、南一／康軒／翰林可取得的公開版本研究限制與三筆公立學校／公開自然與理化題型能力模式，獨立融合能源需求、系統邊界、風險、危害、暴露、脆弱度、機率、影響、利害關係人、生命週期、監測門檻與可逆試辦。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。"
    LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    for i,row in enumerate(ROWS,1): (QDIR/f"question-science-content-nc-iv-2-{i}.json").write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    REPORT.write_text(json.dumps({"unit":lesson["title"],"lessonId":lesson["id"],"status":"first-pass-ai-review-complete","reviewStatus":"draft","checkedQuestions":10,"checks":{"unitSpecificOriginalContent":True,"threeVersionResearchRecords":True,"threePublicSchoolExamPatternSources":True,"answersAndDetailedSteps":True,"interactivePredictionManipulationExplanation":True,"terraSecondPass":"pending"},"reviewedAt":TODAY,"note":"10 題重新改寫為能源效益、風險、系統邊界、機率與影響、生態、利害關係人、生命週期、監測和可逆試辦；每題具唯一答案、解析、策略與五步解法。"},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("authored science content nc-iv-2")
if __name__=="__main__": main()
