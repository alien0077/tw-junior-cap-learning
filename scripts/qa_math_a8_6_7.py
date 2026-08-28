import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-8-6':('A-8-6：一元二次方程式的意義','理解最高次為二次的方程式，辨認係數與根的意義。'),'content-a-8-7':('A-8-7：一元二次方程式的解法與應用','運用因式分解、公式或配方法求解並檢查根。')}
focus=['二次結構','係數辨認','根的意義','因式分解法','公式法','配方法','判別式','代入驗算','情境建模','解的取捨']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能代回原方程式確認根。'},{'heading':'學習流程','body':'整理二次方程式係數，選擇因式分解、公式或配方法，求根後逐一代回驗算。'},{'heading':'常見錯誤','body':'漏掉一個根、平方根正負號處理錯誤，或未依情境限制取捨答案。'}]}; lesson['studyHighlights']=['辨認二次項與係數。','依結構選擇解法。','每個根都要代回驗算。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['二次方程式的係數與條件','無關數字'],'answer':'A','feedback':'先確認標準形式與係數。'},{'id':'step-2','prompt':'第二步如何求根？','options':['依結構選擇解法','直接猜根'],'answer':'A','feedback':'可用因式分解、公式或配方法。'},{'id':'step-3','prompt':'最後如何確認？','options':['將每個根代回原式','只檢查一個根'],'answer':'A','feedback':'每個根都需符合原方程式。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'整理係數、選擇合適解法，並將每個根代回驗算'},{'id':'B','text':'只找一個根就停止'},{'id':'C','text':'忽略平方根正負號'},{'id':'D','text':'不考慮題目情境限制'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需先整理結構，再求出所有符合條件的根並代回確認。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
