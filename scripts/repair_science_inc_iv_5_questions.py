import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('尺度轉換','看到一滴水在杯中，若要解釋蒸發現象，哪種尺度的模型最有幫助？',['以水分子運動與表面逸出解釋','只比較杯子顏色','只量杯子重量而不談粒子','把水滴當作一個不可分割的原子'],'以水分子運動與表面逸出解釋','宏觀可見的是水量減少，微觀模型可用分子運動與表面逸出連結兩種尺度。'),
('原子分子尺度','下列哪項是原子與分子模型能解釋的微觀問題？',['物質由哪些粒子組成及粒子如何排列','操場面積的直接丈量','天氣預報的所有結果','物體名稱的字數'],'物質由哪些粒子組成及粒子如何排列','原子與分子模型用於說明物質組成、排列、運動與反應，不能取代所有宏觀測量。'),
('宏觀微觀','鹽溶於水後肉眼看不到鹽粒，最合理的微觀解釋？',['鹽解離成離子並分散在水中，粒子仍存在','鹽的原子完全消失','鹽變成光線','水把元素變成空氣'],'鹽解離成離子並分散在水中，粒子仍存在','宏觀上看不見不代表物質消失；微觀粒子可均勻分散於水中。'),
('氣體壓縮','氣體可被壓縮，粒子模型最能支持哪項推論？',['氣體粒子間平均空隙較大','氣體粒子沒有質量','氣體粒子一定變成液體','壓縮會消滅原子'],'氣體粒子間平均空隙較大','壓縮主要減少粒子間距離；模型不表示粒子本身被消滅。'),
('熱與粒子','加熱固體時溫度升高，微觀上通常可描述為？',['粒子平均運動能增加，振動更劇烈','原子序全部增加','粒子種類必定改變','所有分子都停止運動'],'粒子平均運動能增加，振動更劇烈','溫度可與粒子平均動能相關；加熱不必然造成元素或粒子種類改變。'),
('反應尺度','化學反應在微觀層次主要發生什麼？',['原子重新排列並形成新的分子或離子組合','原子核全部消失','物質只改變觀察者名稱','質量必定憑空增加'],'原子重新排列並形成新的分子或離子組合','化學反應改變原子的鍵結與排列，元素原子數在適當系統中守恆。'),
('守恆連結','密閉容器中反應前後總質量相同，哪個微觀說明合理？',['原子總數與種類守恆，只是排列方式改變','粒子全部離開容器','分子變成沒有質量的影像','原子數量由天平決定'],'原子總數與種類守恆，只是排列方式改變','宏觀質量守恆可用微觀原子守恆與重新排列來解釋。'),
('模型限制','粒子模型中的球常用不同顏色代表不同元素，正確理解是？',['顏色是表徵符號，不一定是元素真實外觀','所有元素真實顏色就是球色','球的大小必定是真實比例','顏色本身能證明化學反應'],'顏色是表徵符號，不一定是元素真實外觀','模型用可視化符號表示粒子差異，需清楚說明比例與顏色的假設。'),
('證據推論','氣味擴散到教室各處，哪項微觀推論最合理？',['氣體分子持續運動並在空間中分散','氣味分子只向上靜止移動','所有空氣分子變成氣味物質','擴散代表原子序改變'],'氣體分子持續運動並在空間中分散','擴散現象支持粒子持續運動與空間分散，但不表示元素種類必然改變。'),
('跨尺度表述','寫科學解釋時，哪種表述能正確連結宏觀與微觀？',['宏觀觀察到液面下降，微觀可用分子逸出解釋','只寫液面下降就等於證明分子消失','只畫分子就不必記錄觀察','宏觀與微觀必定互相矛盾'],'宏觀觀察到液面下降，微觀可用分子逸出解釋','好的解釋要先描述觀察，再以可檢驗的粒子模型連結原因，不能把模型當成直接影像。')]
TARGET_ANSWERS = 'ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」的宏觀觀察、微觀粒子或尺度轉換。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合模型與證據。','排除誘答：分清觀察到的現象、微觀推論與模型假設，不把不可見粒子當成直接影像。','最後回查：確認宏觀資料與微觀解釋彼此對應，且沒有超出模型適用範圍。']
 return {'id':f'question-science-content-inc-iv-5-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-inc-iv-5'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究原子與分子尺度、粒子模型及宏觀微觀連結的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-inc-iv-5','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'原子與分子尺度、粒子模型及宏觀微觀連結','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先描述宏觀現象，再選擇能對應的微觀粒子模型，最後檢查模型限制。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-inc-iv-5-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
