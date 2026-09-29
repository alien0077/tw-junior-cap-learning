import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('重量百分濃度','把 10 g 食鹽配成總質量 100 g 的溶液，重量百分濃度是多少？',['1%','10%','90%','1000%'],'10%','重量百分濃度＝溶質質量÷溶液質量×100%；10÷100×100%=10%。'),
('溶液總質量','25 g 溶質加入 475 g 水完全溶解，重量百分濃度約為多少？',['5.0%','5.3%','19.0%','95.0%'],'5.0%','溶液質量為 25+475=500 g；25÷500×100%=5.0%。'),
('反推溶質','200 g 的 4% 糖水含有多少克糖？',['4 g','8 g','50 g','196 g'],'8 g','溶質質量＝溶液質量×濃度＝200×0.04=8 g。'),
('反推溶液','若 3 g 溶質配成 2% 重量百分濃度的溶液，溶液總質量應為多少？',['6 g','150 g','300 g','1.5 g'],'150 g','溶液質量＝溶質質量÷濃度＝3÷0.02=150 g。'),
('稀釋','50 g 的 20% 溶液加水稀釋至 200 g，稀釋後濃度為何？',['5%','10%','20%','80%'],'5%','原有溶質為 50×20%=10 g；10÷200×100%=5%，稀釋不改變溶質質量。'),
('ppm換算','水樣中每 1 L 含有 2 mg 某物質，在稀水溶液中約為多少 ppm？',['0.2 ppm','2 ppm','20 ppm','2000 ppm'],'2 ppm','稀水溶液中 1 mg/L 約等於 1 ppm，因此 2 mg/L 約為 2 ppm。'),
('ppm計算','3 L 水樣含 15 mg 污染物，近似水的密度時濃度為多少 ppm？',['3 ppm','5 ppm','15 ppm','45 ppm'],'5 ppm','15 mg÷3 L=5 mg/L；稀水溶液中換算為約 5 ppm。'),
('濃度與取樣','取 250 g 的 12% 溶液，含有多少克溶質？',['3 g','12 g','30 g','238 g'],'30 g','250×0.12=30 g；同一均勻溶液取樣時以質量百分比計算溶質量。'),
('單位判讀','下列哪項濃度表示最適合描述極低量水中污染物？',['重量百分濃度 50%','ppm 8','溶液總質量 8 g','溶質顏色 8 種'],'ppm 8','ppm 表示每一百萬份中的比例，適合表達極低濃度；百分比不一定最清楚。'),
('百分比與ppm','在稀水溶液近似下，1% 與多少 ppm 的比例相同？',['100 ppm','1000 ppm','10000 ppm','1000000 ppm'],'10000 ppm','1%=1/100；換成每百萬份為 10,000 ppm。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」的溶質、溶液總質量、體積與濃度單位。',f'建立公式：{reason}',f'核對答案：選項 {aid}「{ans}」符合計算與單位。','排除誘答：確認分母是溶液總量而非水量，並把百分比、mg/L 與 ppm 單位換清楚。','最後回查：將結果代回濃度公式，檢查數值範圍與單位是否合理。']
 return {'id':f'question-science-content-jb-iv-4-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-jb-iv-4'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究重量百分濃度、稀釋與 ppm 計算的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-jb-iv-4','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'重量百分濃度、稀釋與 ppm 計算','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先辨認溶質與溶液總量，再選用百分濃度或 ppm 公式並檢查單位。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-jb-iv-4-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
