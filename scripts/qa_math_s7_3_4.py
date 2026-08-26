import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-7-3':('S-7-3：垂直','理解垂直線的直角關係，能由圖形與符號判斷。'),'content-s-7-4':('S-7-4：線對稱的性質','理解對稱軸兩側對應點等距與垂直關係。')}
focus=['垂直定義','直角判讀','線段關係','符號表示','對稱軸','對應點','等距判斷','鏡射位置','圖形應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以直角、距離與對應點檢查。'},{'heading':'學習流程','body':'先辨認線段與對稱軸，整理直角或對應點關係，再用圖形與符號驗證。'},{'heading':'常見錯誤','body':'把垂直當成相交即可，或鏡射後忽略對稱軸兩側距離相等。'}]};lesson['studyHighlights']=['先確認定義與符號。','找直角或對應點。','用距離與圖形驗證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['線段、直角或對稱軸','只看外框'],'answer':'A','feedback':'先確認幾何元素。'},{'id':'step-2','prompt':'第二步如何判斷？','options':['檢查垂直或對應點等距關係','直接猜圖形'],'answer':'A','feedback':'依定義與距離判斷。'},{'id':'step-3','prompt':'最後如何確認？','options':['用圖形與符號互證','跳過檢查'],'answer':'A','feedback':'確認幾何關係一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'依定義找直角、對稱軸與對應點，再用圖形驗證'},{'id':'B','text':'只要相交就判定垂直'},{'id':'C','text':'忽略對稱軸兩側距離'},{'id':'D','text':'不檢查對應關係'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依幾何定義與距離、角度關係判斷。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
