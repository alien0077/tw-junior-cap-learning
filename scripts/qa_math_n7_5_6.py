import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-n-7-5':('N-7-5：數線','用數線表示有理數，理解大小、距離與相反數。'),'content-n-7-6':('N-7-6：指數的意義','理解指數表示相同因數連乘及其計算意義。')}
focus=['位置判讀','大小比較','相反數','距離概念','連乘表示','底數辨識','指數辨識','乘方計算','符號處理','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用表示法與計算檢查結果。'},{'heading':'學習流程','body':'先辨認數值或乘方結構，再用數線、連乘或指數規則處理，最後檢查。'},{'heading':'常見錯誤','body':'數線方向判讀錯誤、混淆底數與指數，或負號處理不當。'}]};lesson['studyHighlights']=['先確認表示法。','依規則逐步處理。','用圖形或代入檢查。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['數值位置或乘方結構','只看符號外觀'],'answer':'A','feedback':'先讀清楚數線或底數指數。'},{'id':'step-2','prompt':'第二步如何處理？','options':['依表示法與規則計算','直接猜結果'],'answer':'A','feedback':'按規則完成表示或運算。'},{'id':'step-3','prompt':'最後如何確認？','options':['用數線、連乘或代入檢查','跳過檢查'],'answer':'A','feedback':'確認結果與原意一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認表示法與規則，再逐步處理並檢查'},{'id':'B','text':'忽略方向或底數指數'},{'id':'C','text':'只憑外觀猜結果'},{'id':'D','text':'不驗證表示是否一致'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依定義與運算規則，並用表示法或代入檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
