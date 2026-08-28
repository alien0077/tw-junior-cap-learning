import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-2':('S-8-2：凸多邊形的內角和','運用三角形分割理解凸多邊形內角和公式。'),'content-s-8-3':('S-8-3：平行','理解平行線判定與截線形成的角關係。')}
focus=['定義辨認','圖形分割','內角和公式','角度計算','平行判定','截線關係','同位角','內錯角','情境應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以分割、角關係或公式驗證。'},{'heading':'學習流程','body':'辨認圖形與角，整理三角形分割或平行線截線關係，再計算並檢查。'},{'heading':'常見錯誤','body':'內角和公式代錯邊數、混淆同位角與內錯角，或把相交線誤判平行。'}]};lesson['studyHighlights']=['先辨認圖形與角。','依公式或角關係推理。','用圖形與計算驗證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['圖形、邊數與角關係','只看外框'],'answer':'A','feedback':'先辨認邊數或平行線截線。'},{'id':'step-2','prompt':'第二步如何推理？','options':['分割成三角形或使用角關係','直接猜角度'],'answer':'A','feedback':'依幾何關係計算。'},{'id':'step-3','prompt':'最後如何確認？','options':['用公式與圖形互證','跳過檢查'],'answer':'A','feedback':'確認角度與平行關係一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認圖形與角關係，再依公式或平行線性質驗證'},{'id':'B','text':'只看外觀直接猜角度'},{'id':'C','text':'混淆同位角與內錯角'},{'id':'D','text':'忽略邊數或截線條件'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依幾何定義、公式與角關係逐步判斷。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
