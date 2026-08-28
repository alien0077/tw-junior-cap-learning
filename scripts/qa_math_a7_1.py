import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; key='content-a-7-1'; lid='lesson-math-content-a-7-1'; title='A-7-1：代數符號'
lp=ROOT/f'lessons/math/{lid}.json'; lesson=json.loads(lp.read_text()); lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'}); lesson['content']={'summary':'理解變數、常數、係數與代數式的表示方式，能將文字情境轉成代數式並代入計算。','sections':[{'heading':'學習目標','body':'能辨認代數式中的變數、常數與係數，並依運算順序完成代入。'},{'heading':'學習流程','body':'先用符號表示未知量，再整理項與係數，最後代入數值並檢查單位。'},{'heading':'常見錯誤','body':'把係數與指數混淆，或代入負數時漏寫括號。'}]}; lesson['studyHighlights']=['變數代表可變的量。','係數乘在變數前。','代入負數要加括號。']; lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
items=[('變數辨認','式 3x+2 中可代表不同數值的符號是？','x','3','2','3x'),('係數辨認','式 -5a 中 a 的係數是？','-5','5','-a','a'),('常數辨認','式 7y-4 中的常數項是？','-4','7','y','7y'),('文字轉式','每盒彩筆 x 枝，買 4 盒共有幾枝？','4x','x+4','x/4','4+x'),('代入計算','x=3 時，2x+5 的值是？','11','8','10','13'),('負數代入','a=-2 時，a² 的值是？','4','-4','-2','2'),('同類項','下列何者與 3x 是同類項？','-2x','2y','x²','3'),('分配律','2(x+3) 展開為？','2x+6','2x+3','x+6','2x+9'),('運算順序','x=2 時，3+x² 的值是？','7','25','9','10'),('情境建模','原有 n 元，花 35 元後剩下？','n-35','35-n','n+35','35n')]
for i,(f,p,a,b,c,d) in enumerate(items,1):
 qp=ROOT/f'questions/math/question-math-{key}-{i}.json'; q=json.loads(qp.read_text()); q.update({'prompt':f'{f}：{p}','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':a},{'id':'B','text':b},{'id':'C','text':c},{'id':'D','text':d}],'answer':{'value':'A','explanation':f'依代數符號規則，正確結果為 {a}；其餘選項混淆了變數、係數或運算順序。'}}); qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for r in m['rows']:
 if r.get('lessonId')==lid: r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print(lid)
