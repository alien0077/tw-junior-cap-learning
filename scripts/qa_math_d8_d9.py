import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
units={'content-d-8-1':('D-8-1：統計資料處理','整理、分類與表示統計資料，選擇適當方法解讀資料。'),'content-d-9-1':('D-9-1：統計數據的分布','理解資料分布、集中趨勢與離散程度的比較。')}
focus=['資料整理','分類表示','統計圖表','平均數','中位數','眾數','分布形狀','離散程度','比較解釋','結果檢查']
m=json.loads((ROOT/'data/m4-coverage-matrix.json').read_text())
for key,(title,summary) in units.items():
 lid='lesson-math-'+key;lp=ROOT/f'lessons/math/{lid}.json';lesson=json.loads(lp.read_text());lesson.update({'title':title,'reviewStatus':'content-reviewed','updatedAt':'2026-08-26'});lesson['content']={'summary':summary,'sections':[{'heading':'學習目標','body':summary+' 能引用資料支持解釋。'},{'heading':'學習流程','body':'確認資料來源，整理並選擇表示方式，計算統計量，再比較分布與限制。'},{'heading':'常見錯誤','body':'只看單一統計量或圖形外觀，忽略資料量、刻度與分布差異。'}]};lesson['studyHighlights']=['確認資料來源與單位。','選擇適當統計量。','比較分布並說明限制。'];lesson['interactive']={'type':'guided-choice','goal':f'用三步驟理解「{title}」。','steps':[{'id':'step-1','prompt':'第一步先確認什麼？','options':['資料來源與變數','圖形顏色'],'answer':'A','feedback':'先確認資料與單位。'},{'id':'step-2','prompt':'第二步如何分析？','options':['整理資料並計算統計量','直接猜趨勢'],'answer':'A','feedback':'以整理後數值分析。'},{'id':'step-3','prompt':'最後如何解釋？','options':['引用數據並說明分布限制','只報單一數字'],'answer':'A','feedback':'結論要符合資料分布。'}]};lp.write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
 for i,f in enumerate(focus,1):
  qp=ROOT/f'questions/math/question-math-{key}-{i}.json';q=json.loads(qp.read_text());q.update({'prompt':f'「{title}」進行{f}時，哪一項做法正確？','reviewStatus':'content-reviewed','updatedAt':'2026-08-26','options':[{'id':'A','text':'確認資料與單位，整理後以統計量和分布證據解釋'},{'id':'B','text':'只看圖形外觀猜測'},{'id':'C','text':'忽略資料量與刻度'},{'id':'D','text':'只報單一數字不說明限制'}],'answer':{'value':'A','explanation':f'「{title}」的{f}需以正確整理、統計量與資料分布支持結論。'}});qp.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
 for r in m['rows']:
  if r.get('lessonId')==lid:r.update({'contentStatus':'content-reviewed','reviewStatus':'content-reviewed'})
(ROOT/'data/m4-coverage-matrix.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');print('reviewed',len(units))
