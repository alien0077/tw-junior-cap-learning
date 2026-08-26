import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-f-8-1':('F-8-1：一次函數','理解一次函數 y=ax+b 的變化率、初始值與生活情境。'),'content-f-8-2':('F-8-2：一次函數的圖形','以座標圖表示一次函數，從斜率與截距解讀圖形。')}
focus=['函數定義','變數關係','斜率意義','截距判讀','表格轉式','式轉圖','圖轉式','變化率','情境應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以表格、式子與圖形互相驗證。'},{'heading':'學習流程','body':'辨認輸入輸出，整理變化率與初始值，建立一次函數式，再用表格或座標圖檢查。'},{'heading':'常見錯誤','body':'混淆斜率與截距、讀錯座標刻度，或把一次函數當成固定常數。'}]};lesson['studyHighlights']=['斜率表示變化率。','截距是初始值。','表格、式子、圖形互證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['輸入、輸出與變化率','只看一個點'],'answer':'A','feedback':'先整理變數關係。'},{'id':'step-2','prompt':'第二步如何表示？','options':['用 y=ax+b 或座標圖表示','直接猜圖形'],'answer':'A','feedback':'斜率與截距決定一次函數。'},{'id':'step-3','prompt':'最後如何檢查？','options':['用表格、式子與圖形互證','跳過檢查'],'answer':'A','feedback':'三種表示應彼此一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'辨認斜率與截距，再用表格、式子或圖形驗證'},{'id':'B','text':'只看一個座標點猜測'},{'id':'C','text':'把截距當成斜率'},{'id':'D','text':'忽略座標刻度'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需由變化率、初始值與多種表示互相驗證。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
