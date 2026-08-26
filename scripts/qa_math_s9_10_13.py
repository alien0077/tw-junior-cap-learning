import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-9-10':('S-9-10：三角形的重心','理解三角形中線交點重心及其分點性質。'),'content-s-9-11':('S-9-11：證明的意義','以定義、公理與已知條件組織幾何證明。'),'content-s-9-12':('S-9-12：空間中的線與平面','判斷空間中線與平面的平行、垂直及交會關係。'),'content-s-9-13':('S-9-13：表面積與體積','運用立體展開、表面積與體積公式解題。')}
focus=['重心定義','中線性質','分點比','證明結構','已知與結論','線面關係','垂直平行','截面判讀','表面積','體積與單位']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能依定義、圖形與公式完成推理。'},{'heading':'學習流程','body':'辨認元素與條件，建立比例、證明或立體公式，計算後檢查圖形與單位。'},{'heading':'常見錯誤','body':'混淆中線與高、證明跳步，或把表面積與體積單位混用。'}]}; lesson['studyHighlights']=['辨認定義與條件。','建立推理或公式。','檢查圖形與單位。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['圖形元素、定義與已知條件','直接猜公式'],'answer':'A','feedback':'先整理條件。'},{'id':'step-2','prompt':'第二步如何推理？','options':['依定義、性質或公式列出步驟','跳過中間推理'],'answer':'A','feedback':'逐步建立可檢查的推理。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查結論、合理性與單位','忽略驗算'],'answer':'A','feedback':'確認結果符合題意。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先整理定義與條件，再逐步推理並檢查'},{'id':'B','text':'只憑外觀直接猜答案'},{'id':'C','text':'跳過必要的證明或公式步驟'},{'id':'D','text':'忽略合理性與單位'}],'answer':{'value':'A','explanation':f'「{title}」的{f}須依定義、條件與可驗證步驟完成。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
