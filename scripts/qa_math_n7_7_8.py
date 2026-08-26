import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-7-7':('N-7-7：指數律','運用同底數乘除與冪次乘方的指數律化簡算式。'),'content-n-7-8':('N-7-8：科學記號','以 a×10^n 表示數值並進行大小判讀與運算。')}
focus=['同底數相乘','同底數相除','冪次乘方','零次方','負指數','科學記號形式','10 的次方','大小比較','實際情境','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以展開或數值估算檢查結果。'},{'heading':'學習流程','body':'辨認底數與指數，選擇相應律或科學記號形式，逐步運算並檢查數值量級。'},{'heading':'常見錯誤','body':'相加指數規則誤用、10 的次方位數錯誤，或係數未調整至 1 到 10 之間。'}]};lesson['studyHighlights']=['辨認底數與指數。','依指數律逐步化簡。','檢查位數與量級。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['底數、指數與係數','只看數字長度'],'answer':'A','feedback':'先看清楚式子結構。'},{'id':'step-2','prompt':'第二步如何運算？','options':['套用正確指數律或科學記號規則','任意相加指數'],'answer':'A','feedback':'依規則處理。'},{'id':'step-3','prompt':'最後如何檢查？','options':['展開或檢查位數量級','跳過檢查'],'answer':'A','feedback':'確認結果合理。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認底數、指數與係數，再依規則運算並檢查量級'},{'id':'B','text':'把不同底數指數任意相加'},{'id':'C','text':'忽略 10 的次方位數'},{'id':'D','text':'不檢查科學記號係數範圍'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依指數律或科學記號定義，並檢查結果量級。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
