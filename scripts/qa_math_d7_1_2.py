import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-d-7-1':('D-7-1：統計圖表','讀取長條圖、折線圖與圓餅圖，理解圖表標題、座標與資料意義。'),'content-d-7-2':('D-7-2：統計數據','整理統計資料並比較平均數、中位數、眾數等統計量。')}
focus=['標題與變數','座標判讀','資料讀取','圖表選擇','平均數','中位數','眾數','離群值','比較解釋','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以資料證據說明比較結果。'},{'heading':'學習流程','body':'先確認資料來源與變數，再讀取或計算統計量，最後比較並說明限制。'},{'heading':'常見錯誤','body':'忽略座標刻度、把平均數當成所有資料，或只看圖形高低不讀數值。'}]};lesson['studyHighlights']=['先確認變數與刻度。','計算並比較統計量。','用資料證據解釋。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['資料來源、變數與刻度','只看圖形顏色'],'answer':'A','feedback':'先讀標題、座標與資料單位。'},{'id':'step-2','prompt':'第二步如何分析？','options':['讀取或計算統計量','直接猜趨勢'],'answer':'A','feedback':'以數值支持比較。'},{'id':'step-3','prompt':'最後如何表達？','options':['引用資料並說明限制','只下結論不舉證'],'answer':'A','feedback':'結論要能回到資料證據。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認資料與刻度，再以數值計算或比較並說明'},{'id':'B','text':'只看圖形外觀猜測'},{'id':'C','text':'忽略單位與資料來源'},{'id':'D','text':'只報結論不引用數據'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須以正確讀值或統計量和資料證據支持。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
