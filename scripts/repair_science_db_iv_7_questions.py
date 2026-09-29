import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('雄蕊構造','花的雄蕊通常由哪兩部分組成？',['花藥與花絲','柱頭與花柱','子房與胚珠','花瓣與萼片'],'花藥與花絲','花藥產生花粉，花絲支撐花藥，兩者共同構成雄蕊。'),
('雌蕊構造','花的雌蕊通常包含哪些構造？',['柱頭、花柱與子房','花藥、花絲與花粉','萼片、花瓣與蜜腺','根、莖與葉'],'柱頭、花柱與子房','柱頭接受花粉，花柱連接柱頭與子房，子房內含胚珠。'),
('授粉','授粉的定義是什麼？',['花粉由花藥移到適合的柱頭','精子與卵細胞已經融合','種子萌發成根','花瓣由綠變紅'],'花粉由花藥移到適合的柱頭','授粉是花粉傳到柱頭的過程，受精則是配子融合，兩者不可混為一談。'),
('受精位置','開花植物的受精通常發生在何處？',['胚珠內的卵細胞與精細胞融合','花瓣表面','花藥外壁','根毛內'],'胚珠內的卵細胞與精細胞融合','花粉萌發形成花粉管，將精細胞送到胚珠，與卵細胞融合形成合子。'),
('種子形成','受精後，胚珠通常發育成什麼？',['種子','果皮','花瓣','花粉'],'種子','胚珠受精後形成種子；子房通常發育成果實，兩者需分清。'),
('果實形成','受精後，子房通常發育成什麼？',['果實','種皮','花粉粒','根毛'],'果實','子房壁等構造可發育成果實的一部分，胚珠則與種子形成有關。'),
('花粉管','花粉落到柱頭後，花粉管的主要功能？',['向子房方向生長，讓精細胞抵達胚珠','把花粉變成花瓣','吸收土壤水分到根部','使柱頭變成葉片'],'向子房方向生長，讓精細胞抵達胚珠','花粉管是雄性配子到達胚珠的重要通道，不是根部運輸構造。'),
('傳粉媒介','蜜蜂訪花可能增加授粉機會，主要因為？',['花粉可附著在身體上並帶到另一朵花的柱頭','蜜蜂把卵細胞帶到花藥','蜜蜂使所有花粉變成種子','蜜蜂直接完成植物受精作用'],'花粉可附著在身體上並帶到另一朵花的柱頭','動物可作為傳粉媒介，但授粉後仍需花粉萌發與受精等後續過程。'),
('自交與異交','同一朵花的花粉落到自己的柱頭，這種傳粉可稱為？',['自花授粉','風化作用','無性繁殖必然','種子散播'],'自花授粉','花粉來源與柱頭位置可用來區分自花授粉與異花授粉；授粉不等於沒有遺傳變異。'),
('證據判讀','看到花粉已落在柱頭上，最嚴謹的結論？',['已觀察到授粉線索，但不能僅此證明已完成受精或形成種子','已證明種子一定成熟','已證明花粉管一定到達胚珠','已證明果實已形成'],'已觀察到授粉線索，但不能僅此證明已完成受精或形成種子','授粉、花粉管生長、受精、種子與果實形成是連續但不同的事件，需要各自證據。')]
def make(i,row):
 tag,prompt,opts,ans,reason=row; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(opts)]; aid=next(o['id'] for o in options if o['text']==ans)
 steps=[f'讀題定位：抓出「{tag}」涉及的花部構造、花粉、配子或發育結果。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合植物生殖流程。','排除誘答：依花藥→柱頭→花粉管→胚珠→受精→種子／果實順序辨認，不把事件混在一起。','最後回查：確認觀察證據只支持相應階段，不能由授粉直接跳到種子成熟。']
 return {'id':f'question-science-content-db-iv-7-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-db-iv-7'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究花的生殖構造、配子、授粉、受精與種子形成的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-db-iv-7','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'花的生殖構造、配子、授粉、受精與種子形成','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先沿花粉與配子的生殖流程定位構造，再分辨授粉、受精與發育結果。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-db-iv-7-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
