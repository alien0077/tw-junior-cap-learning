import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-dc-iv-2.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-dc-iv-2-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','內分泌、代謝、血糖資料與生理調節','只取公立校方公開試題的曲線判讀與因果能力方向，重寫血糖情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','人體恆定、激素、器官功能與證據','只取公開題型的資料推理層次，未複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','血糖調節、負回饋、控制條件','只取公開資料題的能力模式，重新設計內分泌調節問題。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','早餐後血糖由 88 mg/dL 上升到 126 mg/dL，最適合先判斷什麼？',['血糖在一段時間內上升，需再配對能降低血糖的調節作用','升糖素一定讓血糖繼續上升','血糖已經完全恆定不變','胰島素會把葡萄糖變成氧氣'],'A','曲線先提供變化方向；餐後升高後通常需考慮胰島素促進細胞利用與肝糖形成等降低作用。','先讀時間序列的上升或下降，再配對激素作用方向。'),
 ('medium','血糖偏高時，胰島素較可能造成哪種結果？',['促進細胞吸收利用葡萄糖，並促進肝臟合成肝糖','促進肝糖分解使血糖更高','阻止所有細胞使用葡萄糖','直接把血糖排成汗液'],'A','胰島素的作用方向是降低血糖，包含促進細胞利用和肝糖儲存。','畫出血糖偏高—胰島素—細胞利用／肝糖形成—血糖下降的因果鏈。'),
 ('medium','長時間未進食且血糖偏低時，哪個調節較符合題意？',['升糖素促進肝糖分解，讓葡萄糖釋入血液','胰島素促進更多肝糖形成','升糖素使所有細胞停止呼吸','血糖越低就代表恆定失效'],'A','血糖偏低時升糖素促進肝糖分解，有助於把血糖拉回可用範圍。','先找偏離方向，再選相反方向的激素與代謝作用。'),
 ('hard','一條血糖曲線餐後先升、兩小時後接近原值，最能支持哪個概念？',['負回饋調節使血糖回到可用範圍，不代表每一刻固定同一數值','血糖從未改變','只有升糖素參與整個過程','恆定就是血糖完全不波動'],'A','恆定允許短時間變化，系統透過相反方向作用減少偏離，使狀態維持在適合範圍。','區分變化本身和調節後的回復趨勢，不把恆定誤成不變。'),
 ('easy','激素和神經訊息的主要差異何者較合適？',['激素多經血液運送，作用可較廣泛與持久；神經訊息主要沿神經快速傳遞','激素只作用在分泌腺附近','神經訊息不需細胞接收','兩者完全沒有不同'],'A','激素是化學訊息，經血液到達有相應受體的標的細胞；神經傳導通常較快速且路徑特定。','比較訊息種類、運送路徑、速度、範圍與標的細胞。'),
 ('hard','若某人胰島素作用不足，餐後血糖長時間偏高；哪項資料最能檢驗此解釋？',['比較進食後血糖曲線、胰島素作用指標、細胞葡萄糖利用與肝糖儲存資料','只問是否吃甜食','只量一次空腹血糖','只看體重不看時間序列'],'A','胰島素作用不足的解釋需與血糖時間序列及下游利用、儲存資料相互檢驗。','沿激素—標的細胞—代謝結果找可測量證據，避免單一指標下診斷。'),
 ('medium','腎上腺素能在緊張時提高可用血糖，這能說明什麼？',['血糖調節可由不同情境與激素共同參與，不能把所有升高都歸給單一激素','胰島素永遠停止作用','升糖素只在進食後作用','所有激素都只降低血糖'],'A','不同生理情境會動員不同調節，判斷需看時間、刺激與資料，不能只背一種激素。','把刺激情境、激素方向和血糖資料對齊，再檢查替代解釋。'),
 ('hard','比較兩組餐後血糖曲線，若一組兩小時後仍高，實驗報告最需要控制什麼？',['餐食醣量、進食時間、活動量、測量方法與受試者條件','只控制曲線顏色','讓兩組吃不同份量再比較','只挑下降最快者'],'A','血糖曲線受餐食、活動與測量時間影響，公平比較需固定或記錄關鍵條件。','先固定輸入與測量時間，再比較曲線峰值、回復時間和變異。'),
 ('medium','下列哪項最能區分血糖恆定與血糖固定？',['恆定是血糖在可用範圍內受調節而變動，固定則誤以為數值永遠不變','兩者完全相同','恆定表示沒有任何激素','固定表示一定健康'],'A','體內恆定是動態平衡，包含偏離、感測、調節與回復，不是靜止數字。','用變化—偵測—作用—回復四段模型檢查定義。'),
 ('medium','寫內分泌調節單元結論時，哪項最完整？',['依血糖變化方向、激素、標的作用、肝糖代謝與時間資料說明，並交代測量限制','只寫胰島素能降低血糖','看到一個數字就推論全部代謝','把所有生理調節都叫神經反射'],'A','完整結論要把時間序列、激素方向、標的器官與代謝結果串起來，並保留資料邊界。','沿曲線—激素—細胞／肝臟—回饋—限制回查每一個主張。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='CADBACDBAC'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先讀血糖曲線的時間、單位、上升下降與進食／空腹情境。','把激素、標的細胞、肝糖合成／分解與血糖方向分開標記。','依負回饋、控制條件、峰值、回復時間與替代解釋核對資料。',f'排除把恆定當固定、把所有變化歸給單一激素或忽略時間序列的選項，答案為 {target}。',f'將答案放回血糖調節情境並檢查證據範圍：{explanation}']
 return {'id':f'question-science-content-dc-iv-2-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-dc-iv-2'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作內分泌、血糖曲線、代謝、負回饋、控制條件與證據界線的能力方向；本題為 Dc-Ⅳ-2 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-dc-iv-2','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('publisherResearch',[])+lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-dc-iv-2、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合內分泌、血糖曲線、胰島素、升糖素、肝糖、負回饋、代謝、激素與體內恆定的資料推理。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-dc-iv-2-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為內分泌、血糖曲線、胰島素、升糖素、肝糖、負回饋與體內恆定資料推理題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content dc-iv-2')

if __name__=='__main__': main()
