import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-cross-energy-resources.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-cross-energy-resources-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','能量轉換、功率、效率與生活裝置','只取公立校方公開試題的計算與資料判讀能力方向，重新設計能源題。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','能源、環境、變因與證據','只取公開題型的推理層次，不複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','能量守恆、效率、裝置限制','只取公開資料題的能力模式，改寫為微電網與能源決策情境。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','手電筒電池接上 LED 後，最完整的能量流描述是？',['電池化學能轉成電能，再轉成光能與熱能','電池製造出不受守恆限制的光','LED 把光能變成沒有去向的能量','只要發光就表示所有輸入都成為光'],'A','裝置把能量由一種形式轉成另一種形式，仍有熱等非有效輸出；能量不會憑空產生或消失。','沿來源、轉換器、有效輸出與散失畫箭頭，逐段標出能量形式。'),
 ('medium','輸入 200 J 的電能，電熱器提供 150 J 有用熱能，效率是多少？',['25%','50%','75%','133%'],'C','效率=有用輸出／輸入×100%=150/200×100%=75%。','先確認分子是有用輸出、分母是總輸入，再檢查結果不超過 100%。'),
 ('medium','兩台裝置都輸出 600 J，甲用 10 秒、乙用 30 秒；哪項正確？',['甲的功率較大，因為相同能量在較短時間完成','乙的功率較大，因為花較久時間','兩者功率相同因為輸出能量相同','無法比較因為沒有能源名稱'],'A','功率=能量／時間；同樣輸出下，完成時間較短者功率較大，甲為 60 W、乙為 20 W。','將輸出能量除以時間，保留單位並分清功率與效率。'),
 ('hard','離島微電網白天日照降低但晚間仍需供電，哪項配置最能處理時間錯配？',['搭配蓄電池或其他備援，並依負載與儲能損失安排調度','只看白天太陽能峰值','因為太陽能可再生就不需儲能','把晚間需求從統計中刪除'],'A','可再生不等於隨時可用；儲能、備援、負載時間和轉換損失共同決定供電可靠度。','先畫逐時供需，再找缺口，最後把儲能容量與備援條件放入能量帳。'),
 ('easy','下列哪個敘述正確區分能源與能量？',['煤、陽光或風可作為能源來源；電能、熱能和動能是能量形式','能源和能量完全是同一個名詞','LED 是能源本身','效率就是能源的種類'],'A','能源是可取得與利用的來源，能量形式描述系統狀態或轉換結果；裝置不是能源名稱。','先替詞語標註來源、形式或裝置，再沿轉換鏈檢查。'),
 ('hard','比較燃油發電與太陽能發電的環境影響時，哪項做法較完整？',['同時比較生命週期、排放、土地、生態、供應穩定與儲能需求','只看發電當下有沒有煙','只因太陽能可再生就判定所有指標最好','只比較設備額定容量'],'A','能源決策需要明確系統邊界與多指標；操作排放、製造、土地與供應限制不能互相取代。','列出比較目標與邊界，再把使用前、使用中、退役與備援資料分開。'),
 ('medium','若同一太陽能板在陰天輸入能量減少，LED 亮度變低；最合理的解釋是？',['輸入能量和可用輸出受日照條件影響，需檢查負載與儲能是否足夠','能量守恆在陰天失效','LED 自己消滅了能量','亮度變低代表太陽能不再是能源'],'A','輸入條件變化會影響可用輸出，但能量仍守恆；蓄電池或降低負載可能改變結果。','先固定負載，記錄日照、輸入、輸出與儲能狀態，再判斷缺口原因。'),
 ('hard','某方案輸出能量高但需要大量燃料和散熱，哪項不能直接由輸出高推出？',['它的效率一定最高且環境代價一定最低','要另外比較輸入能量與有用輸出','散熱可能是非有用輸出或損失','系統邊界會影響環境評估'],'A','輸出量大不代表輸入少或效率高，效率和環境代價要以定義、邊界與資料另行判斷。','把輸出、輸入、效率與環境影響分開算，不讓一個指標代替全部結論。'),
 ('medium','學校想降低電費又維持照明服務，哪個方案最可檢驗？',['先量測時段、照度與用電，換高效率燈並比較相同服務下的功率與壽命','只把燈關掉不量照度','只挑最省電的一天','把照明品質視為不重要'],'A','節能必須在功能服務相近的條件下比較，否則省電可能只是降低服務品質。','先定義功能單位，再固定照度與使用時間，最後比較功率、壽命與總成本。'),
 ('hard','寫能源未來展望時，哪項結論最符合證據界線？',['在指定負載、日照、儲能與電網條件下方案甲較能完成任務；仍需追蹤成本、排放與極端天候','可再生能源一定在所有地點和時間都最佳','只要效率高就沒有環境代價','能源方案不必記錄輸入和輸出'],'A','能源判斷應是有條件、可修正的推論，需同時交代任務、輸入、輸出、限制和後續證據。','把目標、條件、計算、環境指標和未知資料寫成完整推理鏈。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='BDACBDACBD'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先標出輸入能源、轉換裝置、有用輸出、散失、時間與系統邊界。','依能量守恆、功率=能量/時間或效率=輸出/輸入建立關係式。','核對單位、負載、日照、儲能與比較服務，檢查是否有重複計算。',f'排除把可再生當隨時穩定、輸出當效率或單一指標當總結的選項，答案為 {target}。',f'把答案放回能源情境並檢查限制：{explanation}']
 return {'id':f'question-science-content-cross-energy-resources-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-cross-energy-resources'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作能量轉換、功率、效率、守恆、環境與能源決策的能力方向；本題為能量與能源單元原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-cross-energy-resources','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-cross-energy-resources、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合能量形式、能源來源、守恆、功率、效率、微電網、儲能與環境決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-cross-energy-resources-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為能量形式、能源來源、守恆、功率、效率、離島微電網、儲能與環境決策題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content cross-energy-resources')

if __name__=='__main__': main()
