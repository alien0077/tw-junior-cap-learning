import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('循環路徑','含氧血由肺部回到心臟後，通常先進入哪個構造？',['左心房','右心房','右心室','肺動脈'],'左心房','肺部氧合後的血液經肺靜脈回到左心房，再送往左心室與全身。'),
('肺循環','右心室將血液送往肺部的主要血管是？',['肺動脈','肺靜脈','主動脈','腔靜脈'],'肺動脈','右心室將缺氧血經肺動脈送到肺部進行氣體交換；血管名稱依流向而非含氧量命名。'),
('體循環','左心室收縮時，血液主要由哪條大血管送往全身？',['主動脈','肺動脈','肺靜脈','腔靜脈'],'主動脈','左心室把含氧血送入主動脈，再分流到全身組織。'),
('毛細血管','物質在血液與組織細胞間交換，最主要發生在哪裡？',['毛細血管','主動脈','心房','肺靜脈'],'毛細血管','毛細血管壁薄且分布廣，適合氧氣、養分與代謝廢物進行擴散交換。'),
('紅血球','紅血球最主要的運輸功能是什麼？',['利用血紅素運送氧氣','製造抗體並吞噬病菌','形成血小板凝塊','消化食物中的澱粉'],'利用血紅素運送氧氣','紅血球內血紅素可與氧結合，協助將氧氣運到組織；其他功能主要由不同血球或器官負責。'),
('血漿','血漿在循環系統中主要扮演什麼角色？',['作為液體介質運送養分、廢物與部分訊息物質','只負責製造紅血球','把所有氧氣固定成固體','只存在於心臟內'],'作為液體介質運送養分、廢物與部分訊息物質','血漿是血液的液體部分，可溶解並運送多種物質。'),
('靜脈特徵','與動脈相比，靜脈通常具有哪項特徵？',['把血液送回心臟，管壁較薄且常有瓣膜協助回流','一定把含氧血送離心臟','管壁最厚且承受最高壓力','只存在於肺部'],'把血液送回心臟，管壁較薄且常有瓣膜協助回流','血管分類依相對心臟的流向；靜脈回流時瓣膜可減少血液倒流。'),
('物質方向','組織細胞產生的二氧化碳要排出體外，合理路徑為何？',['細胞→組織液／毛細血管→靜脈→心臟→肺→呼出','細胞→主動脈→肺→吞入','肺→動脈→細胞→呼出','細胞→胃→腎臟→呼出'],'細胞→組織液／毛細血管→靜脈→心臟→肺→呼出','二氧化碳由細胞進入血液，經靜脈回心臟，再送至肺泡與外界交換。'),
('淋巴功能','淋巴系統回收組織間多餘液體，對循環系統的意義是？',['協助維持組織液與血液間的液體平衡','取代心臟泵送全部血液','把氧氣變成葡萄糖','使所有血管停止流動'],'協助維持組織液與血液間的液體平衡','淋巴回流可將部分組織液送回循環，避免液體持續積在組織間。'),
('交換證據','運動時肌肉需要較多氧氣，哪項調節最能直接支持運輸需求？',['心跳與呼吸加快，使含氧血液更快到達組織','血液完全停止流動','毛細血管全部封閉','肺泡不再進行氣體交換'],'心跳與呼吸加快，使含氧血液更快到達組織','運動時提高通氣與循環速率，可增加氧氣供應與二氧化碳移除，但仍受多項因素共同影響。')]
def make(i,row):
 tag,prompt,opts,ans,reason=row; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(opts)]; aid=next(o['id'] for o in options if o['text']==ans)
 steps=[f'讀題定位：抓出「{tag}」的血液流向、血管、血液成分或交換位置。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合循環路徑與功能。','排除誘答：先按血液相對心臟的流向判斷血管，再核對含氧量、交換位置與血液成分功能。','最後回查：將路徑從起點走到終點，確認氧氣、二氧化碳、養分或液體方向沒有顛倒。']
 return {'id':f'question-science-content-db-iv-2-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-db-iv-2'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究循環路徑、血液成分、血管與物質交換的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-db-iv-2','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'循環路徑、血液成分、血管與物質交換','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先沿血液流向定位心臟腔室與血管，再對照成分功能與交換方向。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-db-iv-2-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
