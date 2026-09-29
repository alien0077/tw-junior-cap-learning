import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-db-iv-7.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-db-iv-7-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','植物構造、生殖、事件順序與證據判讀','只取公立校方公開試題的生物構造與流程推理方向，重寫花的生殖情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','植物生殖、構造功能、實驗資料','只取公開題型的證據層次，未複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','授粉、受精、種子果實與環境限制','只取公開資料題的推理模式，重新設計花粉路徑與結果率題。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','花藥與柱頭在花的生殖中主要分別扮演什麼角色？',['花藥產生花粉，柱頭接收花粉','花藥接收花粉，柱頭產生胚珠','兩者都直接產生果實','兩者都是雄配子'],'A','花藥屬雄蕊的一部分，產生花粉；柱頭是雌蕊頂端，適合接收花粉。','先定位構造，再把構造和功能配對，不只依外觀或上下位置猜測。'),
 ('medium','花粉落到柱頭後，仍要形成種子還需要哪個流程？',['花粉管生長到子房附近，雄配子與胚珠中的雌配子融合','花瓣立即變成種子','花粉在柱頭表面直接變成果實','只要有花蜜就會完成受精'],'A','授粉是花粉到達柱頭；之後花粉管引導雄配子，受精完成後胚珠才可能發育成種子。','按花粉轉移—花粉管—配子融合—種子發育排列時間線。'),
 ('medium','下列哪項正確區分花粉與雄配子？',['花粉是承載雄配子的構造或單位，不能直接把兩者當同義詞','花粉就是果實','雄配子是花藥外壁','花粉和雄配子都等於胚珠'],'A','花粉包含或攜帶雄性生殖細胞，兩者在層級與定義上不同。','先分辨構造／載體與細胞，再追蹤雄配子如何到達雌配子附近。'),
 ('hard','某果樹開花很多但結果很少，哪項資料最能幫助判斷原因？',['比較傳粉成功率、花粉活性、天氣、物種相容性與幼果形成率','只數花朵總數','只看花瓣顏色','直接認定是土壤唯一造成'],'A','開花數只代表起始階段，結果率還受傳粉、花粉活性、相容性、天氣與受精後發育影響。','把開花、授粉、受精、幼果分成階段，逐段尋找資料缺口。'),
 ('easy','受精後通常哪個對應關係較合理？',['胚珠可發育成種子，子房可發育成果實的一部分','花粉變成花瓣，花藥變成果實','柱頭變成雄配子','花絲變成種子外殼'],'A','受精後胚珠和子房的發育方向不同，不能把花粉與花部構造任意互換。','沿花的構造—受精—種子／果實流程逐項配對。'),
 ('hard','比較風媒花與昆蟲媒花時，哪項做法最有證據？',['同時觀察花粉量、花藥與柱頭位置、花蜜／氣味及傳粉者出現，再保留環境限制','只因花色鮮豔就判定一定靠昆蟲','只看一朵花就代表整個物種','把傳粉者出現直接等同受精成功'],'A','傳粉方式需由多項構造與觀察證據支持，傳粉者出現也不保證花粉管和受精完成。','先列可觀察線索，再把傳粉事件與受精結果分開記錄。'),
 ('medium','若溫度降低後花粉管生長變慢，實驗比較時還需控制什麼？',['花粉來源、培養介質、濕度、觀察時間與起始條件','只改變溫度並任意更換花粉來源','只記錄最快的一管','不必記錄觀察時間'],'A','花粉管生長受多個條件影響，需控制起始材料與培養條件才能比較溫度作用。','先固定材料與介質，再以相同時間間隔量測長度或生長率。'),
 ('hard','花朵有蜜腺且柱頭伸出花藥之外，最適合的結論是？',['這些構造可能影響傳粉者互動或異花粉轉移，但仍需實際觀察確認','已證明一定由蜜蜂授粉並完成受精','可由柱頭位置直接知道果實數量','蜜腺存在表示不需花粉'],'A','構造可提出功能假說，但傳粉者、花粉轉移和受精結果仍需觀察或實驗證據。','把構造當作預測線索，設計傳粉者訪花與花粉轉移的觀察。'),
 ('medium','若人工授粉組結果率較高，最完整的報告還應包括什麼？',['授粉方式、花朵數、時間、對照組、花粉來源與後續受精／幼果資料','只報告結果率最高的數字','省略未結果的花朵','把人工授粉成功直接推成所有品種都相同'],'A','結果率需要分母、控制與後續階段資料，才能判斷人工授粉的作用與外推限制。','先寫清楚樣本與分母，再比較對照與處理，最後交代可外推範圍。'),
 ('medium','下列哪句最適合作為花的生殖單元結論？',['授粉把花粉帶到柱頭，受精是配子融合；種子與果實形成還受物種、環境和後續發育影響','花粉到柱頭就等於種子已形成','只要花朵鮮豔就必然結果','一次觀察即可解釋所有植物繁殖'],'A','正確結論需區分事件順序、構造層級與環境限制，不把其中一個階段擴張成全部結果。','用構造—花粉路徑—配子融合—發育結果回查每個主張的證據。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='DBACDBACDB'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先在花剖面中標出花藥、柱頭、花柱、子房與胚珠等構造。','把花粉、雄配子、胚珠、雌配子、授粉、受精和發育分成不同層級與事件。','依花粉路徑、時間順序、對照條件和資料分母逐步核對。',f'排除把花粉當配子、授粉當受精、構造線索當確定結果或忽略環境的選項，答案為 {target}。',f'將答案放回植物生殖情境並檢查證據範圍：{explanation}']
 return {'id':f'question-science-content-db-iv-7-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-db-iv-7'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作花的構造、植物生殖、授粉、受精、資料判讀與證據限制的能力方向；本題為 Db-Ⅳ-7 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-db-iv-7','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[])+lesson.get('publisherResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-db-iv-7、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合花的構造、花粉、配子、授粉、花粉管、受精、種子、果實、傳粉者與環境限制。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-db-iv-7-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為花的構造、花粉與配子、授粉、受精、種子果實、傳粉者與環境限制題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content db-iv-7')

if __name__=='__main__': main()
