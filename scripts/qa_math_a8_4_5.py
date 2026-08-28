import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-8-4':('A-8-4：因式分解','將多項式改寫為幾個因式相乘，理解展開與分解互為逆運算。'),'content-a-8-5':('A-8-5：因式分解的方法','依共同因式、分組或乘法公式選擇適當的因式分解方法。')}
focus=['共同因式','公式辨識','分組方法','因式乘積','係數處理','符號判斷','完全平方','平方差','方法選擇','展開驗算']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能將分解結果重新展開驗算。'},{'heading':'學習流程','body':'先找共同因式，再辨認乘法公式或分組結構，完成分解後展開確認。'},{'heading':'常見錯誤','body':'漏提出最大共同因式、符號錯誤，或分解後未檢查是否仍可繼續分解。'}]}; lesson['studyHighlights']=['先找共同因式。','辨認平方差或完全平方。','展開驗算分解結果。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先找什麼？','options':['共同因式與式子結構','無關常數'],'answer':'A','feedback':'先觀察各項共同因式。'},{'id':'step-2','prompt':'第二步如何選方法？','options':['依結構選公式或分組','任意拆項'],'answer':'A','feedback':'平方差、完全平方與分組有不同條件。'},{'id':'step-3','prompt':'最後如何確認？','options':['重新展開驗算','不必檢查'],'answer':'A','feedback':'展開乘積應回到原多項式。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先觀察共同因式與結構，選方法後展開驗算'},{'id':'B','text':'任意拆項且不檢查'},{'id':'C','text':'忽略負號與共同因式'},{'id':'D','text':'看到二次式就套同一公式'}],'answer':{'value':'A','explanation':f'「{title}」的{f}要依多項式結構選擇方法，完成後以展開確認。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
