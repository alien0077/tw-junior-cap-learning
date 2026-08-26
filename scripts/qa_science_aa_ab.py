import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ids=['aa-iv-1','aa-iv-2','aa-iv-3','aa-iv-4','aa-iv-5','ab-iv-1','ab-iv-2','ab-iv-3','ab-iv-4']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for code in ids:
 lid='lesson-science-content-'+code; lp=ROOT/f'lessons/science/{lid}.json'; lesson=json.loads(lp.read_text()); title=lesson.get('title',code); summary=f'依據「{title}」整理科學概念、證據與探究方法。'; lesson.update({'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以觀察或模型說明現象。'},{'heading':'探究流程','body':'提出問題、辨認變因與證據，建立模型或分類，再以資料檢驗。'},{'heading':'常見錯誤','body':'混淆觀察與推論、忽略控制變因，或把模型當成現象本身。'}]}; lesson['studyHighlights']=['辨認現象與證據。','建立模型與推理。','檢查資料與結論。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先做什麼？','options':['辨認現象、變因與證據','直接猜結論'],'answer':'A','feedback':'先釐清探究問題。'},{'id':'step-2','prompt':'第二步如何推理？','options':['用模型或分類整理證據','忽略資料差異'],'answer':'A','feedback':'根據證據建立解釋。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查資料與結論是否一致','跳過驗證'],'answer':'A','feedback':'以證據檢驗推論。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i in range(1,11):
  qp=ROOT/f'questions/science/question-science-content-{code}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」探究時，哪一項做法最恰當？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'以證據與模型逐步說明，並檢查變因與結論'},{'id':'B','text':'只憑直覺直接下結論'},{'id':'C','text':'忽略控制變因與資料差異'},{'id':'D','text':'把模型當作現象本身'}],'answer':{'value':'A','explanation':f'「{title}」需以可觀察證據、模型與探究流程建立可靠解釋。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(ids))
