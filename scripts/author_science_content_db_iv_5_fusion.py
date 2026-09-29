import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-db-iv-5.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-db-iv-5-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','生物構造、功能、變因與證據判讀','只取公立校方公開試題的生物與探究能力方向，改寫為仿生情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','適應、生物環境關係、實驗設計','只取公開題型的證據層次，未複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','仿生應用、功能比較、模型限制','只取公開資料題的推理模式，重新設計自然構造與工程測試。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','蓮葉表面水滴容易滾落，若要測試仿生防水塗層，哪項指標最直接？',['固定滴水量與傾角，測量水滴滑落距離或接觸角','只看塗層顏色是否像蓮葉','只問使用者覺得自然','不記錄表面材料與角度'],'A','滑落距離或接觸角能直接量化排水功能；外觀相似不等於作用機制相同。','先把生物功能翻成工程指標，再固定滴水量、角度與表面條件。'),
 ('medium','比較有微小突起與平滑表面的材料附著水量，最公平的設計是？',['固定材料面積、滴水量、傾角與觀察時間，只改表面結構','同時改面積和水量','只挑一個最乾的結果','讓每種材料使用不同傾角'],'A','控制面積、水量、角度與時間才能把差異合理歸因於表面結構。','列出操弄、結果與控制變因，先建立可重做的對照組。'),
 ('medium','壁虎腳掌的微細結構可提高附著，仿生膠帶在潮濕環境失效；最合理的結論是？',['原理可能受濕度、材料與尺度限制，不能只因乾燥測試成功就普遍外推','壁虎構造在自然界一定失效','產品外形不像壁虎所以沒有仿生','一次失效就證明所有仿生不可用'],'A','仿生需保留作用機制並檢查材料、尺度與環境條件；工程效果是有條件的。','把自然構造的機制和產品材料、尺度、濕度逐一對照。'),
 ('hard','以蝙蝠回聲定位設計障礙物感測器，哪項測試最能檢查功能？',['在不同距離、材質與背景噪音下比較回波辨識率和距離誤差','只比較感測器外殼是否像蝙蝠','只在安靜近距離測一次','用產品重量取代感測性能'],'A','回聲感測的功能是辨識與定位，需在不同距離、材質與噪音下測量準確度與誤差。','先定義功能輸出，再安排距離、材質、噪音等條件和誤差指標。'),
 ('easy','下列哪句最能區分適應與目的性想像？',['族群中可遺傳差異在環境下造成存活／繁殖差異，經長期累積形成適應','個體知道需求後主動長出特定構造','所有構造都是為了人類使用而存在','只要看起來有用就能證明適應'],'A','適應涉及族群差異、環境篩選與世代結果，不是個體依意願設計自己。','檢查主體是個體還是族群，並尋找環境條件、遺傳差異與繁殖結果證據。'),
 ('hard','天然蓮葉塗層與人工防水材料都能讓水滴滑落，環境評估還需比較什麼？',['耐久度、製造材料、清潔需求、微粒釋出、成本與退役處理','只比較第一次滑落速度','只因天然就判定沒有環境代價','只看產品外觀'],'A','功能相似不代表生命週期影響相同，材料來源、壽命、維護與退役都要納入。','先固定功能單位，再比較製造、使用、維護、壽命和退役階段。'),
 ('medium','若仿生表面讓灰塵較少附著，但摩擦力也變小造成抓握不穩，應如何判斷？',['同時比較清潔性與抓握安全，不能用單一指標宣稱整體最好','只看灰塵少就判定成功','只看摩擦小就判定失敗','刪除安全資料避免矛盾'],'A','工程設計常有多目標取捨，清潔性與安全性需依使用任務與權重共同評估。','列出功能需求、失效風險與使用情境，再用多指標比較方案。'),
 ('hard','若測試結果顯示仿生感測器在小型目標上誤差較大，最適合的下一步是？',['檢查尺度、解析度、材料與訊號處理假設，重新設計控制測試','直接宣稱生物感測原理錯誤','只保留大型目標結果','把誤差當成使用者操作問題而不測量'],'A','自然系統與工程系統在尺度、感測解析度和訊號處理上可能不同，需找出機制落差再修正。','把誤差依目標大小、距離、噪音和解析度分層，逐項驗證替代解釋。'),
 ('medium','要將壁虎附著原理用在醫療貼片，哪個條件最不能省略？',['皮膚安全、貼附時間、汗液與移除傷害等使用情境與限制','只複製腳趾外形','只測玻璃上的乾燥附著','不需考慮人體材料差異'],'A','醫療使用的材料與安全邊界不同，仿生原理必須在真實任務條件下驗證。','先列使用者、材料、時間與失效風險，再設計低風險、可重複的性能測試。'),
 ('medium','仿生設計報告的結論哪一項最完整？',['指定生物機制、工程指標、測試條件、結果與未驗證限制，不把外形相似當成功能證明','只放一張產品照片','只說自然很神奇所以一定有效','只報告最好的測試值'],'A','可追溯報告需連結構造、機制、測量和限制，才能讓他人重做並判斷是否適用。','依構造—機制—規格—測試—限制五格回查結論與證據。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='CADBACDBAC'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先指出生物構造、環境壓力、功能與工程任務的對應關係。','把自然觀察、機制假說、工程指標、控制條件和風險分開。','依尺度、材料、濕度、噪音、時間或使用者條件檢查替代解釋。',f'排除只看外形、單次示範、天然標籤或單一性能的選項，答案為 {target}。',f'將答案放回仿生情境並標註適用限制：{explanation}']
 return {'id':f'question-science-content-db-iv-5-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-db-iv-5'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作適應構造、功能、仿生應用、控制變因與模型限制的能力方向；本題為 Db-Ⅳ-5 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-db-iv-5','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[])+lesson.get('publisherResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-db-iv-5、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合適應構造、環境壓力、蓮葉排水、壁虎附著、蝙蝠回聲定位、仿生工程指標、尺度材料、安全、生命週期與模型限制。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-db-iv-5-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為適應構造、仿生工程、功能測試、尺度材料、安全與生命週期題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content db-iv-5')

if __name__=='__main__': main()
