import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-d-9-2':('D-9-2：認識機率','以隨機試驗、樣本空間與事件理解機率的範圍與意義。'),'content-d-9-3':('D-9-3：古典機率','在等可能情況下以有利結果數除以所有可能結果數計算機率。')}
focus=['隨機試驗','樣本空間','事件定義','等可能性','有利結果','分母判斷','機率範圍','互補事件','情境計算','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能檢查機率是否介於 0 與 1。'},{'heading':'學習流程','body':'定義試驗與事件，列出樣本空間，確認等可能性，再計算並檢查結果。'},{'heading':'常見錯誤','body':'分母漏列可能結果、把有利結果與全部結果顛倒，或忽略等可能條件。'}]};lesson['studyHighlights']=['先列出樣本空間。','確認等可能與有利結果。','檢查機率範圍。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先定義什麼？','options':['試驗、樣本空間與事件','只看一個結果'],'answer':'A','feedback':'先列出所有可能結果。'},{'id':'step-2','prompt':'第二步如何計算？','options':['確認等可能後比較有利與全部結果','直接猜比例'],'answer':'A','feedback':'古典機率需有等可能前提。'},{'id':'step-3','prompt':'最後如何檢查？','options':['確認結果介於 0 與 1','忽略範圍'],'answer':'A','feedback':'機率不會小於 0 或大於 1。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'列出樣本空間，確認等可能後以有利結果與全部結果計算'},{'id':'B','text':'只列想要的結果當分母'},{'id':'C','text':'忽略等可能條件直接猜比例'},{'id':'D','text':'接受大於 1 的機率'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需先定義樣本空間與事件，並確認計算結果在 0 到 1 之間。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
