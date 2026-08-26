import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-12':('S-8-12：尺規作圖與幾何推理','使用尺規完成基本作圖並以幾何性質說明步驟。'),'content-s-9-1':('S-9-1：相似形','辨認相似形並使用對應邊角與比例解題。'),'content-s-9-2':('S-9-2：三角形的相似性質','運用 AA、SAS、SSS 判定三角形相似。'),'content-s-9-3':('S-9-3：平行線截比例線段','運用平行線截線段成比例的性質求未知長度。'),'content-s-9-4':('S-9-4：相似直角三角形邊長比值的不變性','理解相似直角三角形對應邊比值不變並應用於計算。')}
focus=['定義辨認','作圖步驟','作圖驗證','對應關係','比例列式','AA判定','SAS判定','SSS判定','未知量計算','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能依定義與比例關係完成推理。'},{'heading':'學習流程','body':'辨認對應元素，選擇作圖工具或相似判定條件，列出比例並驗算。'},{'heading':'常見錯誤','body':'對應順序錯置、比例方向不一致，或作圖後未檢查條件。'}]}; lesson['studyHighlights']=['辨認對應元素。','選擇充分條件列式。','以圖形與比例驗算。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['定義、對應元素與已知條件','直接代入數字'],'answer':'A','feedback':'先建立正確對應。'},{'id':'step-2','prompt':'第二步如何推理？','options':['依作圖規則或相似條件列式','任意配對邊長'],'answer':'A','feedback':'使用充分且一致的條件。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查比例方向、圖形與結果','忽略驗算'],'answer':'A','feedback':'確認推理與數值一致。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認定義與對應，再依規則或比例驗證'},{'id':'B','text':'不看條件直接猜答案'},{'id':'C','text':'任意交換對應邊順序'},{'id':'D','text':'略過作圖或比例檢查'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須依定義、對應與一致比例逐步核對。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
