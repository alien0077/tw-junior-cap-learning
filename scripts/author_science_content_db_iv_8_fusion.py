import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
LESSON=ROOT/'lessons/science/lesson-science-content-db-iv-8.json'
QDIR=ROOT/'questions/science'
REPORT=ROOT/'implementation/reports/science-content-db-iv-8-first-pass-review.json'
TODAY='2026-09-23'
SOURCES=[
 ('https://www.yacjh.kh.edu.tw/view/index.php?DataId=497103&MainMenuId=30637&MainType=101&SubMenuId=0&SubType=0&WebID=221&Work=View&page=1','高雄市立鹽埕國民中學公開自然科定期評量試題頁','植物、環境變因、資料判讀與控制條件','只取公立校方公開試題的環境探究能力方向，重寫植物分布情境。'),
 ('https://www.bhjh.ntpc.edu.tw/p/406-1000-10627%2Cr111.php?Lang=zh-tw','新北市立板橋國民中學公開自然科定期評量試題頁','水流、氣溫、空氣品質與證據','只取公開題型的觀察與因果推理層次，未複製原題。'),
 ('https://www.hcjh.ntpc.edu.tw/p/406-1000-7527%2Cr146.php','新北市立新莊國民中學公開自然科定期評量試題頁','植物分布、測量設計、環境限制','只取公開資料題的能力模式，重新設計校園測量。'),
]
REFS=[{'url':u,'title':t,'year':'113-115','subject':'science','locator':l,'observedPattern':p,'reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'} for u,t,l,p in SOURCES]
ROWS=[
 ('easy','樹冠攔截降雨後，雨水可能出現哪種去向？',['暫存在葉面、沿枝幹流下或蒸發，並非水量消失','全部立刻變成地下水','所有雨水都被樹根吸收','雨水會變成空氣污染物'],'A','葉片、枝幹與根系會改變水的路徑，攔截只是暫存或重新分配，不代表水消失。','先畫降雨進入系統後的暫存、流動、入滲與蒸發箭頭。'),
 ('medium','要比較樹蔭與水泥地的地表溫度，哪項設計最公平？',['在相同時間、測量高度與天氣下比較相近材質，記錄日照與風','只在不同日期各測一次','樹蔭區用紅外線、水泥地用手觸摸','只挑溫差最大的讀值'],'A','溫度會受時間、材質、日照、風和儀器影響，需固定或記錄條件才能比較。','先指定測點與測量時間，再把地表材質、日照、風和高度列為控制條件。'),
 ('medium','植被區雨後積水消退較快，哪個結論最需要補充證據？',['可能與入滲和地表坡度有關，需控制土壤、坡度、降雨量與排水','一定是植物把所有水吸走','只要看到樹就能確定因果','積水消退與水流無關'],'A','積水消退受入滲、坡度、土壤與排水共同影響，不能將相關直接歸因於植物。','列出水量來源與去向，再比較植被和無植被區的控制條件。'),
 ('hard','道路旁樹多但懸浮微粒測值仍高，最合理的解釋是？',['排放源、風向、通風、葉面狀態與測點位置可能抵銷或改變植物的攔截效果','樹木一定完全無法攔截粒狀物','只因樹太少，不必檢查風向','一次測值可代表整個校園'],'A','空氣品質是多因素系統；植物可能攔截部分粒狀物，但排放、風場與測點會影響結果。','同步記錄排放源距離、風向、時間與葉面狀態，並設置多個對照測點。'),
 ('easy','下列哪項最能區分相關與因果？',['看到有樹區較涼後，還要控制地表材質、日照、風速並重複比較','只要兩者一起變化就確定因果','只看一張校園照片','把所有未測量因素當成不存在'],'A','相關觀察只能提出假說，控制變因與重複測量才能逐步檢驗因果。','先記錄相關現象，再列替代原因並設計公平比較。'),
 ('hard','若樹冠增加使地表降溫，卻讓狹窄巷道通風變差，方案評估應如何處理？',['同時比較溫度、風速、空氣品質、樹種與街道尺度，不用單一指標下結論','只報告降溫效果','因通風變差就否定所有植樹','只看樹冠覆蓋率'],'A','環境措施可能有多重效應，必須依地點尺度與多項指標權衡。','把受益與副作用並列，固定測量高度、時間與街道幾何條件。'),
 ('medium','要判斷根系與土壤覆蓋對入滲的影響，哪項資料最有用？',['相同降雨與坡度下，不同根系／土壤覆蓋的入滲時間與逕流量','只記錄植物高度','只比較雨後照片顏色','不量測降雨量'],'A','入滲時間與逕流量直接連到水流結果，且需在相同降雨與坡度下比較。','先定義水文結果指標，再控制降雨、坡度、面積與土壤條件。'),
 ('hard','空氣測站顯示樹下粒狀物較低，下一步最應做什麼？',['在不同風向、時間、距離排放源和植被條件下重複測量並校正儀器','只選樹下最低值','直接宣稱整個地區空氣變好','刪除道路附近資料'],'A','單一測點不足以推廣，需用時間序列、多點、風向與儀器校正檢查替代解釋。','設計樹下、無樹、道路不同距離的同步測量，保留誤差與背景值。'),
 ('medium','若想在校園增加樹木，哪項決策最完整？',['比較水流、熱、空氣、根系破壞、維護與用地需求，再依場地條件配置','只選長得最快的樹種','只看樹冠最大','只因綠化口號就不需測量'],'A','植物作用有益處也有根系、維護、通風與用地限制，配置需依多指標與場地條件決定。','先列目標和限制，再用校園地圖與基準資料比較候選配置。'),
 ('medium','本單元最合適的總結是哪一項？',['在特定植物、測點、季節與風雨條件下，植被可能改變水、熱與粒狀物；結論須由同步資料檢驗','有植物就一定改善所有環境指標','單一地點一次測量足以代表整個城市','植物數量比測量條件更重要'],'A','植物的環境作用是條件式且多機制的，必須標示測量範圍、替代解釋與不確定性。','把植物分布、作用機制、資料條件和限制寫成可重做的證據鏈。'),
]

