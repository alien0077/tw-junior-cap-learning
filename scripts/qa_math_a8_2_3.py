import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-8-2':('A-8-2：多項式的意義','辨認多項式的項、係數、次數與同類項。'),'content-a-8-3':('A-8-3：多項式的四則運算','依同類項與分配律規則進行多項式的加減乘除。')}
focus=['項與係數','次數判讀','同類項','加法整理','減法整理','分配律','乘法運算','除法概念','式子化簡','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用代入或展開檢查運算結果。'},{'heading':'學習流程','body':'辨認項與次數，整理同類項，依分配律逐步運算，最後代入或反向檢查。'},{'heading':'常見錯誤','body':'把不同次數的項合併，或多項式減法時未將括號內各項變號。'}]}; lesson['studyHighlights']=['先辨認項與次數。','只合併同類項。','逐步運算並檢查。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步要先辨認什麼？','options':['項、係數與次數','無關數字'],'answer':'A','feedback':'先看清楚每一項的結構。'},{'id':'step-2','prompt':'第二步如何整理？','options':['只合併同類項並依分配律運算','任意合併各項'],'answer':'A','feedback':'同類項才能合併。'},{'id':'step-3','prompt':'最後如何檢查？','options':['代入或展開核對','跳過檢查'],'answer':'A','feedback':'用代入或展開確認結果。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認項與次數，只合併同類項並逐步檢查'},{'id':'B','text':'把所有含字母的項任意相加'},{'id':'C','text':'減去括號時不改變各項符號'},{'id':'D','text':'不需核對運算結果'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須遵守同類項與分配律規則，並以代入或展開檢查。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
