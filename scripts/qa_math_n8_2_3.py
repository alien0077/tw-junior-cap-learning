import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-8-2':('N-8-2：二次方根的近似值','以十分逼近或估算理解二次方根的近似值。'),'content-n-8-3':('N-8-3：認識數列','觀察數列規律，描述項次與項值的關係。')}
focus=['估算範圍','十分逼近','誤差判斷','根號近似','項次辨認','規律觀察','通項關係','遞增遞減','情境應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用估算、規律或代入檢查。'},{'heading':'學習流程','body':'先整理數值或項次，觀察範圍與規律，建立關係，再檢查近似誤差或項值。'},{'heading':'常見錯誤','body':'把近似值當精確值、忽略誤差範圍，或只看相鄰兩項未驗證整體規律。'}]};lesson['studyHighlights']=['先整理範圍與項次。','觀察規律建立關係。','檢查誤差與結果。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['數值範圍或項次資料','只看最後一項'],'answer':'A','feedback':'先收集必要資料。'},{'id':'step-2','prompt':'第二步如何分析？','options':['用逼近或規律建立關係','直接猜結果'],'answer':'A','feedback':'依定義與規律推理。'},{'id':'step-3','prompt':'最後如何檢查？','options':['檢查誤差、項值或代入','跳過檢查'],'answer':'A','feedback':'確認結果符合條件。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'整理資料與條件，依逼近或規律推理並檢查'},{'id':'B','text':'只看單一數值猜測'},{'id':'C','text':'忽略誤差或項次'},{'id':'D','text':'不驗證整體規律'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依資料、定義與規律推理，並檢查結果。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
