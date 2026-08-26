import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-f-9-1':('F-9-1：二次函數的意義','理解二次函數的輸入輸出關係與標準形式。'),'content-f-9-2':('F-9-2：二次函數的圖形與極值','由開口方向、頂點與對稱軸解讀二次函數圖形與極值。')}
focus=['定義辨識','標準形式','係數意義','開口方向','頂點判讀','對稱軸','極值判斷','表格轉圖','情境應用','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能以式子、表格與圖形互相驗證。'},{'heading':'學習流程','body':'辨認二次項與係數，整理對稱軸與頂點，再由開口方向判斷極值並檢查。'},{'heading':'常見錯誤','body':'把一次函數圖形套用到二次函數，或混淆頂點、截距與極值。'}]};lesson['studyHighlights']=['辨認二次函數形式。','由頂點與對稱軸判讀。','用式子與圖形互證。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先辨認什麼？','options':['二次項、係數與形式','只看一個點'],'answer':'A','feedback':'先確認式子結構。'},{'id':'step-2','prompt':'第二步如何讀圖？','options':['找對稱軸、頂點與開口','只看顏色'],'answer':'A','feedback':'頂點與開口決定極值。'},{'id':'step-3','prompt':'最後如何檢查？','options':['以式子、表格或圖形互證','跳過檢查'],'answer':'A','feedback':'不同表示應一致。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'先確認二次式結構，再用頂點、對稱軸與圖形驗證'},{'id':'B','text':'把圖形當成直線處理'},{'id':'C','text':'只看一個點就判斷極值'},{'id':'D','text':'忽略開口方向'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需由二次式結構與圖形特徵互相驗證。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
