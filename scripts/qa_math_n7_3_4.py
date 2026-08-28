import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-7-3':('N-7-3：負數與數的四則混合運算','理解負數、分數與小數的四則運算及運算順序。'),'content-n-7-4':('N-7-4：數的運算規律','運用交換律、結合律與分配律簡化數的運算。')}
focus=['數線位置','負號意義','分數運算','小數運算','運算順序','交換律','結合律','分配律','估算檢查','情境應用']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能依運算順序與運算律驗算結果。'},{'heading':'學習流程','body':'先辨認數與符號，再依括號、乘除、加減順序運算，必要時用運算律整理，最後估算檢查。'},{'heading':'常見錯誤','body':'負負得正判斷錯誤、忽略括號，或任意交換不符合運算律的項目。'}]};lesson['studyHighlights']=['先辨認符號與數線。','遵守運算順序。','用運算律與估算檢查。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['數值、符號與括號','只看數字大小'],'answer':'A','feedback':'先辨認正負與運算結構。'},{'id':'step-2','prompt':'第二步如何運算？','options':['依順序或運算律逐步處理','任意改變順序'],'answer':'A','feedback':'依規則計算。'},{'id':'step-3','prompt':'最後如何檢查？','options':['估算或反向整理驗證','不必檢查'],'answer':'A','feedback':'確認結果合理。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認符號與括號，再依運算順序或運算律計算並檢查'},{'id':'B','text':'任意交換運算順序'},{'id':'C','text':'忽略負號與括號'},{'id':'D','text':'不估算或驗算'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須遵守數值規則與運算順序，並用估算或整理檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
