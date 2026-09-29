import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'questions/science'
URL='https://www.yacjh.kh.edu.tw/upload/221/101_30637/114%E4%B8%8B%E5%AD%B8%E6%9C%9F%E7%AC%AC%E4%B8%80%E6%AC%A1%E6%AE%B5%E8%80%83%E4%B8%89%E5%B9%B4%E7%B4%9A%E8%87%AA%E7%84%B6.pdf'
DATA=[
('速率定義','反應 30 秒產生 12 mL 氣體，平均產氣速率為何？',['0.4 mL/s','2.5 mL/s','12 mL/s','360 mL/s'],'0.4 mL/s','平均速率＝產生量÷時間＝12÷30=0.4 mL/s。'),
('表面積','相同質量的大理石，一組整塊、一組磨成粉末，哪組通常與酸反應較快？',['整塊，因為接觸面較小','粉末，因為接觸面較大','兩者必定一樣','無法由表面積提出預測'],'粉末，因為接觸面較大','粉末增加固體與酸的接觸面，碰撞機會通常增加；仍需控制質量與酸條件。'),
('濃度','比較酸濃度對反應速率的影響時，哪個設計較公平？',['只改變酸濃度，其他條件相同','同時改變酸濃度與大理石質量','一組加熱一組不加熱','每組使用不同反應物'],'只改變酸濃度，其他條件相同','單一變因設計才能把速率差異主要歸因於酸濃度。'),
('溫度','提高反應溫度常使反應變快，較合理的粒子解釋？',['粒子碰撞更頻繁且有效碰撞比例可能增加','所有原子變成另一元素','反應物質量必定增加','溫度會直接改變化學式下標'],'粒子碰撞更頻繁且有效碰撞比例可能增加','升溫使粒子平均動能提高，達到反應門檻的碰撞比例可能增加。'),
('催化劑','催化劑在反應中的典型作用是？',['提供較低活化能路徑，使反應較快且本身反應前後大致恢復','增加生成物的原子數','一定成為主要生成物','讓所有反應變成放熱'],'提供較低活化能路徑，使反應較快且本身反應前後大致恢復','催化劑改變反應途徑與速率，不是把自己大量消耗或改變原子守恆。'),
('速率比較','甲反應 20 秒產生 10 mL 氣體，乙反應 10 秒產生 8 mL，哪個平均速率較快？',['甲，0.5 mL/s','乙，0.8 mL/s','兩者相同','資料不足以計算'],'乙，0.8 mL/s','甲速率 10÷20=0.5，乙速率 8÷10=0.8；比較時必須同時考慮產量與時間。'),
('控制變因','研究溫度對反應速率的影響，哪項應保持相同？',['反應物質量、濃度、表面積與測量方式','只保持結果相同','每次都改變攪拌速度','不需記錄起始時間'],'反應物質量、濃度、表面積與測量方式','除自變因溫度外，其他重要條件應控制，才能比較速率。'),
('曲線判讀','反應初期氣體體積增加很快，後期曲線變平，最合理的解釋？',['反應物逐漸消耗，反應速率下降','後期生成物變回所有反應物','後期時間停止','氣體體積必定變成負值'],'反應物逐漸消耗，反應速率下降','反應物濃度降低或接近耗盡時，單位時間生成量常下降，曲線趨於平台。'),
('公平重複','同一條件測量反應速率，重複三次的主要目的？',['估計變異並檢查結果是否穩定','讓每次反應物自動增加','保證所有數據完全相同','取代控制變因'],'估計變異並檢查結果是否穩定','重複試驗可降低偶然誤差並觀察資料一致性，但不能取代公平控制。'),
('結論界線','若只有一組高溫實驗比低溫快，最恰當的結論？',['在本實驗條件下高溫組平均速率較快，仍需重複驗證','溫度是唯一影響所有反應的因素','所有高溫反應都一定更快','已證明生成物種類改變'],'在本實驗條件下高溫組平均速率較快，仍需重複驗證','科學結論應限定在資料與控制條件範圍，不能由單次比較過度推廣。')]
TARGET_ANSWERS='ABCDBCDACB'
def make(i,row):
 tag,prompt,opts,ans,reason=row; target=TARGET_ANSWERS[i-1]; correct_index=opts.index(ans); distractors=[v for j,v in enumerate(opts) if j != correct_index]; position=ord(target)-65; arranged=distractors[:position]+[ans]+distractors[position:]; options=[{'id':chr(65+j),'text':v} for j,v in enumerate(arranged)]; aid=target
 steps=[f'讀題定位：抓出「{tag}」的自變因、反應量、時間與控制條件。',f'建立判準：{reason}',f'核對答案：選項 {aid}「{ans}」符合判準。','排除誘答：速率要同時看反應量與時間，探究題要區分自變因、應變因與控制變因。','最後回查：確認結論只適用於題目條件，並檢查單位、重複測量與替代解釋。']
 return {'id':f'question-science-content-je-iv-1-{i}','subject':'science','type':'single-choice','prompt':prompt,'options':options,'knowledgeIds':['kg-science-content-je-iv-1'],'difficulty':'medium','answer':{'value':aid,'explanation':reason},'provenance':{'origin':'original','license':'All rights reserved','sourceUrl':URL,'sourceLocator':'公立國中段考自然科；研究反應速率、影響因素與公平探究的能力方向。','authoringNote':'依官方課綱 KG 與公立國中公開試題能力方向獨立改寫，未複製原文、選項、圖表或答案；待第二輪 AI／Terra 內容複核。'},'reviewStatus':'draft','updatedAt':'2026-09-08','lessonId':'lesson-science-content-je-iv-1','examPatternRefs':[{'url':URL,'title':'公立國中段考自然科；僅研究題型與能力方向，未複製原題。','year':'114','subject':'science','locator':'反應速率、影響因素與公平探究','observedPattern':'能力方向研究後原創改寫','reuseDecision':'pattern-only','status':'recorded','locatorLevel':'paper'}],'solutionStrategy':'先定義速率，再辨識自變因與控制變因，最後用資料與單位比較。','solutionSteps':steps}
for i,row in enumerate(DATA,1): (OUT/f'question-science-content-je-iv-1-{i}.json').write_text(json.dumps(make(i,row),ensure_ascii=False,indent=2)+'\n')
print('rewrote',len(DATA),'questions')
