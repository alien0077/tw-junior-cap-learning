import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('反應箭頭','化學方程式中的箭頭通常表示什麼？',['反應物轉變成生成物的方向','反應物質量一定增加','電子一定流向左側','實驗必須加熱'],'反應物轉變成生成物的方向','箭頭分隔反應前的反應物與反應後的生成物，表示反應轉變關係。'),
('係數意義','方程式 2H₂＋O₂→2H₂O 中的 2 最主要表示什麼？',['兩個水分子或兩莫耳的比例','每個水分子含兩個氧原子','氫元素原子序是 2','反應時間為 2 秒'],'兩個水分子或兩莫耳的比例','係數改變粒子或莫耳的數量比例；H₂O 的原子組成由下標決定。'),
('下標意義','化學式 CO₂ 中的下標 2 表示什麼？',['一個二氧化碳分子含兩個氧原子','反應需要兩個分子','碳原子有兩個質子','反應速率為 2'],'一個二氧化碳分子含兩個氧原子','下標表示單一粒子內的原子數，不能與方程式前的係數混淆。'),
('配平判準','判斷方程式是否配平，最直接的做法是？',['逐元素比較反應前後原子數','只比較左右物質種類數','只看箭頭兩側字數','只確認有沒有係數'],'逐元素比較反應前後原子數','每種元素左右原子數相等，才符合原子守恆與配平要求。'),
('狀態符號','方程式中的 (s)、(l)、(g)、(aq) 通常提供什麼資訊？',['物質在反應中的物態或水溶液狀態','原子的質子數','反應物的質量','分子的電子數'],'物質在反應中的物態或水溶液狀態','狀態符號補充物質所處狀態；不能拿來當成原子數或質量。'),
('條件符號','方程式箭頭上方寫「加熱」，最合理的解讀？',['表示反應需要加熱條件','表示生成物一定是氣體','表示係數要加 1','表示反應物被消耗一半'],'表示反應需要加熱條件','箭頭上的文字或符號可表示反應條件，不直接改變化學式下標。'),
('文字轉式子','「氫氣與氧氣反應生成水」轉成方程式時，第一步應先做什麼？',['寫出正確反應物和生成物化學式','先任意填入最大係數','先刪除所有下標','先決定容器顏色'],'寫出正確反應物和生成物化學式','先辨認物質與化學式，再配平係數，能避免把下標錯當成可調整數字。'),
('資訊界線','方程式 2Na＋Cl₂→2NaCl 能直接看出哪項？',['反應物、生成物與粒子數量比例','每個反應的實際反應時間','所有物質的沸點','實驗室的溫度'],'反應物、生成物與粒子數量比例','方程式表達反應關係與比例，實際速率、沸點與操作條件需另有資料。'),
('最簡係數','配平後係數為 2、4、2，還能如何整理？',['全部除以 2，寫成 1、2、1','全部乘以 2','只刪除中間係數','改變化學式下標'],'全部除以 2，寫成 1、2、1','方程式係數應化為最簡整數比，但不可因此改變各物質的化學式。'),
('模型與方程式','粒子模型與化學方程式互相核對時，哪項最重要？',['模型中各元素粒子數須符合方程式係數與下標','只要球的顏色漂亮','模型球大小必須是真實比例','只要畫出箭頭就算配平'],'模型中各元素粒子數須符合方程式係數與下標','模型與符號表示都要通過逐元素計數，才能支持反應表示正確。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」涉及的箭頭、係數、下標、狀態或條件。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：分清係數、下標、狀態符號與反應條件的功能。','最後回查：逐元素或逐符號核對，確認沒有改動物質本身的化學式。']
 return {'id':f'question-science-content-ja-iv-4-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-ja-iv-4'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究化學反應式、係數、狀態與條件符號的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-ja-iv-4','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'化學反應式、係數、狀態與條件符號','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先分辨化學方程式各符號的功能，再逐元素核對表示是否正確。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-ja-iv-4-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
