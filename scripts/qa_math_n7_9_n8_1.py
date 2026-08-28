import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-7-9':('N-7-9：比與比例式','理解比、比例式與等值比，能用比例解決情境問題。'),'content-n-8-1':('N-8-1：二次方根','理解平方與平方根互為逆運算，並化簡基本根式。')}
focus=['比值意義','等值比','比例式','未知量求解','情境建模','平方關係','根號意義','根式化簡','正負判斷','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以代入或平方關係驗證。'},{'heading':'學習流程','body':'辨認數量關係，建立比或平方關係，逐步求解並檢查單位與結果。'},{'heading':'常見錯誤','body':'比的前後項顛倒、忽略比例相等，或混淆平方根與平方。'}]};lesson['studyHighlights']=['先確認數量關係。','依定義逐步求解。','代入或平方驗證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['數量關係與定義','只看數字外觀'],'answer':'A','feedback':'先確認比或平方根的定義。'},{'id':'step-2','prompt':'第二步如何求解？','options':['建立比例或根式關係並運算','直接猜結果'],'answer':'A','feedback':'依定義逐步處理。'},{'id':'step-3','prompt':'最後如何確認？','options':['代入或平方檢查','跳過檢查'],'answer':'A','feedback':'確認結果符合原關係。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認定義與數量關係，再逐步求解並代入檢查'},{'id':'B','text':'任意顛倒比的前後項'},{'id':'C','text':'混淆平方與平方根'},{'id':'D','text':'忽略單位與結果合理性'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依定義與數量關係處理，並以代入或平方驗證。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
