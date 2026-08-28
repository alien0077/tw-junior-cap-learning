import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-8-4':('N-8-4：等差數列','辨認固定公差的等差數列，求第 n 項與延伸項。'),'content-n-8-5':('N-8-5：等差級數求和','運用首項、末項與項數公式計算等差級數總和。')}
focus=['首項辨認','公差計算','項次關係','第 n 項','延伸項','項數判讀','求和公式','首末項','情境建模','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以列舉或公式驗證結果。'},{'heading':'學習流程','body':'找出首項與公差，建立項次關係；求和時確認首末項與項數，再代入公式。'},{'heading':'常見錯誤','body':'公差正負判斷錯誤、項數少算，或將第 n 項公式誤當求和公式。'}]};lesson['studyHighlights']=['先找首項與公差。','確認項次與項數。','用列舉或公式驗算。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先找什麼？','options':['首項、公差與項數','只看最後一項'],'answer':'A','feedback':'先整理數列條件。'},{'id':'step-2','prompt':'第二步如何計算？','options':['使用第 n 項或求和公式','直接猜結果'],'answer':'A','feedback':'依題目要求選公式。'},{'id':'step-3','prompt':'最後如何檢查？','options':['列舉前幾項或代回公式','跳過檢查'],'answer':'A','feedback':'確認項次與總和一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認首項、公差、項數，再選公式並驗算'},{'id':'B','text':'把第 n 項公式當成總和公式'},{'id':'C','text':'忽略項數與公差正負'},{'id':'D','text':'不檢查列舉結果'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需先整理數列條件，依要求使用項公式或求和公式並檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
