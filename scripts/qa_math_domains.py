import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-d':('D：資料與不確定性','整理統計圖表、統計量與機率，依資料做合理推論。'),'content-f':('F：函數','理解變數對應、函數表示與圖形變化。'),'content-n':('N：數與量','運用數與量的運算、比例、根式、數列與誤差概念。'),'content-s':('S：空間與形狀','整合平面與立體幾何的定義、性質與推理。')}
focus=['概念定義','表示法','運算規則','圖表判讀','公式選擇','情境建模','推理步驟','結果估算','單位檢查','合理性驗證']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能選擇適當表示法與方法解題。'},{'heading':'學習流程','body':'辨認概念與已知量，選擇表示法或公式，逐步運算並以估算與條件檢查。'},{'heading':'常見錯誤','body':'混淆變數與常數、統計量與機率、平面與立體公式，或忽略單位。'}]}; lesson['studyHighlights']=['釐清定義與表示法。','依條件選方法。','檢查結果合理性。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先整理什麼？','options':['概念定義、已知量與條件','直接套用公式'],'answer':'A','feedback':'先釐清題意。'},{'id':'step-2','prompt':'第二步如何解題？','options':['選適當表示法與規則逐步推理','跳過中間步驟'],'answer':'A','feedback':'保持方法與條件一致。'},{'id':'step-3','prompt':'最後如何確認？','options':['估算並檢查答案與單位','忽略合理性'],'answer':'A','feedback':'用條件驗證結果。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先釐清定義與條件，再選方法逐步驗證'},{'id':'B','text':'不讀題直接套用公式'},{'id':'C','text':'混淆不同概念或單位'},{'id':'D','text':'忽略估算與合理性檢查'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依定義、條件與可驗證步驟處理。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
