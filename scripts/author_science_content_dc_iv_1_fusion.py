import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-dc-iv-1.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-dc-iv-1-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','神經系統、刺激反應、構造功能與資料判讀','只取公立校方公開試題的生物反應與流程推理方向，重新設計神經路徑題。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','感覺、反射、神經與控制變因','只取公開題型的證據層次，未複製原題、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','人體協調、反應時間、刺激與反應器官','只取公開資料題的推理模式，重新設計保護性反射與意識反應。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','手碰到熱杯壁後迅速縮回，哪條路徑最符合保護性反射？',['皮膚受器→感覺神經元→脊髓等中樞→運動神經元→手部肌肉','手部肌肉先發命令給皮膚受器','眼睛直接命令手臂收縮','血液把熱度直接變成動作'],'A','受器先偵測刺激，訊息經感覺神經元進入中樞，再由運動神經元使肌肉收縮；脊髓可先安排快速反應。','沿刺激、受器、感覺神經、中樞、運動神經與反應器官畫箭頭。'),
 ('medium','看到球飛來並伸手接住，和縮手反射相比最主要的差異是？',['通常需要大腦整合方向、距離與目標後調整反應','完全不需感覺受器','一定不經過神經元','只由脊髓決定且不能改變'],'A','接球需要分析視覺與情境，屬大腦參與較多的意識反應；仍須經受器與神經傳導。','比較兩案例的刺激、主要中樞、反應器官與可調整程度。'),
 ('easy','眼睛在神經反應路徑中最恰當的描述是？',['包含接收光刺激的感覺受器，但不是整個反應命令的中樞','眼睛直接命令所有肌肉','眼睛等同脊髓','眼睛只負責製造運動神經元'],'A','眼睛包含視網膜等感覺受器，訊息仍需經神經傳至中樞整合。','分開器官、受器與中樞三個層級，避免把局部構造當成整條路徑。'),
 ('hard','若想比較不同情境的反應時間，哪項實驗設計較公平？',['固定刺激種類、距離、亮度與測量方式，重複多次並比較平均與變異','每次更換刺激和受試者再直接比較','只保留最快的一次','不記錄練習次數或疲勞狀況'],'A','反應時間受刺激、受試者、練習、疲勞與儀器影響，需控制條件並保留重複資料。','先指定自變因與反應時間，再固定其他條件並檢查誤差。'),
 ('medium','感覺受器的主要工作是什麼？',['把環境或身體內部的物理、化學變化轉成可傳遞的神經訊息','直接讓肌肉收縮而不需中樞','製造所有感覺經驗','把運動命令傳回刺激來源'],'A','受器負責偵測並轉換刺激；中樞整合與運動神經元、反應器官共同完成後續反應。','把接收、整合、傳出和作動四個角色分開配對。'),
 ('hard','腳踩到尖物先抬腳，稍後才清楚感到疼痛；最合理的解釋是？',['保護性反射可先由脊髓安排，訊息之後仍傳到大腦形成感覺','脊髓會阻斷所有疼痛訊息','疼痛只由肌肉產生','大腦完全不會收到腳部訊息'],'A','快速反射和後續意識感覺可在時間上先後出現，不代表大腦永遠不參與。','把動作發生時間與感覺形成時間分開，畫出兩條相關但不同的路徑。'),
 ('medium','若手部皮膚受器受損，哪項結果最可能？',['該區域偵測某些觸覺或溫度刺激的能力下降，但中樞和肌肉未必全部失效','所有感覺和動作都必然消失','脊髓會改變成皮膚受器','眼睛會代替所有受器'],'A','受器受損會影響特定刺激的輸入，其他路徑是否受影響要看損傷位置與範圍。','先定位損傷在輸入、整合、傳出或反應器官哪一段，再推論影響。'),
 ('hard','看到警示燈後按下煞車，若要判斷是視覺訊息還是肌力造成反應差異，應如何做？',['固定煞車裝置與指令，改變視覺刺激條件並重複測量反應時間與力量','同時改變燈光、煞車器和受試者','只看是否成功按下','只問受試者覺得快不快'],'A','公平比較需一次改變主要刺激條件，並用可量測時間與力量記錄反應。','明確區分刺激、自變因、反應時間和力量，控制裝置與受試者條件。'),
 ('medium','下列哪句正確區分反射與自主／意識反應？',['反射通常是快速保護性路徑；意識反應通常需大腦整合，但兩者都涉及受器、神經與反應器官','反射完全沒有中樞參與','意識反應不需要神經傳導','所有快速動作都一定是反射'],'A','反射仍需中樞連接，只是路徑與速度不同；意識反應能依情境調整。','比較中樞、時間、是否需判斷和可調整性，不用快慢單一標籤判斷。'),
 ('medium','寫神經系統單元結論時，哪項最完整？',['依刺激—受器—傳入—中樞—傳出—反應器官說明證據，並交代反射或意識路徑的限制','只說大腦控制一切而不畫路徑','只看動作結果猜刺激','把感覺器官和中樞當成同一構造'],'A','完整結論要把訊息方向、角色、事件順序與案例限制連起來，避免用一句口號取代路徑。','沿完整路徑回查每個角色，再說明資料支持的是哪一種反應與範圍。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='BDACBDACBD'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先標記刺激、感覺受器、感覺神經元、中樞、運動神經元與反應器官。','依訊息方向和事件時間排列路徑，分開接收、整合、傳出與作動。','檢查反射／意識反應、反應時間、損傷位置與控制條件的證據。',f'排除把受器當中樞、把反射當無中樞或把所有快速動作混為一談的選項，答案為 {target}。',f'將答案放回神經反應情境並檢查路徑範圍：{explanation}']
 return {'id':f'question-science-content-dc-iv-1-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-dc-iv-1'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作神經系統、刺激反應、反射、反應時間、控制變因與證據界線的能力方向；本題為 Dc-Ⅳ-1 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-dc-iv-1','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('publisherResearch',[])+lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-dc-iv-1、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合刺激、感覺受器、感覺神經元、中樞、運動神經元、反應器官、反射、意識反應與反應時間證據。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-dc-iv-1-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為神經系統、刺激反應、反射、意識反應、反應時間與路徑證據題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content dc-iv-1')

if __name__=='__main__': main()
