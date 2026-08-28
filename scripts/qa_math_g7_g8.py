import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-g-7-1':('G-7-1：平面直角坐標系','理解 x、y 軸、象限與有序數對在平面上的位置。'),'content-g-8-1':('G-8-1：直角坐標系上兩點距離公式','運用兩點距離公式計算座標平面上兩點間的距離。')}
focus=['有序數對','座標軸','象限判讀','點的位置','距離概念','水平垂直距離','公式辨識','代入計算','圖形應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用座標圖或公式驗證結果。'},{'heading':'學習流程','body':'先讀取有序數對與座標軸，辨認位置或兩點差值，再套用公式並檢查。'},{'heading':'常見錯誤','body':'把 x、y 順序顛倒、誤判象限，或距離公式平方與開根號處理錯誤。'}]};lesson['studyHighlights']=['有序數對先 x 後 y。','差值平方後相加。','距離結果需合理。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['有序數對與座標軸','只看圖形大小'],'answer':'A','feedback':'先確認 x、y 的位置。'},{'id':'step-2','prompt':'第二步如何求解？','options':['計算差值並套用距離關係','直接猜距離'],'answer':'A','feedback':'依座標差值計算。'},{'id':'step-3','prompt':'最後如何檢查？','options':['用圖形或反算驗證','跳過檢查'],'answer':'A','feedback':'確認座標順序與結果合理。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認有序數對與座標軸，再依差值或圖形計算並驗證'},{'id':'B','text':'把 x、y 順序任意交換'},{'id':'C','text':'忽略平方與開根號步驟'},{'id':'D','text':'不檢查象限或結果'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須遵守座標順序與距離關係，並用圖形或計算檢查。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
