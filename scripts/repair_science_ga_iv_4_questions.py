import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('遺傳物質','下列哪項最能說明基因與性狀的關係？',['基因提供遺傳資訊，性狀也可能受環境影響','所有性狀只由飲食決定','基因只存在於血液','性狀改變一定代表基因改變'],'基因提供遺傳資訊，性狀也可能受環境影響','基因資訊會影響性狀，但營養、溫度與生活條件等環境也可能造成表現差異。'),
('基因突變','DNA 鹼基序列發生改變，最直接可能造成什麼？',['基因資訊改變，可能影響蛋白質或性狀','所有染色體立即消失','環境因素完全不再影響性狀','細胞一定立刻死亡'],'基因資訊改變，可能影響蛋白質或性狀','突變是遺傳物質序列的改變，影響程度取決於位置、類型與是否改變功能。'),
('細胞類型','若突變發生在皮膚體細胞，通常與生殖細胞突變相比有何差異？',['通常不直接遺傳給下一代','一定會遺傳給所有子女','會改變父母的基因','一定不會影響該個體'],'通常不直接遺傳給下一代','體細胞突變多影響個體本身；只有進入生殖系統的遺傳資訊才有機會傳給後代。'),
('環境與表型','同品種植物在光照不同的環境中葉片大小不同，哪個解釋較合理？',['基因相近但環境差異影響表型','葉片大小差異必定來自DNA突變','植物沒有遺傳物質','光照會把一種元素變成另一種元素'],'基因相近但環境差異影響表型','表型是遺傳與環境共同作用的結果，觀察到差異不能直接等同於突變。'),
('誘變因子','紫外線可能增加 DNA 損傷風險，較合適的安全推論？',['過量曝曬可能增加突變或細胞損傷風險，應做好防護','紫外線必定讓所有細胞產生有利突變','只要有突變就一定遺傳','紫外線能改變元素原子序'],'過量曝曬可能增加突變或細胞損傷風險，應做好防護','某些輻射可造成 DNA 損傷，但結果不一定、也不必然可遺傳；應以風險與防護理解。'),
('染色體','染色體可視為什麼？',['含有 DNA 與基因的細胞內結構','只存在於細胞外的營養物質','一種環境溫度單位','只由水分子組成'],'含有 DNA 與基因的細胞內結構','染色體是 DNA 與相關蛋白質組成的結構，基因位於 DNA 上的特定區段。'),
('遺傳與機率','若某性狀由一對等位基因控制，父母各提供一個等位基因，子代基因型如何形成？',['一個來自父方、一個來自母方','兩個都必定來自父方','由子代自行製造且與父母無關','只由環境決定'],'一個來自父方、一個來自母方','有性生殖時，配子各帶一個等位基因，受精後組合成子代的一對等位基因。'),
('突變結果','下列哪項最符合「突變不一定有害」？',['突變可能無明顯影響、有害或在特定環境有利','所有突變都使生物更強','所有突變都立即致死','突變只會發生在植物'],'突變可能無明顯影響、有害或在特定環境有利','突變效果取決於基因位置、表現與環境，不能只用有利或有害單一分類。'),
('證據判讀','觀察到家族成員都有某性狀，最妥當的下一步？',['比較家族資料並控制環境因素，才能評估遺傳與環境作用','直接斷言一定由單一基因造成','忽略沒有該性狀的成員','把家族相似等同於必然遺傳'],'比較家族資料並控制環境因素，才能評估遺傳與環境作用','家族相似可提供線索，但共享環境也會造成相似，需更多資料與控制。'),
('改變界線','運動後肌肉變粗但 DNA 序列未改變，這較適合稱為？',['個體表型或生理狀態改變，不等同遺傳物質突變','一定是生殖細胞突變','一定能遺傳給子女','染色體數目必定增加'],'個體表型或生理狀態改變，不等同遺傳物質突變','表型可因使用與環境改變；沒有 DNA 或染色體證據，不能直接宣稱遺傳物質發生突變。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; correct=ans; distractors=[v for v in opts if v != correct]; opts=distractors[:ord(target)-65]+[correct]+distractors[ord(target)-65:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(opts)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」涉及的基因、染色體、突變、環境或表型證據。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：分清遺傳物質改變、個體表型改變與環境造成的暫時差異。','最後回查：確認結論有足夠遺傳或環境證據，不能把相關性直接當成必然因果。']
 return {'id':f'question-science-content-ga-iv-4-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-ga-iv-4'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究遺傳物質、突變、環境與性狀改變的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-ga-iv-4','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'遺傳物質、突變、環境與性狀改變','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先分辨遺傳物質與表型，再以細胞類型、環境條件與證據界線判斷。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-ga-iv-4-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
