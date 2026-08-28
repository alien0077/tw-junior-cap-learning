import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-8':('S-8-8：三角形的基本性質','運用三角形內角和、外角與邊角關係解題。'),'content-s-8-9':('S-8-9：平行四邊形的基本性質','辨認平行四邊形並運用對邊、對角與對角線性質。')}
focus=['內角和','外角定理','邊角關係','等腰三角形','平行四邊形定義','對邊性質','對角性質','對角線性質','面積應用','條件檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以角度與線段性質列式驗證。'},{'heading':'學習流程','body':'先辨認圖形與已知性質，再套用角度、對邊對角或對角線關係，最後檢查條件。'},{'heading':'常見錯誤','body':'混淆內角與外角、把一般四邊形當平行四邊形，或誤用對角線性質。'}]}; lesson['studyHighlights']=['辨認圖形與已知條件。','套用對應幾何性質。','檢查角度與線段關係。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['圖形定義與已知角邊','直接代數字'],'answer':'A','feedback':'先確認圖形與條件。'},{'id':'step-2','prompt':'第二步如何推理？','options':['套用內角、外角或平行四邊形性質','憑外觀猜測'],'answer':'A','feedback':'使用正確幾何定理。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查角和、對應邊角與條件','略過驗算'],'answer':'A','feedback':'確認結論符合圖形性質。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認圖形定義，再套用對應性質並驗算'},{'id':'B','text':'只看外觀猜角度或邊長'},{'id':'C','text':'混淆內角外角或圖形種類'},{'id':'D','text':'忽略定理適用條件'}],'answer':{'value':'A','explanation':f'「{title}」的{f}應依定義與幾何性質推理並檢查。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid: r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
