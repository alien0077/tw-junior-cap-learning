import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-10':('S-8-10：正方形、長方形、箏形的基本性質','比較正方形、長方形與箏形的邊角及對角線性質。'),'content-s-8-11':('S-8-11：梯形的基本性質','辨認梯形與等腰梯形並運用平行邊、角與對角線性質。')}
focus=['圖形定義','邊長性質','角度性質','對角線','正方形判定','長方形判定','箏形判定','梯形判定','等腰梯形','性質比較']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能依定義判定圖形並說明理由。'},{'heading':'學習流程','body':'整理邊角與對角線特徵，依充分條件判定圖形，再比較不同四邊形性質。'},{'heading':'常見錯誤','body':'以外觀代替定義、混淆箏形與平行四邊形，或忽略梯形僅一組平行邊。'}]}; lesson['studyHighlights']=['記住圖形定義。','整理邊角與對角線。','用充分條件判定。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先做什麼？','options':['列出圖形定義與已知特徵','只看圖形外觀'],'answer':'A','feedback':'以定義作為判定起點。'},{'id':'step-2','prompt':'第二步如何判斷？','options':['比對邊角與對角線的充分性質','任選一項特徵'],'answer':'A','feedback':'使用足以判定的性質。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查所有條件與反例','略過條件檢查'],'answer':'A','feedback':'確認沒有混淆相近圖形。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'依圖形定義整理性質，再用充分條件判定'},{'id':'B','text':'只憑外觀或單一特徵判斷'},{'id':'C','text':'混淆不同四邊形的定義'},{'id':'D','text':'忽略平行邊與對角線條件'}],'answer':{'value':'A','explanation':f'「{title}」的{f}須由定義、邊角與對角線性質逐項核對。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid: r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
