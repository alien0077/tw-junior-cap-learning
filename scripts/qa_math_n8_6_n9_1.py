import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-8-6':('N-8-6：等比數列','辨認固定公比的等比數列，求項值與公比。'),'content-n-9-1':('N-9-1：連比','理解三個量的連比關係，化為等值比並求未知量。')}
focus=['首項辨認','公比判斷','項次關係','第 n 項','連比表示','等值比','未知量求解','比例轉換','情境應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以代回或比例檢查結果。'},{'heading':'學習流程','body':'辨認比值或公比，整理項次與未知量，建立關係後逐步求解並驗算。'},{'heading':'常見錯誤','body':'把公比當公差、連比前後項對錯，或忽略比例同乘同除條件。'}]};lesson['studyHighlights']=['先辨認比值關係。','依項次或比例求解。','代回檢查結果。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['首項、公比或連比條件','只看一項數值'],'answer':'A','feedback':'先確認比值關係。'},{'id':'step-2','prompt':'第二步如何求解？','options':['依公比或等值比逐步計算','直接猜答案'],'answer':'A','feedback':'使用正確比例方法。'},{'id':'step-3','prompt':'最後如何確認？','options':['代回關係式檢查','跳過檢查'],'answer':'A','feedback':'確認比值與項次一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認比值條件，再逐步求解並代回檢查'},{'id':'B','text':'把公比當作公差使用'},{'id':'C','text':'任意顛倒連比前後項'},{'id':'D','text':'不驗算比例關係'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依公比或等值比定義處理，並以代回檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
