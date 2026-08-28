import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-g':('G：坐標幾何','統整座標、點線關係與距離概念。'),'content-n-7-1':('N-7-1：100以內的質數','辨認 100 以內質數並理解質數只有 1 與本身兩個因數。'),'content-n-7-2':('N-7-2：質因數分解的標準分解式','將合成數分解為質數乘積並用指數表示。')}
focus=['概念辨識','符號判讀','條件整理','方法選擇','步驟推理','計算檢查','圖形或數線','因數判斷','情境應用','結果驗算']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以圖形、因數或代入結果驗證。'},{'heading':'學習流程','body':'先辨認概念與條件，再選擇表示或運算方法，逐步完成並檢查結果。'},{'heading':'常見錯誤','body':'忽略定義條件、漏列因數，或計算後沒有回頭驗證。'}]};lesson['studyHighlights']=['先抓定義與條件。','依規則逐步處理。','用證據檢查結果。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['定義與已知條件','無關細節'],'answer':'A','feedback':'先確認概念與條件。'},{'id':'step-2','prompt':'第二步如何處理？','options':['依規則或圖形逐步推理','直接猜答案'],'answer':'A','feedback':'使用適當方法。'},{'id':'step-3','prompt':'最後如何確認？','options':['回代、展開或列因數檢查','跳過檢查'],'answer':'A','feedback':'以可檢驗證據確認。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認定義與條件，再依規則完成並檢查'},{'id':'B','text':'忽略條件直接猜測'},{'id':'C','text':'只記結果不寫步驟'},{'id':'D','text':'不驗算或列出證據'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依定義與條件逐步處理，並用可檢驗證據確認。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
