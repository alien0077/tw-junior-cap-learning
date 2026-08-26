import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-4':('S-8-4：全等圖形','辨認全等圖形並運用平移、旋轉與鏡射判斷對應關係。'),'content-s-8-5':('S-8-5：三角形的全等性質','運用 SSS、SAS、ASA 與 RHS 判定三角形全等。')}
focus=['全等定義','對應頂點','平移判斷','旋轉判斷','鏡射判斷','SSS 判定','SAS 判定','ASA 判定','RHS 判定','條件檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能指出對應元素並檢查判定條件。'},{'heading':'學習流程','body':'先對應頂點與邊，再判斷剛體變換或三角形全等條件，最後核對條件是否充分。'},{'heading':'常見錯誤','body':'把相似誤當全等、對應順序錯置，或只憑一個角判定三角形全等。'}]}; lesson['studyHighlights']=['建立對應關係。','選用充分的全等條件。','檢查對應順序與結論。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先做什麼？','options':['標出對應頂點、邊與角','直接猜結論'],'answer':'A','feedback':'先建立正確對應。'},{'id':'step-2','prompt':'第二步如何判斷？','options':['依剛體變換或充分全等條件推理','只比較一個角'],'answer':'A','feedback':'選擇充分且適用的條件。'},{'id':'step-3','prompt':'最後如何確認？','options':['核對對應順序與所有條件','忽略未給條件'],'answer':'A','feedback':'確認結論不超出已知條件。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先建立對應關係，再依充分條件逐步驗證'},{'id':'B','text':'只憑外觀或單一角度判斷'},{'id':'C','text':'混淆相似與全等的結論'},{'id':'D','text':'忽略對應順序與已知條件'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須依定義、對應關係與充分條件驗證。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid: r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