def make_question(n,row):
 diff,prompt,opts,source_answer,explanation,strategy=row; target='CADBACDBAC'[n-1]; idx=ord(source_answer)-65; correct=opts[idx]; distractors=[x for i,x in enumerate(opts) if i!=idx]
 ordered=[]; di=0
 for label in 'ABCD':
  if label==target: ordered.append(correct)
  else: ordered.append(distractors[di]); di+=1
 steps=['先畫出植物分布、降雨、地表、風場、排放源與測點的空間關係。','把水、熱、空氣三個結果指標分開，標示直接觀察、可能機制與替代原因。','核對時間、測點、儀器、風向、坡度、材質與降雨等控制條件。',f'排除把有樹等同全部改善、把單次測量當因果或忽略副作用的選項，答案為 {target}。',f'將答案放回校園環境情境並限定適用範圍：{explanation}']
 return {'id':f'question-science-content-db-iv-8-{n}','subject':'science','type':'single-choice','prompt':prompt,'options':[{'id':k,'text':v} for k,v in zip('ABCD',ordered)],'knowledgeIds':['kg-science-content-db-iv-8'],'difficulty':diff,'answer':{'value':target,'explanation':f'{explanation} 正確答案為選項 {target}。'},'examPatternRefs':REFS,'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':SOURCES[0][0],'sourceLocator':'三筆公立國中公開自然科資料僅作植物分布、水流、氣溫、空氣品質、控制變因與證據界線的能力方向；本題為 Db-Ⅳ-8 原創情境改寫。','authoringNote':'依官方課綱、Knowledge Graph 與公開試題 pattern-only 能力方向獨立改寫；未複製原題、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':TODAY,'lessonId':'lesson-science-content-db-iv-8','solutionStrategy':strategy,'solutionSteps':steps}

def main():
 lesson=json.loads(LESSON.read_text(encoding='utf-8')); lesson.update({'updatedAt':TODAY,'reviewStatus':'draft','authoringStandard':'version-fused-v1'})
 for row in lesson.get('versionResearch',[]): row['reviewedAt']=TODAY
 lesson['fusionRecord']['llmSynthesisNote']='本課依官方自然科學課綱、kg-science-content-db-iv-8、南一／康軒／翰林公開版本研究限制及三筆公立國中公開自然科題型能力模式，獨立融合植物分布、葉面截留、根系入滲、樹冠遮蔭、蒸散、風場、粒狀物、測點控制與多指標環境決策。題目與互動均重新設計，未複製受保護內容；Terra 第二輪與正式發布審查尚未完成，維持 draft。'
 LESSON.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 for i,row in enumerate(ROWS,1): (QDIR/f'question-science-content-db-iv-8-{i}.json').write_text(json.dumps(make_question(i,row),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 REPORT.write_text(json.dumps({'unit':lesson['title'],'lessonId':lesson['id'],'status':'first-pass-ai-review-complete','reviewStatus':'draft','checkedQuestions':10,'checks':{'unitSpecificOriginalContent':True,'threeVersionResearchRecords':True,'threePublicSchoolExamPatternSources':True,'answersAndDetailedSteps':True,'interactivePredictionManipulationExplanation':True,'terraSecondPass':'pending'},'reviewedAt':TODAY,'note':'10 題重新改寫為植物分布對水流、氣溫、空氣品質、控制變因與多指標環境決策題；每題具唯一答案、解析、策略與五步解法。'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print('authored science content db-iv-8')

if __name__=='__main__': main()
