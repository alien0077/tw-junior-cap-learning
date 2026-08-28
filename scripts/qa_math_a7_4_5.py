import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-7-4':('A-7-4：二元一次聯立方程式的意義','以兩個未知數與兩個線性等式表示同時存在的數量關係。'),'content-a-7-5':('A-7-5：二元一次聯立方程式的解法與應用','運用代入法或消去法解聯立方程式，並驗證情境答案。')}
focus=['未知數設定','方程式建立','代入法','消去法','等式保持','解的意義','計算檢查','文字轉式','情境應用','結果驗算']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能代回兩式驗證解。'},{'heading':'學習流程','body':'定義兩個未知數，將條件寫成兩式，選擇代入或消去法求解，最後代回檢查。'},{'heading':'常見錯誤','body':'只解出一個未知數、消去時係數未同步處理，或忽略題目限制。'}]}; lesson['studyHighlights']=['兩個未知數對應兩個條件。','選擇代入或消去法。','解出後代回兩式。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟應用「{title}」。','steps':[{'id':'step-1','prompt':'第一步要先整理什麼？','options':['兩個未知數與兩個條件','只看一個數字'],'answer':'A','feedback':'先定義未知數並整理條件。'},{'id':'step-2','prompt':'第二步可採用哪種方法？','options':['代入法或消去法','直接猜答案'],'answer':'A','feedback':'選擇可消去一個未知數的方法。'},{'id':'step-3','prompt':'最後如何確認？','options':['代回兩個原式驗算','只檢查一式'],'answer':'A','feedback':'兩式都成立才是聯立解。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'建立兩式並以代入或消去法求解，再代回兩式檢查'},{'id':'B','text':'只用一個條件猜兩個未知數'},{'id':'C','text':'消去時只改變一邊係數'},{'id':'D','text':'解出一式即可不必驗算'}],'answer':{'value':'A','explanation':f'{title}要求兩個條件同時成立；建立兩式、求解並代回兩式才能完成{f}。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
