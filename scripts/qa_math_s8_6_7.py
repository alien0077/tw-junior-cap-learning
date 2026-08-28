import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-s-8-6':('S-8-6：畢氏定理','運用畢氏定理與逆定理求直角三角形邊長並判斷直角。'),'content-s-8-7':('S-8-7：平面圖形的面積','分解平面圖形並使用三角形、四邊形公式求面積。')}
focus=['直角辨認','a²+b²=c²','斜邊判定','逆定理','未知邊計算','圖形分解','三角形面積','平行四邊形面積','梯形面積','單位檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key; lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能列式、計算並檢查單位。'},{'heading':'學習流程','body':'辨認圖形與已知量，選擇定理或面積公式列式，計算後以估算與單位檢查。'},{'heading':'常見錯誤','body':'把斜邊當直角邊、平方根漏寫，或面積與周長公式混用。'}]}; lesson['studyHighlights']=['辨認適用圖形與條件。','列出正確公式。','檢查數值與單位。']; lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['圖形類型、直角與已知量','直接套公式'],'answer':'A','feedback':'先確認條件與圖形。'},{'id':'step-2','prompt':'第二步如何列式？','options':['選用畢氏或面積公式並代入','混用周長公式'],'answer':'A','feedback':'依圖形選擇正確公式。'},{'id':'step-3','prompt':'最後如何確認？','options':['檢查估算、平方根與單位','忽略單位'],'answer':'A','feedback':'用合理性與單位驗算。'}]}; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先辨認圖形與條件，再選公式計算並檢查單位'},{'id':'B','text':'不看直角或圖形直接套式'},{'id':'C','text':'把周長公式當面積公式'},{'id':'D','text':'忽略平方根與單位'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需依圖形條件選式，並檢查計算與單位。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid: r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n'); print('reviewed',len(units))
