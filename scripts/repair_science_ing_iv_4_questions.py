import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('光合作用固定碳','植物進行光合作用時，空氣中的二氧化碳碳元素主要進入哪裡？',['有機物如葡萄糖等植物體內物質','只進入氧氣','立刻變成氮元素','完全離開生態系'],'有機物如葡萄糖等植物體內物質','光合作用把二氧化碳中的碳固定到有機物，成為生物體與食物鏈的碳來源。'),
('呼吸釋放碳','植物或動物呼吸作用會使部分碳以哪種物質回到環境？',['二氧化碳','氮氣','金屬碳酸鹽必然增加','純氧'],'二氧化碳','呼吸分解有機物取得能量，碳的一部分以二氧化碳形式釋放。'),
('分解作用','落葉被分解者分解後，碳可能經哪條途徑回到大氣？',['分解者呼吸釋放二氧化碳','直接變成太陽光','所有碳立刻沉入地核','變成氧氣而沒有碳'],'分解者呼吸釋放二氧化碳','分解者利用有機物，代謝過程可將其中碳以二氧化碳釋放，部分也留在土壤。'),
('食物鏈流動','草中的碳進入兔子體內，主要經由什麼過程？',['兔子取食草並吸收其中有機物','兔子把氧氣變成碳','碳從土壤直接跳入兔子','陽光把碳吹進兔子'],'兔子取食草並吸收其中有機物','碳沿食物鏈隨有機物轉移，取食是生產者碳進入消費者的重要途徑。'),
('燃燒','燃燒煤炭使大氣二氧化碳增加，主要是因為？',['煤中原先儲存的碳與氧反應形成二氧化碳','燃燒創造新的碳元素','氧氣本身變成碳','煤中的碳完全消失'],'煤中原先儲存的碳與氧反應形成二氧化碳','燃燒把長期儲存在化石燃料中的碳快速轉移到大氣。'),
('碳庫','森林砍伐後焚燒，可能同時造成哪種碳循環改變？',['短期增加大氣碳輸入並減少植物碳庫','大氣二氧化碳必定下降且植物增加','碳元素從自然界消失','只改變氮循環而不影響碳'],'短期增加大氣碳輸入並減少植物碳庫','焚燒釋放碳，植被減少也降低固定二氧化碳的能力，因此影響碳輸入與碳庫大小。'),
('海洋碳庫','海水吸收部分大氣二氧化碳，這表示海洋在碳循環中可作為？',['碳的儲存庫與交換場所','只會製造氮氣的器官','不含任何碳的空間','只會把碳變成金屬'],'碳的儲存庫與交換場所','海洋可溶解、儲存並與大氣交換含碳物質，速率受溫度與化學條件影響。'),
('快速慢速循環','植物光合作用與呼吸作用的碳交換，通常相較岩石風化屬於？',['較快速的生物碳循環','完全不涉及碳','只能發生在地核','必定比所有地質作用更慢'],'較快速的生物碳循環','生物吸收與呼吸可在短時間發生；岩石風化與沉積等地質碳循環通常較慢。'),
('碳守恆','一片葉子腐爛後質量減少，最妥當的碳循環解釋？',['部分碳轉成二氧化碳或溶解物離開葉片，並非碳憑空消失','碳元素被破壞','所有碳變成光','葉片質量減少表示碳守恆不存在'],'部分碳轉成二氧化碳或溶解物離開葉片，並非碳憑空消失','腐敗使碳在不同碳庫間轉移；量測單一物體的質量不能代表整個系統的碳消失。'),
('資料判讀','若某地大氣 CO₂ 上升且植被覆蓋下降，哪個結論最合適？',['資料與植物固定碳減少或碳排放增加的解釋相容，仍需更多資料驗證','已證明只有砍伐一個原因','已證明所有碳庫都同時增加','CO₂ 上升與碳循環無關'],'資料與植物固定碳減少或碳排放增加的解釋相容，仍需更多資料驗證','兩項資料可支持合理假設，但需排除燃料使用、季節與測量誤差等其他因素。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; position=ord(target)-65; distractors=[v for v in opts if v != ans]; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」涉及的碳庫、流動過程與資料條件。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合碳循環方向。','排除誘答：沿著碳元素追蹤光合作用、呼吸、取食、分解、燃燒與儲存，不把碳誤當成氧或氮。','最後回查：確認結論限定在題目資料與系統邊界，必要時提出其他可能因素。']
 return {'id':f'question-science-content-ing-iv-4-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-ing-iv-4'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究碳庫、碳循環、物質流動與人類影響的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-ing-iv-4','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'碳庫、碳循環、物質流動與人類影響','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'沿著碳元素在生物與非生物碳庫間的流向，判斷過程與證據界線。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-ing-iv-4-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
