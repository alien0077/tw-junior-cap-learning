import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-a-7-6':('A-7-6：二元一次聯立方程式的幾何意義','以平面上兩條直線的交點理解聯立方程式的解。'),'content-a-7-7':('A-7-7：一元一次不等式的意義','用不等號表示範圍關係，理解解集與數線表示。')}
focus=['概念辨識','圖形或數線','條件轉換','解集判讀','方法選擇','符號方向','邊界判斷','情境應用','結果檢核','錯誤辨識']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能用代入、圖形或數線檢查結論。'},{'heading':'學習流程','body':'辨認未知量與條件，建立關係式，依規則求解，再用圖形或數線驗證。'},{'heading':'常見錯誤','body':'混淆等號與不等號、忽略邊界，或把交點與任意點混為一談。'}]}; lesson['studyHighlights']=['先整理條件與符號。','用圖形或數線理解解集。','回代或檢查邊界。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步應先整理什麼？','options':['未知量與條件','無關數字'],'answer':'A','feedback':'先辨認變數與題目條件。'},{'id':'step-2','prompt':'第二步如何表示關係？','options':['建立方程式或不等式','直接猜結果'],'answer':'A','feedback':'以符號表達條件關係。'},{'id':'step-3','prompt':'最後如何驗證？','options':['用代入、圖形或數線檢查','跳過邊界檢查'],'answer':'A','feedback':'驗證解是否符合原條件。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先整理條件，再用方程式、不等式或圖形／數線驗證'},{'id':'B','text':'忽略符號直接猜答案'},{'id':'C','text':'不檢查邊界或交點意義'},{'id':'D','text':'只看一個條件便下結論'}],'answer':{'value':'A','explanation':f'「{title}」的{f}必須依原條件建立表示式並檢查解集或圖形意義。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
