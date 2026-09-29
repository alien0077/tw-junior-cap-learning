import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('氣泡證據','兩種澄清溶液混合後持續產生氣泡，最合理的初步判斷？',['一定只是液體沸騰','可能生成氣體，需再用性質測試確認','溶液一定變成元素','氣泡不可能與反應有關'],'可能生成氣體，需再用性質測試確認','持續產氣是化學反應線索，但仍要排除溶解氣體逸出或加熱等替代解釋。'),
('沉澱現象','兩種無色溶液混合後出現不溶固體，這項現象通常表示？',['可能生成難溶的新物質','兩溶液一定都變成氣體','所有原子消失','只代表容器變重'],'可能生成難溶的新物質','沉澱表示溶液中形成難溶物，是化學變化的重要線索，但須配合對照與成分證據。'),
('顏色改變','反應後顏色改變，哪個說法最嚴謹？',['是化學反應的可能證據，仍需排除混合或指示劑效果','只要變色就能知道所有生成物','顏色改變代表質量消失','顏色永遠不能作為證據'],'是化學反應的可能證據，仍需排除混合或指示劑效果','顏色改變可提示新物質或酸鹼變化，但單一現象不足以確定完整反應機制。'),
('溫度改變','兩種溶液混合後溫度明顯上升，合理解釋是？',['反應可能放出能量，仍應與單純混合的對照比較','溫度上升表示原子數增加','熱量一定從外界消失','只要升溫就代表生成氣體'],'反應可能放出能量，仍應與單純混合的對照比較','放熱是化學反應線索；控制初溫、容器與攪拌才能排除外界熱源。'),
('氣味安全','觀察未知反應是否產生氣體或氣味時，最安全的作法？',['不可直接嗅聞，依規範以適當方法檢測並保持通風','把鼻子靠近容器確認','用手把氣體扇向臉部','加大量試劑讓氣味更明顯'],'不可直接嗅聞，依規範以適當方法檢測並保持通風','未知物質可能有毒或刺激性，應遵守安全規範，以儀器或指定檢測方法判讀。'),
('酸鹼指示','紫色石蕊試紙變紅，最直接支持哪項？',['溶液呈酸性','必定生成沉澱','必定產生氧氣','溶液一定是純水'],'溶液呈酸性','指示劑顏色提供酸鹼性線索，不足以單獨判定所有反應物與生成物。'),
('質量觀察','密閉系統反應前後質量相同，能否據此判斷沒有化學反應？',['不能，質量守恆與是否反應是不同問題','可以，反應必使質量增加','可以，反應必使質量減半','不能，因為天平一定錯'],'不能，質量守恆與是否反應是不同問題','化學反應可在總質量守恆下發生；需觀察新物質、氣體、沉澱或能量等證據。'),
('可逆現象','加熱後固體溶解、冷卻又結晶，最妥當的判斷？',['可能是物理變化，還要看是否產生新物質','一定是化學反應','只要可逆就沒有粒子','結晶代表元素變少'],'可能是物理變化，還要看是否產生新物質','可逆性可提供線索，但不能單獨作為物理或化學變化的充分判準。'),
('多重證據','要提高「發生化學反應」的可信度，哪種做法最好？',['同時記錄氣體、沉澱、溫度或顏色等證據並設對照','只記錄一次顏色','只問操作者的感覺','省略反應前資料'],'同時記錄氣體、沉澱、溫度或顏色等證據並設對照','多項可重複證據加上對照，能降低替代解釋造成的誤判。'),
('證據界線','看到冒泡時，哪個結論最符合科學表述？',['觀察到產氣現象，是否為新物質仍需進一步檢驗','已證明生成物一定是氧氣','已證明所有氣泡都是化學反應','已證明反應式可以直接寫出'],'觀察到產氣現象，是否為新物質仍需進一步檢驗','觀察與解釋要分開；冒泡可能來自反應，也可能是溶解氣體逸出或沸騰。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」的可觀察現象與實驗條件。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：區分觀察到的現象、可能機制與仍需驗證的結論。','最後回查：確認安全、對照與替代解釋都被納入，不能由單一現象過度推論。']
 return {'id':f'question-science-content-ja-iv-3-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-ja-iv-3'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究化學反應可觀察現象與證據判讀的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-ja-iv-3','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'化學反應現象與證據判讀','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先記錄現象，再檢查對照、替代解釋與證據強度。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-ja-iv-3-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
