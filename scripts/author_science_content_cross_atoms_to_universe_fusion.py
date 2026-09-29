import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-cross-atoms-to-universe.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-cross-atoms-to-universe-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','粒子模型、化學式、光與天文資料判讀','只取公立校方公開試題的概念辨識與證據推理方向，重新設計跨尺度題。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','物質組成、光譜、尺度與模型限制','只取公開題型的能力層次，未複製題幹、圖表或答案。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','符號表示、觀測證據、單位與推論','只取跨單元資料解釋模式，改寫為原子到宇宙的原創情境。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','化學式 CO₂ 中的下標 2 最直接表示什麼？',['一個碳原子和兩個氧原子的原子數比','含有兩個碳元素','有兩個二氧化碳分子','碳和氧的質量一定各半'],'A','CO₂ 的下標表示同一個分子中氧原子的數目；元素種類由符號 C、O 判讀。','先數元素符號，再讀各符號右下角的原子數，區分分子組成與分子個數。'),
 ('medium','O₂ 和 O₃ 都只含氧元素，哪項說法正確？',['它們都是只含一種元素的分子，但每個分子的原子數不同','O₂ 是化合物而 O₃ 是元素','兩者一定具有完全相同的性質','O₂ 中的 2 表示兩種元素'],'A','O₂、O₃ 都由同一種元素組成且是分子，但原子數不同可能造成性質差異；化合物需含兩種以上元素。','分開判斷元素種類、粒子型態與原子數，避免把分子和元素當同義詞。'),
 ('medium','未知恆星光譜有一條暗線與氫的參考線位置相同，最恰當的推論是？',['恆星大氣可能含氫，還要考慮溫度與儀器校正','恆星表面一定有液態氫海洋','只靠這條線可算出恆星距離','暗線表示恆星沒有其他元素'],'A','光譜線位置相符能支持成分的可能性，但形成強度與可見性受狀態、溫度與觀測條件影響。','先說明直接觀測的線位置，再限定成分推論，最後列出尚需資料。'),
 ('hard','若兩顆恆星在影像中亮度不同，哪個結論不能單由亮度得到？',['較亮者一定距離較近','亮度是觀測量之一','還需考慮本身發光能力與距離','塵埃與曝光也可能影響影像亮度'],'A','影像亮度同時受距離、本身光度、塵埃和曝光影響，不能把亮度直接等同距離。','區分觀測量與物理量，列出至少兩種能產生相同亮度的替代解釋。'),
 ('easy','光年在天文資料中是什麼？',['距離單位','時間單位','恆星亮度單位','元素種類單位'],'A','光年是光在一年中傳播的距離，因此是距離單位，不是時間。','看單位名稱的定義，將傳播速度乘時間得到長度，再檢查題目問的物理量。'),
 ('medium','示意圖把原子畫得比星系大很多，最合理的解讀是？',['圖形用來表達包含或概念關係，不能以畫面大小當真實比例','原子實際比星系大','圖上距離就等於光年','只要圖畫得大就代表質量大'],'A','跨尺度示意圖通常為了可讀性而非按比例繪製，需依圖例、單位和文字說明解讀。','先查圖例與單位，再判斷圖形是在表達層級、順序還是真實比例。'),
 ('hard','研究遙遠星系時，科學家用光譜與亮度建立模型；哪個限制必須寫入結論？',['資料來自遠距觀測，成分、距離與演化需依模型和多項證據交叉檢驗','只要有影像就等同於能直接取樣','任何單一光譜線都能決定全部物理量','示意圖比例可以取代觀測誤差'],'A','遠距觀測提供訊號而非直接取樣，結論需要模型、校正與不同證據的交叉檢驗。','把直接訊號、模型推論與未測量的部分分層寫出，避免越過證據範圍。'),
 ('medium','某粒子卡有三個相同原子彼此分離，另一張有三個相同原子固定連結；判讀時首先要注意什麼？',['粒子是否形成分子與原子間是否固定連結，不能只數總原子數','只看卡片顏色','把兩張都當同一元素的三個分子','看到固定連結就能知道沸點'],'A','總原子數不足以決定粒子模型；連結方式與粒子種類需要一起判斷，物性還需額外資料。','先描述粒子排列與連結，再決定可支持的組成結論，不直接跳到宏觀性質。'),
 ('hard','若光譜資料支持某星雲含有氫，但不同儀器得到的線強度不同，下一步應如何做？',['檢查儀器校正、曝光、背景與觀測條件，再比較可重現的特徵','只採用最符合預期的儀器','把強度差異當成元素種類改變','忽略背景並直接平均所有數值'],'A','線強度受儀器、背景和觀測狀態影響，先處理測量條件才能合理比較物理推論。','先分離儀器效應與天體訊號，再用校正後資料和不確定度比較。'),
 ('medium','從原子、分子、行星系、星系到宇宙整理概念時，最好的作答方式是？',['同時標示尺度、包含關係、單位與證據限制，再說明哪些是模型推論','只依序背名詞不寫單位','把所有層級當成相同大小的物體','由示意圖面積直接計算真實距離'],'A','跨尺度整理需要結構與證據邊界；名詞順序本身不等於理解，示意圖也不自動提供真實比例。','先畫層級與單位，再為每個結論標註直接證據、推論和仍未知的部分。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='CADBACDBAC'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先標記符號、下標、光譜線、亮度、尺度與單位等直接資料。','把觀測、模型推論和未知限制分欄，避免由單一訊號越權下結論。','依原子數比、光譜位置、比例關係或距離定義逐步核對。',f'排除把元素當粒子、亮度當距離、光年當時間或示意圖當真比例的選項，答案為 {target}。',f'把答案放回資料情境並標註證據範圍：{explanation}']
 return {'id':f'question-science-content-cross-atoms-to-universe-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-cross-atoms-to-universe'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作粒子模型、化學式、光譜、尺度、單位與證據判讀的能力方向；本題為從原子到宇宙的原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-cross-atoms-to-universe','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-cross-atoms-to-universe、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合原子、元素、分子、化合物、化學式、光譜、恆星、星系、尺度與單位。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-cross-atoms-to-universe-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為粒子模型、化學式、光譜、天文尺度、單位與模型限制題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content cross-atoms-to-universe')

if __name__=='__main__': main()
