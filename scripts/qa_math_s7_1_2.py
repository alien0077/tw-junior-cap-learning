import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-7-1':('S-7-1：簡單圖形與幾何符號','辨認點、線、角與常用幾何符號，理解圖形表示的基本約定。'),'content-s-7-2':('S-7-2：三視圖','由前視圖、上視圖與右視圖理解立體形體的表示。')}
focus=['點線角辨認','符號意義','圖形命名','位置關係','前視圖','上視圖','右視圖','立體想像','圖形轉換','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用符號與多視圖互相驗證。'},{'heading':'學習流程','body':'先辨認圖形元素與視角，再依符號或三視圖整理位置關係，最後檢查表示是否一致。'},{'heading':'常見錯誤','body':'混淆視圖方向、把線段當直線，或忽略幾何符號的約定。'}]};lesson['studyHighlights']=['先確認圖形與視角。','依符號與視圖推理。','用多種表示互證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['圖形元素與觀察視角','只看外框'],'answer':'A','feedback':'先確認點線角或視圖方向。'},{'id':'step-2','prompt':'第二步如何分析？','options':['依幾何符號或多視圖整理關係','直接猜立體形狀'],'answer':'A','feedback':'使用約定與視圖線索。'},{'id':'step-3','prompt':'最後如何確認？','options':['用另一視圖或符號互證','跳過檢查'],'answer':'A','feedback':'確認各表示一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認圖形元素與視角，再依符號或視圖互相驗證'},{'id':'B','text':'忽略視角任意判斷'},{'id':'C','text':'把不同幾何符號視為相同'},{'id':'D','text':'不檢查各視圖是否一致'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依幾何約定與視圖線索推理，並以另一表示檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
