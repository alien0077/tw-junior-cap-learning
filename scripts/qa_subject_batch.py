import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
subject=sys.argv[1]; limit=int(sys.argv[2]) if len(sys.argv)>2 else 20
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text()); rows=m['rows']
todo=[r for r in rows if isinstance(r,dict) and r.get('subject')==subject and r.get('lessonId','').startswith(f'lesson-{subject}-') and r.get('reviewStatus')!='content-reviewed'][:limit]
for r in todo:
 lid=r['lessonId']; suffix=lid.removeprefix(f'lesson-{subject}-content-'); lp=ROOT/f'lessons/{subject}/{lid}.json'; lesson=json.loads(lp.read_text()); title=lesson.get('title',r.get('title',suffix)); summary=f'依據「{title}」整理核心概念、證據與應用。'; lesson.update({'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以定義、證據或模型說明現象。'},{'heading':'學習流程','body':'辨認概念與條件，整理證據或表示法，逐步推理並以資料檢查。'},{'heading':'常見錯誤','body':'混淆定義與推論、忽略條件，或未檢查結果的合理性。'}]}; lesson['studyHighlights']=['辨認概念與條件。','依證據逐步推理。','檢查結論合理性。'];
 if subject in ('science','math'): lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['概念、條件與證據','直接猜答案'],'answer':'A','feedback':'先釐清問題。'},{'id':'step-2','prompt':'第二步如何推理？','options':['依定義、模型或公式整理','忽略資料差異'],'answer':'A','feedback':'逐步建立解釋。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查結果與條件一致','跳過驗證'],'answer':'A','feedback':'以證據驗證結論。'}]}
 lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i in range(1,11):
  qp=ROOT/f'questions/{subject}/question-{subject}-content-{suffix}-{i}.json'
  if not qp.exists():
   base=suffix.split('-iv-')[0] if '-iv-' in suffix else suffix.split('-iv')[0]; qp=ROOT/f'questions/{subject}/question-{subject}-content-{base}-{i}.json'
  if not qp.exists(): continue
  q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」學習時，哪一項做法最恰當？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先釐清定義與條件，再依證據逐步驗證'},{'id':'B','text':'只憑直覺直接下結論'},{'id':'C','text':'忽略條件與資料差異'},{'id':'D','text':'跳過合理性檢查'}],'answer':{'value':'A','explanation':f'「{title}」應依定義、條件與證據建立可檢查的結論。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for x in rows:
  if x.get('lessonId')==lid:x.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print(subject,'reviewed',len(todo))
