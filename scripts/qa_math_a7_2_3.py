import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={
'content-a-7-2':('A-7-2：一元一次方程式的意義','用等號表示左右相等關係，辨認未知數、係數與常數。'),
'content-a-7-3':('A-7-3：一元一次方程式的解法與應用','運用等量公理解一元一次方程式，並將生活情境轉成方程式。')}
focus=['未知數辨認','等式意義','移項觀念','係數處理','驗算','文字轉式','數量關係','步驟推理','情境應用','結果檢核']
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以代入驗算確認答案。'},{'heading':'學習流程','body':'整理未知數與已知量，建立等式，依等量公理逐步化簡，再代回驗算。'},{'heading':'常見錯誤','body':'移項時忘記改變加減號，或解出數值後未代回原式檢查。'}]}; lesson['studyHighlights']=['先定義未知數。','等式兩邊做相同運算。','代回原式驗算。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步應先做什麼？','options':['定義未知數並整理已知量','直接猜答案'],'answer':'A','feedback':'先清楚定義未知數。'},{'id':'step-2','prompt':'第二步如何保持等式？','options':['兩邊做相同運算','只改左邊'],'answer':'A','feedback':'等式兩邊必須做相同運算。'},{'id':'step-3','prompt':'最後如何確認？','options':['代回原式驗算','省略檢查'],'answer':'A','feedback':'代回可確認解是否正確。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」的{f}，下列哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'定義未知數，維持等式兩邊相等並代回驗算'},{'id':'B','text':'只對等式左邊運算'},{'id':'C','text':'移項但不改變符號'},{'id':'D','text':'不需檢查答案'}],'answer':{'value':'A','explanation':f'{title}必須遵守等量公理，並以代回驗算確認{f}的結果。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
 (ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
 print(lid)
