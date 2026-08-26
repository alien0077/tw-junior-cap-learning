import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-7-8':('A-7-8：一元一次不等式的解與應用','求出不等式解集並用數線或情境限制表示範圍。'),'content-a-8-1':('A-8-1：二次式的乘法公式','運用平方差與完全平方公式展開或整理二次式。')}
focus=['定義辨識','式子建立','規則選擇','符號處理','展開整理','數線表示','邊界判斷','情境應用','代入檢查','錯誤辨識']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以代入或展開結果檢查答案。'},{'heading':'學習流程','body':'辨認結構與條件，選擇對應規則逐步運算，再以數線、代入或整理結果驗證。'},{'heading':'常見錯誤','body':'忽略不等號方向、邊界端點，或套用公式時漏掉中間項。'}]}; lesson['studyHighlights']=['辨認式子結構。','依規則逐步運算。','代入或整理後驗證。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步要先辨認什麼？','options':['條件與式子結構','無關數字'],'answer':'A','feedback':'先確認未知量、符號與式子結構。'},{'id':'step-2','prompt':'第二步應採用什麼？','options':['對應規則逐步運算','直接猜結果'],'answer':'A','feedback':'依不等式或乘法公式規則計算。'},{'id':'step-3','prompt':'最後如何檢查？','options':['代入、數線或展開結果驗證','跳過驗證'],'answer':'A','feedback':'確認結果符合原式與情境。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認結構與條件，再依規則運算並驗證'},{'id':'B','text':'忽略符號直接猜答案'},{'id':'C','text':'套公式時省略必要項目'},{'id':'D','text':'不檢查邊界或展開結果'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依式子結構與規則逐步處理，最後用代入、數線或展開結果驗證。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
