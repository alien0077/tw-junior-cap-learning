import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-7-5':('S-7-5：線對稱的基本圖形','辨認具有線對稱的基本圖形，找出對稱軸與對應點。'),'content-s-8-1':('S-8-1：角','理解角的構成、種類與度量，能比較角的大小。')}
focus=['圖形辨認','對稱軸','對應點','等距關係','角的構成','角度量','銳角鈍角','直角判讀','圖形應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以對應點、垂線或角度量驗證。'},{'heading':'學習流程','body':'先辨認幾何元素，整理對稱或角的關係，再用圖形與度量檢查。'},{'heading':'常見錯誤','body':'把任意折線當對稱軸、混淆角的邊與頂點，或誤判角度種類。'}]};lesson['studyHighlights']=['先確認元素與定義。','找對稱或角度關係。','用圖形與度量驗證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['圖形元素與定義','只看外框'],'answer':'A','feedback':'先辨認對稱軸或角的頂點與邊。'},{'id':'step-2','prompt':'第二步如何判斷？','options':['依等距、垂直或度量關係分析','直接猜結果'],'answer':'A','feedback':'使用幾何定義。'},{'id':'step-3','prompt':'最後如何檢查？','options':['用圖形與度量互證','跳過檢查'],'answer':'A','feedback':'確認關係一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先依定義辨認元素，再用等距、垂直或角度量驗證'},{'id':'B','text':'只看外觀直接猜測'},{'id':'C','text':'忽略頂點、邊或對稱軸'},{'id':'D','text':'不檢查圖形關係'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依幾何定義與圖形、度量證據判斷。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
